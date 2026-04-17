
======================================================================
„LibreOffice 26.2“ informacija naudotojui
======================================================================


Naujausią informaciją naudotojui skaitykite faile https://git.libreoffice.org/core/tree/master/README.md

Šiame faile pateikiama svarbi informacija apie LibreOffice programą. Rekomenduojame atidžiai perskaityti šią informaciją prieš pradedant diegimą.

Šį produktą vysto „LibreOffice“ bendruomenė, į kurią esate kviečiami įsijungti ir Jūs. Jeigu esate naujas „LibreOffice“ naudotojas, galite aplankyti „LibreOffice“ svetainę, kurioje rasite informacijos apie šį programų paketą ir prie jo vystymo prisidedančias bendruomenes. Svetainės adresas – https://www.libreoffice.org/.

Ar tikrai „LibreOffice“ visiems nemokamas?
----------------------------------------------------------------------

„LibreOffice“ gali nemokamai ir laisvai naudoti visi. „LibreOffice“ galima įdiegti daugelyje kompiuterių ir naudoti įvairiausiais tikslais (įskaitant komercinį, vyriausybinį, viešąjį ir edukacinį naudojimą). Išsamiau galima paskaityti licencijoje, pateikiamoje šiame „LibreOffice“ diegimo pakete.

Kodėl „LibreOffice“ visiems nemokamas?
----------------------------------------------------------------------

„LibreOffice“ nemokamai galima naudoti todėl, kad jį kūrė, programavo, testavo, vertė, aprašė, reklamavo pavieniai asmenys ir įmonės bei taip padarė „LibreOffice“ tuo, kuo ši programa dabar yra – pasaulyje pirmaujančiu atviruoju raštinės programų paketu, skirtu ir namams, ir biurui.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Pastabos apie diegimą
----------------------------------------------------------------------

Kad veiktų visos „LibreOffice“ funkcijos, reikalinga „Java“ programų vykdymo terpė (JRE). JRE nėra įtraukta į „LibreOffice“ diegimo paketą, ją reikia įdiegti atskirai.

Reikalavimai sistemai
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Svarbu: diegiant programą reikalingos administratoriaus teisės.

„LibreOffice“ nustatymas numatytąja programa „Microsoft Office“ formato dokumentams atverti gali būti priverstinai iškviečiamas arba neleidžiamas naudojant šiuos komandų eilutės jungiklius diegimo programai:

* REGISTER_ALL_MSO_TYPES=1 – „LibreOffice“ nustatoma numatytąja programa „Microsoft Office“ formato dokumentams atverti.
* REGISTER_NO_MSO_TYPES=1 – neleidžiama „LibreOffice“ nustatyti numatytąja programa „Microsoft Office“ formato dokumentams atverti.

Įsitikinkite, kad turite pakankamai laisvos vietos laikinajame aplanke. Taip pat įsitikinkite, kad turite skaitymo, rašymo ir paleidimo teises. Išjunkite visas programas prieš pradėdami diegimo procesą.

„LibreOffice“ diegimas į „Debian“ („Ubuntu“) šeimos „Linux“ sistemas
----------------------------------------------------------------------

Instrukcijos, kaip įdiegti kalbos paketą (prieš tai įdiegus anglišką „LibreOffice“ versiją), pateikiamos skyriuje „Kalbos paketo diegimas“.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Šiame aplanke yra poaplankis „DEBS“. Pereikite į poaplankį „DEBS“.

Atverkite veikiamąjį aplanką terminale. Tai galima padaryti aplanke spustelėjus dešiniuoju pelės klavišu ir pasirinkus „Atverti terminale“. Atsivėrusiame lange komandos eilutėje įveskite šią komandą (kad ji būtų įvykdyta, reikės įvesti pagrindinio naudotojo slaptažodį):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Diegimo procesas baigtas. Dabar visų „LibreOffice“ programų piktogramas turėtumėte matyti programų meniu dalyje „Biuro programos“.

„LibreOffice“ diegimas „Fedora“, „openSUSE“, „Mandriva“ ir kitose „Linux“ sistemose, naudojančiose RPM paketus
----------------------------------------------------------------------

Instrukcijos, kaip įdiegti kalbos paketą (prieš tai įdiegus anglišką „LibreOffice“ versiją), pateikiamos skyriuje „Kalbos paketo diegimas“.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Šiame aplanke yra poaplankis „RPMS“. Pereikite į poaplankį „RPMS“.

Atverkite veikiamąjį aplanką terminale. Tai galima padaryti aplanke spustelėjus dešiniuoju pelės klavišu ir pasirinkus „Atverti terminale“. Atsivėrusiame lange komandos eilutėje įveskite šią komandą (kad ji būtų įvykdyta, reikės įvesti pagrindinio naudotojo slaptažodį):

„Fedora“ pagrindu sukurtoms sistemoms: sudo dnf install *.rpm

„Mandriva“ pagrindu sukurtoms sistemoms: sudo urpmi *.rpm

