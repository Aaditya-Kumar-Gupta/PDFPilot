
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


Za najnowše aktualizacije k dataji readme, hlejće https://git.libreoffice.org/core/tree/master/README.md

Dataja wobsahuje wažne informacije wo softwarje LibreOffice. Poruča so, tute informacije před startom instalacije jara starosćiwje přečitać.

Zhromadźenstwo LibreOffice je zamołwite za wuwiwanje tutoho produkta a přeproša was, so z čłonom zhromadźenstwa stać, zo byšće so wobdźělił. Jeli sće nowy wužiwar, móžeće sydło LibreOffice wopytać, hdźež wjele informacijow wo projekće LibreOffice a zhromadźenstwach, kotrež wokoło njeho eksistuja, namakaće. Dźiće k https://hsb.libreoffice.org/.

Je LibreOffice woprawdźe zadarmo za kóždeho wužiwarja?
----------------------------------------------------------------------

LibreOffice smě so wot kóždeho swobodnje wužiwać. Móžeće tutu kopiju LibreOffice na tak wjele ličakach instalować, kaž wy chceće, a jón za kóždyžkuli zaměr wužiwać (inkluziwnje za komercielne a knježerstwowe zaměry, za zjawne zarjadowanje a kubłanje). Za dalše podrobnosće hlejće licencny tekst, kotryž je w tutym sćehnjenju LibreOffice wobsahowany.

Čehodla je LibreOffice zadarmo za kóždeho wužiwarja?
----------------------------------------------------------------------

Móžeće tutu kopiju LibreOffice zadarmo wužiwać, dokelž jednoliwi sobuskutkowarjo a firmowi sponsorojo su designowali, wuwili, testowali, přełožili, dokumentowali, podpěrali, zwičnili a na wjele wašnjow pomhali, zo bychu LibreOffice k tomu činili, štož je dźensa - načolna běrowowa softwara wotewrjeneho žórła za wužiwanje doma a we firmach.

Jeli jich prócowanja hódnoćiće, a byšće rady zawěsćił, zo LibreOffice je w přichodźe dale k dispoziciji, rozwažće, k tutomu projektej přinošować - hlejće https://www.libreoffice.org/community/get-involved/ za podrobnosće. Kóždy móže někak přinošować.

----------------------------------------------------------------------
Pokazki wo instalaciji
----------------------------------------------------------------------

LibreOffice wužaduje sej aktualnu wersiju wokoliny běžneho časa Java (JRE) za połnu funkcionalnosć. JRE dźěl instalaciskeho paketa LibreOffice njeje a dyrbi so tuž separatnje instalować.

Systemowe žadanja
----------------------------------------------------------------------

* Microsoft Windows 10 abo nowši

Prošu wobkedźbujće, zo administratorowe prawa su trěbne za instalaciju.

Wužiwajće slědowace parametry přikazoweje linki z instalowanskim programom, zo byšće registraciju LibreOffice jako standardny program za formaty Microsoft Office wunuzował abo potłóčił:

* REGISTER_ALL_MSO_TYPES=1 wunuzuje registrowanje LibreOffice jako standardny program za formaty Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 zadźěwa registrowanju LibreOffice jako standardny program za formaty Microsoft Office.

Prošu zawěsćće, zo maće dosć swobodneho składa w nachwilnym zapisu swojeho systema a zo prawa za čitanje, pisanje a wuwjedźenje su date. Začińće wšě běžace programy, prjedy hač instalaciju započnjeće.

Instalacija LibreOffice na linuxowych systemach, kotrež na Debian/Ubuntu bazuja
----------------------------------------------------------------------

Za instrukcije, kak rěčny pakćik instalujeće (po tym, zo sće jendźelsku wersiju LibreOffice instalował), čitajće prošu deleka wotrězk z titulom Instalacija rěčneho pakćika.

Hdyž sćehnjeny archiw wupakujeće, budźeće widźeć, zo je so wobsah do podzapisa dekomprimował. Wočińće wokno zrjadowaka datajow a změńće zapis do toho, kotryž so z „LibreOffice_“ startuje, slědowany přez wersijowe čisło a informacije wo platformje.

Tutón zapis wobsahuje podzapis z mjenom „DEBS“. Přeńdźće k zapisej „DEBS“.

Klikńće z prawej tastu do zapisa a wubjerće „W terminalu wočinić“. Terminalowe wokno so wočini. Zapodajće slědowacy přikaz do přikazoweje linki terminaloweho wokna (dóstanjeće namołwu, hesło wužiwarja root zapodać, prjedy hač so přikaz wuwjedźe):

