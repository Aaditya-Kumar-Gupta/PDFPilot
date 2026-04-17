
======================================================================
File łèzame de LibreOffice 26.2
======================================================================


Par l'ajornamento ùltemo de 'sto file łèzame, varda https://git.libreoffice.org/core/tree/master/README.md

'Sto file cuà el gà rento informasion inportanti so'l programa LibreOffice. Prima de ndar vanti co l'instałasion, te racomandemo de łèzare 'ste informasion co tanta atension.

Ła comunidà de LibreOffice ła ze responsàbiłe de'l dezviłupo de 'sto prodoto e ła te invita a considarar ła to partesipasion cofà menbro de ła comunidà. Se te si un novo utente, te pol vizitar el sito de LibreOffice, indove A te podarè catar tute łe informasion so'l projeto LibreOffice e łe comunidà che ghe jira intorno. Vìzita https://www.libreoffice.org/.

LibreOffice zeło davero un prodoto łìbaro par tuti?
----------------------------------------------------------------------

Tuti ze łìbari de doparar LibreOffice. Te pol instałar 'sta copia de LibreOffice in calsiasi computer e dopararla par calsiasi fin che te vol (incluzo comersiałe, governativo, aministrasion pùblega e scołe). Par aver pì detaji, varda ła łisensa contenjùa in 'sta copia de LibreOffice.

Parché LibreOffice el ze łìbaro par tuti?
----------------------------------------------------------------------

Te połi doparar 'sta copia de LibreOffice sensa pagar njente daché contribudori individuałi e aziende patrosinanti i ga projetà, dezviłupà, provà, traduzesto, documentà, suportà, publisizà e jutà in racuante altre manjere par rèndar LibreOffice cuel che l'e uncò: el programa de produtività open source primo inte'l mondo, par ła caza e l'ufisio.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Note so l'instałasion
----------------------------------------------------------------------

LibreOffice par funsionar in maniera conpleta el ga de bezonjo de na version resente de l'anbiente de runtime Java (JRE). JRE no'l fa parte de'l pacheto de instałasion de LibreOffice e el ga da èsar instałà separadamente.

Recueziti de sistema
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Par l'instałasion ze nesesario aver i deriti de aministrador.

L'inpostasion de LibreOffice cofà aplegasion predefenìa par i formati de documento Microsoft Office ła połe èsar forsada o escludesta doparando i paràmetri de comando par l'instałasion drioman:

* REGISTER_ALL_MSO_TYPES=1 forsarà ła rejistrasion de LibreOffice cofà aplegasion predefenìa par i formati Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 el dezabiłitarà ła rejistrasion de LibreOffice cofà aplegasion predefenìa par i formati Microsoft Office.

Segùrate che ghe sia spasio łìbaro sufisiente inte ła carteła tenporànea de'l to sistema e de aver i deriti de łetura, scritura e ezecusion. Prima de far partìr el proseso de instałasion sara su tuti i altri programi.

Instałasion de LibreOffice su sistemi Linux bazai Debian/Ubuntu
----------------------------------------------------------------------

Par inparar a instałar un pacheto de łengua (dopo ver instałà ła varsion Ingleze US de LibreOffice), łezi ła sesion drioman intitołà "Instałar un pacheto de łengua".

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

'Sta carteła ła contien na sotocarteła ciamada "DEBS". Spóstate inte ła carteła "DEBS".

Faghe click drito inte ła carteła e sełesiona "Verzi so'l terminałe". Se verzarà na fenestra de terminałe. Da ła riga de comando de ła fenestra, meti rento el comando seguente (par ezeguir el comando te venjarà domandà de métar rento ła to password de aministrasion):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

El proseso de instałasion deso el ze conpletà, e te dovarisi aver łe icone par tute łe aplegasion de LibreOffice inte'l menu Aplegasion/Ufisio de'l to desktop.

Instałasion de LibreOffice so sistemi Linux Fedora, openSUSE, Mandriva e altri, che i dòpara pacheti RPM
----------------------------------------------------------------------

Par inparar a instałar un pacheto de łengua (dopo ver instałà ła varsion Ingleze US de LibreOffice), łezi ła sesion drioman intitołà "Instałar un pacheto de łengua".

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

