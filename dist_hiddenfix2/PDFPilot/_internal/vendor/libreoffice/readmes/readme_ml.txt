
======================================================================
LibreOffice 26.2 റീഡ്മീ
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

LibreOffice സോഫ്റ്റ്‌വെയര്‍ സംബന്ധിച്ചുള്ള പ്രധാന വിവരങ്ങള്‍ ഈ ഫയലില്‍ അടങ്ങുന്നു. ഇന്‍സ്റ്റലേഷന്‍ ആരംഭിയ്ക്കുന്നതിനു് മുമ്പായി ദയവായി ഈ വിവരങ്ങള്‍ സൂക്ഷിച്ചു് വായിയ്ക്കുക.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

ഏതു് ഉപയോക്താവിനും LibreOffice സ്വതന്ത്രമായി ഉപയോഗിയ്ക്കുവാന്‍ സാധിയ്ക്കുമോ?
----------------------------------------------------------------------

LibreOffice ഏവര്‍ക്കും സൌജന്യമായി ലഭ്യമാകുന്നു. LibreOffice-ന്റെ ഒരു പകര്‍പ്പു് ലഭ്യമാക്കി എത്ര കമ്പ്യൂട്ടറുകളില്‍ വേണമെങ്കിലും ഇന്‍സ്റ്റോള്‍ ചെയ്യാം. നിങ്ങള്‍ക്കു് ആവശ്യമുള്ള രീതിയില്‍ ഇതു് ഉപയോഗിയ്ക്കാം. ഉദാഹരണത്തിനു്, ഗവണ്മെന്റ്, പബ്ലിക്, അഡ്മിനിസ്ട്രേഷന്‍, പഠനം. കൂടുതല്‍ വിവരങ്ങള്‍ക്കായി LibreOffice ഡൌണ്‍ലോഡിനൊപ്പമുള്ള ലൈസന്‍സ് ടെക്സ്റ്റ് കാണുക.

ഏതു് ഉപയോക്താവിനും LibreOffice എന്തുകൊണ്ട് സ്വതന്ത്യമാണു്?
----------------------------------------------------------------------

You can use this copy of LibreOffice free of charge because individual contributors and corporate sponsors have designed, developed, tested, translated, documented, supported, marketed, and helped in many other ways to make LibreOffice what it is today - the world's leading Open Source productivity software for home and office.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
സ്ഥാപിക്കുന്നതിനുള്ള കുറിപ്പുകള്
----------------------------------------------------------------------

LibreOffice-നു് പൂര്‍ണ്ണ പ്രവര്‍ത്തനത്തിനു് ജാവാ റണ്‍ടൈം എന്‍വയണ്മെന്റിന്റെ (ജെആര്‍ഇ) പുതിയ പതിപ്പു് ആവശ്യമുണ്ടു്. ജെആര്‍ഇ LibreOffice ഇന്‍സ്റ്റലേഷന്‍ പാക്കേജിന്റെ ഭാഗമല്ല, ഇതു് വേറെ ഇന്‍സ്റ്റോള്‍ ചെയ്യേണ്ടതുണ്ടു്.

സിസ്റ്റത്തിന‌് ആവശ്യമായത്:
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

ഇന്‍സ്റ്റലേഷന്‍ പ്രക്രിയയ്ക്കു് അഡ്മിസിസ്ട്റേറ്റീവ് ആധികാരികതകള്‍ ആവശ്യമുണ്ടെന്നു് ദയവായി മനസ്സിലാക്കുക.

Registration of LibreOffice as default application for Microsoft Office formats can be forced or suppressed by using the following command line switches with the installer:

* മൈക്രോസോഫ്റ്റ് ഓഫീസ് ഫോര്‍മാറ്റുകള്‍ക്കു് സ്വതവേയുള്ള പ്രയോഗമായി LibreOffice രജിസ്ടര്‍ ചെയ്യുന്നതു് REGISTER_NO_MSO_TYPES=1 നിര്‍ബന്ധിയ്ക്കുന്നു.
* മൈക്രോസോഫ്റ്റ് ഓഫീസ് ഫോര്‍മാറ്റുകള്‍ക്കു് സ്വതവേയുള്ള പ്രയോഗമായി LibreOffice രജിസ്ടര്‍ ചെയ്യുന്നതു് REGISTER_NO_MSO_TYPES=1 തടയുന്നു.