Slědowace přikazy LibreOffice a integraciske pakety desktopa instaluja (móžeće prosće je do wobrazowki terminala kopěrować, město toho, zo byšće spytał, je zapisać):

sudo dpkg -i *.deb

Instalaciski proces je nětko dokónčeny a symbole wšěch nałoženjow LibreOffice měli w meniju Programy/Běrowowe nałoženja swojeho desktopa być.

Instalacija LibreOffice na Fedora, openSUSE, Mandriva a druhich linuxowych systemach z pomocu RPM-pakćikow
----------------------------------------------------------------------

Za instrukcije, kak rěčny pakćik instalujeće (po tym, zo sće jendźelsku wersiju LibreOffice instalował), čitajće prošu deleka wotrězk z titulom Instalacija rěčneho pakćika.

Hdyž sćehnjeny archiw wupakujeće, budźeće widźeć, zo je so wobsah do podzapisa dekomprimował. Wočińće wokno zrjadowaka datajow a změńće zapis do toho, kotryž so z „LibreOffice_“ startuje, slědowany přez wersijowe čisło a informacije wo platformje.

Tutón zapis wobsahuje podzapis z mjenom „RPMS“. Přeńdźće k zapisej „RPMS“.

Klikńće z prawej tastu do zapisa a wubjerće „W terminalu wočinić“. Terminalowe wokno so wočini. Zapodajće slědowacy přikaz do přikazoweje linki terminaloweho wokna (dóstanjeće namołwu, hesło wužiwarja root zapodać, prjedy hač so přikaz wuwjedźe):

Za systemy, kotrež na Fedora bazuja: sudo dnf install *.rpm

Za systemy, kotrež na Mandriva bazuja: sudo urpmi *.rpm

Za druhe systemy, kotrež RPM wužiwaja (openSUSE atd.): rpm -Uvh *.rpm

Instalaciski proces je nětko dokónčeny a symbole wšěch nałoženjow LibreOffice měli w meniju Programy/Běrowowe nałoženja swojeho desktopa być.

Jako alternatiwu móžeće skript „install“ wužiwać, kotryž je w korjentnym zapisu tutoho archiwa, zo byšće instalaciju jako wužiwar přewjedł. Skript LibreOffice tak připrawi, zo ma swójski profil za instalaciju, wotdźěleny wot wašeho normalneho profila LibreOffice. Wobkedźbujće, zo to njebudźe dźěle systemoweje integracije kaž menijowe zapiski desktopa a registracije MIME-typow desktopa instalować.

Pokazki nastupajo deskotopowu integraciju za linuxowe distribucije, kotrež w instalaciskich instrukcijach horjeka wobkedźbowane njejsu
----------------------------------------------------------------------

Měło dosć lochko być, LibreOffice na druhich linuxowych distribucijach instalować, kotrež tute instalaciske instrukcije njewobjednawaja. Rozdźěle móža hłownje při desktopowej integraciji wustupować.

