# -*- coding: utf-8 -*-
import re
if __name__ == '__main__':
    bad_opts = [u'Новости',u'Книги и журналы',u'Обучение иностранным языкам',u'Аудиокниги',u'Музыка',u'Популярная музыка',u'Джазовая и Блюзовая музыка',u'Рок-музыка',
                u'Электронная музыка',u'Hi-Res форматы, оцифровки',u'Игры',u'Программы и Дизайн',u'Мобильные устройства',u'Медицина и здоровье',u'Разное',u'Обсуждения, встречи, общение']
    opt = u"""
    <optgroup label="&nbsp;Новости">
                                            <option id="fs-1289" value="1289" class="root_forum has_sf">Rutracker Awards (мероприятия и конкурсы)&nbsp;</option>
                                            <option id="fs-2214" value="2214"> |- Rutracker Awards (Раздачи)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Кино, Видео и ТВ">
                                            <option id="fs-7" value="7" class="root_forum has_sf">Зарубежное кино&nbsp;</option>
                                            <option id="fs-187" value="187"> |- Классика мирового кинематографа&nbsp;</option>
                                            <option id="fs-2090" value="2090"> |- Фильмы до 1990 года&nbsp;</option>
                                            <option id="fs-2221" value="2221"> |- Фильмы 1991-2000&nbsp;</option>
                                            <option id="fs-2091" value="2091"> |- Фильмы 2001-2005&nbsp;</option>
                                            <option id="fs-2092" value="2092"> |- Фильмы 2006-2010&nbsp;</option>
                                            <option id="fs-2093" value="2093"> |- Фильмы 2011-2015&nbsp;</option>
                                            <option id="fs-2200" value="2200"> |- Фильмы 2016-2017&nbsp;</option>
                                            <option id="fs-1950" value="1950"> |- Фильмы 2018&nbsp;</option>
                                            <option id="fs-2540" value="2540"> |- Фильмы Ближнего Зарубежья&nbsp;</option>
                                            <option id="fs-934" value="934"> |- Азиатские фильмы&nbsp;</option>
                                            <option id="fs-505" value="505"> |- Индийское кино&nbsp;</option>
                                            <option id="fs-212" value="212"> |- Сборники фильмов&nbsp;</option>
                                            <option id="fs-2459" value="2459"> |- Короткий метр&nbsp;</option>
                                            <option id="fs-1235" value="1235"> |- Грайндхаус&nbsp;</option>
                                            <option id="fs-185" value="185"> |- Звуковые дорожки и Переводы&nbsp;</option>
                                            <option id="fs-22" value="22" class="root_forum has_sf">Наше кино&nbsp;</option>
                                            <option id="fs-941" value="941"> |- Кино СССР&nbsp;</option>
                                            <option id="fs-1666" value="1666"> |- Детские отечественные фильмы&nbsp;</option>
                                            <option id="fs-376" value="376"> |- Авторские дебюты&nbsp;</option>
                                            <option id="fs-124" value="124" class="root_forum has_sf">Арт-хаус и авторское кино&nbsp;</option>
                                            <option id="fs-1543" value="1543"> |- Короткий метр (Арт-хаус и авторское кино)&nbsp;</option>
                                            <option id="fs-709" value="709"> |- Документальные фильмы (Арт-хаус и авторское кино)&nbsp;</option>
                                            <option id="fs-1577" value="1577"> |- Анимация (Арт-хаус и авторское кино)&nbsp;</option>
                                            <option id="fs-511" value="511" class="root_forum has_sf">Театр&nbsp;</option>
                                            <option id="fs-93" value="93" class="root_forum has_sf">DVD Video&nbsp;</option>
                                            <option id="fs-905" value="905"> |- Классика мирового кинематографа (DVD Video)&nbsp;</option>
                                            <option id="fs-1576" value="1576"> |- Азиатские фильмы (DVD Video)&nbsp;</option>
                                            <option id="fs-101" value="101"> |- Зарубежное кино (DVD Video)&nbsp;</option>
                                            <option id="fs-100" value="100"> |- Наше кино (DVD Video)&nbsp;</option>
                                            <option id="fs-877" value="877"> |- Фильмы Ближнего Зарубежья (DVD Video)&nbsp;</option>
                                            <option id="fs-572" value="572"> |- Арт-хаус и авторское кино (DVD Video)&nbsp;</option>
                                            <option id="fs-2220" value="2220"> |- Индийское кино (DVD Video)&nbsp;</option>
                                            <option id="fs-1670" value="1670"> |- Грайндхаус (DVD Video)&nbsp;</option>
                                            <option id="fs-2198" value="2198" class="root_forum has_sf">HD Video&nbsp;</option>
                                            <option id="fs-1457" value="1457"> |- UHD Video&nbsp;</option>
                                            <option id="fs-2199" value="2199"> |- Классика мирового кинематографа (HD Video)&nbsp;</option>
                                            <option id="fs-313" value="313"> |- Зарубежное кино (HD Video)&nbsp;</option>
                                            <option id="fs-2201" value="2201"> |- Азиатские фильмы (HD Video)&nbsp;</option>
                                            <option id="fs-312" value="312"> |- Наше кино (HD Video)&nbsp;</option>
                                            <option id="fs-2339" value="2339"> |- Арт-хаус и авторское кино (HD Video)&nbsp;</option>
                                            <option id="fs-140" value="140"> |- Индийское кино (HD Video)&nbsp;</option>
                                            <option id="fs-194" value="194"> |- Грайндхаус (HD Video)&nbsp;</option>
                                            <option id="fs-352" value="352" class="root_forum has_sf">3D/Стерео Кино, Видео, TV и Спорт&nbsp;</option>
                                            <option id="fs-549" value="549"> |- 3D Кинофильмы&nbsp;</option>
                                            <option id="fs-1213" value="1213"> |- 3D Мультфильмы&nbsp;</option>
                                            <option id="fs-2109" value="2109"> |- 3D Документальные фильмы&nbsp;</option>
                                            <option id="fs-514" value="514"> |- 3D Спорт&nbsp;</option>
                                            <option id="fs-2097" value="2097"> |- 3D Ролики, Музыкальное видео, Трейлеры к фильмам&nbsp;</option>
                                            <option id="fs-4" value="4" class="root_forum has_sf">Мультфильмы&nbsp;</option>
                                            <option id="fs-2343" value="2343"> |- Отечественные мультфильмы (HD Video)&nbsp;</option>
                                            <option id="fs-930" value="930"> |- Иностранные мультфильмы (HD Video)&nbsp;</option>
                                            <option id="fs-2365" value="2365"> |- Иностранные короткометражные мультфильмы (HD Video)&nbsp;</option>
                                            <option id="fs-1900" value="1900"> |- Отечественные мультфильмы (DVD)&nbsp;</option>
                                            <option id="fs-521" value="521"> |- Иностранные мультфильмы (DVD)&nbsp;</option>
                                            <option id="fs-2258" value="2258"> |- Иностранные короткометражные мультфильмы (DVD)&nbsp;</option>
                                            <option id="fs-208" value="208"> |- Отечественные мультфильмы&nbsp;</option>
                                            <option id="fs-539" value="539"> |- Отечественные полнометражные мультфильмы&nbsp;</option>
                                            <option id="fs-209" value="209"> |- Иностранные мультфильмы&nbsp;</option>
                                            <option id="fs-484" value="484"> |- Иностранные короткометражные мультфильмы&nbsp;</option>
                                            <option id="fs-822" value="822"> |- Сборники мультфильмов&nbsp;</option>
                                            <option id="fs-921" value="921" class="root_forum has_sf">Мультсериалы&nbsp;</option>
                                            <option id="fs-815" value="815"> |- Мультсериалы (SD Video)&nbsp;</option>
                                            <option id="fs-816" value="816"> |- Мультсериалы (DVD Video)&nbsp;</option>
                                            <option id="fs-1460" value="1460"> |- Мультсериалы (HD Video)&nbsp;</option>
                                            <option id="fs-33" value="33" class="root_forum has_sf">Аниме&nbsp;</option>
                                            <option id="fs-2484" value="2484"> |- Артбуки и журналы (Аниме)&nbsp;</option>
                                            <option id="fs-1386" value="1386"> |- Обои, сканы, аватары, арт&nbsp;</option>
                                            <option id="fs-1387" value="1387"> |- AMV и другие ролики&nbsp;</option>
                                            <option id="fs-599" value="599"> |- Аниме (DVD)&nbsp;</option>
                                            <option id="fs-1105" value="1105"> |- Аниме (HD Video)&nbsp;</option>
                                            <option id="fs-1389" value="1389"> |- Аниме (основной подраздел)&nbsp;</option>
                                            <option id="fs-1391" value="1391"> |- Аниме (плеерный подраздел)&nbsp;</option>
                                            <option id="fs-2491" value="2491"> |- Аниме (QC подраздел)&nbsp;</option>
                                            <option id="fs-404" value="404"> |- Покемоны&nbsp;</option>
                                            <option id="fs-1390" value="1390"> |- Наруто&nbsp;</option>
                                            <option id="fs-1642" value="1642"> |- Гандам&nbsp;</option>
                                            <option id="fs-893" value="893"> |- Японские мультфильмы&nbsp;</option>
                                            <option id="fs-809" value="809"> |- Звуковые дорожки и Переводы (Аниме)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Сериалы">
                                            <option id="fs-9" value="9" class="root_forum has_sf">Русские сериалы&nbsp;</option>
                                            <option id="fs-80" value="80"> |- Возвращение Мухтара&nbsp;</option>
                                            <option id="fs-1535" value="1535"> |- Воронины&nbsp;</option>
                                            <option id="fs-856" value="856"> |- Глухарь / Пятницкий / Карпов&nbsp;</option>
                                            <option id="fs-188" value="188"> |- Земский доктор&nbsp;</option>
                                            <option id="fs-202" value="202"> |- Каменская&nbsp;</option>
                                            <option id="fs-91" value="91"> |- Кухня / Отель Элеон&nbsp;</option>
                                            <option id="fs-805" value="805"> |- Ментовские войны&nbsp;</option>
                                            <option id="fs-172" value="172"> |- Молодежка / Интерны&nbsp;</option>
                                            <option id="fs-1356" value="1356"> |- Морские дьяволы&nbsp;</option>
                                            <option id="fs-119" value="119"> |- Москва. Три вокзала&nbsp;</option>
                                            <option id="fs-990" value="990"> |- Нюхач&nbsp;</option>
                                            <option id="fs-935" value="935"> |- Обратная сторона Луны&nbsp;</option>
                                            <option id="fs-1408" value="1408"> |- Ольга / Физрук&nbsp;</option>
                                            <option id="fs-123" value="123"> |- Пуля Дура&nbsp;</option>
                                            <option id="fs-310" value="310"> |- Сваты&nbsp;</option>
                                            <option id="fs-175" value="175"> |- След&nbsp;</option>
                                            <option id="fs-79" value="79"> |- Солдаты и пр.&nbsp;</option>
                                            <option id="fs-104" value="104"> |- Тайны следствия&nbsp;</option>
                                            <option id="fs-812" value="812"> |- Улицы разбитых фонарей (Менты) / Опера / Убойная сила&nbsp;</option>
                                            <option id="fs-189" value="189" class="root_forum has_sf">Зарубежные сериалы&nbsp;</option>
                                            <option id="fs-842" value="842"> |- Новинки и сериалы в стадии показа&nbsp;</option>
                                            <option id="fs-235" value="235"> |- Сериалы США и Канады&nbsp;</option>
                                            <option id="fs-242" value="242"> |- Сериалы Великобритании и Ирландии&nbsp;</option>
                                            <option id="fs-819" value="819"> |- Скандинавские сериалы&nbsp;</option>
                                            <option id="fs-1531" value="1531"> |- Испанские сериалы&nbsp;</option>
                                            <option id="fs-721" value="721"> |- Итальянские сериалы&nbsp;</option>
                                            <option id="fs-1102" value="1102"> |- Европейские сериалы&nbsp;</option>
                                            <option id="fs-1120" value="1120"> |- Сериалы стран Африки, Ближнего и Среднего Востока&nbsp;</option>
                                            <option id="fs-1214" value="1214"> |- Сериалы Австралии и Новой Зеландии&nbsp;</option>
                                            <option id="fs-387" value="387"> |- Сериалы совместного производства нескольких стран&nbsp;</option>
                                            <option id="fs-1359" value="1359"> |- Веб-сериалы, Вебизоды к сериалам и Пилотные серии сериалов&nbsp;</option>
                                            <option id="fs-271" value="271"> |- 24 часа / 24&nbsp;</option>
                                            <option id="fs-743" value="743"> |- Анатомия Грей + Частная Практика&nbsp;</option>
                                            <option id="fs-184" value="184"> |- Бесстыжие / Shameless (US)&nbsp;</option>
                                            <option id="fs-85" value="85"> |- Вавилон 5 / Babylon 5&nbsp;</option>
                                            <option id="fs-1171" value="1171"> |- Викинги / Vikings&nbsp;</option>
                                            <option id="fs-1417" value="1417"> |- Во все тяжкие / Breaking Bad&nbsp;</option>
                                            <option id="fs-595" value="595"> |- Герои / Heroes&nbsp;</option>
                                            <option id="fs-1288" value="1288"> |- Декстер / Dexter&nbsp;</option>
                                            <option id="fs-1605" value="1605"> |- Два с половиной человека / Two and a Half Men&nbsp;</option>
                                            <option id="fs-1690" value="1690"> |- Дневники вампира + Настоящая кровь&nbsp;</option>
                                            <option id="fs-820" value="820"> |- Доктор Кто + Торчвуд&nbsp;</option>
                                            <option id="fs-625" value="625"> |- Доктор Хаус / House M.D.&nbsp;</option>
                                            <option id="fs-84" value="84"> |- Друзья + Джоуи&nbsp;</option>
                                            <option id="fs-623" value="623"> |- За Гранью / Fringe&nbsp;</option>
                                            <option id="fs-1798" value="1798"> |- Звёздные Врата : Атлантида; Вселенная&nbsp;</option>
                                            <option id="fs-106" value="106"> |- Звёздные Врата: СГ1 / Stargate: SG1&nbsp;</option>
                                            <option id="fs-166" value="166"> |- Звёздный крейсер Галактика + Каприка&nbsp;</option>
                                            <option id="fs-236" value="236"> |- Звёздный путь / Star Trek&nbsp;</option>
                                            <option id="fs-1449" value="1449"> |- Игра престолов / Game of Thrones&nbsp;</option>
                                            <option id="fs-273" value="273"> |- Карточный Домик / House of Cards&nbsp;</option>
                                            <option id="fs-504" value="504"> |- Клан Сопрано / The Sopranos&nbsp;</option>
                                            <option id="fs-920" value="920"> |- Кости / Bones&nbsp;</option>
                                            <option id="fs-636" value="636"> |- Менталист + Касл&nbsp;</option>
                                            <option id="fs-606" value="606"> |- Место преступления / CSI: Crime Scene Investigation&nbsp;</option>
                                            <option id="fs-181" value="181"> |- Морская полиция: Спецотдел; Лос-Анджелес; Новый Орлеан&nbsp;</option>
                                            <option id="fs-918" value="918"> |- Оранжевый — хит сезона / Orange Is the New Black&nbsp;</option>
                                            <option id="fs-81" value="81"> |- Остаться в Живых / LOST&nbsp;</option>
                                            <option id="fs-266" value="266"> |- Отчаянные домохозяйки / Desperate Housewives&nbsp;</option>
                                            <option id="fs-252" value="252"> |- Побег из тюрьмы / Prison Break&nbsp;</option>
                                            <option id="fs-372" value="372"> |- Сверхъестественное / Supernatural&nbsp;</option>
                                            <option id="fs-110" value="110"> |- Секретные материалы / The X-Files&nbsp;</option>
                                            <option id="fs-193" value="193"> |- Секс в большом городе / Sex And The City&nbsp;</option>
                                            <option id="fs-121" value="121"> |- Твин пикс / Twin Peaks&nbsp;</option>
                                            <option id="fs-507" value="507"> |- Теория большого взрыва / The Big Bang Theory&nbsp;</option>
                                            <option id="fs-536" value="536"> |- Форс-мажоры / Костюмы в законе / Suits&nbsp;</option>
                                            <option id="fs-1144" value="1144"> |- Ходячие мертвецы + Бойтесь ходячих мертвецов&nbsp;</option>
                                            <option id="fs-173" value="173"> |- Черное зеркало / Black Mirror&nbsp;</option>
                                            <option id="fs-195" value="195"> |- Для некондиционных раздач&nbsp;</option>
                                            <option id="fs-2366" value="2366" class="root_forum has_sf">Зарубежные сериалы (HD Video)&nbsp;</option>
                                            <option id="fs-2390" value="2390"> |- Два с половиной человека / Two and a Half Men (HD Video)&nbsp;</option>
                                            <option id="fs-2391" value="2391"> |- Декстер / Dexter (HD Video)&nbsp;</option>
                                            <option id="fs-1669" value="1669"> |- Викинги / Vikings (HD Video)&nbsp;</option>
                                            <option id="fs-2392" value="2392"> |- Друзья / Friends (HD Video)&nbsp;</option>
                                            <option id="fs-2407" value="2407"> |- Доктор Кто + Торчвуд (HD Video)&nbsp;</option>
                                            <option id="fs-2393" value="2393"> |- Доктор Хаус / House M.D. (HD Video)&nbsp;</option>
                                            <option id="fs-2370" value="2370"> |- За Гранью / Fringe (HD Video)&nbsp;</option>
                                            <option id="fs-2394" value="2394"> |- Звёздные Врата (HD Video)&nbsp;</option>
                                            <option id="fs-2408" value="2408"> |- Звёздный крейсер Галактика + Каприка (HD Video)&nbsp;</option>
                                            <option id="fs-2395" value="2395"> |- Звёздный путь / Star Trek (HD Video)&nbsp;</option>
                                            <option id="fs-265" value="265"> |- Игра престолов / Game of Thrones (HD Video)&nbsp;</option>
                                            <option id="fs-2406" value="2406"> |- Карточный домик (HD Video)&nbsp;</option>
                                            <option id="fs-2397" value="2397"> |- Кости / Bones (HD Video)&nbsp;</option>
                                            <option id="fs-2399" value="2399"> |- Менталист + Касл (HD Video)&nbsp;</option>
                                            <option id="fs-2400" value="2400"> |- Место преступления / CSI: Crime Scene Investigation (HD Video)&nbsp;</option>
                                            <option id="fs-2402" value="2402"> |- Остаться в Живых / LOST (HD Video)&nbsp;</option>
                                            <option id="fs-2403" value="2403"> |- Побег из тюрьмы / Prison Break (HD Video)&nbsp;</option>
                                            <option id="fs-2404" value="2404"> |- Сверхъестественное / Supernatural (HD Video)&nbsp;</option>
                                            <option id="fs-2405" value="2405"> |- Секретные материалы / The X-Files (HD Video)&nbsp;</option>
                                            <option id="fs-2396" value="2396"> |- Теория Большого Взрыва / The Big Bang Theory (HD Video)&nbsp;</option>
                                            <option id="fs-2398" value="2398"> |- Ходячие мертвецы + Бойтесь ходячих мертвецов (HD Video)&nbsp;</option>
                                            <option id="fs-1949" value="1949"> |- Черное зеркало / Black Mirror (HD Video)&nbsp;</option>
                                            <option id="fs-1498" value="1498"> |- Для некондиционных раздач (HD Video)&nbsp;</option>
                                            <option id="fs-911" value="911" class="root_forum has_sf">Сериалы Латинской Америки, Турции и Индии&nbsp;</option>
                                            <option id="fs-1493" value="1493"> |- Актёры и актрисы латиноамериканских сериалов&nbsp;</option>
                                            <option id="fs-325" value="325"> |- Сериалы Аргентины&nbsp;</option>
                                            <option id="fs-534" value="534"> |- Сериалы Бразилии&nbsp;</option>
                                            <option id="fs-594" value="594"> |- Сериалы Венесуэлы&nbsp;</option>
                                            <option id="fs-1301" value="1301"> |- Сериалы Индии&nbsp;</option>
                                            <option id="fs-607" value="607"> |- Сериалы Колумбии&nbsp;</option>
                                            <option id="fs-1574" value="1574"> |- Сериалы Латинской Америки с озвучкой (раздачи папками)&nbsp;</option>
                                            <option id="fs-1539" value="1539"> |- Сериалы Латинской Америки с субтитрами&nbsp;</option>
                                            <option id="fs-1940" value="1940"> |- Официальные краткие версии сериалов Латинской Америки&nbsp;</option>
                                            <option id="fs-694" value="694"> |- Сериалы Мексики&nbsp;</option>
                                            <option id="fs-775" value="775"> |- Сериалы Перу, Сальвадора, Чили и других стран&nbsp;</option>
                                            <option id="fs-781" value="781"> |- Сериалы совместного производства&nbsp;</option>
                                            <option id="fs-718" value="718"> |- Сериалы США (латиноамериканские)&nbsp;</option>
                                            <option id="fs-704" value="704"> |- Сериалы Турции&nbsp;</option>
                                            <option id="fs-1537" value="1537"> |- Для некондиционных раздач&nbsp;</option>
                                            <option id="fs-1500" value="1500"> |- OST Сериалы Латинской Америки, Турции и Индии (lossy и lossless)&nbsp;</option>
                                            <option id="fs-2100" value="2100" class="root_forum has_sf">Азиатские сериалы&nbsp;</option>
                                            <option id="fs-717" value="717"> |- Китайские сериалы с субтитрами&nbsp;</option>
                                            <option id="fs-915" value="915"> |- Корейские сериалы с озвучкой&nbsp;</option>
                                            <option id="fs-1242" value="1242"> |- Корейские сериалы с субтитрами&nbsp;</option>
                                            <option id="fs-2412" value="2412"> |- Прочие азиатские сериалы с озвучкой&nbsp;</option>
                                            <option id="fs-1938" value="1938"> |- Тайваньские сериалы с субтитрами&nbsp;</option>
                                            <option id="fs-2104" value="2104"> |- Японские сериалы с субтитрами&nbsp;</option>
                                            <option id="fs-1939" value="1939"> |- Японские сериалы с озвучкой&nbsp;</option>
                                            <option id="fs-2102" value="2102"> |- VMV и др. ролики&nbsp;</option>
                                            <option id="fs-2103" value="2103"> |- OST Азиатские сериалы (lossy и lossless)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Документалистика и юмор">
                                            <option id="fs-670" value="670" class="root_forum has_sf">Вера и религия&nbsp;</option>
                                            <option id="fs-1475" value="1475"> |- [Видео Религия] Христианство&nbsp;</option>
                                            <option id="fs-2107" value="2107"> |- [Видео Религия] Ислам&nbsp;</option>
                                            <option id="fs-294" value="294"> |- [Видео Религия] Религии Индии, Тибета и Восточной Азии&nbsp;</option>
                                            <option id="fs-1453" value="1453"> |- [Видео Религия] Культы и новые религиозные движения&nbsp;</option>
                                            <option id="fs-46" value="46" class="root_forum has_sf">Документальные фильмы и телепередачи&nbsp;</option>
                                            <option id="fs-103" value="103"> |- Документальные (DVD)&nbsp;</option>
                                            <option id="fs-671" value="671"> |- [Док] Биографии. Личности и кумиры&nbsp;</option>
                                            <option id="fs-2177" value="2177"> |- [Док] Кинематограф и мультипликация&nbsp;</option>
                                            <option id="fs-656" value="656"> |- [Док] Мастера искусств Театра и Кино&nbsp;</option>
                                            <option id="fs-2538" value="2538"> |- [Док] Искусство, история искусств&nbsp;</option>
                                            <option id="fs-2159" value="2159"> |- [Док] Музыка&nbsp;</option>
                                            <option id="fs-251" value="251"> |- [Док] Криминальная документалистика&nbsp;</option>
                                            <option id="fs-98" value="98"> |- [Док] Тайны века / Спецслужбы / Теории Заговоров&nbsp;</option>
                                            <option id="fs-97" value="97"> |- [Док] Военное дело&nbsp;</option>
                                            <option id="fs-851" value="851"> |- [Док] Вторая мировая война&nbsp;</option>
                                            <option id="fs-2178" value="2178"> |- [Док] Аварии / Катастрофы / Катаклизмы&nbsp;</option>
                                            <option id="fs-821" value="821"> |- [Док] Авиация&nbsp;</option>
                                            <option id="fs-2076" value="2076"> |- [Док] Космос&nbsp;</option>
                                            <option id="fs-56" value="56"> |- [Док] Научно-популярные фильмы&nbsp;</option>
                                            <option id="fs-2123" value="2123"> |- [Док] Флора и фауна&nbsp;</option>
                                            <option id="fs-876" value="876"> |- [Док] Путешествия и туризм&nbsp;</option>
                                            <option id="fs-2380" value="2380"> |- [Док] Социальные ток-шоу&nbsp;</option>
                                            <option id="fs-1467" value="1467" title="[Док] Информационно-аналитические и общественно-политические передачи"> |- [Док] Информационно-аналитические и общественно-политические перед..&nbsp;</option>
                                            <option id="fs-1469" value="1469"> |- [Док] Архитектура и строительство&nbsp;</option>
                                            <option id="fs-672" value="672"> |- [Док] Всё о доме, быте и дизайне&nbsp;</option>
                                            <option id="fs-249" value="249"> |- [Док] BBC&nbsp;</option>
                                            <option id="fs-552" value="552"> |- [Док] Discovery&nbsp;</option>
                                            <option id="fs-500" value="500"> |- [Док] National Geographic&nbsp;</option>
                                            <option id="fs-2112" value="2112"> |- [Док] История: Древний мир / Античность / Средневековье&nbsp;</option>
                                            <option id="fs-1327" value="1327"> |- [Док] История: Новое и Новейшее время&nbsp;</option>
                                            <option id="fs-1468" value="1468"> |- [Док] Эпоха СССР&nbsp;</option>
                                            <option id="fs-1280" value="1280" title="[Док] Битва экстрасенсов / Теория невероятности / Искатели / Галилео"> |- [Док] Битва экстрасенсов / Теория невероятности / Искатели / Галил..&nbsp;</option>
                                            <option id="fs-752" value="752"> |- [Док] Русские сенсации / Программа Максимум / Профессия репортёр&nbsp;</option>
                                            <option id="fs-1114" value="1114"> |- [Док] Паранормальные явления&nbsp;</option>
                                            <option id="fs-2168" value="2168"> |- [Док] Альтернативная история и наука&nbsp;</option>
                                            <option id="fs-2160" value="2160"> |- [Док] Внежанровая документалистика&nbsp;</option>
                                            <option id="fs-2176" value="2176"> |- [Док] Разное / некондиция&nbsp;</option>
                                            <option id="fs-314" value="314" class="root_forum has_sf">Документальные (HD Video)&nbsp;</option>
                                            <option id="fs-2323" value="2323"> |- Информационно-аналитические и общественно-политические (HD Video)&nbsp;</option>
                                            <option id="fs-1278" value="1278"> |- Биографии. Личности и кумиры (HD Video)&nbsp;</option>
                                            <option id="fs-1281" value="1281"> |- Военное дело (HD Video)&nbsp;</option>
                                            <option id="fs-2110" value="2110"> |- Естествознание, наука и техника (HD Video)&nbsp;</option>
                                            <option id="fs-979" value="979"> |- Путешествия и туризм (HD Video)&nbsp;</option>
                                            <option id="fs-2169" value="2169"> |- Флора и фауна (HD Video)&nbsp;</option>
                                            <option id="fs-2166" value="2166"> |- История (HD Video)&nbsp;</option>
                                            <option id="fs-2164" value="2164"> |- BBC, Discovery, National Geographic (HD Video)&nbsp;</option>
                                            <option id="fs-2163" value="2163"> |- Криминальная документалистика (HD Video)&nbsp;</option>
                                            <option id="fs-24" value="24" class="root_forum has_sf">Развлекательные телепередачи и шоу, приколы и юмор&nbsp;</option>
                                            <option id="fs-1959" value="1959"> |- [Видео Юмор] Интеллектуальные игры и викторины&nbsp;</option>
                                            <option id="fs-939" value="939"> |- [Видео Юмор] Реалити и ток-шоу / номинации / показы&nbsp;</option>
                                            <option id="fs-1481" value="1481"> |- [Видео Юмор] Детские телешоу&nbsp;</option>
                                            <option id="fs-113" value="113"> |- [Видео Юмор] КВН&nbsp;</option>
                                            <option id="fs-115" value="115"> |- [Видео Юмор] Пост КВН&nbsp;</option>
                                            <option id="fs-882" value="882"> |- [Видео Юмор] Кривое Зеркало / Городок / В Городке&nbsp;</option>
                                            <option id="fs-1482" value="1482"> |- [Видео Юмор] Ледовые шоу&nbsp;</option>
                                            <option id="fs-393" value="393"> |- [Видео Юмор] Музыкальные шоу&nbsp;</option>
                                            <option id="fs-1569" value="1569"> |- [Видео Юмор] Званый ужин&nbsp;</option>
                                            <option id="fs-373" value="373"> |- [Видео Юмор] Хорошие Шутки&nbsp;</option>
                                            <option id="fs-1186" value="1186"> |- [Видео Юмор] Вечерний Квартал&nbsp;</option>
                                            <option id="fs-137" value="137"> |- [Видео Юмор] Фильмы со смешным переводом (пародии)&nbsp;</option>
                                            <option id="fs-2537" value="2537"> |- [Видео Юмор] Stand-up comedy&nbsp;</option>
                                            <option id="fs-532" value="532"> |- [Видео Юмор] Украинские Шоу&nbsp;</option>
                                            <option id="fs-827" value="827"> |- [Видео Юмор] Танцевальные шоу, концерты, выступления&nbsp;</option>
                                            <option id="fs-1484" value="1484"> |- [Видео Юмор] Цирк&nbsp;</option>
                                            <option id="fs-1485" value="1485"> |- [Видео Юмор] Школа злословия&nbsp;</option>
                                            <option id="fs-114" value="114"> |- [Видео Юмор] Сатирики и юмористы&nbsp;</option>
                                            <option id="fs-1332" value="1332"> |- Юмористические аудиопередачи&nbsp;</option>
                                            <option id="fs-1495" value="1495"> |- Аудио и видео ролики (Приколы и юмор)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Спорт">
                                            <option id="fs-1315" value="1315" class="root_forum has_sf">Зимние Олимпийские игры 2018&nbsp;</option>
                                            <option id="fs-1336" value="1336"> |- Биатлон&nbsp;</option>
                                            <option id="fs-2171" value="2171"> |- Лыжные гонки&nbsp;</option>
                                            <option id="fs-1339" value="1339"> |- Прыжки на лыжах с трамплина / Лыжное двоеборье&nbsp;</option>
                                            <option id="fs-2455" value="2455"> |- Горные лыжи / Сноубординг / Фристайл&nbsp;</option>
                                            <option id="fs-1434" value="1434"> |- Бобслей / Санный спорт / Скелетон&nbsp;</option>
                                            <option id="fs-2350" value="2350"> |- Конькобежный спорт / Шорт-трек&nbsp;</option>
                                            <option id="fs-1472" value="1472"> |- Фигурное катание&nbsp;</option>
                                            <option id="fs-2068" value="2068"> |- Хоккей&nbsp;</option>
                                            <option id="fs-2016" value="2016"> |- Керлинг&nbsp;</option>
                                            <option id="fs-1311" value="1311"> |- Обзорные и аналитические программы&nbsp;</option>
                                            <option id="fs-255" value="255" class="root_forum has_sf">Спортивные турниры, фильмы и передачи&nbsp;</option>
                                            <option id="fs-256" value="256"> |- Автоспорт&nbsp;</option>
                                            <option id="fs-1986" value="1986"> |- Мотоспорт&nbsp;</option>
                                            <option id="fs-660" value="660"> |- Формула-1 (2018)&nbsp;</option>
                                            <option id="fs-1551" value="1551"> |- Формула-1 (2012-2017)&nbsp;</option>
                                            <option id="fs-626" value="626"> |- Формула 1 (до 2011 вкл.)&nbsp;</option>
                                            <option id="fs-262" value="262"> |- Велоспорт&nbsp;</option>
                                            <option id="fs-1326" value="1326"> |- Волейбол/Гандбол&nbsp;</option>
                                            <option id="fs-978" value="978"> |- Бильярд&nbsp;</option>
                                            <option id="fs-1287" value="1287"> |- Покер&nbsp;</option>
                                            <option id="fs-1188" value="1188"> |- Бодибилдинг/Силовые виды спорта&nbsp;</option>
                                            <option id="fs-1667" value="1667"> |- Бокс&nbsp;</option>
                                            <option id="fs-1675" value="1675"> |- Классические единоборства&nbsp;</option>
                                            <option id="fs-257" value="257"> |- Смешанные единоборства и K-1&nbsp;</option>
                                            <option id="fs-875" value="875"> |- Американский футбол&nbsp;</option>
                                            <option id="fs-263" value="263"> |- Регби&nbsp;</option>
                                            <option id="fs-2073" value="2073"> |- Бейсбол&nbsp;</option>
                                            <option id="fs-550" value="550"> |- Теннис&nbsp;</option>
                                            <option id="fs-2124" value="2124"> |- Бадминтон/Настольный теннис&nbsp;</option>
                                            <option id="fs-1470" value="1470"> |- Гимнастика/Соревнования по танцам&nbsp;</option>
                                            <option id="fs-528" value="528"> |- Лёгкая атлетика/Водные виды спорта&nbsp;</option>
                                            <option id="fs-486" value="486"> |- Зимние виды спорта&nbsp;</option>
                                            <option id="fs-854" value="854"> |- Фигурное катание&nbsp;</option>
                                            <option id="fs-2079" value="2079"> |- Биатлон&nbsp;</option>
                                            <option id="fs-260" value="260"> |- Экстрим&nbsp;</option>
                                            <option id="fs-1319" value="1319"> |- Спорт (видео)&nbsp;</option>
                                            <option id="fs-1608" value="1608" class="root_forum has_sf">Футбол&nbsp;</option>
                                            <option id="fs-2533" value="2533"> |- &#9917; Чемпионат Мира 2018 (плей-офф финального турнира)&nbsp;</option>
                                            <option id="fs-497" value="497"> |- Чемпионат Мира 2018 (групповой этап финального турнира)&nbsp;</option>
                                            <option id="fs-1952" value="1952"> |- Чемпионат Мира 2018 (обзорные передачи, документалистика)&nbsp;</option>
                                            <option id="fs-1668" value="1668"> |- Чемпионат Мира 2018 (отборочный турнир)&nbsp;</option>
                                            <option id="fs-1621" value="1621"> |- Чемпионаты Мира&nbsp;</option>
                                            <option id="fs-2075" value="2075"> |- Россия 2018-2019&nbsp;</option>
                                            <option id="fs-592" value="592"> |- Лига Наций 2018&nbsp;</option>
                                            <option id="fs-1998" value="1998"> |- Товарищеские турниры и матчи&nbsp;</option>
                                            <option id="fs-1613" value="1613"> |- Россия/СССР&nbsp;</option>
                                            <option id="fs-1614" value="1614"> |- Англия&nbsp;</option>
                                            <option id="fs-1623" value="1623"> |- Испания&nbsp;</option>
                                            <option id="fs-1615" value="1615"> |- Италия&nbsp;</option>
                                            <option id="fs-1630" value="1630"> |- Германия&nbsp;</option>
                                            <option id="fs-2425" value="2425"> |- Франция&nbsp;</option>
                                            <option id="fs-2514" value="2514"> |- Украина&nbsp;</option>
                                            <option id="fs-1616" value="1616"> |- Другие национальные чемпионаты и кубки&nbsp;</option>
                                            <option id="fs-2014" value="2014"> |- Международные турниры&nbsp;</option>
                                            <option id="fs-1442" value="1442"> |- Еврокубки 2018-2019&nbsp;</option>
                                            <option id="fs-1491" value="1491"> |- Еврокубки 2017-2018&nbsp;</option>
                                            <option id="fs-1987" value="1987"> |- Еврокубки 2011-2017&nbsp;</option>
                                            <option id="fs-1617" value="1617"> |- Еврокубки&nbsp;</option>
                                            <option id="fs-1620" value="1620"> |- Чемпионаты Европы&nbsp;</option>
                                            <option id="fs-1343" value="1343"> |- Обзорные и аналитические передачи 2018-2019&nbsp;</option>
                                            <option id="fs-751" value="751"> |- Обзорные и аналитические передачи&nbsp;</option>
                                            <option id="fs-1697" value="1697"> |- Мини-футбол/Пляжный футбол&nbsp;</option>
                                            <option id="fs-2004" value="2004" class="root_forum has_sf">Баскетбол&nbsp;</option>
                                            <option id="fs-2001" value="2001"> |- Международные соревнования&nbsp;</option>
                                            <option id="fs-2002" value="2002"> |- NBA / NCAA (до 2000 г.)&nbsp;</option>
                                            <option id="fs-283" value="283"> |- NBA / NCAA (2000-2010 гг.)&nbsp;</option>
                                            <option id="fs-1997" value="1997"> |- NBA / NCAA (2010-2018 гг.)&nbsp;</option>
                                            <option id="fs-2003" value="2003"> |- Европейский клубный баскетбол&nbsp;</option>
                                            <option id="fs-2009" value="2009" class="root_forum has_sf">Хоккей&nbsp;</option>
                                            <option id="fs-2010" value="2010"> |- Хоккей с мячом / Бенди&nbsp;</option>
                                            <option id="fs-2006" value="2006"> |- Международные турниры&nbsp;</option>
                                            <option id="fs-2007" value="2007"> |- КХЛ&nbsp;</option>
                                            <option id="fs-2005" value="2005"> |- НХЛ (до 2011/12)&nbsp;</option>
                                            <option id="fs-259" value="259"> |- НХЛ (с 2013)&nbsp;</option>
                                            <option id="fs-2008" value="2008"> |- СССР - Канада&nbsp;</option>
                                            <option id="fs-126" value="126"> |- Документальные фильмы и аналитика&nbsp;</option>
                                            <option id="fs-845" value="845" class="root_forum has_sf">Рестлинг&nbsp;</option>
                                            <option id="fs-343" value="343"> |- Professional Wrestling&nbsp;</option>
                                            <option id="fs-2111" value="2111"> |- Independent Wrestling&nbsp;</option>
                                            <option id="fs-1527" value="1527"> |- International Wrestling&nbsp;</option>
                                            <option id="fs-2069" value="2069"> |- Oldschool Wrestling&nbsp;</option>
                                            <option id="fs-1323" value="1323"> |- Documentary Wrestling&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Книги и журналы">
                                            <option id="fs-1411" value="1411"> |- Сканирование, обработка сканов&nbsp;</option>
                                            <option id="fs-21" value="21" class="root_forum has_sf">Книги и журналы (общий раздел)&nbsp;</option>
                                            <option id="fs-2157" value="2157"> |- Кино, театр, ТВ, мультипликация, цирк&nbsp;</option>
                                            <option id="fs-765" value="765"> |- Рисунок, графический дизайн&nbsp;</option>
                                            <option id="fs-2019" value="2019"> |- Фото и видеосъемка&nbsp;</option>
                                            <option id="fs-31" value="31"> |- Журналы и газеты (общий раздел)&nbsp;</option>
                                            <option id="fs-1427" value="1427"> |- Эзотерика, гадания, магия, фен-шуй&nbsp;</option>
                                            <option id="fs-2422" value="2422"> |- Астрология&nbsp;</option>
                                            <option id="fs-2195" value="2195"> |- Красота. Уход. Домоводство&nbsp;</option>
                                            <option id="fs-2521" value="2521"> |- Мода. Стиль. Этикет&nbsp;</option>
                                            <option id="fs-2223" value="2223"> |- Путешествия и туризм&nbsp;</option>
                                            <option id="fs-2447" value="2447"> |- Знаменитости и кумиры&nbsp;</option>
                                            <option id="fs-39" value="39"> |- Разное (книги)&nbsp;</option>
                                            <option id="fs-1101" value="1101" class="root_forum has_sf">Для детей, родителей и учителей&nbsp;</option>
                                            <option id="fs-745" value="745" title="Учебная литература для детского сада и начальной школы (до 4 класса)"> |- Учебная литература для детского сада и начальной школы (до 4 класс..&nbsp;</option>
                                            <option id="fs-1689" value="1689"> |- Учебная литература для старших классов (5-11 класс)&nbsp;</option>
                                            <option id="fs-2336" value="2336"> |- Учителям и педагогам&nbsp;</option>
                                            <option id="fs-2337" value="2337"> |- Научно-популярная и познавательная литература (для детей)&nbsp;</option>
                                            <option id="fs-1353" value="1353"> |- Досуг и творчество&nbsp;</option>
                                            <option id="fs-1400" value="1400"> |- Воспитание и развитие&nbsp;</option>
                                            <option id="fs-1415" value="1415"> |- Худ. лит-ра для дошкольников и младших классов&nbsp;</option>
                                            <option id="fs-2046" value="2046"> |- Худ. лит-ра для средних и старших классов&nbsp;</option>
                                            <option id="fs-1802" value="1802" class="root_forum has_sf">Спорт, физическая культура, боевые искусства&nbsp;</option>
                                            <option id="fs-2189" value="2189"> |- Футбол (книги и журналы)&nbsp;</option>
                                            <option id="fs-2190" value="2190"> |- Хоккей (книги и журналы)&nbsp;</option>
                                            <option id="fs-2443" value="2443"> |- Игровые виды спорта&nbsp;</option>
                                            <option id="fs-1477" value="1477"> |- Легкая атлетика. Плавание. Гимнастика. Тяжелая атлетика. Гребля&nbsp;</option>
                                            <option id="fs-669" value="669"> |- Автоспорт. Мотоспорт. Велоспорт&nbsp;</option>
                                            <option id="fs-2196" value="2196"> |- Шахматы. Шашки&nbsp;</option>
                                            <option id="fs-2056" value="2056"> |- Боевые искусства, единоборства&nbsp;</option>
                                            <option id="fs-1436" value="1436"> |- Экстрим (книги)&nbsp;</option>
                                            <option id="fs-2191" value="2191"> |- Физкультура, фитнес, бодибилдинг&nbsp;</option>
                                            <option id="fs-2477" value="2477"> |- Спортивная пресса&nbsp;</option>
                                            <option id="fs-1680" value="1680" class="root_forum has_sf">Гуманитарные науки&nbsp;</option>
                                            <option id="fs-1684" value="1684"> |- Искусствоведение. Культурология&nbsp;</option>
                                            <option id="fs-2446" value="2446"> |- Фольклор. Эпос. Мифология&nbsp;</option>
                                            <option id="fs-2524" value="2524"> |- Литературоведение&nbsp;</option>
                                            <option id="fs-2525" value="2525"> |- Лингвистика&nbsp;</option>
                                            <option id="fs-995" value="995"> |- Философия&nbsp;</option>
                                            <option id="fs-2022" value="2022"> |- Политология&nbsp;</option>
                                            <option id="fs-2471" value="2471"> |- Социология&nbsp;</option>
                                            <option id="fs-2375" value="2375"> |- Публицистика, журналистика&nbsp;</option>
                                            <option id="fs-764" value="764"> |- Бизнес, менеджмент&nbsp;</option>
                                            <option id="fs-1685" value="1685"> |- Маркетинг&nbsp;</option>
                                            <option id="fs-1688" value="1688"> |- Экономика&nbsp;</option>
                                            <option id="fs-2472" value="2472"> |- Финансы&nbsp;</option>
                                            <option id="fs-1687" value="1687"> |- Юридические науки. Право. Криминалистика&nbsp;</option>
                                            <option id="fs-2020" value="2020" class="root_forum has_sf">Исторические науки&nbsp;</option>
                                            <option id="fs-1349" value="1349"> |- Методология и философия исторической науки&nbsp;</option>
                                            <option id="fs-1967" value="1967"> |- Исторические источники (книги, периодика)&nbsp;</option>
                                            <option id="fs-1341" value="1341"> |- Исторические источники (документы)&nbsp;</option>
                                            <option id="fs-2049" value="2049"> |- Исторические персоны&nbsp;</option>
                                            <option id="fs-1681" value="1681"> |- Альтернативные исторические теории&nbsp;</option>
                                            <option id="fs-2319" value="2319"> |- Археология&nbsp;</option>
                                            <option id="fs-2434" value="2434"> |- Древний мир. Античность&nbsp;</option>
                                            <option id="fs-1683" value="1683"> |- Средние века&nbsp;</option>
                                            <option id="fs-2444" value="2444"> |- История Нового и Новейшего времени&nbsp;</option>
                                            <option id="fs-2427" value="2427"> |- История Европы&nbsp;</option>
                                            <option id="fs-2452" value="2452"> |- История Азии и Африки&nbsp;</option>
                                            <option id="fs-2445" value="2445"> |- История Америки, Австралии, Океании&nbsp;</option>
                                            <option id="fs-2435" value="2435"> |- История России&nbsp;</option>
                                            <option id="fs-2436" value="2436"> |- Эпоха СССР&nbsp;</option>
                                            <option id="fs-2453" value="2453"> |- История стран бывшего СССР&nbsp;</option>
                                            <option id="fs-2320" value="2320"> |- Этнография, антропология&nbsp;</option>
                                            <option id="fs-1801" value="1801"> |- Международные отношения. Дипломатия&nbsp;</option>
                                            <option id="fs-2023" value="2023" class="root_forum has_sf">Точные, естественные и инженерные науки&nbsp;</option>
                                            <option id="fs-2024" value="2024"> |- Авиация / Космонавтика&nbsp;</option>
                                            <option id="fs-2026" value="2026"> |- Физика&nbsp;</option>
                                            <option id="fs-2192" value="2192"> |- Астрономия&nbsp;</option>
                                            <option id="fs-2027" value="2027"> |- Биология / Экология&nbsp;</option>
                                            <option id="fs-295" value="295"> |- Химия / Биохимия&nbsp;</option>
                                            <option id="fs-2028" value="2028"> |- Математика&nbsp;</option>
                                            <option id="fs-2029" value="2029"> |- География / Геология / Геодезия&nbsp;</option>
                                            <option id="fs-1325" value="1325"> |- Электроника / Радио&nbsp;</option>
                                            <option id="fs-2386" value="2386"> |- Схемы и сервис-мануалы (оригинальная документация)&nbsp;</option>
                                            <option id="fs-2031" value="2031"> |- Архитектура / Строительство / Инженерные сети&nbsp;</option>
                                            <option id="fs-2030" value="2030"> |- Машиностроение&nbsp;</option>
                                            <option id="fs-2526" value="2526"> |- Сварка / Пайка / Неразрушающий контроль&nbsp;</option>
                                            <option id="fs-2527" value="2527"> |- Автоматизация / Робототехника&nbsp;</option>
                                            <option id="fs-2254" value="2254"> |- Металлургия / Материаловедение&nbsp;</option>
                                            <option id="fs-2376" value="2376"> |- Механика, сопротивление материалов&nbsp;</option>
                                            <option id="fs-2054" value="2054"> |- Энергетика / электротехника&nbsp;</option>
                                            <option id="fs-770" value="770"> |- Нефтяная, газовая и химическая промышленность&nbsp;</option>
                                            <option id="fs-2476" value="2476"> |- Сельское хозяйство и пищевая промышленность&nbsp;</option>
                                            <option id="fs-2494" value="2494"> |- Железнодорожное дело&nbsp;</option>
                                            <option id="fs-1528" value="1528"> |- Нормативная документация&nbsp;</option>
                                            <option id="fs-2032" value="2032"> |- Журналы: научные, научно-популярные, радио и др.&nbsp;</option>
                                            <option id="fs-919" value="919" class="root_forum has_sf">Ноты и Музыкальная литература&nbsp;</option>
                                            <option id="fs-944" value="944"> |- Академическая музыка (Ноты и Media CD)&nbsp;</option>
                                            <option id="fs-980" value="980"> |- Другие направления (Ноты, табулатуры)&nbsp;</option>
                                            <option id="fs-946" value="946"> |- Самоучители и Школы&nbsp;</option>
                                            <option id="fs-977" value="977"> |- Песенники (Songbooks)&nbsp;</option>
                                            <option id="fs-2074" value="2074"> |- Музыкальная литература и Теория&nbsp;</option>
                                            <option id="fs-2349" value="2349"> |- Музыкальные журналы&nbsp;</option>
                                            <option id="fs-768" value="768" class="root_forum has_sf">Военное дело&nbsp;</option>
                                            <option id="fs-2099" value="2099"> |- Милитария&nbsp;</option>
                                            <option id="fs-2021" value="2021"> |- Военная история&nbsp;</option>
                                            <option id="fs-2437" value="2437"> |- История Второй мировой войны&nbsp;</option>
                                            <option id="fs-1337" value="1337"> |- Биографии и мемуары военных деятелей&nbsp;</option>
                                            <option id="fs-1447" value="1447"> |- Военная техника&nbsp;</option>
                                            <option id="fs-2468" value="2468"> |- Стрелковое оружие&nbsp;</option>
                                            <option id="fs-2469" value="2469"> |- Учебно-методическая литература&nbsp;</option>
                                            <option id="fs-2470" value="2470"> |- Спецслужбы мира&nbsp;</option>
                                            <option id="fs-1686" value="1686" class="root_forum has_sf">Вера и религия&nbsp;</option>
                                            <option id="fs-2215" value="2215"> |- Христианство&nbsp;</option>
                                            <option id="fs-2216" value="2216"> |- Ислам&nbsp;</option>
                                            <option id="fs-2217" value="2217"> |- Религии Индии, Тибета и Восточной Азии / Иудаизм&nbsp;</option>
                                            <option id="fs-2218" value="2218"> |- Нетрадиционные религиозные, духовные и мистические учения&nbsp;</option>
                                            <option id="fs-2252" value="2252"> |- Религиоведение. История Религии. Атеизм&nbsp;</option>
                                            <option id="fs-767" value="767" class="root_forum has_sf">Психология&nbsp;</option>
                                            <option id="fs-2515" value="2515"> |- Общая и прикладная психология&nbsp;</option>
                                            <option id="fs-2516" value="2516"> |- Психотерапия и консультирование&nbsp;</option>
                                            <option id="fs-2517" value="2517"> |- Психодиагностика и психокоррекция&nbsp;</option>
                                            <option id="fs-2518" value="2518"> |- Социальная психология и психология отношений&nbsp;</option>
                                            <option id="fs-2519" value="2519"> |- Тренинг и коучинг&nbsp;</option>
                                            <option id="fs-2520" value="2520"> |- Саморазвитие и самосовершенствование&nbsp;</option>
                                            <option id="fs-1696" value="1696"> |- Популярная психология&nbsp;</option>
                                            <option id="fs-2253" value="2253"> |- Сексология. Взаимоотношения полов&nbsp;</option>
                                            <option id="fs-2033" value="2033" class="root_forum has_sf">Коллекционирование, увлечения и хобби&nbsp;</option>
                                            <option id="fs-1412" value="1412"> |- Коллекционирование и вспомогательные ист. дисциплины&nbsp;</option>
                                            <option id="fs-1446" value="1446"> |- Вышивание&nbsp;</option>
                                            <option id="fs-753" value="753"> |- Вязание&nbsp;</option>
                                            <option id="fs-2037" value="2037"> |- Шитье, пэчворк&nbsp;</option>
                                            <option id="fs-2224" value="2224"> |- Кружевоплетение&nbsp;</option>
                                            <option id="fs-2194" value="2194"> |- Бисероплетение. Ювелирика. Украшения из проволоки.&nbsp;</option>
                                            <option id="fs-2418" value="2418"> |- Бумажный арт&nbsp;</option>
                                            <option id="fs-1410" value="1410"> |- Другие виды декоративно-прикладного искусства&nbsp;</option>
                                            <option id="fs-2034" value="2034"> |- Домашние питомцы и аквариумистика&nbsp;</option>
                                            <option id="fs-2433" value="2433"> |- Охота и рыбалка&nbsp;</option>
                                            <option id="fs-1961" value="1961"> |- Кулинария (книги)&nbsp;</option>
                                            <option id="fs-2432" value="2432"> |- Кулинария (газеты и журналы)&nbsp;</option>
                                            <option id="fs-565" value="565"> |- Моделизм&nbsp;</option>
                                            <option id="fs-1523" value="1523"> |- Приусадебное хозяйство / Цветоводство&nbsp;</option>
                                            <option id="fs-1575" value="1575"> |- Ремонт, частное строительство, дизайн интерьеров&nbsp;</option>
                                            <option id="fs-1520" value="1520"> |- Деревообработка&nbsp;</option>
                                            <option id="fs-2424" value="2424"> |- Настольные игры&nbsp;</option>
                                            <option id="fs-769" value="769"> |- Прочие хобби&nbsp;</option>
                                            <option id="fs-2038" value="2038" class="root_forum has_sf">Художественная литература&nbsp;</option>
                                            <option id="fs-2043" value="2043"> |- Русская литература&nbsp;</option>
                                            <option id="fs-2042" value="2042"> |- Зарубежная литература (до 1900 г.)&nbsp;</option>
                                            <option id="fs-2041" value="2041"> |- Зарубежная литература (XX и XXI век)&nbsp;</option>
                                            <option id="fs-2044" value="2044"> |- Детектив, боевик&nbsp;</option>
                                            <option id="fs-2039" value="2039"> |- Женский роман&nbsp;</option>
                                            <option id="fs-2045" value="2045"> |- Отечественная фантастика / фэнтези / мистика&nbsp;</option>
                                            <option id="fs-2080" value="2080"> |- Зарубежная фантастика / фэнтези / мистика&nbsp;</option>
                                            <option id="fs-2047" value="2047"> |- Приключения&nbsp;</option>
                                            <option id="fs-2193" value="2193"> |- Литературные журналы&nbsp;</option>
                                            <option id="fs-1418" value="1418" class="root_forum has_sf">Компьютерная литература&nbsp;</option>
                                            <option id="fs-1422" value="1422"> |- Программы от Microsoft&nbsp;</option>
                                            <option id="fs-1423" value="1423"> |- Другие программы&nbsp;</option>
                                            <option id="fs-1424" value="1424"> |- Mac OS; Linux, FreeBSD и прочие *NIX&nbsp;</option>
                                            <option id="fs-1445" value="1445"> |- СУБД&nbsp;</option>
                                            <option id="fs-1425" value="1425"> |- Веб-дизайн и программирование&nbsp;</option>
                                            <option id="fs-1426" value="1426"> |- Программирование (книги)&nbsp;</option>
                                            <option id="fs-1428" value="1428"> |- Графика, обработка видео&nbsp;</option>
                                            <option id="fs-1429" value="1429"> |- Сети / VoIP&nbsp;</option>
                                            <option id="fs-1430" value="1430"> |- Хакинг и безопасность&nbsp;</option>
                                            <option id="fs-1431" value="1431"> |- Железо (книги о ПК)&nbsp;</option>
                                            <option id="fs-1433" value="1433"> |- Инженерные и научные программы (книги)&nbsp;</option>
                                            <option id="fs-1432" value="1432"> |- Компьютерные журналы и приложения к ним&nbsp;</option>
                                            <option id="fs-2202" value="2202"> |- Дисковые приложения к игровым журналам&nbsp;</option>
                                            <option id="fs-862" value="862" class="root_forum has_sf">Комиксы, манга, ранобэ&nbsp;</option>
                                            <option id="fs-2461" value="2461"> |- Комиксы на русском языке&nbsp;</option>
                                            <option id="fs-2462" value="2462"> |- Комиксы издательства Marvel&nbsp;</option>
                                            <option id="fs-2463" value="2463"> |- Комиксы издательства DC&nbsp;</option>
                                            <option id="fs-2464" value="2464"> |- Комиксы других издательств&nbsp;</option>
                                            <option id="fs-2473" value="2473"> |- Комиксы на других языках&nbsp;</option>
                                            <option id="fs-281" value="281"> |- Манга (на русском языке)&nbsp;</option>
                                            <option id="fs-2465" value="2465"> |- Манга (на иностранных языках)&nbsp;</option>
                                            <option id="fs-2458" value="2458"> |- Ранобэ&nbsp;</option>
                                            <option id="fs-2048" value="2048" class="root_forum has_sf">Коллекции книг и библиотеки&nbsp;</option>
                                            <option id="fs-1238" value="1238"> |- Библиотеки (зеркала сетевых библиотек/коллекций)&nbsp;</option>
                                            <option id="fs-2055" value="2055"> |- Тематические коллекции (подборки)&nbsp;</option>
                                            <option id="fs-754" value="754"> |- Многопредметные коллекции (подборки)&nbsp;</option>
                                            <option id="fs-2114" value="2114" class="root_forum has_sf">Мультимедийные и интерактивные издания&nbsp;</option>
                                            <option id="fs-2438" value="2438"> |- Мультимедийные энциклопедии&nbsp;</option>
                                            <option id="fs-2439" value="2439"> |- Интерактивные обучающие и развивающие материалы&nbsp;</option>
                                            <option id="fs-2440" value="2440"> |- Обучающие издания для детей&nbsp;</option>
                                            <option id="fs-2441" value="2441"> |- Кулинария. Цветоводство. Домоводство&nbsp;</option>
                                            <option id="fs-2442" value="2442"> |- Культура. Искусство. История&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Обучение иностранным языкам">
                                            <option id="fs-2362" value="2362" class="root_forum has_sf">Иностранные языки для взрослых&nbsp;</option>
                                            <option id="fs-1265" value="1265"> |- Английский язык (для взрослых)&nbsp;</option>
                                            <option id="fs-1266" value="1266"> |- Немецкий язык&nbsp;</option>
                                            <option id="fs-1267" value="1267"> |- Французский язык&nbsp;</option>
                                            <option id="fs-1358" value="1358"> |- Испанский язык&nbsp;</option>
                                            <option id="fs-2363" value="2363"> |- Итальянский язык&nbsp;</option>
                                            <option id="fs-734" value="734"> |- Финский язык&nbsp;</option>
                                            <option id="fs-1268" value="1268"> |- Другие европейские языки&nbsp;</option>
                                            <option id="fs-1673" value="1673"> |- Арабский язык&nbsp;</option>
                                            <option id="fs-1269" value="1269"> |- Китайский язык&nbsp;</option>
                                            <option id="fs-1270" value="1270"> |- Японский язык&nbsp;</option>
                                            <option id="fs-1275" value="1275"> |- Другие восточные языки&nbsp;</option>
                                            <option id="fs-2364" value="2364"> |- Русский язык как иностранный&nbsp;</option>
                                            <option id="fs-1276" value="1276"> |- Мультиязычные сборники&nbsp;</option>
                                            <option id="fs-2094" value="2094"> |- LIM-курсы&nbsp;</option>
                                            <option id="fs-1274" value="1274"> |- Разное (иностранные языки)&nbsp;</option>
                                            <option id="fs-1264" value="1264" class="root_forum has_sf">Иностранные языки для детей&nbsp;</option>
                                            <option id="fs-2358" value="2358"> |- Английский язык (для детей)&nbsp;</option>
                                            <option id="fs-2359" value="2359"> |- Другие европейские языки (для детей)&nbsp;</option>
                                            <option id="fs-2360" value="2360"> |- Восточные языки (для детей)&nbsp;</option>
                                            <option id="fs-2361" value="2361"> |- Школьные учебники, ЕГЭ&nbsp;</option>
                                            <option id="fs-2057" value="2057" class="root_forum has_sf">Художественная литература (ин.языки)&nbsp;</option>
                                            <option id="fs-2355" value="2355"> |- Художественная литература на английском языке&nbsp;</option>
                                            <option id="fs-2474" value="2474"> |- Художественная литература на французском языке&nbsp;</option>
                                            <option id="fs-2356" value="2356"> |- Художественная литература на других европейских языках&nbsp;</option>
                                            <option id="fs-2357" value="2357"> |- Художественная литература на восточных языках&nbsp;</option>
                                            <option id="fs-2413" value="2413" class="root_forum has_sf">Аудиокниги на иностранных языках&nbsp;</option>
                                            <option id="fs-1501" value="1501"> |- Аудиокниги на английском языке&nbsp;</option>
                                            <option id="fs-1580" value="1580"> |- Аудиокниги на немецком языке&nbsp;</option>
                                            <option id="fs-525" value="525"> |- Аудиокниги на других иностранных языках&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Обучающее видео">
                                            <option id="fs-610" value="610" class="root_forum has_sf">Видеоуроки и обучающие интерактивные DVD&nbsp;</option>
                                            <option id="fs-1568" value="1568"> |- Кулинария&nbsp;</option>
                                            <option id="fs-1542" value="1542"> |- Спорт&nbsp;</option>
                                            <option id="fs-2335" value="2335"> |- Фитнес - Кардио-Силовые Тренировки&nbsp;</option>
                                            <option id="fs-1544" value="1544"> |- Фитнес - Разум и Тело&nbsp;</option>
                                            <option id="fs-1546" value="1546"> |- Бодибилдинг&nbsp;</option>
                                            <option id="fs-1549" value="1549"> |- Оздоровительные практики&nbsp;</option>
                                            <option id="fs-1597" value="1597"> |- Йога&nbsp;</option>
                                            <option id="fs-1552" value="1552"> |- Видео- и фотосъёмка&nbsp;</option>
                                            <option id="fs-1550" value="1550"> |- Уход за собой&nbsp;</option>
                                            <option id="fs-1553" value="1553"> |- Рисование&nbsp;</option>
                                            <option id="fs-1554" value="1554"> |- Игра на гитаре&nbsp;</option>
                                            <option id="fs-617" value="617"> |- Ударные инструменты&nbsp;</option>
                                            <option id="fs-1555" value="1555"> |- Другие музыкальные инструменты&nbsp;</option>
                                            <option id="fs-2017" value="2017"> |- Игра на бас-гитаре&nbsp;</option>
                                            <option id="fs-1257" value="1257"> |- Бальные танцы&nbsp;</option>
                                            <option id="fs-1258" value="1258"> |- Танец живота&nbsp;</option>
                                            <option id="fs-2208" value="2208"> |- Уличные и клубные танцы&nbsp;</option>
                                            <option id="fs-677" value="677"> |- Танцы, разное&nbsp;</option>
                                            <option id="fs-1255" value="1255"> |- Охота&nbsp;</option>
                                            <option id="fs-1479" value="1479"> |- Рыболовство и подводная охота&nbsp;</option>
                                            <option id="fs-1261" value="1261"> |- Фокусы и трюки&nbsp;</option>
                                            <option id="fs-614" value="614"> |- Образование&nbsp;</option>
                                            <option id="fs-1583" value="1583"> |- Финансы&nbsp;</option>
                                            <option id="fs-1259" value="1259"> |- Продажи, бизнес&nbsp;</option>
                                            <option id="fs-2065" value="2065"> |- Беременность, роды, материнство&nbsp;</option>
                                            <option id="fs-1254" value="1254"> |- Учебные видео для детей&nbsp;</option>
                                            <option id="fs-1260" value="1260"> |- Психология&nbsp;</option>
                                            <option id="fs-2209" value="2209"> |- Эзотерика, саморазвитие&nbsp;</option>
                                            <option id="fs-2210" value="2210"> |- Пикап, знакомства&nbsp;</option>
                                            <option id="fs-1547" value="1547"> |- Строительство, ремонт и дизайн&nbsp;</option>
                                            <option id="fs-1548" value="1548"> |- Дерево- и металлообработка&nbsp;</option>
                                            <option id="fs-2211" value="2211"> |- Растения и животные&nbsp;</option>
                                            <option id="fs-1596" value="1596"> |- Хобби и рукоделие&nbsp;</option>
                                            <option id="fs-615" value="615"> |- Разное&nbsp;</option>
                                            <option id="fs-1581" value="1581" class="root_forum has_sf">Боевые искусства (Видеоуроки)&nbsp;</option>
                                            <option id="fs-1590" value="1590"> |- Айкидо и айки-дзюцу&nbsp;</option>
                                            <option id="fs-1587" value="1587"> |- Вин чун&nbsp;</option>
                                            <option id="fs-1594" value="1594"> |- Джиу-джитсу&nbsp;</option>
                                            <option id="fs-1591" value="1591"> |- Дзюдо и самбо&nbsp;</option>
                                            <option id="fs-1588" value="1588"> |- Каратэ&nbsp;</option>
                                            <option id="fs-1585" value="1585"> |- Работа с оружием&nbsp;</option>
                                            <option id="fs-1586" value="1586"> |- Русский стиль&nbsp;</option>
                                            <option id="fs-2078" value="2078"> |- Рукопашный бой&nbsp;</option>
                                            <option id="fs-1929" value="1929"> |- Смешанные стили&nbsp;</option>
                                            <option id="fs-1593" value="1593"> |- Ударные стили&nbsp;</option>
                                            <option id="fs-1592" value="1592"> |- Ушу&nbsp;</option>
                                            <option id="fs-1595" value="1595"> |- Разное&nbsp;</option>
                                            <option id="fs-1556" value="1556" class="root_forum has_sf">Компьютерные видеоуроки и обучающие интерактивные DVD&nbsp;</option>
                                            <option id="fs-1560" value="1560"> |- Компьютерные сети и безопасность&nbsp;</option>
                                            <option id="fs-1561" value="1561"> |- ОС и серверные программы Microsoft&nbsp;</option>
                                            <option id="fs-1653" value="1653"> |- Офисные программы Microsoft&nbsp;</option>
                                            <option id="fs-1570" value="1570"> |- ОС и программы семейства UNIX&nbsp;</option>
                                            <option id="fs-1654" value="1654"> |- Adobe Photoshop&nbsp;</option>
                                            <option id="fs-1655" value="1655"> |- Autodesk Maya&nbsp;</option>
                                            <option id="fs-1656" value="1656"> |- Autodesk 3ds Max&nbsp;</option>
                                            <option id="fs-1930" value="1930"> |- Autodesk Softimage (XSI)&nbsp;</option>
                                            <option id="fs-1931" value="1931"> |- ZBrush&nbsp;</option>
                                            <option id="fs-1932" value="1932"> |- Flash, Flex и ActionScript&nbsp;</option>
                                            <option id="fs-1562" value="1562"> |- 2D-графика&nbsp;</option>
                                            <option id="fs-1563" value="1563"> |- 3D-графика&nbsp;</option>
                                            <option id="fs-1626" value="1626"> |- Инженерные и научные программы (видеоуроки)&nbsp;</option>
                                            <option id="fs-1564" value="1564"> |- Web-дизайн&nbsp;</option>
                                            <option id="fs-1545" value="1545"> |- WEB, SMM, SEO, интернет-маркетинг&nbsp;</option>
                                            <option id="fs-1565" value="1565"> |- Программирование (видеоуроки)&nbsp;</option>
                                            <option id="fs-1559" value="1559"> |- Программы для Mac OS&nbsp;</option>
                                            <option id="fs-1566" value="1566"> |- Работа с видео&nbsp;</option>
                                            <option id="fs-1573" value="1573"> |- Работа со звуком&nbsp;</option>
                                            <option id="fs-1567" value="1567"> |- Разное (Компьютерные видеоуроки)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Аудиокниги">
                                            <option id="fs-2326" value="2326" class="root_forum has_sf">Радиоспектакли, история, мемуары&nbsp;</option>
                                            <option id="fs-574" value="574"> |- [Аудио] Радиоспектакли и литературные чтения&nbsp;</option>
                                            <option id="fs-1036" value="1036"> |- [Аудио] Жизнь замечательных людей&nbsp;</option>
                                            <option id="fs-400" value="400"> |- [Аудио] История, культурология, философия&nbsp;</option>
                                            <option id="fs-2389" value="2389" class="root_forum has_sf">Фантастика, фэнтези, мистика, ужасы, фанфики&nbsp;</option>
                                            <option id="fs-2388" value="2388"> |- [Аудио] Зарубежная фантастика, фэнтези, мистика, ужасы, фанфики&nbsp;</option>
                                            <option id="fs-2387" value="2387"> |- [Аудио] Российская фантастика, фэнтези, мистика, ужасы, фанфики&nbsp;</option>
                                            <option id="fs-661" value="661"> |- [Аудио] Любовно-фантастический роман&nbsp;</option>
                                            <option id="fs-2348" value="2348" title="[Аудио] Сборники/разное Фантастика, фэнтези, мистика, ужасы, фанфики"> |- [Аудио] Сборники/разное Фантастика, фэнтези, мистика, ужасы, фанфи..&nbsp;</option>
                                            <option id="fs-2327" value="2327" class="root_forum has_sf">Художественная литература&nbsp;</option>
                                            <option id="fs-695" value="695"> |- [Аудио] Поэзия&nbsp;</option>
                                            <option id="fs-399" value="399"> |- [Аудио] Зарубежная литература&nbsp;</option>
                                            <option id="fs-402" value="402"> |- [Аудио] Русская литература&nbsp;</option>
                                            <option id="fs-490" value="490"> |- [Аудио] Детская литература&nbsp;</option>
                                            <option id="fs-499" value="499"> |- [Аудио] Детективы, приключения, триллеры, боевики&nbsp;</option>
                                            <option id="fs-2324" value="2324" class="root_forum has_sf">Религии&nbsp;</option>
                                            <option id="fs-2325" value="2325"> |- [Аудио] Православие&nbsp;</option>
                                            <option id="fs-2342" value="2342"> |- [Аудио] Ислам&nbsp;</option>
                                            <option id="fs-530" value="530"> |- [Аудио] Другие традиционные религии&nbsp;</option>
                                            <option id="fs-2152" value="2152"> |- [Аудио] Нетрадиционные религиозно-философские учения&nbsp;</option>
                                            <option id="fs-2328" value="2328" class="root_forum has_sf">Прочая литература&nbsp;</option>
                                            <option id="fs-403" value="403"> |- [Аудио] Учебная и научно-популярная литература&nbsp;</option>
                                            <option id="fs-1279" value="1279"> |- [Аудио] lossless-аудиокниги&nbsp;</option>
                                            <option id="fs-716" value="716"> |- [Аудио] Бизнес&nbsp;</option>
                                            <option id="fs-2165" value="2165"> |- [Аудио] Разное&nbsp;</option>
                                            <option id="fs-401" value="401"> |- [Аудио] Некондиционные раздачи&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Все по авто и мото">
                                            <option id="fs-1964" value="1964" class="root_forum has_sf">Ремонт и эксплуатация транспортных средств&nbsp;</option>
                                            <option id="fs-1973" value="1973"> |- Оригинальные каталоги по подбору запчастей&nbsp;</option>
                                            <option id="fs-1974" value="1974"> |- Неоригинальные каталоги по подбору запчастей&nbsp;</option>
                                            <option id="fs-1975" value="1975"> |- Программы по диагностике и ремонту&nbsp;</option>
                                            <option id="fs-1976" value="1976"> |- Тюнинг, чиптюнинг, настройка&nbsp;</option>
                                            <option id="fs-1977" value="1977"> |- Книги по ремонту/обслуживанию/эксплуатации ТС&nbsp;</option>
                                            <option id="fs-1203" value="1203"> |- Мультимедийки по ремонту/обслуживанию/эксплуатации ТС&nbsp;</option>
                                            <option id="fs-1978" value="1978"> |- Учет, утилиты и прочее&nbsp;</option>
                                            <option id="fs-1979" value="1979"> |- Виртуальная автошкола&nbsp;</option>
                                            <option id="fs-1980" value="1980"> |- Видеоуроки по вождению транспортных средств&nbsp;</option>
                                            <option id="fs-1981" value="1981"> |- Видеоуроки по ремонту транспортных средств&nbsp;</option>
                                            <option id="fs-1970" value="1970"> |- Журналы по авто/мото&nbsp;</option>
                                            <option id="fs-334" value="334"> |- Водный транспорт&nbsp;</option>
                                            <option id="fs-1202" value="1202" class="root_forum has_sf">Фильмы и передачи по авто/мото&nbsp;</option>
                                            <option id="fs-1985" value="1985"> |- Документальные/познавательные фильмы&nbsp;</option>
                                            <option id="fs-1982" value="1982"> |- Развлекательные передачи&nbsp;</option>
                                            <option id="fs-2151" value="2151"> |- Top Gear/Топ Гир&nbsp;</option>
                                            <option id="fs-1983" value="1983"> |- Тест драйв/Обзоры/Автосалоны&nbsp;</option>
                                            <option id="fs-1984" value="1984"> |- Тюнинг/форсаж&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Музыка">
                                            <option id="fs-409" value="409" class="root_forum has_sf">Классическая и современная академическая музыка&nbsp;</option>
                                            <option id="fs-445" value="445"> |- Классическая музыка (Видео)&nbsp;</option>
                                            <option id="fs-984" value="984"> |- Классическая музыка (DVD и HD Видео)&nbsp;</option>
                                            <option id="fs-702" value="702"> |- Опера (Видео)&nbsp;</option>
                                            <option id="fs-983" value="983"> |- Опера (DVD и HD Видео)&nbsp;</option>
                                            <option id="fs-1990" value="1990"> |- Балет и современная хореография (Видео, DVD и HD Видео)&nbsp;</option>
                                            <option id="fs-560" value="560"> |- Полные собрания сочинений и многодисковые издания (lossless)&nbsp;</option>
                                            <option id="fs-794" value="794"> |- Опера (lossless)&nbsp;</option>
                                            <option id="fs-556" value="556"> |- Вокальная музыка (lossless)&nbsp;</option>
                                            <option id="fs-2307" value="2307"> |- Хоровая музыка (lossless)&nbsp;</option>
                                            <option id="fs-557" value="557"> |- Оркестровая музыка (lossless)&nbsp;</option>
                                            <option id="fs-2308" value="2308"> |- Концерт для инструмента с оркестром (lossless)&nbsp;</option>
                                            <option id="fs-558" value="558"> |- Камерная инструментальная музыка (lossless)&nbsp;</option>
                                            <option id="fs-793" value="793"> |- Сольная инструментальная музыка (lossless)&nbsp;</option>
                                            <option id="fs-1395" value="1395"> |- Духовные песнопения и музыка (lossless)&nbsp;</option>
                                            <option id="fs-1396" value="1396"> |- Духовные песнопения и музыка (lossy)&nbsp;</option>
                                            <option id="fs-436" value="436"> |- Полные собрания сочинений и многодисковые издания (lossy)&nbsp;</option>
                                            <option id="fs-2309" value="2309"> |- Вокальная и хоровая музыка (lossy)&nbsp;</option>
                                            <option id="fs-2310" value="2310"> |- Оркестровая музыка (lossy)&nbsp;</option>
                                            <option id="fs-2311" value="2311"> |- Камерная и сольная инструментальная музыка (lossy)&nbsp;</option>
                                            <option id="fs-969" value="969" title="Классика в современной обработке, Classical Crossover (lossy и lossless)"> |- Классика в современной обработке, Classical Crossover (lossy и los..&nbsp;</option>
                                            <option id="fs-1125" value="1125" class="root_forum has_sf">Фольклор, Народная и Этническая музыка&nbsp;</option>
                                            <option id="fs-1130" value="1130"> |- Восточноевропейский фолк (lossy)&nbsp;</option>
                                            <option id="fs-1131" value="1131"> |- Восточноевропейский фолк (lossless)&nbsp;</option>
                                            <option id="fs-1132" value="1132"> |- Западноевропейский фолк (lossy)&nbsp;</option>
                                            <option id="fs-1133" value="1133"> |- Западноевропейский фолк (lossless)&nbsp;</option>
                                            <option id="fs-2084" value="2084"> |- Klezmer и Еврейский фольклор (lossy и lossless)&nbsp;</option>
                                            <option id="fs-1128" value="1128"> |- Этническая музыка Сибири, Средней и Восточной Азии (lossy)&nbsp;</option>
                                            <option id="fs-1129" value="1129"> |- Этническая музыка Сибири, Средней и Восточной Азии (lossless)&nbsp;</option>
                                            <option id="fs-1856" value="1856"> |- Этническая музыка Индии (lossy)&nbsp;</option>
                                            <option id="fs-2430" value="2430"> |- Этническая музыка Индии (lossless)&nbsp;</option>
                                            <option id="fs-1283" value="1283"> |- Этническая музыка Африки и Ближнего Востока (lossy)&nbsp;</option>
                                            <option id="fs-2085" value="2085"> |- Этническая музыка Африки и Ближнего Востока (lossless)&nbsp;</option>
                                            <option id="fs-1282" value="1282" title="Фольклорная, Народная, Эстрадная музыка Кавказа и Закавказья (lossy и lossless)"> |- Фольклорная, Народная, Эстрадная музыка Кавказа и Закавказья (loss..&nbsp;</option>
                                            <option id="fs-1284" value="1284"> |- Этническая музыка Северной и Южной Америки (lossy)&nbsp;</option>
                                            <option id="fs-1285" value="1285"> |- Этническая музыка Северной и Южной Америки (lossless)&nbsp;</option>
                                            <option id="fs-1138" value="1138" title="Этническая музыка Австралии, Тихого и Индийского океанов (lossy и lossless)"> |- Этническая музыка Австралии, Тихого и Индийского океанов (lossy и ..&nbsp;</option>
                                            <option id="fs-1136" value="1136"> |- Country, Bluegrass (lossy)&nbsp;</option>
                                            <option id="fs-1137" value="1137"> |- Country, Bluegrass (lossless)&nbsp;</option>
                                            <option id="fs-1141" value="1141"> |- Фольклор, Народная и Этническая музыка (Видео)&nbsp;</option>
                                            <option id="fs-1142" value="1142"> |- Фольклор, Народная и Этническая музыка (DVD Video)&nbsp;</option>
                                            <option id="fs-2530" value="2530"> |- Фольклор, Народная и Этническая музыка (HD Видео)&nbsp;</option>
                                            <option id="fs-1849" value="1849" class="root_forum has_sf">New Age, Relax, Meditative &amp; Flamenco&nbsp;</option>
                                            <option id="fs-1126" value="1126"> |- New Age &amp; Meditative (lossy)&nbsp;</option>
                                            <option id="fs-1127" value="1127"> |- New Age &amp; Meditative (lossless)&nbsp;</option>
                                            <option id="fs-1134" value="1134"> |- Фламенко и акустическая гитара (lossy)&nbsp;</option>
                                            <option id="fs-1135" value="1135"> |- Фламенко и акустическая гитара (lossless)&nbsp;</option>
                                            <option id="fs-2018" value="2018"> |- Музыка для бальных танцев (lossy и lossless)&nbsp;</option>
                                            <option id="fs-2352" value="2352"> |- New Age, Relax, Meditative &amp; Flamenco (Видео)&nbsp;</option>
                                            <option id="fs-2351" value="2351"> |- New Age, Relax, Meditative &amp; Flamenco (DVD и HD Видео)&nbsp;</option>
                                            <option id="fs-855" value="855"> |- Звуки природы&nbsp;</option>
                                            <option id="fs-408" value="408" class="root_forum has_sf">Рэп, Хип-Хоп, R&#039;n&#039;B&nbsp;</option>
                                            <option id="fs-441" value="441"> |- Отечественный Рэп, Хип-Хоп (lossy)&nbsp;</option>
                                            <option id="fs-1173" value="1173"> |- Отечественный R&#039;n&#039;B (lossy)&nbsp;</option>
                                            <option id="fs-1486" value="1486"> |- Отечественный Рэп, Хип-Хоп, R&#039;n&#039;B (lossless)&nbsp;</option>
                                            <option id="fs-1172" value="1172"> |- Зарубежный R&#039;n&#039;B (lossy)&nbsp;</option>
                                            <option id="fs-446" value="446"> |- Зарубежный Рэп, Хип-Хоп (lossy)&nbsp;</option>
                                            <option id="fs-909" value="909"> |- Зарубежный Рэп, Хип-Хоп (lossless)&nbsp;</option>
                                            <option id="fs-1665" value="1665"> |- Зарубежный R&#039;n&#039;B (lossless)&nbsp;</option>
                                            <option id="fs-1189" value="1189"> |- Отечественный Рэп, Хип-Хоп (Видео)&nbsp;</option>
                                            <option id="fs-1455" value="1455"> |- Отечественный R&#039;n&#039;B (Видео)&nbsp;</option>
                                            <option id="fs-442" value="442"> |- Зарубежный Рэп, Хип-Хоп (Видео)&nbsp;</option>
                                            <option id="fs-1174" value="1174"> |- Зарубежный R&#039;n&#039;B (Видео)&nbsp;</option>
                                            <option id="fs-1107" value="1107"> |- Рэп, Хип-Хоп, R&#039;n&#039;B (DVD Video)&nbsp;</option>
                                            <option id="fs-2529" value="2529"> |- Рэп, Хип-Хоп, R&#039;n&#039;B (HD Видео)&nbsp;</option>
                                            <option id="fs-1760" value="1760" class="root_forum has_sf">Reggae, Ska, Dub&nbsp;</option>
                                            <option id="fs-1764" value="1764"> |- Rocksteady, Early Reggae, Ska-Jazz, Trad.Ska (lossy и lossless)&nbsp;</option>
                                            <option id="fs-1766" value="1766"> |- Punky-Reggae, Rocksteady-Punk, Ska Revival (lossy)&nbsp;</option>
                                            <option id="fs-1767" value="1767"> |- 3rd Wave Ska (lossy)&nbsp;</option>
                                            <option id="fs-1769" value="1769"> |- Ska-Punk, Ska-Core (lossy)&nbsp;</option>
                                            <option id="fs-1765" value="1765"> |- Reggae (lossy)&nbsp;</option>
                                            <option id="fs-1771" value="1771"> |- Dub (lossy)&nbsp;</option>
                                            <option id="fs-1770" value="1770"> |- Dancehall, Raggamuffin (lossy)&nbsp;</option>
                                            <option id="fs-1768" value="1768"> |- Reggae, Dancehall, Dub (lossless)&nbsp;</option>
                                            <option id="fs-1774" value="1774"> |- Ska, Ska-Punk, Ska-Jazz (lossless)&nbsp;</option>
                                            <option id="fs-1772" value="1772"> |- Отечественный Reggae, Dub (lossy и lossless)&nbsp;</option>
                                            <option id="fs-1773" value="1773"> |- Отечественная Ska музыка (lossy и lossless)&nbsp;</option>
                                            <option id="fs-2233" value="2233"> |- Reggae, Ska, Dub (компиляции) (lossy и lossless)&nbsp;</option>
                                            <option id="fs-1775" value="1775"> |- Reggae, Ska, Dub (Видео)&nbsp;</option>
                                            <option id="fs-1777" value="1777"> |- Reggae, Ska, Dub (DVD и HD Video)&nbsp;</option>
                                            <option id="fs-416" value="416" class="root_forum has_sf">Саундтреки, караоке и мюзиклы&nbsp;</option>
                                            <option id="fs-782" value="782"> |- Караоке (аудио)&nbsp;</option>
                                            <option id="fs-2377" value="2377"> |- Караоке (видео)&nbsp;</option>
                                            <option id="fs-468" value="468"> |- Минусовки (lossy и lossless)&nbsp;</option>
                                            <option id="fs-691" value="691"> |- Саундтреки к отечественным фильмам (lossless)&nbsp;</option>
                                            <option id="fs-469" value="469"> |- Саундтреки к отечественным фильмам (lossy)&nbsp;</option>
                                            <option id="fs-786" value="786"> |- Саундтреки к зарубежным фильмам (lossless)&nbsp;</option>
                                            <option id="fs-785" value="785"> |- Саундтреки к зарубежным фильмам (lossy)&nbsp;</option>
                                            <option id="fs-1631" value="1631"> |- Саундтреки к сериалам (lossless)&nbsp;</option>
                                            <option id="fs-1499" value="1499"> |- Саундтреки к сериалам (lossy)&nbsp;</option>
                                            <option id="fs-715" value="715"> |- Саундтреки к мультфильмам (lossy и lossless)&nbsp;</option>
                                            <option id="fs-1388" value="1388"> |- Саундтреки к аниме (lossless)&nbsp;</option>
                                            <option id="fs-282" value="282"> |- Саундтреки к аниме (lossy)&nbsp;</option>
                                            <option id="fs-796" value="796"> |- Неофициальные саундтреки к фильмам и сериалам (lossy)&nbsp;</option>
                                            <option id="fs-784" value="784"> |- Саундтреки к играм (lossless)&nbsp;</option>
                                            <option id="fs-783" value="783"> |- Саундтреки к играм (lossy)&nbsp;</option>
                                            <option id="fs-2331" value="2331"> |- Неофициальные саундтреки к играм (lossy)&nbsp;</option>
                                            <option id="fs-2431" value="2431"> |- Аранжировки музыки из игр (lossy и lossless)&nbsp;</option>
                                            <option id="fs-880" value="880"> |- Мюзикл (lossy и lossless)&nbsp;</option>
                                            <option id="fs-655" value="655"> |- Мюзикл (Видео и DVD Video)&nbsp;</option>
                                            <option id="fs-1215" value="1215" class="root_forum has_sf">Шансон, Авторская и Военная песня&nbsp;</option>
                                            <option id="fs-1220" value="1220"> |- Отечественный шансон (lossless)&nbsp;</option>
                                            <option id="fs-1221" value="1221"> |- Отечественный шансон (lossy)&nbsp;</option>
                                            <option id="fs-1334" value="1334"> |- Сборники отечественного шансона (lossy)&nbsp;</option>
                                            <option id="fs-1216" value="1216"> |- Военная песня, марши (lossless)&nbsp;</option>
                                            <option id="fs-1223" value="1223"> |- Военная песня, марши (lossy)&nbsp;</option>
                                            <option id="fs-1224" value="1224"> |- Авторская песня (lossless)&nbsp;</option>
                                            <option id="fs-1225" value="1225"> |- Авторская песня (lossy)&nbsp;</option>
                                            <option id="fs-1226" value="1226"> |- Менестрели и ролевики (lossy и lossless)&nbsp;</option>
                                            <option id="fs-1227" value="1227"> |- Видео (Шансон, Авторская и Военная песня)&nbsp;</option>
                                            <option id="fs-1228" value="1228"> |- DVD Видео (Шансон, Авторская и Военная песня)&nbsp;</option>
                                            <option id="fs-413" value="413" class="root_forum has_sf">Музыка других жанров&nbsp;</option>
                                            <option id="fs-466" value="466"> |- Зарубежная музыка других жанров (lossy)&nbsp;</option>
                                            <option id="fs-465" value="465"> |- Зарубежная музыка других жанров (lossless)&nbsp;</option>
                                            <option id="fs-475" value="475"> |- Видео (Музыка других жанров)&nbsp;</option>
                                            <option id="fs-988" value="988"> |- DVD Video (Музыка других жанров)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Популярная музыка">
                                            <option id="fs-2495" value="2495" class="root_forum has_sf">Отечественная поп-музыка&nbsp;</option>
                                            <option id="fs-424" value="424"> |- Отечественная поп-музыка (lossy)&nbsp;</option>
                                            <option id="fs-1361" value="1361"> |- Отечественная поп-музыка (сборники) (lossy)&nbsp;</option>
                                            <option id="fs-425" value="425"> |- Отечественная поп-музыка (lossless)&nbsp;</option>
                                            <option id="fs-1635" value="1635"> |- Советская эстрада, ретро, романсы (lossy)&nbsp;</option>
                                            <option id="fs-1634" value="1634"> |- Советская эстрада, ретро, романсы (lossless)&nbsp;</option>
                                            <option id="fs-1351" value="1351"> |- Сборники песен для детей (lossy и lossless)&nbsp;</option>
                                            <option id="fs-2497" value="2497" class="root_forum has_sf">Зарубежная поп-музыка&nbsp;</option>
                                            <option id="fs-428" value="428"> |- Зарубежная поп-музыка (lossy)&nbsp;</option>
                                            <option id="fs-1362" value="1362"> |- Зарубежная поп-музыка (сборники) (lossy)&nbsp;</option>
                                            <option id="fs-429" value="429"> |- Зарубежная поп-музыка (lossless)&nbsp;</option>
                                            <option id="fs-735" value="735"> |- Итальянская поп-музыка (lossy)&nbsp;</option>
                                            <option id="fs-1753" value="1753"> |- Итальянская поп-музыка (lossless)&nbsp;</option>
                                            <option id="fs-2232" value="2232"> |- Латиноамериканская поп-музыка (lossy)&nbsp;</option>
                                            <option id="fs-714" value="714"> |- Латиноамериканская поп-музыка (lossless)&nbsp;</option>
                                            <option id="fs-1331" value="1331"> |- Восточноазиатская поп-музыка (lossy)&nbsp;</option>
                                            <option id="fs-1330" value="1330"> |- Восточноазиатская поп-музыка (lossless)&nbsp;</option>
                                            <option id="fs-1219" value="1219"> |- Зарубежный шансон (lossy)&nbsp;</option>
                                            <option id="fs-1452" value="1452"> |- Зарубежный шансон (lossless)&nbsp;</option>
                                            <option id="fs-2275" value="2275"> |- Easy Listening, Instrumental Pop (lossy)&nbsp;</option>
                                            <option id="fs-2270" value="2270"> |- Easy Listening, Instrumental Pop (lossless)&nbsp;</option>
                                            <option id="fs-2499" value="2499" class="root_forum has_sf">Eurodance, Disco, Hi-NRG&nbsp;</option>
                                            <option id="fs-2503" value="2503"> |- Eurodance, Euro-House, Technopop (lossy)&nbsp;</option>
                                            <option id="fs-2504" value="2504"> |- Eurodance, Euro-House, Technopop (сборники) (lossy)&nbsp;</option>
                                            <option id="fs-2502" value="2502"> |- Eurodance, Euro-House, Technopop (lossless)&nbsp;</option>
                                            <option id="fs-2501" value="2501"> |- Disco, Italo-Disco, Euro-Disco, Hi-NRG (lossy)&nbsp;</option>
                                            <option id="fs-2505" value="2505"> |- Disco, Italo-Disco, Euro-Disco, Hi-NRG (сборники) (lossy)&nbsp;</option>
                                            <option id="fs-2500" value="2500"> |- Disco, Italo-Disco, Euro-Disco, Hi-NRG (lossless)&nbsp;</option>
                                            <option id="fs-2507" value="2507" class="root_forum has_sf">Видео, DVD Video, HD Video (поп-музыка)&nbsp;</option>
                                            <option id="fs-1121" value="1121"> |- Отечественная поп-музыка (Видео)&nbsp;</option>
                                            <option id="fs-1122" value="1122"> |- Отечественная поп-музыка (DVD Video)&nbsp;</option>
                                            <option id="fs-2510" value="2510"> |- Советская эстрада, ретро, романсы (Видео)&nbsp;</option>
                                            <option id="fs-2509" value="2509"> |- Советская эстрада, ретро, романсы (DVD Video)&nbsp;</option>
                                            <option id="fs-431" value="431"> |- Зарубежная поп-музыка (Видео)&nbsp;</option>
                                            <option id="fs-986" value="986"> |- Зарубежная поп-музыка (DVD Video)&nbsp;</option>
                                            <option id="fs-2532" value="2532"> |- Eurodance, Disco (Видео)&nbsp;</option>
                                            <option id="fs-2531" value="2531"> |- Eurodance, Disco (DVD Video)&nbsp;</option>
                                            <option id="fs-2378" value="2378"> |- Восточноазиатская поп-музыка (Видео)&nbsp;</option>
                                            <option id="fs-2379" value="2379"> |- Восточноазиатская поп-музыка (DVD Video)&nbsp;</option>
                                            <option id="fs-2383" value="2383"> |- Зарубежный шансон (Видео)&nbsp;</option>
                                            <option id="fs-2384" value="2384"> |- Зарубежный шансон (DVD Video)&nbsp;</option>
                                            <option id="fs-2088" value="2088" title="Отечественная поп-музыка (Сборные концерты, док. видео) (Видео и DVD)"> |- Отечественная поп-музыка (Сборные концерты, док. видео) (Видео и D..&nbsp;</option>
                                            <option id="fs-2089" value="2089"> |- Зарубежная поп-музыка (Сборные концерты, док. видео) (Видео и DVD)&nbsp;</option>
                                            <option id="fs-2426" value="2426"> |- Отечественная Поп-музыка, Шансон, Eurodance, Disco (HD Video)&nbsp;</option>
                                            <option id="fs-2508" value="2508"> |- Зарубежная Поп-музыка, Шансон, Eurodance, Disco (HD Video)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Джазовая и Блюзовая музыка">
                                            <option id="fs-2267" value="2267" class="root_forum has_sf">Зарубежный джаз&nbsp;</option>
                                            <option id="fs-2277" value="2277"> |- Early Jazz, Swing, Gypsy (lossless)&nbsp;</option>
                                            <option id="fs-2278" value="2278"> |- Bop (lossless)&nbsp;</option>
                                            <option id="fs-2279" value="2279"> |- Mainstream Jazz, Cool (lossless)&nbsp;</option>
                                            <option id="fs-2280" value="2280"> |- Jazz Fusion (lossless)&nbsp;</option>
                                            <option id="fs-2281" value="2281"> |- World Fusion, Ethnic Jazz (lossless)&nbsp;</option>
                                            <option id="fs-2282" value="2282"> |- Avant-Garde Jazz, Free Improvisation (lossless)&nbsp;</option>
                                            <option id="fs-2353" value="2353"> |- Modern Creative, Third Stream (lossless)&nbsp;</option>
                                            <option id="fs-2284" value="2284"> |- Smooth, Jazz-Pop (lossless)&nbsp;</option>
                                            <option id="fs-2285" value="2285"> |- Vocal Jazz (lossless)&nbsp;</option>
                                            <option id="fs-2283" value="2283"> |- Funk, Soul, R&amp;B (lossless)&nbsp;</option>
                                            <option id="fs-2286" value="2286"> |- Сборники зарубежного джаза (lossless)&nbsp;</option>
                                            <option id="fs-2287" value="2287"> |- Зарубежный джаз (lossy)&nbsp;</option>
                                            <option id="fs-2268" value="2268" class="root_forum has_sf">Зарубежный блюз&nbsp;</option>
                                            <option id="fs-2293" value="2293"> |- Blues (Texas, Chicago, Modern and Others) (lossless)&nbsp;</option>
                                            <option id="fs-2292" value="2292"> |- Blues-rock (lossless)&nbsp;</option>
                                            <option id="fs-2290" value="2290"> |- Roots, Pre-War Blues, Early R&amp;B, Gospel (lossless)&nbsp;</option>
                                            <option id="fs-2289" value="2289"> |- Зарубежный блюз (сборники; Tribute VA) (lossless)&nbsp;</option>
                                            <option id="fs-2288" value="2288"> |- Зарубежный блюз (lossy)&nbsp;</option>
                                            <option id="fs-2269" value="2269" class="root_forum has_sf">Отечественный джаз и блюз&nbsp;</option>
                                            <option id="fs-2297" value="2297"> |- Отечественный джаз (lossless)&nbsp;</option>
                                            <option id="fs-2295" value="2295"> |- Отечественный джаз (lossy)&nbsp;</option>
                                            <option id="fs-2296" value="2296"> |- Отечественный блюз (lossless)&nbsp;</option>
                                            <option id="fs-2298" value="2298"> |- Отечественный блюз (lossy)&nbsp;</option>
                                            <option id="fs-2271" value="2271" class="root_forum has_sf">Видео, DVD Video, HD Video (Джаз и блюз)&nbsp;</option>
                                            <option id="fs-2305" value="2305"> |- Джаз и Блюз (Видео)&nbsp;</option>
                                            <option id="fs-2304" value="2304"> |- Джаз и Блюз (DVD Видео)&nbsp;</option>
                                            <option id="fs-2306" value="2306"> |- Джаз и Блюз (HD Video)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Рок-музыка">
                                            <option id="fs-1698" value="1698" class="root_forum has_sf">Зарубежный Rock&nbsp;</option>
                                            <option id="fs-1702" value="1702"> |- Classic Rock &amp; Hard Rock (lossless)&nbsp;</option>
                                            <option id="fs-1703" value="1703"> |- Classic Rock &amp; Hard Rock (lossy)&nbsp;</option>
                                            <option id="fs-1704" value="1704"> |- Progressive &amp; Art-Rock (lossless)&nbsp;</option>
                                            <option id="fs-1705" value="1705"> |- Progressive &amp; Art-Rock (lossy)&nbsp;</option>
                                            <option id="fs-1706" value="1706"> |- Folk-Rock (lossless)&nbsp;</option>
                                            <option id="fs-1707" value="1707"> |- Folk-Rock (lossy)&nbsp;</option>
                                            <option id="fs-2329" value="2329"> |- AOR (Melodic Hard Rock, Arena rock) (lossless)&nbsp;</option>
                                            <option id="fs-2330" value="2330"> |- AOR (Melodic Hard Rock, Arena rock) (lossy)&nbsp;</option>
                                            <option id="fs-1708" value="1708"> |- Pop-Rock &amp; Soft Rock (lossless)&nbsp;</option>
                                            <option id="fs-1709" value="1709"> |- Pop-Rock &amp; Soft Rock (lossy)&nbsp;</option>
                                            <option id="fs-1710" value="1710"> |- Instrumental Guitar Rock (lossless)&nbsp;</option>
                                            <option id="fs-1711" value="1711"> |- Instrumental Guitar Rock (lossy)&nbsp;</option>
                                            <option id="fs-1712" value="1712"> |- Rockabilly, Psychobilly, Rock&#039;n&#039;Roll (lossless)&nbsp;</option>
                                            <option id="fs-1713" value="1713"> |- Rockabilly, Psychobilly, Rock&#039;n&#039;Roll (lossy)&nbsp;</option>
                                            <option id="fs-731" value="731"> |- Сборники зарубежного рока (lossless)&nbsp;</option>
                                            <option id="fs-1799" value="1799"> |- Сборники зарубежного рока (lossy)&nbsp;</option>
                                            <option id="fs-1714" value="1714"> |- Восточноазиатский рок (lossless)&nbsp;</option>
                                            <option id="fs-1715" value="1715"> |- Восточноазиатский рок (lossy)&nbsp;</option>
                                            <option id="fs-1716" value="1716" class="root_forum has_sf">Зарубежный Metal&nbsp;</option>
                                            <option id="fs-1796" value="1796"> |- Avant-garde, Experimental Metal (lossless)&nbsp;</option>
                                            <option id="fs-1797" value="1797"> |- Avant-garde, Experimental Metal (lossy)&nbsp;</option>
                                            <option id="fs-1719" value="1719"> |- Black (lossless)&nbsp;</option>
                                            <option id="fs-1778" value="1778"> |- Black (lossy)&nbsp;</option>
                                            <option id="fs-1779" value="1779"> |- Death, Doom (lossless)&nbsp;</option>
                                            <option id="fs-1780" value="1780"> |- Death, Doom (lossy)&nbsp;</option>
                                            <option id="fs-1720" value="1720"> |- Folk, Pagan, Viking (lossless)&nbsp;</option>
                                            <option id="fs-798" value="798"> |- Folk, Pagan, Viking (lossy)&nbsp;</option>
                                            <option id="fs-1724" value="1724"> |- Gothic Metal (lossless)&nbsp;</option>
                                            <option id="fs-1725" value="1725"> |- Gothic Metal (lossy)&nbsp;</option>
                                            <option id="fs-1730" value="1730"> |- Grind, Brutal Death (lossless)&nbsp;</option>
                                            <option id="fs-1731" value="1731"> |- Grind, Brutal Death (lossy)&nbsp;</option>
                                            <option id="fs-1726" value="1726"> |- Heavy, Power, Progressive (lossless)&nbsp;</option>
                                            <option id="fs-1727" value="1727"> |- Heavy, Power, Progressive (lossy)&nbsp;</option>
                                            <option id="fs-1815" value="1815"> |- Sludge, Stoner, Post-Metal (lossless)&nbsp;</option>
                                            <option id="fs-1816" value="1816"> |- Sludge, Stoner, Post-Metal (lossy)&nbsp;</option>
                                            <option id="fs-1728" value="1728"> |- Thrash, Speed (lossless)&nbsp;</option>
                                            <option id="fs-1729" value="1729"> |- Thrash, Speed (lossy)&nbsp;</option>
                                            <option id="fs-2230" value="2230"> |- Сборники (lossless)&nbsp;</option>
                                            <option id="fs-2231" value="2231"> |- Сборники (lossy)&nbsp;</option>
                                            <option id="fs-1732" value="1732" class="root_forum has_sf">Зарубежные Alternative, Punk, Independent&nbsp;</option>
                                            <option id="fs-1736" value="1736"> |- Alternative &amp; Nu-metal (lossless)&nbsp;</option>
                                            <option id="fs-1737" value="1737"> |- Alternative &amp; Nu-metal (lossy)&nbsp;</option>
                                            <option id="fs-1738" value="1738"> |- Punk (lossless)&nbsp;</option>
                                            <option id="fs-1739" value="1739"> |- Punk (lossy)&nbsp;</option>
                                            <option id="fs-1740" value="1740"> |- Hardcore (lossless)&nbsp;</option>
                                            <option id="fs-1741" value="1741"> |- Hardcore (lossy)&nbsp;</option>
                                            <option id="fs-1742" value="1742"> |- Indie, Post-Rock &amp; Post-Punk (lossless)&nbsp;</option>
                                            <option id="fs-1743" value="1743"> |- Indie, Post-Rock &amp; Post-Punk (lossy)&nbsp;</option>
                                            <option id="fs-1744" value="1744"> |- Industrial &amp; Post-industrial (lossless)&nbsp;</option>
                                            <option id="fs-1745" value="1745"> |- Industrial &amp; Post-industrial (lossy)&nbsp;</option>
                                            <option id="fs-1746" value="1746"> |- Emocore, Post-hardcore, Metalcore (lossless)&nbsp;</option>
                                            <option id="fs-1747" value="1747"> |- Emocore, Post-hardcore, Metalcore (lossy)&nbsp;</option>
                                            <option id="fs-1748" value="1748"> |- Gothic Rock &amp; Dark Folk (lossless)&nbsp;</option>
                                            <option id="fs-1749" value="1749"> |- Gothic Rock &amp; Dark Folk (lossy)&nbsp;</option>
                                            <option id="fs-2175" value="2175"> |- Avant-garde, Experimental Rock (lossless)&nbsp;</option>
                                            <option id="fs-2174" value="2174"> |- Avant-garde, Experimental Rock (lossy)&nbsp;</option>
                                            <option id="fs-722" value="722" class="root_forum has_sf">Отечественный Rock, Metal&nbsp;</option>
                                            <option id="fs-737" value="737"> |- Rock (lossless)&nbsp;</option>
                                            <option id="fs-738" value="738"> |- Rock (lossy)&nbsp;</option>
                                            <option id="fs-464" value="464"> |- Alternative, Punk, Independent (lossless)&nbsp;</option>
                                            <option id="fs-463" value="463"> |- Alternative, Punk, Independent (lossy)&nbsp;</option>
                                            <option id="fs-739" value="739"> |- Metal (lossless)&nbsp;</option>
                                            <option id="fs-740" value="740"> |- Metal (lossy)&nbsp;</option>
                                            <option id="fs-951" value="951"> |- Rock на языках народов xUSSR (lossless)&nbsp;</option>
                                            <option id="fs-952" value="952"> |- Rock на языках народов xUSSR (lossy)&nbsp;</option>
                                            <option id="fs-1781" value="1781" class="root_forum has_sf">Видео, DVD Video, HD Video (Рок-музыка)&nbsp;</option>
                                            <option id="fs-1782" value="1782"> |- Rock (Видео)&nbsp;</option>
                                            <option id="fs-1783" value="1783"> |- Rock (DVD Video)&nbsp;</option>
                                            <option id="fs-2261" value="2261"> |- Rock (Неофициальные DVD Video)&nbsp;</option>
                                            <option id="fs-1787" value="1787"> |- Metal (Видео)&nbsp;</option>
                                            <option id="fs-1788" value="1788"> |- Metal (DVD Video)&nbsp;</option>
                                            <option id="fs-2262" value="2262"> |- Metal (Неофициальные DVD Video)&nbsp;</option>
                                            <option id="fs-1789" value="1789"> |- Alternative, Punk, Independent (Видео)&nbsp;</option>
                                            <option id="fs-1790" value="1790"> |- Alternative, Punk, Independent (DVD Video)&nbsp;</option>
                                            <option id="fs-2263" value="2263"> |- Alternative, Punk, Independent (Неофициальные DVD Video)&nbsp;</option>
                                            <option id="fs-1791" value="1791"> |- Отечественный Рок, Панк, Альтернатива (Видео)&nbsp;</option>
                                            <option id="fs-1792" value="1792"> |- Отечественный Рок, Панк, Альтернатива (DVD Video)&nbsp;</option>
                                            <option id="fs-1793" value="1793"> |- Отечественный Металл (Видео)&nbsp;</option>
                                            <option id="fs-1794" value="1794"> |- Отечественный Металл (DVD Video)&nbsp;</option>
                                            <option id="fs-2264" value="2264" title="Отечественный Рок, Панк, Альтернатива, Металл (Неофициальные DVD Video)"> |- Отечественный Рок, Панк, Альтернатива, Металл (Неофициальные DVD V..&nbsp;</option>
                                            <option id="fs-1795" value="1795"> |- Рок-музыка (HD Video)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Электронная музыка">
                                            <option id="fs-1821" value="1821" class="root_forum has_sf">Trance, Goa Trance, Psy-Trance, PsyChill, Ambient, Dub&nbsp;</option>
                                            <option id="fs-1844" value="1844"> |- Goa Trance, Psy-Trance (lossless)&nbsp;</option>
                                            <option id="fs-1822" value="1822"> |- Goa Trance, Psy-Trance (lossy)&nbsp;</option>
                                            <option id="fs-1894" value="1894"> |- PsyChill, Ambient, Dub (lossless)&nbsp;</option>
                                            <option id="fs-1895" value="1895"> |- PsyChill, Ambient, Dub (lossy)&nbsp;</option>
                                            <option id="fs-460" value="460" title="Goa Trance, Psy-Trance, PsyChill, Ambient, Dub (Live Sets, Mixes) (lossy)"> |- Goa Trance, Psy-Trance, PsyChill, Ambient, Dub (Live Sets, Mixes) ..&nbsp;</option>
                                            <option id="fs-1818" value="1818"> |- Trance (lossless)&nbsp;</option>
                                            <option id="fs-1819" value="1819"> |- Trance (lossy)&nbsp;</option>
                                            <option id="fs-1847" value="1847"> |- Trance (Singles, EPs) (lossy)&nbsp;</option>
                                            <option id="fs-1824" value="1824"> |- Trance (Radioshows, Podcasts, Live Sets, Mixes) (lossy)&nbsp;</option>
                                            <option id="fs-1807" value="1807" class="root_forum has_sf">House, Techno, Hardcore, Hardstyle, Jumpstyle&nbsp;</option>
                                            <option id="fs-1829" value="1829"> |- Hardcore, Hardstyle, Jumpstyle (lossless)&nbsp;</option>
                                            <option id="fs-1830" value="1830"> |- Hardcore, Hardstyle, Jumpstyle (lossy)&nbsp;</option>
                                            <option id="fs-1831" value="1831"> |- Hardcore, Hardstyle, Jumpstyle (vinyl, web)&nbsp;</option>
                                            <option id="fs-1857" value="1857"> |- House (lossless)&nbsp;</option>
                                            <option id="fs-1859" value="1859"> |- House (Radioshow, Podcast, Liveset, Mixes)&nbsp;</option>
                                            <option id="fs-1858" value="1858"> |- House (lossy)&nbsp;</option>
                                            <option id="fs-840" value="840"> |- House (Проморелизы, сборники) (lossy)&nbsp;</option>
                                            <option id="fs-1860" value="1860"> |- House (Singles, EPs) (lossy)&nbsp;</option>
                                            <option id="fs-1825" value="1825"> |- Techno (lossless)&nbsp;</option>
                                            <option id="fs-1826" value="1826"> |- Techno (lossy)&nbsp;</option>
                                            <option id="fs-1827" value="1827"> |- Techno (Radioshows, Podcasts, Livesets, Mixes)&nbsp;</option>
                                            <option id="fs-1828" value="1828"> |- Techno (Singles, EPs) (lossy)&nbsp;</option>
                                            <option id="fs-1808" value="1808" class="root_forum has_sf">Drum &amp; Bass, Jungle, Breakbeat, Dubstep, IDM, Electro&nbsp;</option>
                                            <option id="fs-797" value="797"> |- Electro, Electro-Freestyle, Nu Electro (lossless)&nbsp;</option>
                                            <option id="fs-1805" value="1805"> |- Electro, Electro-Freestyle, Nu Electro (lossy)&nbsp;</option>
                                            <option id="fs-1832" value="1832"> |- Drum &amp; Bass, Jungle (lossless)&nbsp;</option>
                                            <option id="fs-1833" value="1833"> |- Drum &amp; Bass, Jungle (lossy)&nbsp;</option>
                                            <option id="fs-1834" value="1834"> |- Drum &amp; Bass, Jungle (Radioshows, Podcasts, Livesets, Mixes)&nbsp;</option>
                                            <option id="fs-1836" value="1836"> |- Breakbeat (lossless)&nbsp;</option>
                                            <option id="fs-1837" value="1837"> |- Breakbeat (lossy)&nbsp;</option>
                                            <option id="fs-1839" value="1839"> |- Dubstep (lossless)&nbsp;</option>
                                            <option id="fs-454" value="454"> |- Dubstep (lossy)&nbsp;</option>
                                            <option id="fs-1838" value="1838"> |- Breakbeat, Dubstep (Radioshows, Podcasts, Livesets, Mixes)&nbsp;</option>
                                            <option id="fs-1840" value="1840"> |- IDM (lossless)&nbsp;</option>
                                            <option id="fs-1841" value="1841"> |- IDM (lossy)&nbsp;</option>
                                            <option id="fs-2229" value="2229"> |- IDM Discography &amp; Collections (lossy)&nbsp;</option>
                                            <option id="fs-1809" value="1809" class="root_forum has_sf">Chillout, Lounge, Downtempo, Trip-Hop&nbsp;</option>
                                            <option id="fs-1861" value="1861"> |- Chillout, Lounge, Downtempo (lossless)&nbsp;</option>
                                            <option id="fs-1862" value="1862"> |- Chillout, Lounge, Downtempo (lossy)&nbsp;</option>
                                            <option id="fs-1947" value="1947"> |- Nu Jazz, Acid Jazz, Future Jazz (lossless)&nbsp;</option>
                                            <option id="fs-1946" value="1946"> |- Nu Jazz, Acid Jazz, Future Jazz (lossy)&nbsp;</option>
                                            <option id="fs-1945" value="1945"> |- Trip Hop, Abstract Hip-Hop (lossless)&nbsp;</option>
                                            <option id="fs-1944" value="1944"> |- Trip Hop, Abstract Hip-Hop (lossy)&nbsp;</option>
                                            <option id="fs-1810" value="1810" class="root_forum has_sf" title="Traditional Electronic, Ambient, Modern Classical, Electroacoustic, Experimental">Traditional Electronic, Ambient, Modern Classical, Electroacoustic, Ex..&nbsp;</option>
                                            <option id="fs-1864" value="1864"> |- Traditional Electronic, Ambient (lossless)&nbsp;</option>
                                            <option id="fs-1865" value="1865"> |- Traditional Electronic, Ambient (lossy)&nbsp;</option>
                                            <option id="fs-1871" value="1871"> |- Modern Classical, Electroacoustic (lossless)&nbsp;</option>
                                            <option id="fs-1867" value="1867"> |- Modern Classical, Electroacoustic (lossy)&nbsp;</option>
                                            <option id="fs-1869" value="1869"> |- Experimental (lossless)&nbsp;</option>
                                            <option id="fs-1873" value="1873"> |- Experimental (lossy)&nbsp;</option>
                                            <option id="fs-1907" value="1907"> |- 8-bit, Chiptune (lossy &amp; lossless)&nbsp;</option>
                                            <option id="fs-1811" value="1811" class="root_forum has_sf">Industrial, Noise, EBM, Dark Electro, Aggrotech, Synthpop, New Wave&nbsp;</option>
                                            <option id="fs-1868" value="1868"> |- EBM, Dark Electro, Aggrotech (lossless)&nbsp;</option>
                                            <option id="fs-1875" value="1875"> |- EBM, Dark Electro, Aggrotech (lossy)&nbsp;</option>
                                            <option id="fs-1877" value="1877"> |- Industrial, Noise (lossless)&nbsp;</option>
                                            <option id="fs-1878" value="1878"> |- Industrial, Noise (lossy)&nbsp;</option>
                                            <option id="fs-1880" value="1880"> |- Synthpop, New Wave (lossless)&nbsp;</option>
                                            <option id="fs-1881" value="1881"> |- Synthpop, New Wave (lossy)&nbsp;</option>
                                            <option id="fs-1866" value="1866"> |- Darkwave, Neoclassical, Ethereal, Dungeon Synth (lossless)&nbsp;</option>
                                            <option id="fs-406" value="406"> |- Darkwave, Neoclassical, Ethereal, Dungeon Synth (lossy)&nbsp;</option>
                                            <option id="fs-1842" value="1842" class="root_forum">Label Packs (lossless)&nbsp;</option>
                                            <option id="fs-1648" value="1648" class="root_forum">Label packs, Scene packs (lossy)&nbsp;</option>
                                            <option id="fs-1812" value="1812" class="root_forum has_sf">Электронная музыка (Видео, DVD Video, HD Video)&nbsp;</option>
                                            <option id="fs-1886" value="1886"> |- Электронная музыка (Официальные DVD Video)&nbsp;</option>
                                            <option id="fs-1887" value="1887"> |- Электронная музыка (Неофициальные, любительские DVD Video)&nbsp;</option>
                                            <option id="fs-1912" value="1912"> |- Электронная музыка (Видео)&nbsp;</option>
                                            <option id="fs-1913" value="1913"> |- Электронная музыка (HD Video)&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Hi-Res форматы, оцифровки">
                                            <option id="fs-1299" value="1299" class="root_forum has_sf">Hi-Res stereo и многоканальная музыка&nbsp;</option>
                                            <option id="fs-1884" value="1884"> |- Классика и классика в современной обработке (Hi-Res stereo)&nbsp;</option>
                                            <option id="fs-1164" value="1164" title="Классика и классика в современной обработке (многоканальная музыка)"> |- Классика и классика в современной обработке (многоканальная музыка..&nbsp;</option>
                                            <option id="fs-2513" value="2513" title="New Age, Relax, Meditative &amp; Flamenco (Hi-Res stereo и многоканальная музыка)"> |- New Age, Relax, Meditative &amp; Flamenco (Hi-Res stereo и многоканаль..&nbsp;</option>
                                            <option id="fs-1397" value="1397"> |- Саундтреки (Hi-Res stereo и многоканальная музыка)&nbsp;</option>
                                            <option id="fs-2512" value="2512"> |- Музыка разных жанров (Hi-Res stereo и многоканальная музыка)&nbsp;</option>
                                            <option id="fs-1885" value="1885"> |- Поп-музыка (Hi-Res stereo)&nbsp;</option>
                                            <option id="fs-1163" value="1163"> |- Поп-музыка (многоканальная музыка)&nbsp;</option>
                                            <option id="fs-2302" value="2302"> |- Джаз и Блюз (Hi-Res stereo)&nbsp;</option>
                                            <option id="fs-2303" value="2303"> |- Джаз и Блюз (многоканальная музыка)&nbsp;</option>
                                            <option id="fs-1755" value="1755"> |- Рок-музыка (Hi-Res stereo)&nbsp;</option>
                                            <option id="fs-1757" value="1757"> |- Рок-музыка (многоканальная музыка)&nbsp;</option>
                                            <option id="fs-1893" value="1893"> |- Электронная музыка (Hi-Res stereo)&nbsp;</option>
                                            <option id="fs-1890" value="1890"> |- Электронная музыка (многоканальная музыка)&nbsp;</option>
                                            <option id="fs-2219" value="2219" class="root_forum has_sf">Оцифровки с аналоговых носителей&nbsp;</option>
                                            <option id="fs-1660" value="1660"> |- Классика и классика в современной обработке (оцифровки)&nbsp;</option>
                                            <option id="fs-506" value="506"> |- Фольклор, народная и этническая музыка (оцифровки)&nbsp;</option>
                                            <option id="fs-1835" value="1835"> |- Rap, Hip-Hop, R&#039;n&#039;B, Reggae, Ska, Dub (оцифровки)&nbsp;</option>
                                            <option id="fs-1625" value="1625"> |- Саундтреки и мюзиклы (оцифровки)&nbsp;</option>
                                            <option id="fs-1217" value="1217"> |- Шансон, авторские, военные песни и марши (оцифровки)&nbsp;</option>
                                            <option id="fs-974" value="974"> |- Музыка других жанров (оцифровки)&nbsp;</option>
                                            <option id="fs-1444" value="1444"> |- Зарубежная поп-музыка (оцифровки)&nbsp;</option>
                                            <option id="fs-2401" value="2401"> |- Советская эстрада, ретро, романсы (оцифровки)&nbsp;</option>
                                            <option id="fs-239" value="239"> |- Отечественная поп-музыка (оцифровки)&nbsp;</option>
                                            <option id="fs-450" value="450"> |- Инструментальная поп-музыка (оцифровки)&nbsp;</option>
                                            <option id="fs-2301" value="2301"> |- Джаз и блюз (оцифровки)&nbsp;</option>
                                            <option id="fs-1756" value="1756"> |- Зарубежная рок-музыка (оцифровки)&nbsp;</option>
                                            <option id="fs-1758" value="1758"> |- Отечественная рок-музыка (оцифровки)&nbsp;</option>
                                            <option id="fs-1754" value="1754"> |- Электронная музыка (оцифровки)&nbsp;</option>
                                            <option id="fs-860" value="860" class="root_forum has_sf">Неофициальные конверсии цифровых форматов&nbsp;</option>
                                            <option id="fs-453" value="453"> |- Конверсии Quadraphonic&nbsp;</option>
                                            <option id="fs-1170" value="1170"> |- Конверсии SACD&nbsp;</option>
                                            <option id="fs-1759" value="1759"> |- Конверсии Blu-Ray, ADVD и DVD-Audio&nbsp;</option>
                                            <option id="fs-1852" value="1852"> |- Апмиксы-Upmixes/Даунмиксы-Downmix&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Игры">
                                            <option id="fs-5" value="5" class="root_forum has_sf">Игры для Windows&nbsp;</option>
                                            <option id="fs-635" value="635"> |- Горячие Новинки&nbsp;</option>
                                            <option id="fs-647" value="647"> |- Экшены от первого лица&nbsp;</option>
                                            <option id="fs-646" value="646"> |- Экшены от третьего лица&nbsp;</option>
                                            <option id="fs-50" value="50"> |- Хорроры&nbsp;</option>
                                            <option id="fs-127" value="127"> |- Аркады&nbsp;</option>
                                            <option id="fs-2203" value="2203"> |- Файтинги&nbsp;</option>
                                            <option id="fs-53" value="53"> |- Приключения и квесты&nbsp;</option>
                                            <option id="fs-1008" value="1008"> |- Квесты в стиле &quot;Поиск предметов&quot;&nbsp;</option>
                                            <option id="fs-900" value="900"> |- Аниме-игры&nbsp;</option>
                                            <option id="fs-128" value="128"> |- Для самых маленьких&nbsp;</option>
                                            <option id="fs-2204" value="2204"> |- Логические игры&nbsp;</option>
                                            <option id="fs-2118" value="2118"> |- Многопользовательские игры&nbsp;</option>
                                            <option id="fs-52" value="52"> |- Ролевые игры&nbsp;</option>
                                            <option id="fs-54" value="54"> |- Симуляторы&nbsp;</option>
                                            <option id="fs-51" value="51"> |- Стратегии в реальном времени&nbsp;</option>
                                            <option id="fs-2226" value="2226"> |- Пошаговые стратегии&nbsp;</option>
                                            <option id="fs-278" value="278"> |- Шахматы&nbsp;</option>
                                            <option id="fs-246" value="246"> |- Эротические игры&nbsp;</option>
                                            <option id="fs-2228" value="2228"> |- IBM PC-несовместимые&nbsp;</option>
                                            <option id="fs-2142" value="2142" class="root_forum has_sf">Microsoft Flight Simulator, X-Plane и аддоны для них&nbsp;</option>
                                            <option id="fs-2060" value="2060"> |- Сценарии, меши и аэропорты для FS2004, FSX, P3D&nbsp;</option>
                                            <option id="fs-2145" value="2145"> |- Самолёты и вертолёты для FS2004, FSX, P3D&nbsp;</option>
                                            <option id="fs-2146" value="2146"> |- Миссии, трафик, звуки, паки и утилиты для FS2004, FSX, P3D&nbsp;</option>
                                            <option id="fs-2143" value="2143"> |- Сценарии для X-Plane&nbsp;</option>
                                            <option id="fs-2012" value="2012"> |- Самолёты и вертолёты для X-Plane&nbsp;</option>
                                            <option id="fs-2188" value="2188"> |- Миссии, трафик, звуки, паки и утилиты для X-Plane&nbsp;</option>
                                            <option id="fs-139" value="139" class="root_forum has_sf">Прочее для Windows-игр&nbsp;</option>
                                            <option id="fs-2478" value="2478"> |- Официальные патчи, моды, плагины, дополнения&nbsp;</option>
                                            <option id="fs-2480" value="2480"> |- Неофициальные моды, плагины, дополнения&nbsp;</option>
                                            <option id="fs-2481" value="2481"> |- Русификаторы&nbsp;</option>
                                            <option id="fs-240" value="240" class="root_forum has_sf">Игровое видео&nbsp;</option>
                                            <option id="fs-2415" value="2415"> |- Видеопрохождения игр&nbsp;</option>
                                            <option id="fs-548" value="548" class="root_forum has_sf">Игры для консолей&nbsp;</option>
                                            <option id="fs-908" value="908"> |- PS&nbsp;</option>
                                            <option id="fs-357" value="357"> |- PS2&nbsp;</option>
                                            <option id="fs-886" value="886"> |- PS3&nbsp;</option>
                                            <option id="fs-546" value="546"> |- Игры PS1, PS2 и PSP для PS3&nbsp;</option>
                                            <option id="fs-1352" value="1352"> |- PSP&nbsp;</option>
                                            <option id="fs-1116" value="1116"> |- Игры PS1 для PSP&nbsp;</option>
                                            <option id="fs-973" value="973"> |- PS4, PSVITA&nbsp;</option>
                                            <option id="fs-887" value="887"> |- Original Xbox&nbsp;</option>
                                            <option id="fs-510" value="510"> |- Xbox 360&nbsp;</option>
                                            <option id="fs-773" value="773"> |- Wii/WiiU&nbsp;</option>
                                            <option id="fs-774" value="774"> |- NDS/3DS&nbsp;</option>
                                            <option id="fs-968" value="968"> |- Dreamcast&nbsp;</option>
                                            <option id="fs-129" value="129"> |- Остальные платформы&nbsp;</option>
                                            <option id="fs-2185" value="2185" class="root_forum has_sf">Видео для консолей&nbsp;</option>
                                            <option id="fs-2487" value="2487"> |- Видео для PSVita&nbsp;</option>
                                            <option id="fs-2182" value="2182"> |- Фильмы для PSP&nbsp;</option>
                                            <option id="fs-2181" value="2181"> |- Сериалы для PSP&nbsp;</option>
                                            <option id="fs-2180" value="2180"> |- Мультфильмы для PSP&nbsp;</option>
                                            <option id="fs-2179" value="2179"> |- Дорамы для PSP&nbsp;</option>
                                            <option id="fs-2186" value="2186"> |- Аниме для PSP&nbsp;</option>
                                            <option id="fs-700" value="700"> |- Видео для PSP&nbsp;</option>
                                            <option id="fs-1926" value="1926"> |- Видео для PS3 и других консолей&nbsp;</option>
                                            <option id="fs-899" value="899" class="root_forum has_sf">Игры для Linux&nbsp;</option>
                                            <option id="fs-1992" value="1992"> |- Нативные игры для Linux&nbsp;</option>
                                            <option id="fs-2059" value="2059"> |- Портированные игры для Linux&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Программы и Дизайн">
                                            <option id="fs-1012" value="1012" class="root_forum has_sf">Операционные системы от Microsoft&nbsp;</option>
                                            <option id="fs-2523" value="2523"> |- Настольные ОС от Microsoft - Windows 8 и далее&nbsp;</option>
                                            <option id="fs-1019" value="1019"> |- Настольные ОС от Microsoft (выпущенные до Windows XP)&nbsp;</option>
                                            <option id="fs-2153" value="2153"> |- Настольные ОС от Microsoft - Windows XP - Windows 7&nbsp;</option>
                                            <option id="fs-1021" value="1021"> |- Серверные ОС от Microsoft&nbsp;</option>
                                            <option id="fs-1025" value="1025"> |- Разное (Операционные системы от Microsoft)&nbsp;</option>
                                            <option id="fs-1376" value="1376" class="root_forum has_sf">Linux, Unix и другие ОС&nbsp;</option>
                                            <option id="fs-1379" value="1379"> |- Операционные системы (Linux, Unix)&nbsp;</option>
                                            <option id="fs-1381" value="1381"> |- Программное обеспечение (Linux, Unix)&nbsp;</option>
                                            <option id="fs-1473" value="1473"> |- Другие ОС и ПО под них&nbsp;</option>
                                            <option id="fs-1195" value="1195" class="root_forum">Тестовые диски для настройки аудио/видео аппаратуры&nbsp;</option>
                                            <option id="fs-1013" value="1013" class="root_forum has_sf">Системные программы&nbsp;</option>
                                            <option id="fs-1028" value="1028"> |- Работа с жёстким диском&nbsp;</option>
                                            <option id="fs-1029" value="1029"> |- Резервное копирование&nbsp;</option>
                                            <option id="fs-1030" value="1030"> |- Архиваторы и файловые менеджеры&nbsp;</option>
                                            <option id="fs-1031" value="1031"> |- Программы для настройки и оптимизации ОС&nbsp;</option>
                                            <option id="fs-1032" value="1032"> |- Сервисное обслуживание компьютера&nbsp;</option>
                                            <option id="fs-1033" value="1033"> |- Работа с носителями информации&nbsp;</option>
                                            <option id="fs-1034" value="1034"> |- Информация и диагностика&nbsp;</option>
                                            <option id="fs-1066" value="1066"> |- Программы для интернет и сетей&nbsp;</option>
                                            <option id="fs-1035" value="1035"> |- ПО для защиты компьютера (Антивирусное ПО, Фаерволлы)&nbsp;</option>
                                            <option id="fs-1038" value="1038"> |- Анти-шпионы и анти-трояны&nbsp;</option>
                                            <option id="fs-1039" value="1039"> |- Программы для защиты информации&nbsp;</option>
                                            <option id="fs-1536" value="1536"> |- Драйверы и прошивки&nbsp;</option>
                                            <option id="fs-1051" value="1051"> |- Оригинальные диски к компьютерам и комплектующим&nbsp;</option>
                                            <option id="fs-1040" value="1040"> |- Серверное ПО для Windows&nbsp;</option>
                                            <option id="fs-1041" value="1041"> |- Изменение интерфейса ОС Windows&nbsp;</option>
                                            <option id="fs-1636" value="1636"> |- Скринсейверы&nbsp;</option>
                                            <option id="fs-1042" value="1042"> |- Разное (Системные программы под Windows)&nbsp;</option>
                                            <option id="fs-1014" value="1014" class="root_forum has_sf">Системы для бизнеса, офиса, научной и проектной работы&nbsp;</option>
                                            <option id="fs-1060" value="1060"> |- Всё для дома: кройка, шитьё, кулинария&nbsp;</option>
                                            <option id="fs-1061" value="1061"> |- Офисные системы&nbsp;</option>
                                            <option id="fs-1062" value="1062"> |- Системы для бизнеса&nbsp;</option>
                                            <option id="fs-1067" value="1067"> |- Распознавание текста, звука и синтез речи&nbsp;</option>
                                            <option id="fs-1086" value="1086"> |- Работа с PDF и DjVu&nbsp;</option>
                                            <option id="fs-1068" value="1068"> |- Словари, переводчики&nbsp;</option>
                                            <option id="fs-1063" value="1063"> |- Системы для научной работы&nbsp;</option>
                                            <option id="fs-1087" value="1087"> |- САПР (общие и машиностроительные)&nbsp;</option>
                                            <option id="fs-1192" value="1192"> |- САПР (электроника, автоматика, ГАП)&nbsp;</option>
                                            <option id="fs-1088" value="1088"> |- Программы для архитекторов и строителей&nbsp;</option>
                                            <option id="fs-1193" value="1193"> |- Библиотеки и проекты для архитекторов и дизайнеров интерьеров&nbsp;</option>
                                            <option id="fs-1071" value="1071"> |- Прочие справочные системы&nbsp;</option>
                                            <option id="fs-1073" value="1073"> |- Разное (Системы для бизнеса, офиса, научной и проектной работы)&nbsp;</option>
                                            <option id="fs-1052" value="1052" class="root_forum has_sf">Веб-разработка и Программирование&nbsp;</option>
                                            <option id="fs-1053" value="1053"> |- WYSIWYG Редакторы для веб-диза&nbsp;</option>
                                            <option id="fs-1054" value="1054"> |- Текстовые редакторы с подсветкой&nbsp;</option>
                                            <option id="fs-1055" value="1055"> |- Среды программирования, компиляторы и вспомогательные программы&nbsp;</option>
                                            <option id="fs-1056" value="1056"> |- Компоненты для сред программирования&nbsp;</option>
                                            <option id="fs-2077" value="2077"> |- Системы управления базами данных&nbsp;</option>
                                            <option id="fs-1057" value="1057"> |- Скрипты и движки сайтов, CMS а также расширения к ним&nbsp;</option>
                                            <option id="fs-1018" value="1018"> |- Шаблоны для сайтов и CMS&nbsp;</option>
                                            <option id="fs-1058" value="1058"> |- Разное (Веб-разработка и программирование)&nbsp;</option>
                                            <option id="fs-1016" value="1016" class="root_forum has_sf">Программы для работы с мультимедиа и 3D&nbsp;</option>
                                            <option id="fs-1079" value="1079"> |- Программные комплекты&nbsp;</option>
                                            <option id="fs-1080" value="1080"> |- Плагины для программ компании Adobe&nbsp;</option>
                                            <option id="fs-1081" value="1081"> |- Графические редакторы&nbsp;</option>
                                            <option id="fs-1082" value="1082"> |- Программы для верстки, печати и работы со шрифтами&nbsp;</option>
                                            <option id="fs-1083" value="1083"> |- 3D моделирование, рендеринг и плагины для них&nbsp;</option>
                                            <option id="fs-1084" value="1084"> |- Анимация&nbsp;</option>
                                            <option id="fs-1085" value="1085"> |- Создание BD/HD/DVD-видео&nbsp;</option>
                                            <option id="fs-1089" value="1089"> |- Редакторы видео&nbsp;</option>
                                            <option id="fs-1090" value="1090"> |- Видео- Аудио- конверторы&nbsp;</option>
                                            <option id="fs-1065" value="1065"> |- Аудио- и видео-, CD- проигрыватели и каталогизаторы&nbsp;</option>
                                            <option id="fs-1064" value="1064"> |- Каталогизаторы и просмотрщики графики&nbsp;</option>
                                            <option id="fs-1092" value="1092"> |- Разное (Программы для работы с мультимедиа и 3D)&nbsp;</option>
                                            <option id="fs-1204" value="1204"> |- Виртуальные студии, секвенсоры и аудиоредакторы&nbsp;</option>
                                            <option id="fs-1027" value="1027"> |- Виртуальные инструменты и синтезаторы&nbsp;</option>
                                            <option id="fs-1199" value="1199"> |- Плагины для обработки звука&nbsp;</option>
                                            <option id="fs-1091" value="1091"> |- Разное (Программы для работы со звуком)&nbsp;</option>
                                            <option id="fs-828" value="828" class="root_forum has_sf">Материалы для мультимедиа и дизайна&nbsp;</option>
                                            <option id="fs-1357" value="1357"> |- Авторские работы&nbsp;</option>
                                            <option id="fs-890" value="890"> |- Официальные сборники векторных клипартов&nbsp;</option>
                                            <option id="fs-830" value="830"> |- Прочие векторные клипарты&nbsp;</option>
                                            <option id="fs-1290" value="1290"> |- Photostoсks&nbsp;</option>
                                            <option id="fs-1962" value="1962"> |- Костюмы для фотомонтажа&nbsp;</option>
                                            <option id="fs-831" value="831"> |- Рамки и виньетки для оформления фотографий&nbsp;</option>
                                            <option id="fs-829" value="829"> |- Прочие растровые клипарты&nbsp;</option>
                                            <option id="fs-633" value="633"> |- 3D модели, сцены и материалы&nbsp;</option>
                                            <option id="fs-1009" value="1009"> |- Футажи&nbsp;</option>
                                            <option id="fs-1963" value="1963"> |- Прочие сборники футажей&nbsp;</option>
                                            <option id="fs-1954" value="1954"> |- Музыкальные библиотеки&nbsp;</option>
                                            <option id="fs-1010" value="1010"> |- Звуковые эффекты&nbsp;</option>
                                            <option id="fs-1674" value="1674"> |- Библиотеки сэмплов&nbsp;</option>
                                            <option id="fs-2421" value="2421"> |- Библиотеки и саундбанки для сэмплеров, пресеты для синтезаторов&nbsp;</option>
                                            <option id="fs-2492" value="2492"> |- Multitracks&nbsp;</option>
                                            <option id="fs-839" value="839"> |- Материалы для создания меню и обложек DVD&nbsp;</option>
                                            <option id="fs-1679" value="1679"> |- Стили, кисти, формы и узоры для Adobe Photoshop&nbsp;</option>
                                            <option id="fs-1011" value="1011"> |- Шрифты&nbsp;</option>
                                            <option id="fs-835" value="835"> |- Разное (Материалы для мультимедиа и дизайна)&nbsp;</option>
                                            <option id="fs-1503" value="1503" class="root_forum has_sf">ГИС, системы навигации и карты&nbsp;</option>
                                            <option id="fs-1507" value="1507"> |- ГИС (Геоинформационные системы)&nbsp;</option>
                                            <option id="fs-1526" value="1526"> |- Карты, снабженные программной оболочкой&nbsp;</option>
                                            <option id="fs-1508" value="1508"> |- Атласы и карты современные (после 1950 г.)&nbsp;</option>
                                            <option id="fs-1509" value="1509"> |- Атласы и карты старинные (до 1950 г.)&nbsp;</option>
                                            <option id="fs-1510" value="1510"> |- Карты прочие (астрономические, исторические, тематические)&nbsp;</option>
                                            <option id="fs-1511" value="1511"> |- Встроенная автомобильная навигация&nbsp;</option>
                                            <option id="fs-1512" value="1512"> |- Garmin&nbsp;</option>
                                            <option id="fs-1513" value="1513"> |- Ozi&nbsp;</option>
                                            <option id="fs-1514" value="1514"> |- TomTom&nbsp;</option>
                                            <option id="fs-1515" value="1515"> |- Navigon / Navitel&nbsp;</option>
                                            <option id="fs-1516" value="1516"> |- Igo&nbsp;</option>
                                            <option id="fs-1517" value="1517"> |- Разное - системы навигации и карты&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Мобильные устройства">
                                            <option id="fs-285" value="285" class="root_forum has_sf">Игры, приложения и прочее для мобильных устройств&nbsp;</option>
                                            <option id="fs-2149" value="2149"> |- Игры для Android OS&nbsp;</option>
                                            <option id="fs-2154" value="2154"> |- Приложения для Android OS&nbsp;</option>
                                            <option id="fs-2420" value="2420"> |- Игры для Windows Phone 7, 8&nbsp;</option>
                                            <option id="fs-2419" value="2419"> |- Приложения для Windows Phone 7, 8&nbsp;</option>
                                            <option id="fs-1004" value="1004"> |- Игры для Symbian&nbsp;</option>
                                            <option id="fs-289" value="289"> |- Приложения для Symbian&nbsp;</option>
                                            <option id="fs-1001" value="1001"> |- Игры для Java&nbsp;</option>
                                            <option id="fs-1005" value="1005"> |- Приложения для Java&nbsp;</option>
                                            <option id="fs-1002" value="1002"> |- Игры для Windows Mobile, Palm OS, BlackBerry и прочих&nbsp;</option>
                                            <option id="fs-290" value="290"> |- Приложения для Windows Mobile, Palm OS, BlackBerry и прочих&nbsp;</option>
                                            <option id="fs-288" value="288"> |- Софт для работы с телефоном&nbsp;</option>
                                            <option id="fs-292" value="292"> |- Прошивки для телефонов&nbsp;</option>
                                            <option id="fs-291" value="291"> |- Обои и темы&nbsp;</option>
                                            <option id="fs-957" value="957" class="root_forum has_sf">Видео для мобильных устройств&nbsp;</option>
                                            <option id="fs-287" value="287"> |- Видео для смартфонов и КПК&nbsp;</option>
                                            <option id="fs-286" value="286"> |- Видео в формате 3GP для мобильных&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Медицина и здоровье">
                                            <option id="fs-2125" value="2125" class="root_forum has_sf">Книги, журналы и программы&nbsp;</option>
                                            <option id="fs-2133" value="2133"> |- Клиническая медицина до 1980 г.&nbsp;</option>
                                            <option id="fs-2130" value="2130"> |- Клиническая медицина с 1980 по 2000 г.&nbsp;</option>
                                            <option id="fs-2313" value="2313"> |- Клиническая медицина после 2000 г.&nbsp;</option>
                                            <option id="fs-2314" value="2314"> |- Популярная медицинская периодика (газеты и журналы)&nbsp;</option>
                                            <option id="fs-2528" value="2528"> |- Научная медицинская периодика (газеты и журналы)&nbsp;</option>
                                            <option id="fs-2129" value="2129"> |- Медико-биологические науки&nbsp;</option>
                                            <option id="fs-2141" value="2141"> |- Фармация и фармакология&nbsp;</option>
                                            <option id="fs-2132" value="2132"> |- Нетрадиционная, народная медицина и популярные книги о здоровье&nbsp;</option>
                                            <option id="fs-2131" value="2131"> |- Ветеринария, разное&nbsp;</option>
                                            <option id="fs-2315" value="2315"> |- Тематические коллекции книг&nbsp;</option>
                                            <option id="fs-1350" value="1350"> |- Аудиокниги по медицине&nbsp;</option>
                                            <option id="fs-2134" value="2134"> |- Медицинский софт&nbsp;</option>
                                            <option id="fs-2126" value="2126" class="root_forum has_sf">Видеоуроки, док. фильмы и телепередачи по медицине&nbsp;</option>
                                            <option id="fs-2135" value="2135"> |- Медицина и стоматология&nbsp;</option>
                                            <option id="fs-2140" value="2140"> |- Психотерапия и клиническая психология&nbsp;</option>
                                            <option id="fs-2136" value="2136"> |- Массаж&nbsp;</option>
                                            <option id="fs-2138" value="2138"> |- Здоровье&nbsp;</option>
                                            <option id="fs-2139" value="2139"> |- Документальные фильмы и телепередачи по медицине&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Apple">
                                            <option id="fs-1366" value="1366" class="root_forum has_sf">Apple Macintosh&nbsp;</option>
                                            <option id="fs-1368" value="1368"> |- Mac OS (для Macintosh)&nbsp;</option>
                                            <option id="fs-1383" value="1383"> |- Mac OS (для РС-Хакинтош)&nbsp;</option>
                                            <option id="fs-537" value="537"> |- Игры (Mac OS)&nbsp;</option>
                                            <option id="fs-1394" value="1394"> |- Программы для просмотра и обработки видео (Mac OS)&nbsp;</option>
                                            <option id="fs-1370" value="1370"> |- Программы для создания и обработки графики (Mac OS)&nbsp;</option>
                                            <option id="fs-2237" value="2237"> |- Плагины для программ компании Adobe (Mac OS)&nbsp;</option>
                                            <option id="fs-1372" value="1372"> |- Аудио редакторы и конвертеры (Mac OS)&nbsp;</option>
                                            <option id="fs-1373" value="1373"> |- Системные программы (Mac OS)&nbsp;</option>
                                            <option id="fs-1375" value="1375"> |- Офисные программы (Mac OS)&nbsp;</option>
                                            <option id="fs-1371" value="1371"> |- Программы для интернета и сетей (Mac OS)&nbsp;</option>
                                            <option id="fs-1374" value="1374"> |- Другие программы (Mac OS)&nbsp;</option>
                                            <option id="fs-1933" value="1933" class="root_forum has_sf">iOS&nbsp;</option>
                                            <option id="fs-1935" value="1935"> |- Программы для iOS&nbsp;</option>
                                            <option id="fs-1003" value="1003"> |- Игры для iOS&nbsp;</option>
                                            <option id="fs-1937" value="1937"> |- Разное для iOS&nbsp;</option>
                                            <option id="fs-2235" value="2235" class="root_forum has_sf">Видео&nbsp;</option>
                                            <option id="fs-1908" value="1908"> |- Фильмы для iPod, iPhone, iPad&nbsp;</option>
                                            <option id="fs-864" value="864"> |- Сериалы для iPod, iPhone, iPad&nbsp;</option>
                                            <option id="fs-863" value="863"> |- Мультфильмы для iPod, iPhone, iPad&nbsp;</option>
                                            <option id="fs-2535" value="2535"> |- Аниме для iPod, iPhone, iPad&nbsp;</option>
                                            <option id="fs-2534" value="2534"> |- Музыкальное видео для iPod, iPhone, iPad&nbsp;</option>
                                            <option id="fs-2238" value="2238" class="root_forum has_sf">Видео HD&nbsp;</option>
                                            <option id="fs-1936" value="1936"> |- Фильмы HD для Apple TV&nbsp;</option>
                                            <option id="fs-315" value="315"> |- Сериалы HD для Apple TV&nbsp;</option>
                                            <option id="fs-1363" value="1363"> |- Мультфильмы HD для Apple TV&nbsp;</option>
                                            <option id="fs-2082" value="2082"> |- Документальное видео HD для Apple TV&nbsp;</option>
                                            <option id="fs-2241" value="2241"> |- Музыкальное видео HD для Apple TV&nbsp;</option>
                                            <option id="fs-2236" value="2236" class="root_forum has_sf">Аудио&nbsp;</option>
                                            <option id="fs-1909" value="1909"> |- Аудиокниги (AAC, ALAC)&nbsp;</option>
                                            <option id="fs-1927" value="1927"> |- Музыка Lossless (ALAC)&nbsp;</option>
                                            <option id="fs-2240" value="2240"> |- Музыка Lossy (AAC-iTunes)&nbsp;</option>
                                            <option id="fs-2248" value="2248"> |- Музыка Lossy (AAC)&nbsp;</option>
                                            <option id="fs-2244" value="2244"> |- Музыка Lossy (AAC) (Singles, EPs)&nbsp;</option>
                                            <option id="fs-2243" value="2243" class="root_forum has_sf">F.A.Q.&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Разное">
                                            <option id="fs-10" value="10" class="root_forum has_sf">Разное (раздачи)&nbsp;</option>
                                            <option id="fs-865" value="865"> |- Психоактивные аудиопрограммы&nbsp;</option>
                                            <option id="fs-1100" value="1100"> |- Аватары, Иконки, Смайлы&nbsp;</option>
                                            <option id="fs-1643" value="1643"> |- Живопись, Графика, Скульптура, Digital Art&nbsp;</option>
                                            <option id="fs-848" value="848"> |- Картинки&nbsp;</option>
                                            <option id="fs-808" value="808"> |- Любительские фотографии&nbsp;</option>
                                            <option id="fs-630" value="630"> |- Обои&nbsp;</option>
                                            <option id="fs-1664" value="1664"> |- Фото знаменитостей&nbsp;</option>
                                            <option id="fs-148" value="148"> |- Аудио&nbsp;</option>
                                            <option id="fs-965" value="965"> |- Музыка (lossy)&nbsp;</option>
                                            <option id="fs-134" value="134"> |- Музыка (lossless)&nbsp;</option>
                                            <option id="fs-807" value="807"> |- Видео&nbsp;</option>
                                            <option id="fs-147" value="147"> |- Публикации и учебные материалы (тексты)&nbsp;</option>
                                            <option id="fs-847" value="847"> |- Трейлеры и дополнительные материалы к фильмам&nbsp;</option>
                                            <option id="fs-1167" value="1167"> |- Любительские видеоклипы&nbsp;</option>
                                            <option id="fs-19" value="19" class="root_forum">Тестовый форум&nbsp;</option>
                                            </optgroup>
                                            <optgroup label="&nbsp;Обсуждения, встречи, общение">
                                            <option id="fs-321" value="321"> |- Отчеты о встречах&nbsp;</option>
                                            </optgroup>"""
    bad_forum = []
    regex = '''<optgroup label="&nbsp;(.+?)">(.+?)</optgroup>'''
    regex_tr = '<option id="fs-(\d+)".+?>(.+?)&nbsp;</option>'
    for group, tr in re.compile(regex, re.DOTALL).findall(opt):
        result = re.compile(regex_tr, re.DOTALL).findall(tr)
        for id, name in result:
            if group in bad_opts:
                bad_forum.append(int(id))
                print u'{}, {}, {}'.format(group, id, name)

    print bad_forum