Please make sure you have enough free memory in the temporary directory on your system, and please ensure that read, write and run access rights have been granted. Close all other programs before starting the installation process.

Installation of LibreOffice on Debian/Ubuntu-based Linux systems
----------------------------------------------------------------------

ഒരു ഭാഷയ്ക്കാവശ്യമായ പാക്കുകള്‍ ഇന്‍സ്റ്റോള്‍ ചെയ്യുന്നതിനായി (LibreOffice-ന്റെ യുഎസ് ഇംഗ്ലീഷ് പതിപ്പു് ഇന്‍സ്റ്റോള്‍ ചെയ്ത ശേഷം), ഒരു ഭാഷയ്ക്കുള്ള പാക്ക് ഇന്‍സ്റ്റോള്‍ ചെയ്യുക എന്ന ഭാഗം വായിയ്ക്കുക.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

This directory contains a subdirectory called "DEBS". Change directory to the "DEBS" directory.

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

ആര്‍പിഎം പാക്കേജുകള്‍ ഉപയോഗിയ്ത്തു് ഫെഡോറാ, ഓപ്പണ്‍സുസേ, മാന്‍ഡ്രിവാ, മറ്റു് പല ലിനക്സ് സിസ്റ്റങ്ങളിലും LibreOffice-ന്റെ ഇന്‍സ്റ്റലേഷന്‍
----------------------------------------------------------------------

ഒരു ഭാഷയ്ക്കാവശ്യമായ പാക്കുകള്‍ ഇന്‍സ്റ്റോള്‍ ചെയ്യുന്നതിനായി (LibreOffice-ന്റെ യുഎസ് ഇംഗ്ലീഷ് പതിപ്പു് ഇന്‍സ്റ്റോള്‍ ചെയ്ത ശേഷം), ഒരു ഭാഷയ്ക്കുള്ള പാക്ക് ഇന്‍സ്റ്റോള്‍ ചെയ്യുക എന്ന ഭാഗം വായിയ്ക്കുക.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

This directory contains a subdirectory called "RPMS". Change directory to the "RPMS" directory.

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

For Fedora-based systems: sudo dnf install *.rpm

മാന്‍ഡ്രിവാ സിസ്റ്റങ്ങള്‍ക്കു്: sudo urpmi *.rpm

മറ്റു് ആര്‍പിഎം സിസ്റ്റങ്ങള്‍ക്കു്: (ഓപ്പണ്‍സുസേ, എന്നിവ.): rpm -Uvh *.rpm

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Notes Concerning Desktop Integration for Linux Distributions Not Covered in the Above Installation Instructions
----------------------------------------------------------------------

It should be easily possible to install LibreOffice on other Linux distributions not specifically covered in these installation instructions. The main aspect for which differences might be encountered is desktop integration.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

ഒരു ഭാഷയ്ക്കുള്ള പാക്ക് ഇന്‍സ്റ്റോള്‍ ചെയ്യുന്നു
----------------------------------------------------------------------

Download the language pack for your desired language and platform. They are available from the same location as the main installation archive. From the Nautilus file manager, extract the downloaded archive into a directory (your desktop, for instance). Ensure that you have exited all LibreOffice applications (including the QuickStarter, if it is started).

Change directory to the directory in which you extracted your downloaded language pack.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

ഇന്‍സ്റ്റോള്‍ ചെയ്യുവാനുള്ള  പാക്കേജുകളുള്ള ഡയറക്ടറിയിലേക്കു് ഡയറക്ടറി മാറ്റുക. ഡെബിയന്‍/ഉബുന്ദു സിസ്റ്റങ്ങളില്‍, DEBS ആകുന്ന ഡയറക്ടറി. ഫെഡോറാ, ഓപ്പണ്‍സുസേ, അല്ലെങ്കില്‍ മാന്‍ഡ്രിവൈ സിസ്റ്റങ്ങളില്‍  RPMS ആകുന്നു ഡയറക്ടറി.

