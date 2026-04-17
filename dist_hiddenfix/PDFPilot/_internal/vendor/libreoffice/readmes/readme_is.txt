
======================================================================
Lesefni LibreOffice 26.2
======================================================================


Til að sjá allra nýjustu uppfærslur við þetta skjal, er hægt að skoða https://git.libreoffice.org/core/tree/master/README.md

Þetta skjal inniheldur mikilvægar upplýsingar um LibreOffice hugbúnaðinn. Endilega lestu þær gaumgæfilega áður en þú byrjar að vinna með hann.

LibreOffice samfélagið er ábyrgt fyrir þróun þessa hugbúnaðar, við bjóðum þér að taka þátt í þessu með okkur - ef þú hefur áhuga. Sértu alveg nýr notandi geturðu heimsótt LibreOffice vefinn, þar geturðu fundið mikið af upplýsingum um LibreOffice verkefnið og samfélagið í kringum það. Farðu á https://www.libreoffice.org/.

Er LibreOffice í alvörunni ókeypis fyrir alla?
----------------------------------------------------------------------

LibreOffice er frjáls hverjum sem er til notkunar, án endurgjalds. Þú mátt taka þetta eintak af LibreOffice og setja upp á eins mörgum tölvum og þú vilt, nota í hvaða tilgangi sem þér dettur í hug (þar með talin viðskipti, ríkisrekstur, almenningsafnot og notkun í skólum). Til að skoða ítarlegri atriði í þessu sambandi má lesa texta notendaleyfisins sem fylgdi LibreOffice pakkanum.

Hversvegna er LibreOffice ókeypis fyrir alla?
----------------------------------------------------------------------

Þú getur í dag notað þetta eintak af LibreOffice án nokkurs endurgjalds vegna þess að einstaklingar og fyrirtæki hafa hannað, þróað, prófað, þýtt, skrifað um, stutt við, kynnt og hjálpað til við á marga vegu við að gera LibreOffice að því sem það er í dag - fremsta opna skrifstofuhugbúnaðnum.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Athugasemdir um uppsetningu
----------------------------------------------------------------------

LibreOffice þarfnast nýlegrar útgáfu af Java keyrsluumhverfinu (JRE) til að ná öllum eiginleikum kerfisins. JRE er ekki hluti af LibreOffice uppsetningarpakkanum, heldur þarf að setja það upp sérstaklega.

Kerfiskröfur
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Athugið: Það þarf kerfisstjóraréttindi (administrator) við uppsetninguna.

Kerfisskráningu LibreOffice sem sjálfgefinna forrita til meðhöndlunar á Microsoft Office skráasniðum er hægt að þvinga fram eða sleppa alveg með því að nota eftirfarandi rofa á skipanalínu með ræsingu uppsetningarforritsins:

* REGISTER_ALL_MSO_TYPES=1 þvingar kerfisskráningu LibreOffice sem sjálfgefinna forrita fyrir Microsoft Office skjalasnið.
* REGISTER_NO_MSO_TYPES=1 sleppir kerfisskráningu LibreOffice sem sjálfgefinna forrita fyrir Microsoft Office skjalasnið.

Gakktu úr skugga um að þú hafir nægilegt laust pláss í bráðabirgðamöppu kerfisins og að les-, skrif- og keyrsluréttindi hafi verið veitt. Lokaðu öllum öðrum forritum áður en uppsetningaferlið er ræst.

Uppsetning LibreOffice á Linux dreifingar sem byggjast á Debian/Ubuntu
----------------------------------------------------------------------

Til að sjá leiðbeiningar um hvernig setja eigi upp tungumálapakka (eftir að hafa sett upp ensku (US English) útgáfuna af LibreOffice), lestu þá greinina hér fyrir neðan sem heitir Uppsetning tungumálapakka.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Mappan inniheldur undirmöppu sem kallast "DEBS". Farðu inn í "DEBS" möppuna.