'Sta carteła ła contien na sotocarteła ciamada "RPMS". Spóstate inte ła carteła "RPMS".

Faghe click drito inte ła carteła e sełesiona "Verzi so'l terminałe". Se verzarà na fenestra de terminałe. Da ła riga de comando de ła fenestra, meti rento el comando seguente (par ezeguir el comando te venjarà domandà de métar rento ła to password de aministrasion):

Par i sistemi bazài so Fedora: sudo dnf install *.rpm

Par i sistemi bazài so Mandriva: sudo urpmi *.rpm

Par cheł'altri sistemi bazài so RPM (openSUSE, ese.): rpm -Uvh *.rpm

El proseso de instałasion deso el ze conpletà, e te dovarisi aver łe icone par tute łe aplegasion de LibreOffice inte'l menu Aplegasion/Ufisio de'l to desktop.

In alternativa, par ezeguir na instałasion cofà utente te pol doparar el script 'install', che se trova inte ła carteła prinsipałe de sto archivio. El script el inpostarà LibreOffice in maniera da aver un so profiło par 'sta instałasion cuà, separà da'l to normałe profiło LibreOffice. Tien prezente che 'sta operasion cuà no ła instałarà mìa łe parti par l'integrasione de'l sistema, cofà i ełementi de menu e łe rejistrasion de i tipi MIME.

Note reguardo l'integrasion desktop par łe distribusion Linux mìa tratà inte łe istrusion de instałasion presedenti
----------------------------------------------------------------------

Dovarìa èsar posìbiłe instałar fasilmente LibreOffice so altre distribusion Linux mìa spesifegamente definìe in 'ste istrusion de instałasion. Łe difarense prinsipałi che se podarìa incontrar łe ze so l'integrasion de'l desktop.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Instałar un pacheto de łengua
----------------------------------------------------------------------

