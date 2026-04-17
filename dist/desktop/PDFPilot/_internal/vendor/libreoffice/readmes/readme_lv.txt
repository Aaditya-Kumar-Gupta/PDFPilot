
======================================================================
LibreOffice 26.2 LasiMani
======================================================================


Lai iegūtu jaunākos šīs LASIMANI datnes atjauninājumus, jādodas uz https://git.libreoffice.org/core/tree/master/README.md

Šī datne satur svarīgu informāciju par LibreOffice programmatūru. Iesakām šo datni rūpīgi izlasīt, pirms sākt instalēšanu.

LibreOffice kopiena ir atbildīga par šī produkta izstrādāšanu un aicina jūs apsvērt piedalīties kā kopienas dalībniekam. Ja esat jauns lietotājs, varat apmeklēt LibreOffice vietni, kur atradīsiet daudz informācijas par LibreOffice projektu un ap to esošajām kopienām. Ejiet uz https://www.libreoffice.org/.

Vai LibreOffice tiešām ir brīvs katram lietotājam?
----------------------------------------------------------------------

LibreOffice var brīvi lietot katrs. Jūs varat instalēt LibreOffice uz tik datoriem, cik vēlaties, un izmantot jebkuriem mērķiem (tai skaitā komerciāliem, valsts iestādēs un izglītībai). Sīkākai informācijai skatiet licences tekstu, kas nāk kopā ar LibreOffice.

Kāpēc LibreOffice ir brīvs katram lietotājam?
----------------------------------------------------------------------

Jūs varat kopēt LibreOffice bez maksas, jo individuāli veidotāji un kooperatīvie sponsori ir projektējuši, izstrādājuši, testējuši, tulkojuši, dokumentējuši, atbalstījuši, reklamējuši un palīdzējuši daudzos citos veidos padarīt LibreOffice par to, kas tas ir šodien – pasaules vadošā atvērtā pirmkoda biroja programmatūru.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Instalēšanas piezīmes
----------------------------------------------------------------------

LibreOffice vajag nesenu Java Runtime Environment (JRE) versiju pilnai funkcionalitātei. JRE nav daļa no LibreOffice instalācijas pakotnes, to vajadzētu instalēt atsevišķi.

Sistēmas prasības
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Lūdzu, ņemiet vērā, ka instalēšanas turpināšanai ir nepieciešama administratora tiesības.

LibreOffice reģistrēšanu par noklusējuma programmu Microsoft Office formātu atvēršanai var uzspiest vai aizliegt, izmantojot šādus instalātora komandrindas parametrus:

* REGISTER_ALL_MSO_TYPES=1 liks reģistrēt LibreOffice kā noklusējuma lietotni Microsoft Office formātiem.
* REGISTER_ALL_MSO_TYPES=1 neļaus reģistrēt LibreOffice kā noklusējuma lietotni Microsoft Office formātiem.

Lūdzu, pārliecinieties, ka sistēmas pagaidu mapē ir pietiekami daudz brīvas vietas, un pārliecinieties, ka jums ir piešķirtas gan rakstīšanas, gan lasīšanas, gan izpildes tiesības. Pirms instalēšanas sākšanas, aizveriet visas citas programmas.

LibreOffice instalēšana uz Debian/Ubuntu bāzētām Linux sistēmām
----------------------------------------------------------------------

Lai saņemtu norādes, kā instalēt valodas paku (pēc tam, kad ir uzinstalēta LibreOffice US English versija), lūdzu, izlasiet nodaļu "Valodas pakas instalēšana" zemāk.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Tajā atrodas mape "DEBS". Atveriet to.

Veiciet labo klikšķi mapē un izvēlieties "Atvērt terminālī". Parādīsies termināļa logs. No komandrindas termināļa logā ievadiet sekojošo komandu (pirms komandas izpildes jums prasīs jūsu root lietotāja paroli):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Instalēšanas process nu ir pabeigts, visām LibreOffice lietotņu ikonām vajadzētu būt Lietotnes/Birojs izvēlnē.

LibreOffice instalēšana uz Fedora, openSuse, Mandriva un citām Linux sistēmām, kas izmanto RPM pakotnes
----------------------------------------------------------------------