Hægrismelltu innan í möppunni og veldu "Opna í skjáhermi". Skjáhermir getur einnig veriðkallaður "Útstöð" eða "Skel". Í glugganum sem opnast er svokölluð skipanalína, á hana skrifarðu eftirfarandi skipun (þú verður spurð/ur um rótarlykilorðið áður en skipunin er framkvæmd):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Uppsetningarferlinu er núna lokið og þú ættir að sjá táknmyndir fyrir öll LibreOffice forritin undir valmyndinni Forrit/Skrifstofuforrit (Applications/Office).

Uppsetning LibreOffice á Fedora, Suse, Mandriva og öðrum Linux dreifingum sem nota RPM pakka
----------------------------------------------------------------------

Til að sjá leiðbeiningar um hvernig setja eigi upp tungumálapakka (eftir að hafa sett upp ensku (US English) útgáfuna af LibreOffice), lestu þá greinina hér fyrir neðan sem heitir Uppsetning tungumálapakka.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Þessi mappa inniheldur undirmöppu sem kallast "RPMS". Skiptu um staðsetningu og farðu inn í þessa "RPMS" möppu.

Hægrismelltu innan í möppunni og veldu "Opna í skjáhermi". Skjáhermir getur einnig veriðkallaður "Útstöð" eða "Skel". Í glugganum sem opnast er svokölluð skipanalína, á hana skrifarðu eftirfarandi skipun (þú verður spurð/ur um rótarlykilorðið áður en skipunin er framkvæmd):

Á kerfum sem byggjast á Fedora: sudo dnf install *.rpm

Á kerfum sem byggjast á Mandriva: sudo urpmi *.rpm

Á kerfum sem byggjast á RPM pakkakerfinu (OpenSUSE, o.s.frv.): rpm -Uvh *.rpm

Uppsetningarferlinu er núna lokið og þú ættir að sjá táknmyndir fyrir öll LibreOffice forritin undir valmyndinni Forrit/Skrifstofuforrit (Applications/Office).

Einnig geturðu notað 'install' skriftuna, sem staðsett er í rót þessarar safnskrár, til að framkvæma uppsetningu sem venjulegur notandi / user. Skriftan setur upp LibreOffice þannig að uppsetningin hefur sitt eigið notandasnið, aðskilið frá venjulega LibreOffice sniðinu.Athugaðu að þetta mun ekki setja upp kerfisaðlögunarhluta á borð við færslur í skjáborðsvalmynd eða skráavensl við MIME tegundir.

Athugasemdir varðandi samhæfingu við skjáborðsumhverfi (Desktop Integration) í Linux-dreifingum sem ekki koma fram í upplýsingunum hér að ofan
----------------------------------------------------------------------

Það ætti að vera tiltölulega einfalt að setja LibreOffice upp á aðrar Linux dreifingar en þær sem lýst er í þessum leiðbeiningum. Helsti munurinn ætti að vera að hve miklu leyti samþætting í viðkomandi skjáborðsumhverfi gengur fyrir sig.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Uppsetning tungumálapakka
----------------------------------------------------------------------

Náðu í tungumálapakkann sem tilheyrir tungumálinu og stýrikerfinu þínu. Þessir pakkar eru tiltækir á sama niðurhalssvæði og aðaluppsetningarskrain. Með Nautilus skráastjóranum geturðu afþjappað safnskrárpakkanum (sem þú náðir í) í einhverja möppu (til dæmis á skjáborðið). Gakktu úr skugga um að þú sért búin/n að loka öllum forritum sem tengjast LibreOffice (þar með talið flýtiræsingunni, QuickStarter).

Skiptu um staðsetningu yfir í möppuna þar sem þú afþjappaðir tungumálapakkanum.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Skiptu síðan yfir í möppuna sem inniheldur sjálfa uppsetningarpakkana. Á kerfum sem byggð eru á Debian/Ubuntu kallast sú mappa "DEBS". Á kerfum sem byggjast á Fedora, Suse eða Mandriva heitir þessi mappa "RPMS".

Í Nautilus skráastjóranum getur þú hægrismellt innan í möppunni og valið "Opna í skjáhermi". Skjáhermir getur einnig veriðkallaður "Útstöð" eða "Skel". Í glugganum sem opnast er svokölluð skipanalína, á hana skrifarðu eftirfarandi skipun (þú verður spurð/ur um rótarlykilorðið áður en skipunin er framkvæmd):