From the Nautilus file manager, right-click in the directory and choose the command "Open in terminal". In the terminal window you just opened, execute the command to install the language pack (with all of the commands below, you may be prompted to enter your root user's password):

ഡെബിയന്‍/ഉബുന്തു സിസ്റ്റങ്ങള്‍ക്കു്: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

മാന്‍ഡ്രിവാ സിസ്റ്റങ്ങള്‍ക്കു്: sudo urpmi *.rpm

ആര്‍പിഎം ഉപയോഗിയ്ക്കുന്ന മറ്റു് സിസ്റ്റങ്ങള്‍ക്കു് (ഓപ്പണ്‍സുസേ എന്നി‌വ.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

After adjusting those settings, click on OK. The dialog box will close, and you will see an information message telling you that your changes will only be activated after you exit LibreOffice and start it again (remember to also exit the QuickStarter if it is started).

അടുത്ത തവണ LibreOffice ആരംഭിയ്ക്കുമ്പോള്‍, നിങ്ങള്‍ ഇന്‍സ്റ്റോള്‍ ചെയ്ത ഭാഷയില്‍ ഇതു് ആരംഭിയ്ക്കുന്നു.

----------------------------------------------------------------------
പ്രോഗ്രാം സജ്ജമാക്കുന്നതിലുള്ള പ്രശ്നങ്ങള്‍
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
ALPS/ സിനാപ്ടിക് നോട്ട്ബുക്ക് ടച്ച്പാഡ് വിന്ഡോയില്.
----------------------------------------------------------------------

വിന്‍ഡോസ് ഡ്രൈവറിന്റെ പ്രശ്നം കാരണം, താങ്കളുടെ വിരലുകള് ALPS/സിനാപ്ടിക് ടച്ച്പാഡില്‍ ഇരിക്കുമ്പോള്‍ താങ്കള്‍ക്ക് LibreOffice ഡോക്കുമെന്റുകളിലൂടെ സ്ക്രോള് ചെയ്യാന്‍ കഴിയില്ല.

ടച്ച്പാഡ് സ്ക്രോലിങ്ങ് പ്രവര്‍ത്തന സജ്ജമാക്കുാന്‍, താഴെ തന്നിരിക്കുന്ന വരികള്‍ "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" ഫയലില്‍ ചേര്‍ത്ത്, കമ്പ്യൂട്ടര്‍ ഓഫാക്കി, വിണ്ടും തുടങ്ങുക:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

കുറിപ്പ് - രൂപരേഖ ചെയ്ത് ഫയലിന്റെ ലൊക്കേഷന്  വിന്ഡോകളുടെ പരിഭാഷ അനുസരിച്ച് മാറും.

----------------------------------------------------------------------
എളുപ്പ പ്രയോഗ കീകള്
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
പ്രധാനപ്പെട്ട ആക്സബിളിറ്റി കുറിപ്പുകള്‍
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
ഉപഭോക്തൃ പിന്താങ്ങ്
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
ബഗുകള്‍ & പ്രശ്നങ്ങള്‍ രേഖപ്പെടുത്തല്‍
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
ഉള്പ്പെടുക
----------------------------------------------------------------------

LibreOffice സമൂഹത്തില്‍ താങ്കളുടെ സജീവമായ പങ്കാളിത്തം വളരെയധികം ഗുണകരമാണ‌്.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

എങ്ങനെ ആരംഭിയ്ക്കണം
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

അംഗമാകുക
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* വാര്‍ത്തകള്‍: announce@documentfoundation.org *എല്ലാ ഉപയോക്താക്കള്‍ക്കും ഉത്തമം* 
* പ്രധാന ഉപയോക്തൃ പട്ടിക: users@global.libreoffice.org *ചര്‍ച്ചകള്‍ക്കു്*
* മാര്‍ക്കറ്റിങ് സംരംഭം: marketing@global.libreoffice.org *ഡവലപ്പ്മെന്റില്‍ കൂടുതല്‍* 
* സാധാരണ ഡവലപ്പര്‍ പട്ടിക: libreoffice@lists.freedesktop.org 

ഒന്നില്‍ കൂടുതല്‍ സംരംഭങ്ങളില്‍ പങ്കു് ചേരുക
----------------------------------------------------------------------

You can make major contributions to this important open source project even if you have limited software design or coding experience. Yes, you!

താങ്കള്‍ LibreOffice 26.2 ജോലി ചെയ്യുന്നത് ആസ്വദിക്കുന്നുവെന്നും പിന്നെ ഞങ്ങളുടെ കൂടെ ഓണ്‍ലൈനില് ചേരുമെന്നും ഞങ്ങള്‍ കരുതുന്നു.

ലിബര്‍ഓഫീസ് കൂട്ടായ്മ

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