Lai saņemtu norādes, kā instalēt valodas paku (pēc tam, kad ir uzinstalēta LibreOffice US English versija), lūdzu, izlasiet nodaļu “Valodas pakas instalēšana” zemāk.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Šī mape satur apakšmapi "RPMS". Mainiet mapi uz "RPMS" mapi.

Veiciet labo klikšķi mapē un izvēlieties "Atvērt terminālī". Parādīsies termināļa logs. No komandrindas termināļa logā ievadiet sekojošo komandu (pirms komandas izpildes jums prasīs jūsu root lietotāja paroli):

For Fedora-based systems: sudo dnf install *.rpm

Uz Mandriva bāzētām sistēmām: sudo urpmi *.rpm

Uz citām RPM bāzētām sistēmām (openSUSE, u.c.): rpm -Uvh *.rpm

Instalēšanas process nu ir pabeigts, visām LibreOffice lietotņu ikonām vajadzētu būt Lietotnes/Birojs izvēlnē.

Vai arī varat izmantot skriptu “install”, kas atrodas šī arhīva augšējā direktorijā, lai instalēšanu veiktu kā lietotājs. Skripts instalēs LibreOffice ar atsevišķu profilu, kas ir atdalīts no parastā LibreOffice profila. Ņemiet vērā, ka netiks instalētas sistēmas integrācijas daļas, piemēram, darbvirsmas izvēlnes vienumi un darbvirsmas MIME tipu reģistrēšana.

Piezīmes par integrēšanu darbvirsmā Linux distribūcijām, kas nav aprakstītas instalēšanas instrukcijās augstāk
----------------------------------------------------------------------

LibreOffice vajadzētu varēt viegli uzinstalēt uz citām Linux distribūcijām, kas nav aprakstītas šajās instrukcijās. Galvenās atšķirības varētu būt integrēšana darbvirsmā.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Valodas pakas instalēšana
----------------------------------------------------------------------

Lejupielādējiet valodas paku sev vēlamajai valodai un platformai. Tās ir pieejamas no tās pašas vietas, kur atradās galvenais instalācijas arhīvs. No Nautilus datņu pārvaldnieka, atspiediet lejupielādēto arhīvu mapē (piemēram, uz darbvirsmas). Pārliecinieties, ka esat izgājis no visām LibreOffice lietotnēm (tai skaitā no ātrā palaidēja, ja tas ir startēts).

Atveriet mapi, kurā lejupielādējāt valodas paku.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Tagad atveriet mapi, kura satur pakotnes, kuras jāinstalē. Uz Debian/Ubuntu bāzētām sistēmām mapes nosaukums ir DEBS. Uz Fedora, openSUSE vai Mandriva sistēmām mape ir RPMS.

No Nautilus datņu pārvaldnieka, veiciet labo klikšķi uz mapes un izvēlieties "Atvērt terminālī". Tikko atvērtajā termināļa logā izpildiet komandu, lai instalētu valodas paku (visām komandām zemāk varētu prasīt root lietotāja paroli):

Uz Debian/Ubuntu bāzētām sistēmām: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Uz Mandriva bāzētām sistēmām: sudo urpmi *.rpm