Á kerfum sem byggjast á Debian/Ubuntu: sudo dpkg -i *.deb

Á kerfum sem byggjast á Fedora: su -c 'dnf install *.rpm'

Á kerfum sem byggjast á Mandriva: sudo urpmi *.rpm

Á kerfum sem byggjast á RPM pakkakerfinu (OpenSUSE, o.s.frv.): rpm -Uvh *.rpm

Ræstu núna eitthvert af LibreOffice forritunum -til dæmis Writer Farðu í valmyndina "Verkfæri" og veldu "Valkostir". Í stillingaglugganum sem þá opnast, veldu "Tungumál og staðfærsla" og smelltu síðan á "Almennt". Veldu úr tungumálið sem þú varst að setja upp úr fellilistanum "Notendaviðmót". Ef þér sýnist svo geturðu gert hið sama fyrir stillingarnar "Staðfærsla", "Sjálfgefinn gjaldmiðill" og "Sjálfgefið tungumál fyrir skjöl".

Eftir að hafa stillt þetta, smelltu á "Í lagi". Stillingaglugginn mun lokast og þú færð að sjá skilaboð um að breytingarnar þínar verði ekki virkar eftir að þú hefur lokað öllum LibreOffice forritum og ræst síðpan aftur (muna að loka líka flýtiræsingunni QuickStarter ef hún er í gangi).

Næst þegar þú ræsir LibreOffice mun viðmót þess vera á tungumálinu sem þú varst að setja upp.

----------------------------------------------------------------------
Vandamál við ræsingu forrits
----------------------------------------------------------------------

Erfiðleikar við að ræsa LibreOffice (t.d. forritin frjósa) auk vandamála í sambandi við birtingu á skjá er oft af völdum rekla fyrir skjákort. Ef slík vandamál koma upp, skaltu uppfæra rekilinn fyrir skjákortið þitt eða prófa að nota skjákortsrekilinn sem kom með stýrikerfinu þínu.

----------------------------------------------------------------------
ALPS/Synaptics fartölvu-snertispjöld (touchpad) í Windows
----------------------------------------------------------------------

Vegna galla í Windows rekli, getuðu ekki skrunað í gegnum LibreOffice skjöl með því að renna fingrinum eftir ALPS/Synaptics snertispjöldum (touchpad).

Til að virkja skrun á Touchpad snertispjaldi, bættu þá við eftirfarandi línum í "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" stillingaskrána, og endurræstu síðan tölvuna:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Staðsetning stillingaskrárinnar gæti verið eitthvað breytileg eftir því um hvaða útgáfu Windows er að ræða.

----------------------------------------------------------------------
Flýtilyklar
----------------------------------------------------------------------

Einungis flýtilyklar (lyklasamsetningar) sem ekki eru í notkun af stýrikerfinu geta verið notaðir í LibreOffice. Ef lyklasamsetning í LibreOffice virkar ekki eins og lýst er í LibreOffice hjálpinni, athugaðu hvort sá flýtilykill sé þegar í notkun af stýrikerfinu. Til að laga slíka árekstra er venjulega hægt að breyta þeim lyklum sem stýrikerfið notar. Hitt er líka mögulegt, þú getur breytt næstum öllum lyklasamsetningum í LibreOffice. Til að skoða nánari upplýsingar um þetta er best að lesa LibreOffice hjálpina eða hjálparskjöl stýrikerfisins.

----------------------------------------------------------------------
Vandamál við að senda skjöl sem tölvupóst úr LibreOffice
----------------------------------------------------------------------

Þegar skjal er sent með 'Skrá - Senda - Skjal sem tölvupóst' eða 'Skrá - Senda - Skjal sem PDF-viðhengi' (File - Send - Email Document' eða 'Email as PDF) þá geta komið upp vandamál (forritið hrynur eða hangir). Þetta er um að kenna Windows-kerfisskránni "Mapi" (Messaging Application Programming Interface) sem veldur vandamálum í sumum útgáfum skráa. Því miður hefur ekki verið hægt að þrengja ástæðurnar niður í einhverja ákveðna útgáfu. Til að nálgast ítarlegri upplýsingar er hægt að heimsækja https://www.microsoft.com og leita í Microsoft Knowledge Base eftir "mapi dll".

