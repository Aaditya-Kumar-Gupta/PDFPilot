
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


Ари афаил аҵыхәтәантәи аверсиа адрес: https://git.libreoffice.org/core/tree/master/README.md

Ари афаил иаҵанакуеит LibreOffice иазку, ихәарҭоу аинформациа. Ақәыргылара аԥхьа ари аинформациа аԥхьара рекомендациоуп.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

LibreOffice ахы иақәиҭума ахархәаҩцәа зегьы рзы?
----------------------------------------------------------------------

LibreOffice зегьы рзы ихәыда-ԥсадоуп. LibreOffice ари акопиа заҟа шәҭаху акомпиутерқәа рҟны иқәшәыргылар ҟалоит, иарбан хықәкызаалак азы шәхы иашәырхәар ҟалоит (акоммерциатә, аҳәынҭқарратә, административтә, арҵаратә). Еиҳа инарҭбаау аинформациа шәахә. LibreOffice иацу алицензиатә еиқәышаҳаҭра атекст аҟны.

Избан LibreOffice зхәыда-ԥсадоу ахархәаҩцәа зегьы рзы?
----------------------------------------------------------------------

You can use this copy of LibreOffice free of charge because individual contributors and corporate sponsors have designed, developed, tested, translated, documented, supported, marketed, and helped in many other ways to make LibreOffice what it is today - the world's leading Open Source productivity software for home and office.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Ақәыргылараз аҵаҳәарақәа
----------------------------------------------------------------------

LibreOffice афункциақәа зегьы рхархәаразы иаҭахуп Java Runtime Environment (JRE) аҵыхәтәантәи аверсиа. JRE ақәыргыларатә пакет LibreOffice иаҵанакӡом, хазы иқәыргылатәуп.

Асистематә ҭахрақәа
----------------------------------------------------------------------

* Microsoft Windows 10 ма еиҳау аверсиа

Азгәаҭа: ақәыргылара анагӡараз ихымԥадатәиуп администратор изинқәа.

Registration of LibreOffice as default application for Microsoft Office formats can be forced or suppressed by using the following command line switches with the installer:

* REGISTER_ALL_MSO_TYPES=1 арегистрациа ҟаҵатәуп LibreOffice Microsoft Office аформатқәа рзы апрограмма хада аҳасабала.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

Please make sure you have enough free memory in the temporary directory on your system, and please ensure that read, write and run access rights have been granted. Close all other programs before starting the installation process.

LibreOffice Debian/Ubuntu-иашьашәалоу Linux аҟны ақәыргылара
----------------------------------------------------------------------

Абызшәатә пакет ақәыргылара иазку аинструкциа (иқәыргылоу англыз ахыхь (US English) аверсиа LibreOffice) ыҟоуп Абызшәатә пакет ақәыргылара иазку аҟәша аҟны.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Акаталог иаҵанакуеит акаталоггәыла «DEBS» хьӡыс измоу. Шәыиас акаталог «DEBS» ахь.

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Уажәшьҭа ақәыргылара апроцесс хыркәшоуп, асистематә мениу Апрограммақәа/Аофис аҟны ицәырҵроуп LibreOffice апрограммақәа рдәықәҵара иазку адыгаҷқәа.

RPM-апакетқәа рхархәарала Fedora, openSUSE, Mandriva, егьырҭ Linux асистемақәеи рҟны LibreOffice ақәыргылара
----------------------------------------------------------------------

Абызшәатә пакет ақәыргылара иазку аинструкциа (иқәыргылоу англыз ахыхь (US English) аверсиа LibreOffice) ыҟоуп Абызшәатә пакет ақәыргылара иазку аҟәша аҟны.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Акаталог иаҵанакуеит акаталогеиҵа «RPMS». Шәыиас акаталог «RPMS» ахь.

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

Fedora-иашьашәалоу асистемақәа рзы: sudo dnf install *.rpm

Mandriva-иашьашәалоу асистемақәа рзы: sudo urpmi *.rpm

Егьырҭ RPM-асистемақәа рзы (openSUSE -и егь.-и): rpm -Uvh *.rpm

Уажәшьҭа ақәыргылара апроцесс хыркәшоуп, асистематә мениу Апрограммақәа/Аофис аҟны ицәырҵроуп LibreOffice апрограммақәа рдәықәҵара иазку адыгаҷқәа.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Notes Concerning Desktop Integration for Linux Distributions Not Covered in the Above Installation Instructions
----------------------------------------------------------------------

