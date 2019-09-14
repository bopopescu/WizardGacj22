import xbmc
import xbmcaddon
import xbmcgui
import urllib
import os
import os.path
import time
import urlparse
from qtfaststart import processor
from kmediatorrent import plugin, torrent2http
from kmediatorrent.common import RESOURCES_PATH
from kmediatorrent.platform import PLATFORM
from kmediatorrent.ga import track_event
from kmediatorrent.utils import url_get_json
from contextlib import contextmanager, closing, nested

TORRENT2HTTP_TIMEOUT = 20
TORRENT2HTTP_POLL = 1000
PLAYING_EVENT_INTERVAL = 60
WINDOW_FULLSCREEN_VIDEO = 12005
buffer_percentage = 0
max_buffer_size = 1000000000000000000
extension_message = ""

XBFONT_LEFT = 0x00000000
XBFONT_RIGHT = 0x00000001
XBFONT_CENTER_X = 0x00000002
XBFONT_CENTER_Y = 0x00000004
XBFONT_TRUNCATED = 0x00000008
XBFONT_JUSTIFY = 0x00000010

STATE_STRS = [
    'Queued',
    'Checking',
    'Downloading metadata',
    'Downloading',
    'Finished',
    'Seeding',
    'Allocating',
    'Allocating file & Checking resume',
    'Buffering'
]

VIEWPORT_WIDTH = 1920.0
VIEWPORT_HEIGHT = 1088.0
OVERLAY_WIDTH = int(VIEWPORT_WIDTH * 0.7) # 70% size
OVERLAY_HEIGHT = 150

ENCRYPTION_SETTINGS = {
    "Forced": 0,
    "Enabled": 1,
    "Disabled": 2,
}


class OverlayText(object):
    def __init__(self, w, h, *args, **kwargs):
        self.window = xbmcgui.Window(WINDOW_FULLSCREEN_VIDEO)
        viewport_w, viewport_h = self._get_skin_resolution()
        # Adjust size based on viewport, we are using 1080p coordinates
        w = int(w * viewport_w / VIEWPORT_WIDTH)
        h = int(h * viewport_h / VIEWPORT_HEIGHT)
        x = (viewport_w - w) / 2
        y = (viewport_h - h) / 2
        self._shown = False
        self._text = ""
        self._label = xbmcgui.ControlLabel(x, y, w, h, self._text, *args, **kwargs)
        self._background = xbmcgui.ControlImage(x, y, w, h, os.path.join(RESOURCES_PATH, "images", "black.png"))
        self._background.setColorDiffuse("0xD0000000")

    def show(self):
        if not self._shown:
            self.window.addControls([self._background, self._label])
            self._shown = True

    def hide(self):
        if self._shown:
            self._shown = False
            self.window.removeControls([self._background, self._label])

    def close(self):
        self.hide()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        if self._shown:
            self._label.setLabel(self._text)

    # This is so hackish it hurts.
    def _get_skin_resolution(self):
        import xml.etree.ElementTree as ET
        skin_path = xbmc.translatePath("special://skin/")
        tree = ET.parse(os.path.join(skin_path, "addon.xml"))
        res = tree.findall("./extension/res")[0]
        return int(res.attrib["width"]), int(res.attrib["height"])