----------------------------------------------------------------------
Mikilvægar athugasemdir varðandi aðgangsmál
----------------------------------------------------------------------

Fyrir upplýsingar um aðgengismál í LibreOffice, skoðaðu https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Stuðningur notenda
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Skoðaðu líka algengar spurningar (FAQ) á vefsvæði LibreOffice.

----------------------------------------------------------------------
Tilkynna villur og vandamál
----------------------------------------------------------------------

Kerfið sem við notum fyrir villuskýrslur, eftirfylgni og lausn á göllum er þessa stundina BugZilla, sem er hýst hjá https://bugs.documentfoundation.org/. Við hvetjum alla notendur til að finnast þeir velkomnir við að tilkynna um hverskyns villur og galla sem fundist gætu við notkun. Virkt flæði tilkynninga um það sem betur mætti fara er eitt mikilvægasta framlagið sem notendur geta gefið af sér til áframhaldandi þróunar og bætingar á LibreOffice hugbúnaðinum.

----------------------------------------------------------------------
Taka þátt
----------------------------------------------------------------------

LibreOffice samfélagið myndi hafa mikinn hag af virkri þátttöku þinni í þróun þessa mikilvæga opna hugbúnaðarverkefnis.

Sem notandi ertu nú þegar orðin/n mikilvægur hluti í þróunarferli hugbúnaðarins, við viljum hvetja þig til að taka enn virkari þátt í samfélaginu Endilega skráðu þig og skoðaðu vefsvæði LibreOffice þar sem fram kemur hvernig þú getur komið að enn meira gagni.

Leiðir til að byrja
----------------------------------------------------------------------

Besta leiðin til að taka þátt er að gerast áskrifandi að einum eða fleiri póstlistum, fylgjast með því sem fram fer um stund auk þess að fletta í eldri pósti til að kynnast því sem áður hefur farið fram á listunum síðan grunnkóðiLibreOffice var gefinn frjáls í október árið 2000 Þegar þér finnst tími til kominn, er gott að senda fyrst dálítinn kynningarpóst um sjálfa/n.þig og hoppa síðan í djúpu laugina Ef þú ert þegar búin/n að kynna þér út á hvað opinn og frjáls hugbúnaður gengur (Open Source Projects), skoðaðu þá verkefnalista LibreOffice (To-Dos) og athugaðu hvort þar er eitthvað sem þú gætir hjálpað til við að framkvæma.

Gerast áskrifandi
----------------------------------------------------------------------

Hér eru nokkrir af póstlistum verkefnisins sem þú getur gerst áskrifandi að á https://www.libreoffice.org/get-help/mailing-lists/

* Fréttir: announce@documentfoundation.org *mælt með þessu fyrir alla notendur* (lítil umferð)
* Aðalpóstlisti fyrir notendur: users@global.libreoffice.org *góð leið til að hlera umræður* (mikil umferð)
* Markaðssetning: marketing@global.libreoffice.org *kynningarmál og margt fleira* (umferð að aukast)
* Almennur listi fyrir hugbúnaðarþróun: libreoffice@lists.freedesktop.org (mikil umferð)

Taka þátt í einu eða fleiri verkefnum
----------------------------------------------------------------------

Þú getur gert heilmargt fyrir þetta mikilvæga opna hugbúnaðarverkefni jafnvel þó þú sért ekki með neina reynslu af forritun eða hugbúnaðarhönnun. Já, þú getur verið með!

Við vonumst til að þú njótir þess að vinna með nýja LibreOffice 26.2 og munir ganga til liðs við okkur á netinu.

LibreOffice samfélagið

----------------------------------------------------------------------
Notaður / breyttur grunnkóði
----------------------------------------------------------------------

Höfundarréttur að hluta til: 1998, 1999 James Clark. Höfundarréttur að hluta til: 1996, 1998 Netscape Communications Corporation.
