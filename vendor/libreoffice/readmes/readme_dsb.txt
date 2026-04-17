
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


Za nejnowše aktualizacije k dataji readme, glejśo https://git.libreoffice.org/core/tree/master/README.md

Dataja wopśimujo wažne informacije wó software LibreOffice. Pśiraźijo se, toś te informacije pśed startom instalacije wjelgin kradosćiwje pśecytaś.

Zgromaźeństwo LibreOffice jo zagronite za wuwijanje toś togo produkta a kažo was, se z cłonkom zgromaźeństwa staś, aby se wobźělił. Jolic sćo nowy wužywaŕ, móžośo se k sedłoju LibreOffice woglědaś, źož wjele informacijow wó projekśe LibreOffice a zgromaźeństwach, kótarež wokoło njogo eksistěruju, namakajośo. Źiśo k https://dsb.libreoffice.org/.

Jo LibreOffice napšawdu dermo za kuždego wužywarja?
----------------------------------------------------------------------

LibreOffice smějo se wót kuždego licho wužywaś. Móžośo toś tu kopiju LibreOffice na tak wjele licadłach instalěrowaś, kaž wy cośo, a jen za kuždyžkuli zaměr wužywaś (inkluziwnje za komercielne a kněžarstwowe zaměry, za zjawne zarědowanje a kubłanje). Za dalšne drobnostki glejśoe licencny tekst, kótaryž jo w toś tom ześěgnjenju LibreOffice wopśimjony.

Cogodla jo LibreOffice zadermo za kuždego wužywarja?
----------------------------------------------------------------------

Móžośo toś tu kopiju LibreOffice zadermo wužywaś, dokulaž jadnotliwi sobustatkujuce a firmowe sponsory su wudesignowali, wuwili, testowali, pśełožili, dokumentěrowali, pódprěli, zwikowali a na wjele wašnjow pomógli, aby LibreOffice k tomu cynili, což źinsa jo - wjeduca běrowa softwara wótwórjonego žrědła za wužywanje doma a we firmach.

Jolic jich napinanja gódnośiśo, a by rady zawěsćił, až LibreOffice jo w pśichoźe dalej k dispoziciji, rozwažćo, k toś tomu projektoju pśinosowaś - glejśo https://www.libreoffice.org/community/get-involved/ za drobnostki. Kuždy móžo někak pśinosowaś.

----------------------------------------------------------------------
Pokazki k instalaciji
----------------------------------------------------------------------

LibreOffice pomina se aktualnu wersiju wokoliny běžnego casa Java (JRE) za połnu funkcionalnosć. JRE njejo źěl instalaciskego paketa LibreOffice a musy se pótakem separatnje instalěrowaś.

Systemowe pominanja
----------------------------------------------------------------------

* Microsoft Windows 10 abo nowšy

Pšosym źiwajśo na to, až administratorowe pšawa su trjebne za instalaciju.

Wužywajśo slědujuce parametry pśikazoweje smužki z instalěrowańskim programom, aby registraciju LibreOffice ako standardny program za formaty Microsoft Office wunuźił abo pódtłocył:

* REGISTER_ALL_MSO_TYPES=1 wunuźijo registrěrowanje LibreOffice ako standardny program za formaty Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 pódtłocyjo registrěrowanje LibreOffice ako standardny program za formaty Microsoft Office.

Pšosym zawěsććo, až maśo dosć lichego składa w nachylnem zapisu swójogo systema a až pšawa za cytanje, pisanje a wuwjedowanje su pśizwólone. Zacyńśo wšě běžece programy, nježli až instalaciju zachopijośo.

Instalacija LibreOffice na linuxowych systemach, kótarež na Debian/Ubuntu bazěruju
----------------------------------------------------------------------

Za instrukcije, kak rěcny pakśik instalěrujośo (za tym až sćo engelsku wersiju LibreOffice zainstalěrował), cytajśo pšosym dokojce wótrězk z titelom Instalacija rěcnego pakśika.

Gaž ześěgnjony archiw wupakujośo, buźośo wiźeś, až wopśimjeśe jo se dekompriměrowało do pódzapisa. Wócyńśo wokno zastojnika datajow a změńśo zapis do togo, kótaryž se z „LibreOffice_“ startujo, slědowany pśez numer wersije a informacije wó platformje.

Toś ten zapis wopśimujo pódzapis z mjenim „DEBS“. Pśejźćo k zapisoju „DEBS“.

Klikniśo z pšaweju tastu do zapisa a wubjeŕśo „W terminalu wócyniś“. Terminalowe wokno se wócynijo. Zapódajśo slědujucy pśikaz do pśikazoweje smužki terminalowego wokna (dostanjośo napominanje, gronidko wužywarja root zapódaś, nježli až se pśikaz wuwjeźo):