Kitoms RPM pagrindo sistemoms („openSUSE“ ir kt.): rpm -Uvh *.rpm

Diegimo procesas baigtas. Dabar visų „LibreOffice“ programų piktogramas turėtumėte matyti programų meniu dalyje „Biuro programos“.

Programą taip pat galima įdiegti naudotojo teisėmis paleidus diegimo scenarijų „install“, esantį pagrindiniame šio pako aplanke. Scenarijumi bus sukurtas atskiras „LibreOffice“ egzemplioriaus profilis, nesusijęs su įprastu „LibreOffice“ profiliu. Atminkite, kad šitaip nebus įdiegta darbalaukio integracija – nebus sukurti darbalaukio meniu elementai ir neužregistruoti MIME tipai.

Pastaba dėl darbalaukio integracijos paketų diegimo kitose, šiose instrukcijose nepaminėtose „Linux“ atmainose
----------------------------------------------------------------------

Turėtų būti įmanoma įdiegti „LibreOffice“ ir kitose, čia nepaminėtose „Linux“ atmainose. Skirtumų gali atsirasti tik diegiant darbalaukio integracijos paketus.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Kalbos paketo diegimas
----------------------------------------------------------------------

Parsisiųskite norimos kalbos paketą, skirtą jūsų operacinei sistemai. Juos galima siųstis iš ten pat, kaip ir pagrindinį programos diegimo paką. Naudodamiesi „Nautilus“ failų tvarkytuve išpakuokite parsisiųstą paką į aplanką (pavyzdžiui, darbalaukyje). Įsitikinkite, kad visos „LibreOffice“ programos išjungtos (taip pat ir sparčioji paleistis, jei ji naudojama).

Atverkite aplanką, į kurį išpakavote parsisiųstą kalbos paketą.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Atverkite poaplankį, kuriame yra diegtini paketai. „Debian“ („Ubuntu“) šeimos sistemose toks poaplankis vadinsis DEBS. „Fedora“, „openSUSE“ ar „Mandriva“ sistemose – RPMS.

Atverkite veikiamąjį aplanką terminale. Tai galima padaryti aplanke spustelėjus dešiniuoju pelės klavišu ir pasirinkus „Atverti terminale“. Atsivėrusiame lange komandos eilutėje įveskite komandą kalbos paketui įdiegti (kad ji būtų įvykdyta, reikės įvesti pagrindinio naudotojo slaptažodį):

„Debian“ („Ubuntu“) šeimos sistemoms: sudo dpkg -i *.deb

„Fedora“ pagrindu sukurtoms sistemoms: su -c 'dnf install *.rpm'

„Mandriva“ pagrindu sukurtoms sistemoms: sudo urpmi *.rpm

