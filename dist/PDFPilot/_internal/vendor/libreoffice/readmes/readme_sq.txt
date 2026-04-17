
======================================================================
Skedar më lexo LibreOffice 26.2
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

Ky skedar përmban informacion të rëndësishëm rreth programit LibreOffice. Ju rekomandojmë që ta lexoni me shumë kujdes këtë informacion përpara se të filloni instalimin.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

A është vertet LibreOffice falas për çdo përdorues?
----------------------------------------------------------------------

LibreOffice është për përdorim falas nga të gjithë. Ju mund ta merrni kopjen e LibreOffice dhe ta instaloni në sa kompjutera të dëshironi, dhe ta përdorni për çfarëdo qëllimi që të dëshironi (duke përfshirë përdorim komercial, qeveritar, administratë publike dhe edukativ). Për më shumë detaje shikoni paketën e liçensave tekst me shkarkimin LibreOffice.

Pse është LibreOffice falas për çdo pëdrorues?
----------------------------------------------------------------------

Mund të përdorësh këtë kopje të LibreOffice pa paguar gjë sepse kontribuues individual dhe korporata sponsor kanë projektuar, zhvilluar, provuar, përkthyer, dokumentuar, mbështetur, reklamuar, dhe ndihmuar në shumë mënyra të tjera për të bërë LibreOffice atë çka është sot: programi i produktivitetit për shtëpi dhe zyrë me burim të hapur i pari në botë.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Vërejtje mbi instalimin
----------------------------------------------------------------------

LibreOffice requires a recent version of Java Runtime Environment (JRE) for full functionality. JRE is not part of the LibreOffice installation package, it should be installed separately.

Sistem tingulli
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Për instalimin nevojiten të drejtat e administratorit.

Regjistrimi i LibreOffice si programi i parazgjedhur për formatet Microsoft Office mund të detyrohet ose të përjashtohet duke përdorur parametrat për komandë të mëtejshme për instalimin:

* REGISTER_ALL_MSO_TYPES=1 do të detyrojë regjistrimin e LibreOffice si program i parazgjedhur për formatet Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 do të çaktivizojë regjistrimin e LibreOffice si program i parazgjedhur për formatet Microsoft Office.

Sigurohu të kesh memorie të lirë të mjaftueshme në dosjen e përkohshme në sistem tënd, dhe sigurohu të kesh të drejtat për të lexuar, për të shkruar dhe për të ekzekutuar. Mbyll të gjithë programet tjera para se të fillosh instalimin.

Instalimi i LibreOffice mbi sistemet Linux të bazuara mbi Debian/Ubuntu
----------------------------------------------------------------------

Për udhëzime mbi instalimin e një pakete gjuhe (pas instalimit të versionit anglisht US të LibreOffice), lexo pjesën e mëposhtme të titulluar Instalimi i një pakete gjuhe.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Dosja përmban një nëndosje të quajtur "DEBS". Shko tek dosja "DEBS".

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Procesi i instalimit tashmë u plotësua, dhe duhet të kesh ikonat për të gjitha programet e LibreOffice në menynë Programet/Zura të hapësirës së punës tende.

Instalimi i LibreOffice mbi Fedora, openSUSE, Mandriva dhe sisteme të tjera Linux që përdorin paketa RPM
----------------------------------------------------------------------

Për udhëzime për instalimin e një pakete gjuhe (pas instalimit të versionit anglisht US të LibreOffice), lexo pjesën e mëposhtme të titulluar Instalimi i një pakete gjuhe.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Dosja përmban një nëndosje të quajtur "RPMS". Shko tek dosja "RPMS".

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

For Fedora-based systems: sudo dnf install *.rpm

Për sistemet e bazuara mbi Mandriva: sudo urpmi *.rpm

Për sistemet tjera të bazuara mbi RPM (openSUSE, etj.): rpm -Uvh *.rpm