class TorrentPlayer(xbmc.Player):
    def init(self, uri, subtitles):
        self.display_name = ""
        self.torrent2http_options = {
            "uri": uri,
            "dlpath": xbmc.validatePath(xbmc.translatePath(plugin.get_setting("dlpath"))) or ".",
            "dlrate": plugin.get_setting("max_download_rate") or "0",
            "ulrate": plugin.get_setting("max_upload_rate") or "0",
            "encryption": plugin.get_setting("encryption"),
        }

        if "://" in self.torrent2http_options["dlpath"]:
            # Translate smb:// url to UNC path on windows, very hackish
            if PLATFORM["os"] == "windows" and self.torrent2http_options["dlpath"].lower().startswith("smb://"):
                self.torrent2http_options["dlpath"] = self.torrent2http_options["dlpath"].replace("smb:", "").replace("/", "\\")
            else:
                plugin.notify("Downloading to an unmounted network share is not supported. Resetting.", delay=15000)
                plugin.set_setting("dlpath", "")
                self.torrent2http_options["dlpath"] = "."
        
        # Check for Android and FAT32 SD card issues
        if PLATFORM["os"] == "android" and self.torrent2http_options["dlpath"] != "." and plugin.get_setting("ignorefat", bool) == False :
            from kmediatorrent.utils import get_path_fs
            fs = get_path_fs(self.torrent2http_options["dlpath"])
            if fs == "vfat": # FAT32 is not supported
                plugin.notify("Downloading to FAT32 is not supported. Resetting.", delay=15000)
                plugin.set_setting("dlpath", "")
                self.torrent2http_options["dlpath"] = "."
        
        if plugin.get_setting("keep_files", bool):
            plugin.log.info("Will keep file after playback.")
            self.torrent2http_options["keep"] = None

        self.on_playback_started = []
        self.on_playback_resumed = []
        self.on_playback_paused = []
        self.on_playback_stopped = []
        self.subtitles = subtitles
        return self

    def onPlayBackStarted(self):
        for f in self.on_playback_started:
            f()
        try: xbmc.Player().setSubtitles(self.subtitles)
        except: pass
        track_event("video", "play", self.display_name)

    def onPlayBackResumed(self):
        for f in self.on_playback_resumed:
            f()
        self.onPlayBackStarted()

    def onPlayBackPaused(self):
        for f in self.on_playback_paused:
            f()
        track_event("video", "pause", self.display_name)

    def onPlayBackStopped(self):
        for f in self.on_playback_stopped:
            f()
        track_event("video", "stop", self.display_name)

    def _get_status_lines(self, status, message1):
        global max_buffer_size
        global buffer_percentage
        if message1 == "":
            message1 = status["name"]
        if (buffer_percentage < 100) and (self.getBufferSize(message1) != max_buffer_size):
            message2 = "%.2f%% %s" % (buffer_percentage, STATE_STRS[8])
        else:
            message2 = "%.2f%% %s" % (status["progress"] * 100, STATE_STRS[status["state"]])

        return [
            message1,
            message2,
            "D:%(download_rate).2fkb/s U:%(upload_rate).2fkb/s S:%(num_seeds)d (%(total_seeds)s) P:%(num_peers)d (%(total_peers)s)" % status
        ]
    @contextmanager
    def attach(self, callback, *events):
        for event in events:
            event.append(callback)
        yield
        for event in events:
            event.remove(callback)

    def _wait_t2h_startup(self, t2h):
        start = time.time()
        while (time.time() - start) < TORRENT2HTTP_TIMEOUT:
            try:
                t2h("status")
                return True
            except:
                pass
            xbmc.sleep(TORRENT2HTTP_POLL)
        return False
    
    def getFileExtension(self, filename):
        return os.path.splitext(filename)[1]
    
    def getBufferSize(self, message):
        global max_buffer_size
        if message == "" and plugin.get_setting("download_full_file", bool) == False:
            BUFFERSIZE = float(plugin.get_setting("min_download_size"))
        else:
            BUFFERSIZE = max_buffer_size
        return BUFFERSIZE
        
    def getExtensionMessage(self, extension):
        dlpath = plugin.get_setting("dlpath")
        if dlpath == "":
            dlpath = torrent2http.get_binary_dir() #default download path
        message = ""
        fileCanStream = False
        filename = (os.path.join(dlpath, self.display_name)).encode("utf-8")
        isFile = os.path.isfile(filename)
        if isFile:
            fileCanStream = processor.process(filename, filename);
            if (extension == ".mp4" or extension == ".m4v") and isFile and fileCanStream:
                message = ""                   
            elif (extension == ".mp4" or extension == ".m4v") and isFile and fileCanStream == False:
                message = "File can not fast start. The whole file must download."
            elif (extension == ".avi" or extension == ".AVI") and isFile and plugin.get_setting("download_full_avi", bool) == True:
                message = "File can not fast start. The whole file must download."
        return message

    def loop(self):
        from kmediatorrent.utils import SafeDialogProgress

        has_resolved = False

        plugin.log.info("Starting torrent2http...")
        with closing(torrent2http.start(**self.torrent2http_options)) as t2h_instance:
            t2h = lambda cmd: url_get_json("http://%s/%s" % (t2h_instance.bind_address, cmd), with_immunicity=False)
            if not self._wait_t2h_startup(t2h):
                return

            plugin.log.info("Opening download dialog...")
            with closing(SafeDialogProgress(delay_create=0)) as dialog:
                dialog.create(plugin.name)

                plugin.log.info("Waiting for file resolution...")
                
                while not has_resolved:
                    if xbmc.abortRequested or dialog.iscanceled():
                        return

                    status = t2h("status")
                    self.display_name = status["name"]
                    global buffer_percentage
                    global extension_message
                    global max_buffer_size
                    extension = self.getFileExtension(self.display_name)
                    BUFFERSIZE = self.getBufferSize(extension_message)
                    
                    if status["state"] >= 0 and buffer_percentage < 100 and BUFFERSIZE != max_buffer_size and extension_message == "":
                        dialog.update(int(buffer_percentage), *self._get_status_lines(status, "")) #buffering
                    elif status["state"] >= 0 and buffer_percentage >= 100 or BUFFERSIZE == max_buffer_size or extension_message != "": 
                        dialog.update(int(status["progress"] * 100), *self._get_status_lines(status, extension_message))#done buffering

                    if status["state"] >= 3 and not has_resolved: # Downloading?
                        files = t2h("ls")["files"]
                        progress = float(t2h("status")["progress"])
                        biggest_file = sorted(files, key=lambda x: x["size"])[-1]
                        biggest_file["name"] = biggest_file["name"].encode("utf-8")

                        # Estimate the video size using the biggest file size
                        # and the progress (progress is: <pcnt downloaded> / 100.0)
                        bytes_complete = float(biggest_file["size"]) * progress
                        mb_complete = bytes_complete / 1024.0 / 1024.0
                        buffer_percentage = (mb_complete / float(plugin.get_setting("min_download_size"))) * 100
                        if buffer_percentage >= 100 and BUFFERSIZE != max_buffer_size:
                            extension_message = self.getExtensionMessage(extension)
                        if extension_message == "File can not fast start. The whole file must download.":
                            BUFFERSIZE = max_buffer_size
                            
                        if mb_complete > BUFFERSIZE or bytes_complete >= biggest_file["size"]:
                            extension_message = ""
                            dialog.update(int(status["progress"] * 100), *self._get_status_lines(status, extension_message))
                            plugin.log.info("Resolving to http://%s/files/%s" % (t2h_instance.bind_address, biggest_file["name"]))
                            has_resolved = True
                            item = {
                                "path": "http://%s/files/%s" % (t2h_instance.bind_address, urllib.quote(biggest_file["name"])),
                            }
                            if not xbmc.getInfoLabel("ListItem.Title"):
                                item["label"] = self.display_name
                            plugin.set_resolved_url(item)
                            break
                    xbmc.sleep(TORRENT2HTTP_POLL)

            # We are now playing
            plugin.log.info("Now playing torrent...")
            last_playing_event = 0
            with closing(OverlayText(w=OVERLAY_WIDTH, h=OVERLAY_HEIGHT, alignment=XBFONT_CENTER_X | XBFONT_CENTER_Y)) as overlay:
                with nested(self.attach(overlay.show, self.on_playback_paused),
                            self.attach(overlay.hide, self.on_playback_resumed, self.on_playback_stopped)):
                    while not xbmc.abortRequested and self.isPlaying():
                        overlay.text = "\n".join(self._get_status_lines(t2h("status"), extension_message))
                        now = time.time()
                        if (now - last_playing_event) > PLAYING_EVENT_INTERVAL:
                            track_event("video", "playing", self.display_name)
                            last_playing_event = now
                        xbmc.sleep(TORRENT2HTTP_POLL)

        plugin.log.info("Closing Torrent player.")