Slědujuce pśikaze LibreOffice a integraciske pakety desktopa instalěruju (móžośo jadnorje je do wobrazowki terminala kopěrowaś, město togo, aby wopytał, je zapisaś):

sudo dpkg -i *.deb

Instalaciski proces jo něnto dokóńcony a symbole wšych nałoženjow LibreOffice měli w meniju Programy/Běrowe nałoženja swójogo desktopa byś.

Instalacija LibreOffice na Fedora, openSUSE, Mandriva a drugich linuxowych systemach z pomocu RPM-pakśikow
----------------------------------------------------------------------

Za instrukcije, kak rěcny pakśik instalěrujośo (za tym až sćo engelsku wersiju LibreOffice zainstalěrował), cytajśo pšosym dokojce wótrězk z titelom Instalacija rěcnego pakśika.

Gaž ześěgnjony archiw wupakujośo, buźośo wiźeś, až wopśimjeśe jo se dekompriměrowało do pódzapisa. Wócyńśo wokno zastojnika datajow a změńśo zapis do togo, kótaryž se z „LibreOffice_“ startujo, slědowany pśez numer wersije a informacije wó platformje.

Toś ten zapis wopśimujo pódzapis z mjenim „RPMS“. Pśejźćo k zapisoju „RPMS“.

Klikniśo z pšaweju tastu do zapisa a wubjeŕśo „W terminalu wócyniś“. Terminalowe wokno se wócynijo. Zapódajśo slědujucy pśikaz do pśikazoweje smužki terminalowego wokna (dostanjośo napominanje, gronidko wužywarja root zapódaś, nježli až se pśikaz wuwjeźo):

Za systemy, kótarež na Fedora bazěruju: sudo dnf install *.rpm

Za systemy, kótarež na Mandriva bazěruju: sudo urpmi *.rpm

Za druge systemy, kótarež RPM wužywaju (openSUSE atd.): rpm -Uvh *.rpm

Instalaciski proces jo něnto dokóńcony a symbole wšych nałoženjow LibreOffice měli w meniju Programy/Běrowe nałoženja swójogo desktopa byś.

Ako alternatiwu móžośo skript „install“ wužywaś, kótaryž jo w kórjenjowem zapisu toś togo archiwa, aby instalaciju ako wužywaŕ pśewjadł. Skript LibreOffice tak zarědujo, až ma swójski profil za instalaciju, wótźělony wót wašogo normalnego profila LibreOffice. Wobmysliśo, až to njebuźo źěle systemoweje integracije ako menijowe zapiski desktopa a registracije MIME-typow desktopa instalěrowaś.

Pokazki nastupajucy deskotopowu integraciju za linuxowe distribucije, kótarež njejsu zapśimjete w instalaciskich instrukcijach górjejce
----------------------------------------------------------------------

Měło dosć lažko byś, LibreOffice na drugich linuxowych distribucijach instalěrowaś, kótarež toś te instalaciske instrukcije njewobjadnaju. Rozdźěle mógu głownje pśi desktopowej integraciji wustupowaś.