Procesi i instalimit tashmë u plotësua, dhe duhet të kesh ikonat për të gjitha programet e LibreOffice në menynë Programet/Zura të hapësirës së punës tende.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Shënime rreth integrimit të fushës së punës për distribucionet Linux jo të trajtuara në udhëzimet e mëparshme për instalimin
----------------------------------------------------------------------

Duhet të jetë e mundur të instalohet LibreOffice mbi distribucione Linux të tjera jo posaçërisht të specifikuara në këta udhëzime për instalimin. Ndryshimet kryesore që mund të hasen janë në integrimin me hapësirën e punës.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Instalimi i një pakete gjuhe
----------------------------------------------------------------------

Shkarko paketën për gjuhën dhe platformën e dëshiruar. Ato kanë të njëjtën vendndodhje me arkivin e instalimit kryesor. Nga menaxheri i skedarëve Nautilus, nxirr arkivat e shkarkuar në një dosje (në hapësirën e punës tënde, për shembull). Sigurohu të kesh mbyllur të gjitha programet e LibreOffice (përfshirë QuickStarter, nëse është i nisur).

Zhvendosu në dosjen në të cilën ke nxjerr paketën e gjuhës së shkarkuar.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Tani zhvendosu në dosjen që përmban paketat e instalimit. Në sistemet e bazuara mbi Debian/Ubuntu, dosja do jetë DEBS. Në sistemet Fedora, openSUSE ose Mandriva, dosja do jetë RPMS.

Nga menaxheri i skedarëve Nautilus, bëj klik të djathtë në dosjen dhe zgjidh komandën "Hap në terminal". Në dritaren e terminalit që sapo hape, ekzekuto komandën për të instaluar paketën e gjuhës (mund të të kërkohet fjalëkalimi i administratorit për të gjitha komandat e mëposhtme):

Për sistemet e bazuara mbi Debian/Ubuntu: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Për sistemet e bazuara mbi Mandriva: sudo urpmi *.rpm

Për sistemet tjera që përdorin RPM (openSUSE, etj.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Pasi të kesh përshtatur këta rregullime, shtyp OK. Dialogu do të mbyllet, dhe do të shohësh një masazh informativ me ndryshimet që do të zbatohen vetëm pasi të mbyllësh dhe ta rinisësh përsëri LibreOffice (kujtohu gjithashtu të mbyllësh edhe QuickStarter nëse është i nisur).

Herën tjetër që do nisësh LibreOffice, do të niset në gjuhën e sapo instaluar.

----------------------------------------------------------------------
Probleme gjatë nisjes së programit
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
ALPS/Synaptics notebook touchpads in Windows
----------------------------------------------------------------------

Due to a Windows driver issue, you cannot scroll through LibreOffice documents when you slide your finger across an ALPS/Synaptics touchpad.

To enable touchpad scrolling, add the following lines to the "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" configuration file, and restart your computer:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Vendndodhje e skedarit të konfigurimit mund të ndryshojë mbi versione të ndryshme të Windows-it.

----------------------------------------------------------------------
Tastet përshpejtuese
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Informata të shënimeve të dokumentit
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
User Support
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
Reporting Bugs & Issues
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
Si të bashkëpunosh
----------------------------------------------------------------------

Komuniteti i LibreOffice do mund të përfitojë shumë nga pjesëmarrja jote aktive në zhvillimin e këtij projekti të rëndësishëm me burim të hapur.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

Kliko këtu për të filluar
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Subscribe
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* News: announce@documentfoundation.org *recommended to all users* (light traffic)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* Lista e përgjithshme për zhvilluesit: libreoffice@lists.freedesktop.org (shumë trafik)

Joining one or more Projects
----------------------------------------------------------------------

You can make major contributions to this important open source project even if you have limited software design or coding experience. Yes, you!

Shpresojmë të të pëlqejë të punosh me versionin e ri të LibreOffice 26.2 dhe shpresojmë që do të bashkohesh me ne në linjë.

Komuniteti i LibreOffice

----------------------------------------------------------------------
Burimi i kodit i përdorur / ndryshuar
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