It should be easily possible to install LibreOffice on other Linux distributions not specifically covered in these installation instructions. The main aspect for which differences might be encountered is desktop integration.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Абызшәатә пакет ақәыргылара
----------------------------------------------------------------------

Download the language pack for your desired language and platform. They are available from the same location as the main installation archive. From the Nautilus file manager, extract the downloaded archive into a directory (your desktop, for instance). Ensure that you have exited all LibreOffice applications (including the QuickStarter, if it is started).

Шәыиас акаталог, зҟны, иҭажәгалаз абызшәатә пакет хшәыртлаз.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Уажәшьҭа шәыиас ақәыргылара иазку апакетқәа ркаталог ахь. Асистемақәа Debian/Ubuntu рҟны акаталог иахьӡуп DEBS. Fedora, openSUSE ма Mandriva рҟны акаталог иахьӡуп RPMS.

From the Nautilus file manager, right-click in the directory and choose the command "Open in terminal". In the terminal window you just opened, execute the command to install the language pack (with all of the commands below, you may be prompted to enter your root user's password):

Debian/Ubuntu-иашьашәалоу асистемақәа рзы: sudo dpkg -i *.deb

Fedora-иашьашәалоу асистемақәа рзы: su -c 'dnf install *.rpm'

Mandriva-иашьашәалоу асистемақәа рзы: sudo urpmi *.rpm

Егьырҭ RPM-асистемақәа рзы (openSUSE -и егь.-и): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

After adjusting those settings, click on OK. The dialog box will close, and you will see an information message telling you that your changes will only be activated after you exit LibreOffice and start it again (remember to also exit the QuickStarter if it is started).

LibreOffice анаҩстәи адәықәҵараан иаатуеит ҿыц иқәшәыргылаз абызшәа ала.

----------------------------------------------------------------------
Апрограмма адәықәҵараан апроблемақәа
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Ноутбукқәа ALPS/Synaptic Windows аҟны рсенсортә панельқәа
----------------------------------------------------------------------

Due to a Windows driver issue, you cannot scroll through LibreOffice documents when you slide your finger across an ALPS/Synaptics touchpad.

To enable touchpad scrolling, add the following lines to the "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" configuration file, and restart your computer:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Азгәаҭа: Windows еиуеиԥшым аверсиақәа рҟны аконфигурациатә фаил аԥыԥқәа еиԥшымхар ауеит.

----------------------------------------------------------------------
Аклавишақәа реицхархәара
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
LibreOfficeаҟынтәи адокументқәа аелектронтә шәҟәқәа раҳасабала рышьҭраан ицәырҵит апроблемақәа
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Испециалу алшарақәа ирызку ихадароу азгәаҭақәа
----------------------------------------------------------------------

LibreOffice аҟны испециалу алшарақәа ирызку иаҳа ирҭбаау аинформациа шәахәаԥш абра https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Ахархәаҩцәа рыдгылара
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Иара убасгьы шәахәаԥш ЛЛИ сайте LibreOffice аҟны.

----------------------------------------------------------------------
Агхақәеи апроблемақәеи ирызку аинформациа
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
Ахеилак аҽалархәра
----------------------------------------------------------------------

The LibreOffice Community would very much benefit from your active participation in the development of this important open source project.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

Аусеицура алагара
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Анапаҵаҩра
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* Ажәабжьқәа: announce@documentfoundation.org *ирекомендациоуп ахархәаҩцәа зегьы рзы* (имаҷу атрафик)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Амаркетингтә проект: marketing@global.libreoffice.org *аусдулара алҵшәақәа* (атрафик ду)
* General developer list: libreoffice@lists.freedesktop.org (heavy traffic)

Апроектқәа рыҽрымадара
----------------------------------------------------------------------

You can make major contributions to this important open source project even if you have limited software design or coding experience. Yes, you!

Ҳақәгәыӷуеит, LibreOffice 26.2 аҟны аусура шышәгәаԥхо, насгьы Аинтернет ахархәарала адгылара ҳашәҭап ҳәа.

LibreOffice ахеилак

----------------------------------------------------------------------
Ихархәоу/Имодификациоу ахлагаратә код
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