Zapis RPMS (resp. DEBS) teke paket z mjenim libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (resp.libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, abo pódobnje) wopśimujo. To jo paket za wšykne distribucije Linux, kótarež specifikacije/dopórucenja Freedesktop.org (https://de.wikipedia.org/wiki/Freedesktop.org) pódpěraju, a staja se za instalaciju na drugich distribucijach k dispoziciji, kótarež njejsu do górjejce naspomnjonych instrukcijow zapśimjone.

Instalacija rěcnego pakśika
----------------------------------------------------------------------

Ześěgniśo rěcny pakśik za waš pominanu rěc a platformu. Stej na tom samskem městnje k dispoziciji ako głowny instalaciski archiw. Wupakujśo ześěgnjony archiw z datajowym zastojnikom do zapisa (ako na pśikład do swójogo desktopa). Zawěsććo, až sćo skóńcył wšykne nałoženja LibreOffice inkluziwnje malsny startowak.

Pśejźćo k zapisoju, do kótaregož sćo swój rěcny pakśik ześěgnuł.

Změńśo něnto zapis do zapisa, kótaryž jo se napórał za proces ekstrakcije. Na pśikład za francojski rěcny pakśik za 32-bitowy system, kótaryž se na Debian/Ubuntu bazěrujo, zapis LibreOffice_ groni, plus někotare informacije wó wersiji a Linux_x86_langpack-deb_fr.

Pśejźćo něnto k zapisoju, kótaryž pakety za instalaciju wopśimujo. Na systemach, kótarež na Debian/Ubuntu bazěruju, jo to zapis DEBS. Na systemach, kótarež na Fedora, openSUSE abo Mandriva bazěruju, jo to zapis RPMS.

Klikniśo z pšaweju tastu w datajowem zastojniku do zapisa a wubjeŕśo pśikaz „W terminalu wócyniś“. Wuwjeźćo w rowno wócynjonem terminalowem woknje pśikaz, aby rěcny pakśik instalěrował (wšykne dołojce pódane pśikaze budu se nejskerjej za gronidłom wašogo wužywarja root pšašaś):

Za systemy, kótarež na Debianu/Ubuntu bazěruju: sudo dpkg -i *.deb

Za systemy, kótarež na Fedora bazěruju: su -c 'dnf install *.rpm'

Za systemy, kótarež na Mandriva bazěruju: sudo urpmi *.rpm

Za druge systemy, kótarež RPM wužywaju (openSUSE atd.): rpm -Uvh *.rpm

Startujśo něnto jadno z nałoženjow LibreOffice - na pśikład Writer. Źiśo k menijoju Rědy a wubjeŕśo Nastajenja. Klikniśo w dialogu Nastajenja na „Rěcy a narodne šemy“ a pón na „Powšykne“. Wubjeŕśo rěc z lisćiny „Wužywaŕski pówjerch“, kótaruž sćo rowno zainstalěrował. Jolic cośo, pśewjeźćo to samske za nastajenja „Teritorialna šema“, „standardne pjenjeze“ a „Standardne rěcy za dokumenty“.

Klikniśo na W pórěźe za tym až sćo pśiměrił toś te nastajenja. Dialog se zacynijo a buźośo powěźeńku wiźeś, kótaraž was informěrujo, až se waše změny akle pó znowegostartowanju LibreOffice wustatkuju. (Njezabywajśo malsny startowak skóńcyś, jolic jo startowany).

Pśiducy raz, gaž LibreOffice startujośo, buźo se w rěcy startowaś, kótaruž sćo rowno zainstalěrował.

----------------------------------------------------------------------
Problemy ze startom programa
----------------------------------------------------------------------

Śěžkosći pśi startowanju LibreOffice (na pś. nałoženja wisaju) a problemy ze zwobraznjenim na wobrazowce se cesto pśez gónjak grafikoweje kórty zawinuju. Jolic toś te problemy wustupuju, aktualizěrujśo pšosy gónjak swójeje grafikoweje kórty abo wopytajśo gónjak grafikoweje kórty swójogo źěłowego systema wužywaś.

----------------------------------------------------------------------
Touchpady ALPS/Synaptics pód Windows
----------------------------------------------------------------------

Problema z gónjakom Windows dla njamóžośo pśez dokumenty LibreOffice kulaś, gaž z palcom touchpad ALPS/Synaptics pótrějośo.

Aby kulanje na touchpaźe zmóžnił, pśidajśo konfiguraciskej dataji „C:\Program Files\Synaptics\SynTP\SynTPEnh.ini“ slědujuce smužki a startujśo swójo licadło znowego:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Składowańske městno konfiguraciskeje dataje móžo se pó wersijach Windows wótchyliś.

----------------------------------------------------------------------
Tastowe skrotconki
----------------------------------------------------------------------

W LibreOffice daju se jano tastowe kombinacije wužywaś, kótarež se pśez źěłowy system njewužywaju. Jolic tastowa kombinacija w LibreOffice njefunkcioněrujo, ako se to w pomocy LibreOffice wopisujo, pśespytajśo, lěc se toś ta tastowa kombinacija južo pśez źěłowy system wužywa. Aby take konflikty rozwězał, móžośo tastowe kombinacije změniś, kótarež waš źěłowy system wužywa. Ako alternatiwu móžośo skóro kuždu tastowu kombinaciju w LibreOffice změniś. Za dalšne informacije wó toś tej temje, cytajśo pomoc LibreOffice abo dokumentaciju pomocy swójogo źěłowego systema.

----------------------------------------------------------------------
Problemy pśi rozesćełanju dokumentow ako mejlki z LibreOffice
----------------------------------------------------------------------

Pśi wótpósćełanju dokumenta pśez 'Dataja – Pósłaś – E-mailowy dokument' abo 'Dataja – Pósłaś – E-mail ako PDF' mógu problemy wustupowaś (program wótwalujo se abo wisy). To se pśez systemowu dataju Windows „Mapi“ (messaging Application Programming Interface) w někotarych datajowych wersijach problemy zawinujo. Bóžko njedajo se problem na wěsty wersijowy numer zagranicowaś. Za dalšne informacije woglědajśo se pšosym k https://www.microsoft.com, aby wědowu datowu banku Microsoft za „mapi.dll“ pśepytował.

----------------------------------------------------------------------
Wažne pokazki wó bźezbariernosći
----------------------------------------------------------------------

Za dalšne informacije wó funkcijach bźezbariernosći w LibreOffice, glejśo https://dsb.libreoffice.org/accessibility/

----------------------------------------------------------------------
Wužywaŕska pódpěra
----------------------------------------------------------------------

Głowny bok pomocy wšake móžnosći za pomoc z LibreOffice bitujo. Na wašo pšašanje jo se snaź južo wótegronjone – glejśo forum zgromaźeństwa na https://ask.libreoffice.org/ abo pśepytajśo archiwy mailingoweje lisćiny ‚users@libreoffice.org‘ na https://www.libreoffice.org/lists/users/. Abo sćelośo swóje pšašanja na users@libreoffice.org. Jolic cośo lisćinu aboněrowaś (aby wótegrona dostał), sćelśo proznu mejlku na: users+subscribe@libreoffice.org.

Pśecytajśo teke ceste pšašanja (FAQ) na websedle LibreOffice.

----------------------------------------------------------------------
Zmólki a problemy k wěsći daś
----------------------------------------------------------------------

Naš system za zdźělenje, slědowanje a rozwězowanje programowych zmólkow jo tuchcylu BugZilla, kótaryž se na https://bugs.documentfoundation.org/ góspodujo. Skoboźijomy wšykne wužywarje, programowe zmólki k wěsći daś, kótarež mógu na jich platformje wustupowaś. Energiske kwěsćidawanje programowych zmólkow jo jaden z nejwažnjejšych pśinoskow, kótaryž wužywaŕske zgromaźeństwo móžo běžecemu wuwijanjeju a pólěpšowanjeju LibreOffice daś.

----------------------------------------------------------------------
Sobuźěło
----------------------------------------------------------------------

Zgromaźeństwo LibreOffice by wjelgin profitěrowało z wašogo aktiwnego wobźělenja na wuwijanju tós togo wažnego projekta wótwórjonego žrědła.

Ako wužywaŕ sćo južo gódnotny źěl wuwijańskego procesa běrowego programowego paketa a my by was rady skoboźili, aktiwnjejšu rolu ako dłujkodobny sobustatkujucy zgromaźeństwa zabraś. Pšosym pśizamkniśo se nam a woglědajśo se k bokoju wó sobuźěle na websedle LibreOffice.

Kak zachopiś?
----------------------------------------------------------------------

Nejlěpša wašnja zachopiś jo, jadnu rozpósłańsku lisćinu abo někotare z nich aboněrowaś, chylku wobglědowaś a póněcom e-mailowe archiwy wužywaś, aby wjele temow póznał, kótarež su se wót wózjawjenja žrědłowego koda w oktobru 2000 LibreOffice wobjadnali. Gaž se derje pśigótowany cujośo, trjebaśo jano mejlku z krotkim sebjepśedstajenim a zachopśo ned. Jolic se z projektami wótwórjonego žrědła wuznawaśo, pśeglědujśo naše nadawkowe lisćiny na websedle LibreOffice a glědajśo, lěc jo něco, pśi kótaremž by rady pomagał.

Aboněrowaś
----------------------------------------------------------------------

How su někotare rozpósłańske lisćiny, kótarež móžośo na https://dsb.libreoffice.org/get-help/mailing-lists/ aboněrowaś

* Nowosći: announce@documentfoundation.org *wšym wužywarjam pśiraźony* (mało wobchada)
* Pomoc wót wužywarjow: users@global.libreoffice.org *jadnora wašnja se na diskusijach wobźěliś* (wjele wobchada)
* Marketing: marketing@global.libreoffice.org *LibreOffice znaty cyniś* (wjele wobchada)
* Generelna lisćina wuwijarjow: libreoffice@lists.freedesktop.org (wjele wobchada)

Jadnomu projektoju abo někotarym projektam se pśizamknuś
----------------------------------------------------------------------

Samo z mało nazgónjenjami w softwarowem designje abo programěrowanju móžośo wažne pśinoski k toś tomu wažnemu projektoju wótwórjonego žrědła spóraś. Jo, teke wy!

Naźejamy se, až maśo radosć na źěle z nowym LibreOffice 26.2 a se nam online pśizamknjośo.

Zgromaźeństwo LibreOffice

----------------------------------------------------------------------
Wužyty / změnjony žrědłowy kod
----------------------------------------------------------------------

Źěle Copyright 1998, 1999 James Clark. Źěle Copyright 1996, 1998 Netscape Communications Corporation.