Uz citām sistēmām, kas lieto RPM (openSUSE, u.c.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Pēc iestatījumu pielāgošanas jāklikšķina uz “Labi”. Dialoglodziņš aizvērsies un Tu redzēsi paziņojumu, ka izmaiņas stāsies spēkā pēc iziešanas no LibreOffice un tā atkārtotas palaišanas (jāatceras, ka jāiziet arī no ātrā palaidēja, ja tas ir palaists).

Nākamo reizi palaižot LibreOffice, tiks startēta valoda, kuru jūs tikko uzinstalējāt.

----------------------------------------------------------------------
Problēmas ar programmas palaišanu
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
ALPS/Synaptics piezīmjdatoru skārienjūtīgie paneļi Windows vidē
----------------------------------------------------------------------

Dažādu Windows draiveru problēmu dēļ jūs nevarat ritināt LibreOffice dokumentus, slidinot pirkstu pār piezīmjdatoru ALPS/Synaptics skārienpalikņiem.

Lai ieslēgtu ritināšanu ar ALPS/Synaptics skārienpalikņiem, pievienojiet sekojošas rindiņas "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" konfigurācijas datnei un pārstartējiet datoru:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Dažādās Windows versijās šī konfigurācijas datnes atrašanās vieta var atšķirties.

----------------------------------------------------------------------
Īsinājumtaustiņi
----------------------------------------------------------------------

LibreOffice kā īsinājumtaustiņus var lietot tikai tās taustiņu kombinācijas, kas netiek lietotas operētājsistēmā. Ja kāda LibreOffice taustiņu kombinācija nedarbojas kā aprakstīts LibreOffice palīdzībā, pārbaudiet, vai to nav aizņēmusi operētājsistēma. Lai atrisinātu iespējamo konfliktu, varat izmainīt operētājsistēmas taustiņu kombinācijas. Vai arī varat izmainīt gandrīz jebkuru LibreOffice taustiņu kombināciju. Sīkāku informāciju lasiet LibreOffice palīdzībā vai savas operētājsistēmas palīdzības dokumentācijā.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Svarīgas pieejamības piezīmes
----------------------------------------------------------------------

Lai iegūtu vairāk informācijas par LibreOffice pieejamības iespējam, skatiet https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Lietotāju atbalsts
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Pārbaudiet arī BUJ sadaļu LibreOffice tīmekļa vietnē.

----------------------------------------------------------------------
Kļūdu un problēmu ziņošana
----------------------------------------------------------------------

Pašlaik mūsu sistēma kļūdu ziņošanai, izsekošanai un labošanai ir Bugzilla, kas tiek izmitināta vietnē https://bugs.documentfoundation.org/. Mēs aicinām lietotājus ziņot par kļūdām un problēmām, kas gadās, lietojot šo programmatūru to izmantotajā platformā. Cītīga ziņošana par kļūdām ir viens no svarīgākajiem pienesumiem, ko lietotāju kopiena var sniegt, lai LibreOffice turpinātu attīstīties un uzlaboties.

----------------------------------------------------------------------
Kā iesaistīties
----------------------------------------------------------------------

LibreOffice kopiena iegūtu ļoti daudz no jūsu aktīvas līdzdalības šajā svarīgajā atvērtā pirmkoda projektā.

Jau kā lietotājam jums ir svarīga loma šīs biroja programmatūras izstrādes procesā, tāpēc mēs gribētu mudināt jūs piedalīties vēl aktīvāk, kļūstot par pastāvīgu mūsu kopienas atbalstītāju. Lūdzu, pievienojieties un apskatiet mūsu lietotāju lapu LibreOffice tīmekļa vietnē.

Kā sākt
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Abonēt
----------------------------------------------------------------------

Šie ir daži no adresātu sarakstiem, kurus jūs varat abonēt: https://www.libreoffice.org/get-help/mailing-lists/

* Ziņas: announce@documentfoundation.org *ieteicams visiem lietotājiem* (maza informācijas plūsma)
* Galvenā lietotāju sarakste: users@global.libreoffice.org *vienkāršs veids, kā novērot sarunas* (liela plūsama)
* Mārketinga projekts: marketing@global.libreoffice.org *vairāk nekā izstrāde* (plūsma kļūst liela)
* Galvenā izstrādātāju sarakste: libreoffice@lists.freedesktop.org (liela plūsma)

Pievienojieties vienam vai vairākiem projektiem
----------------------------------------------------------------------

Jūs varat sniegt nopietnu ieguldījumu šī svarīgā projekta izstrādē un attīstībā, pat ja jums ir ierobežotas programmēšanas zināšanas. Jā, tieši jūs!

Mēs ceram, ka jums patiks strādāt ar jauno LibreOffice 26.2 un jūs mums pievienosieties tiešsaistē.

LibreOffice kopiena

----------------------------------------------------------------------
Izmantotais / modificētais pirmkods
----------------------------------------------------------------------

Daļa no autortiesībām 1998, 1999 James Clark. Daļa no autortiesībām 1996, 1998 Netscape Communications Corporation.