Descarga el pacheto de łengua che te serve par ła to piataforma. El ze desponìbiłe so'l steso posto de l'archivio de instałasion prinsipałe. Cava fora i file de l'archivio descargà da'l jestor Nautilus so na carteła (el to desktop, par ezenpio). Controła de ver sarà su tute łe aplegasion LibreOffice (incrudesto QuickStart se'l ze tacà).

Spostate inte ła carteła indove che te ghe estrato el pacheto de łengua descargà.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Deso spostate inte ła carteła che contien i pacheti da instałar. Inte i sistemi bazài so Debian/Ubuntu, ła carteła ła sarà DEBS. Inte i sistemi Fedora, openSUSE o Mandriva, ła carteła ła sarà RPMS.

Da'l jestor de file Nautilus, faghe click drito inte ła carteła e sełesiona el comando "Verzi so'l terminałe". Inte ła fenestra de'l terminałe pena verta ezegui el comando par instałar el pacheto de łengua (podarìa èsar domandà ła password de aministrasion par tuti i comandi seguenti):

Par i sistemi bazài so Debian/Ubuntu: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Par i sistemi bazài so Mandriva: sudo urpmi *.rpm

Par cheł'altri sistemi che dòpara RPM (openSUSE, ese.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Dopo ver sistemà łe inpostasion, faghe click so OK. Ła fenestra ła se sararà sù e venjarà fora un mesajo informativo che'l te dizarà che łe to modìfeghe łe sarà ative soło dopo che A te gavarè sarà sù e tacà danovo LibreOffice (recòrdate de sarar sù anca QuickStart se'l ze tacà).

Co l'inviamento seguente, LibreOffice el sarà inte ła łengua pena instałà.

----------------------------------------------------------------------
Problemi durando l'inviamento de'l programa
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Touchpad ALPS/Synaptics in MS Windows
----------------------------------------------------------------------

Parvìa de un problema co i driver de MS Windows, no ze mìa posìbiłe doparar ła funsion de scorimento de'l touchpad ALPS/Synaptics inte i documenti de LibreOffice.

Par abiłitar el scorimento, zonta łe righe seguenti so'l file de confegurasion "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" e dopo fa repartir el computer:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Ła pozision de'l file de confegurasion ła pol canbiar so i defarenti sistemi Windows.

----------------------------------------------------------------------
Scurtarołe da tastiera
----------------------------------------------------------------------

Soło łe scurtarołe da tastiera (conbinasion de botoni) mìa doparà da'l sistema oparadivo łe pol èsar doparà in LibreOffice. Se na conbinasion de botoni de LibreOffice no ła funsiona come scrito inte ła guida de LibreOffice, controła se ła scurtaroła ła ze zà doparà da'l sistema oparadivo. Par resolvare 'sti confliti, te pol canbiar łe scurtarołe da tastiera de'l sistema oparadivo. In alternativa A te pol canbiar cuazi tute łe scurtarołe da tastiera de LibreOffice. Par aver pì informasion so 'sta chestion, fà refarimento a ła guida in łinea de LibreOffice o a ła documentasion de'l to sistema oparadivo.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Avertense inportanti par l'acesibiłità
----------------------------------------------------------------------

Par aver pì informasion so łe caraterìsteghe de aceso fasiłità in LibreOffice, varda https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Suporto utenti
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Consulta anca ła sesion FAQ inte'l sito web de LibreOffice.

----------------------------------------------------------------------
Referir erori e problemi
----------------------------------------------------------------------

El nostro sistema de refarir, trasiamento e sołusion de i erori el ze Bugzilla, ospità inte https://bugs.documentfoundation.org/. Invitemo tuti i utenti a refarir i erori rescontrài so ła so piataforma spesìfega. Refarir erori in manjera ativa el ze uno de i contibuti pì inportanti che ła comunidà de utenti ła pol dar par el dezviłupo e el mejoramento futuro de LibreOffice.

----------------------------------------------------------------------
Come cołaborar
----------------------------------------------------------------------

Ła comunidà de LibreOffice ła ga de bezonjo de ła to partesipasion ativa par el dezviłupo de 'sto inportante projeto open source.

Cofà utente, A te si za na parte inportante de'l proseso de dezviłupo de ła suite e vorìsimo che te gavesi na parte ancora pì ativa, co l'obietivo de deventar un contribudor a łongo tèrmine de ła comunidà. Par piaser, contàtane e zòntate a noialtri inte ła pàjina de contribusion sito web LibreOffice.

Come scomisiar
----------------------------------------------------------------------

El modo mejo par scomisiar a contribuir a'l projeto el ze de iscrìvarse a una o pì mailing list, ndarghe drio a łe discusion par un poco e scomisiar a łèzar i archivi par ciapar confidensa co i tanti argomenti tratài da cuando che A ze stà dà fora LibreOffice inte'l łontan meze de otobre de'l 2000. Cuando che A te te sentirè pronto, tuto cueło che te gavarè da far A ze mandar un mesajo de prezentasion e saltar sù so'l caro. Se A te ghè za cołaborà a altri projeti open source, controła ła łista de łe robe da far (To-Do) e varda se A ghe ze calcosa che'l fa par ti so'l sito web de LibreOffice.

Iscrìvate
----------------------------------------------------------------------

Inte 'sta pàjina ghe ze un poche de mailing list ndove che te połi iscrìvarte https://vec.libreoffice.org/suporto/mailing-list/

* News: announce@documentfoundation.org *racomandà a tuti i utenti* (tràfego łejero)
* Łista utenti prinsipałe: users@global.libreoffice.org *metodo senplise par seguir łe discusion* (tràfego pezante)
* Projeto marketing: marketing@global.libreoffice.org *oltre el dezviłupo* (tràfego in cresar)
* Łista jenarałe par dezviłupadori: libreoffice@lists.freedesktop.org (tràfego intenso)

Tacarse a uno o pì projeti
----------------------------------------------------------------------

A te połi dar un contribudo inportante a 'sto inportante projeto open source anca se A no te ghe mìa tanta espariensa de projetasion o programasion de software. Sì, propio ti!

Te auguremo bon łavoro e divertimento co'l novo LibreOffice 26.2 e speremo de incontrarte presto online.

Ła comunidà de LibreOffice

----------------------------------------------------------------------
Còdeze sorjente doparà / modifegà
----------------------------------------------------------------------

Tochi co Copyright 1998, 1999 James Clark. Tochi co Copyright 1996, 1998 Netscape Communications Corporation.