Kitoms RPM pagrindo sistemoms („openSUSE“ ir kt.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Nustatę reikiamas parinktis spustelėkite „Gerai“. Dialogo langas bus užvertas, o programa jus informuos, kad pakeitimai įsigalios tik iš naujo paleidus „LibreOffice“ (nepamirškite išjungti ir sparčiosios paleisties, jei ją naudojate).

Kai kitą kartą paleisite „LibreOffice“, programoje bus nustatyta kalba, kurią ką tik įdiegėte.

----------------------------------------------------------------------
Nesklandumai paleidžiant programą
----------------------------------------------------------------------

Nesklandumus paleidžiant „LibreOffice“, programos strigtis ar vaizdo ekrane problemas dažnai sukelia vaizdo plokštės tvarkyklė. Jei susiduriate su panašiais nesklandumais, atnaujinkite vaizdo plokštės tvarkyklę arba naudokite su operacine sistema pateikiamą tvarkyklę.

----------------------------------------------------------------------
Nešiojamųjų kompiuterių su „ALPS/Synaptics“ jutikliniais kilimėliais ir „Windows“ OS naudotojams
----------------------------------------------------------------------

Dėl klaidos „Windows“ OS skirtoje tvarkyklėje „LibreOffice“ dokumento negalima slinkti braukiant pirštu per „ALPS/Synaptics“ jutiklinį kilimėlį.

Jei norite naudotis jutikliniu kilimėliu dokumentui slinkti, įrašykite šias eilutes į „C:\Program Files\Synaptics\SynTP\SynTPEnh.ini“ sąrankos failą ir iš naujo paleiskite kompiuterį:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Sąrankos failo vieta gali skirtis priklausomai nuo naudojamos „Windows“ OS versijos.

----------------------------------------------------------------------
Spartieji klavišai
----------------------------------------------------------------------

Programoje „LibreOffice“ galima naudotis tik tais sparčiaisiais klavišais (klavišų kombinacijomis), kurių nenaudoja operacinė sistema. Jei kuri nors klavišų kombinacija programoje „LibreOffice“ neveikia, nors pagal informaciją žinyne ji turėtų veikti, reikėtų patikrinti, ar šios klavišų kombinacijos nenaudoja operacinė sistema. Norint pašalinti šiuos nesklandumus, operacinės sistemos sparčiuosius klavišus galima pakeisti. Kita vertus, galima pakeisti ir beveik visus „LibreOffice“ programos sparčiuosius klavišus. Daugiau informacijos apie tai galima ieškoti „LibreOffice“ programos arba kompiuteryje naudojamos operacinės sistemos žinynuose.

----------------------------------------------------------------------
Nesklandumai, galintys kilti siunčiant „LibreOffice“ dokumentus el. paštu
----------------------------------------------------------------------

Norint išsiųsti dokumentą naudojantis komandomis „Failas ▸ Siųsti ▸ Dokumentą el. paštu…“ arba „Siųsti el. paštu – PDF dokumentą…“ gali kilti nesklandumų. Pastarieji gali būti susiję su kai kuriomis „Windows“ sisteminio failo „Mapi“ (Messaging Application Programming Interface) versijomis. Deja, kol kas negalima tiksliai nustatyti probleminės failo versijos. Smulkesnės informacijos ieškokite https://www.microsoft.com, paieškos lauke įvedę „mapi dll“.

----------------------------------------------------------------------
Pastabos apie pritaikymą neįgaliesiems
----------------------------------------------------------------------

Daugiau informacijos apie „LibreOffice“ pritaikymą neįgaliesiems rasite tinklalapyje https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Pagalba naudotojui
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Dar siūlome peržiūrėti klausimų ir atsakymų tinklalapį „LibreOffice“ svetainėje.

----------------------------------------------------------------------
Pranešimai apie kilusius nesklandumus bei defektus
----------------------------------------------------------------------

Klaidoms registruoti, sekti ir taisyti naudojama „Bugzilla“ sistema, esanti svetainėje https://bugs.documentfoundation.org/. Kviečiame visus naudotojus pranešti apie iškilusias problemas. Aktyvus klaidų registravimas – vienas iš svarbiausių darbų, kuriuos gali atlikti naudotojų bendruomenė kuriant ir tobulinant „LibreOffice“.

----------------------------------------------------------------------
Bendradarbiavimas
----------------------------------------------------------------------

„LibreOffice“ bendruomenei būtų malonu, jei Jūs aktyviai bendradarbiautumėte kuriant šį atvirąjį projektą.

Naudodami šią programą Jūs jau svariai prisidedate prie jos vystymo. Visgi norėtume pakviesti Jus prisidėti dar labiau ir tapti nuolatiniu bendradarbiu. Kviestume paskaityti apie tai daugiau tinklalapyje https://www.libreoffice.org/community/get-involved.

Kaip pradėti
----------------------------------------------------------------------

Patogiausias būdas pradėti bendradarbiauti – užsiregistruoti į vieną ar kelias el. pašto grupes, kurį laiką stebėti diskusijas, palaipsniui peržvelgti archyvuose laikomą medžiagą apie pagrindines, nuo 2000 m. spalio (kada pasirodė programos „LibreOffice“ pirminis tekstas) gvildentas temas. Tada telieka parašyti elektroninį laišką apie save ir prisijungti prie mūsų. Jei gaudotės atvirosiose programose, žvilgtelėkite į mūsų pateiktą reikalingų darbų sąrašą: galbūt čia rasite tai, kuo galėtumėte padėti (žr. https://www.libreoffice.org/community/developers).

Užsiregistravimas į el. pašto grupes
----------------------------------------------------------------------

Toliau išvardinta keletas el. pašto grupių, į kurias galima užsiregistruoti iš tinklalapio https://www.libreoffice.org/get-help/mailing-lists/

* Naujienos: announce@documentfoundation.org (rekomenduojama visiems naudotojams, mažas laiškų srautas)
* Pagrindinė naudotojų el. pašto grupė: users@global.libreoffice.org (paprasta sekti diskusijas, didelis laiškų srautas)
* Rinkodaros projektai: marketing@global.libreoffice.org (su programavimu nesusijusios diskusijos, laiškų srautas tampa didelis)
* Pagrindinė programuotojų el. pašto grupė: libreoffice@lists.freedesktop.org (didelis laiškų srautas)

Prisijunkite prie vieno ar kelių projektų
----------------------------------------------------------------------

Rimtai prisidėti prie šio svarbaus atvirojo projekto galima net ir neturint didelės programinės įrangos kūrimo bei programavimo patirties. Neabejokite tuo!

Tikimės, kad patiks dirbti naujuoju „LibreOffice 26.2“ paketu ir prisijungsite prie mūsų bendruomenės internete.

„LibreOffice“ bendruomenė

----------------------------------------------------------------------
Naudotas arba perdarytas pirminis tekstas
----------------------------------------------------------------------

© Dalinės autoriaus teisės: 1998, 1999 James Clark. © Dalinės autoriaus teisės: 1996, 1998 Netscape Communications Corporation.