Zapis RPMS (resp. DEBS) tež paket z mjenom libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (resp.libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, abo podobnje) wobsahuje. To je paket za wšě distribucije Linux, kotrež specifikacije/doporučenja Freedesktop.org (https://de.wikipedia.org/wiki/Freedesktop.org) podpěruja, a staja so za instalaciju na druhich distribucijach k dispoziciji, kotrež do horjeka naspomnjenych instrukcijow zapřijate njejsu.

Instalacija rěčneho pakćika
----------------------------------------------------------------------

Sćehńće rěčny pakćik za waš požadanu rěč a platformu. Stej na samsnym městnje k dispoziciji kaž hłowny instalaciski archiw. Wupakujće sćehnjeny archiw z datajowym zrjadowakom do zapisa (kaž na přikład do swojeho desktopa). Zawěsćće, zo sće wšě nałoženja LibreOffice inkluziwnje spěšny startowak skónčił.

Přeńdźće k zapisej, do kotrehož sće swój rěčny pakćik sćahnył.

Změńće nětko zapis do zapisa, kotryž je so za proces ekstrakcije wutworił. Na přikład za francoski rěčny pakćik za 32-bitowy system, kotryž na Debian/Ubuntu bazuje, zapis LibreOffice_ rěka, plus někotre wersijowe informacije a Linux_x86_langpack-deb_fr.

Přeńdźće nětko k zapisej, kotryž pakety za instalaciju wobsahuje. Na systemach, kotrež na Debian/Ubuntu bazuja, je to zapis DEBS. Na systemach, kotrež na Fedora, openSUSE abo Mandriva bazuja, je to zapis RPMS.

Klikńće z prawej tastu w datajowym zrjadowaku do zapisa a wubjerće přikaz „W terminalu wočinić“. Wuwjedźće w runje wočinjenym terminalowym woknje přikaz, zo byšće rěčny pakćik instalował (wšě deleka podate přikazy budu so najskerje za hesłom wašeho wužiwarja root prašeć):

Za systemy, kotrež na Debianu/Ubuntu bazuja: sudo dpkg -i *.deb

Za systemy, kotrež na Fedora bazuja: su -c 'dnf install *.rpm'

Za systemy, kotrež na Mandriva bazuja: sudo urpmi *.rpm

Za druhe systemy, kotrež RPM wužiwaja (openSUSE atd.): rpm -Uvh *.rpm

Startujće nětko jedne z nałoženjow LibreOffice - na přikład Writer. Dźiće k menijej Nastroje a wubjerće Nastajenja. Klikńće w dialogu Nastajenja na „Rěče a narodne šemy“ a potom na „Powšitkowne“. Wubjerće rěč z lisćiny „Wužiwarski powjerch“, kotruž sće runje instalował. Jeli chceće, přewjedźće samsne za nastajenja „Teritorialna šema“, „standardna měna“ a „Standardne rěče za dokumenty“.

Klikńće na W porjadku po tym, zo sće tute nastajenja přiměrił. Dialog so začini a budźeće zdźělenku widźeć, kotraž was informuje, zo so waše změny hakle po znowastartowanju LibreOffice wuskutkuja. (Njezabywajće spěšny startowak skónčić, jeli je startowany).

Přichodny raz, hdyž LibreOffice startujeće, budźe so w rěči startować, kotruž sće runje nainstalował.

----------------------------------------------------------------------
Problemy ze startom programa
----------------------------------------------------------------------

Ćežkosće při startowanju LibreOffice (na př. nałoženja wisaja) a problemy ze zwobraznjenjom na wobrazowce so husto přez ćěrjak grafikoweje karty zawinuja. Jeli tute problemy wustupuja, aktualizujće prošu ćěrjak swojeje grafikoweje karty abo spytajće ćěrjak grafikoweje karty swojeho dźěłoweho systema wužiwać.

----------------------------------------------------------------------
Touchpady ALPS/Synaptics pod Windows
----------------------------------------------------------------------

Problema z ćěrjakom Windows dla njemóžeće přez dokumenty LibreOffice kulić, hdyž z porstom přez touchpad ALPS/Synaptics přejědźeće.

Zo byšće kulenje na touchpadźe zmóžnił, přidajće konfiguraciskej dataji „C:\Program Files\Synaptics\SynTP\SynTPEnh.ini“ slědowace linki a startujće swój ličak znowa:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Składowanske městno konfiguraciskeje dataje móže so po wersijach Windows wotchilić.

----------------------------------------------------------------------
Tastowe skrótšenki
----------------------------------------------------------------------

W LibreOffice dadźa so jenož tastowe kombinacije wužiwać, kotrež so přez dźěłowy system njewužiwaja. Jeli tastowa kombinacija w LibreOffice njefunguje, kaž so to w pomocy LibreOffice wopisuje, přepruwujće, hač so tuta tastowa kombinacija hižo přez dźěłowy system wužiwa. Zo byšće tajke konflikty rozrisał, móžeće tastowe kombinacije změnić, kotrež waš dźěłowy system wužiwa. Jako alternatiwu móžeće nimale kóždu tastowu kombinaciju w LibreOffice změnić. Za dalše informacije wo tutej temje, čitajće pomoc LibreOffice abo dokumentaciju pomocy swojeho dźěłoweho systema.

----------------------------------------------------------------------
Problemy při rozesyłanju dokumentow jako e-mejle z LibreOffice
----------------------------------------------------------------------

Při wotesyłanju dokumenta přez 'Dataja - Pósłać - E-mejlowy dokument' abo 'Dataja – Pósłać  E-mejl jako PDF' móža problemy wustupować (program spaduje abo wisa). To so přez systemowu dataju Windows „Mapi“ (messaging Application Programming Interface) w někotrych datajowych wersijach problemy zawinuje. Bohužel njeda so problem na wěste wersijowe čisło zamjezować. Za dalše informacije wopytajće prošu https://www.microsoft.com, zo byšće wědowu datowu banku Microsoft za „mapi.dll“ přepytował.

----------------------------------------------------------------------
Wažne pokazki wo bjezbarjernosći
----------------------------------------------------------------------

Za dalše informacije wo funkcijach bjezbarjernosće w LibreOffice, hlejće https://hsb.libreoffice.org/accessibility/

----------------------------------------------------------------------
Wužiwarska podpěra
----------------------------------------------------------------------

Hłowna strona pomocy wšelake móžnosće za pomoc z LibreOffice skići. Na waše prašenje je so snano hižo wotmołwjene – hlejće forum zhromadźenstwa na https://ask.libreoffice.org/ abo přepytajće archiwy mejlingoweje lisćiny ‚users@libreoffice.org‘ na https://www.libreoffice.org/lists/users/. Abo sćeleće swoje prašenja na users@libreoffice.org. Jeli chceće lisćinu abonować (zo byšće wotmołwy dóstał), sćelće prózdnu mejlku na: users+subscribe@libreoffice.org.

Přečitajće tež huste prašenja (FAQ) na websydle LibreOffice.

----------------------------------------------------------------------
Zmylki a problemy zdźělić
----------------------------------------------------------------------

Naš system za zdźělenje, slědowanje a rozrisowanje programowych zmylkow je tuchwilu BugZilla, kotryž so na https://bugs.documentfoundation.org/ hospoduje. Pozbudźamy wšěch wužiwarjow, programowe zmylki zdźělić, kotrež móža na jich platformje wustupować. Skutkowne zdźělenje programowych zmylkow je jedyn z najwažnišich přinoškow, kotryž wužiwarske zhromadźenstwo móže běžacemu wuwiwanju a polěpšowanju LibreOffice dać.

----------------------------------------------------------------------
Sobudźěło
----------------------------------------------------------------------

Zhromadźenstwo LibreOffice by z wašeho aktiwneho wobdźělenja na wuwiwanju tutoho wažneho projekta wotewrjeneho žórła jara profitowało.

Jako wužiwar sće hižo hódnotny dźěl wuwiwanskeho procesa běrowoweho programoweho paketa a bychmy was rady pozbudźili, aktiwnišu rólu jako dołhodobny sobuskutkowar zhromadźenstwa zabrać. Prošu přidružće so nam a wopytajće stronu wo sobudźěle na websydle LibreOffice.

Kak započeć
----------------------------------------------------------------------

Najlěpše wašnje započeć je, jednu rozesyłansku lisćinu abo wjacore z nich abonować, chwilku wobkedźbować a počasu e-mejlowe archiwy wužiwać, zo byšće so z wjele temami zeznał, kotrež su so wot wozjewjenja žórłoweho koda w oktobru 2000 LibreOffice wobjednali. Hdyž so derje přihotowany čujeće, trjebaće jenož e-mejlu z krótkim sebjepředstajenjom a započńće hnydom. Jeli so z projektami wotewrjeneho žórła wuznawaće, přehladujće naše nadawkowe lisćiny na websydle LibreOffice a hladajće, hač je něšto, při kotrymž byšće rady pomhał.

Abonować
----------------------------------------------------------------------

Tu su někotre rozesyłanske lisćiny, kotrež móžeće na https://hsb.libreoffice.org/get-help/mailing-lists/ abonować

* Nowinky: announce@documentfoundation.org *wšěm wužiwarjam doporučowany* (mało wobchada)
* Pomoc wot wužiwarjow: users@global.libreoffice.org *jednore wašnje so na diskusijach wobdźělić* (wjele wobchada)
* Marketing: marketing@global.libreoffice.org *LibreOffice zeznajomić* (wjele wobchada)
* Generelna lisćina wuwiwarjow: libreoffice@lists.freedesktop.org (wjele wobchada)

Jednomu projektej abo wjacorym projektam přistupić
----------------------------------------------------------------------

Samo z mało nazhonjenjemi w softwarowym designje abo programowanju móžeće wažne přinoški k tutomu wažnemu projektej wotewrjeneho žórła přinjesć. Haj, tež wy!

Nadźijamy so, zo maće radosć na dźěle z nowym LibreOffice 26.2 a so nam online přidružiće.

Zhromadźenstwo LibreOffice

----------------------------------------------------------------------
Wužity / změnjeny žórłowy kod
----------------------------------------------------------------------

Dźěle Copyright 1998, 1999 James Clark. Dźěle Copyright 1996, 1998 Netscape Communications Corporation.
