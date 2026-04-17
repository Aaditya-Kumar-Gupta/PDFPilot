
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

Diese Datei enthält wichtige Informationen zur Software LibreOffice. Es wird empfohlen, diese Informationen aufmerksam zu lesen, bevor Sie die Installation starten.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

Ist LibreOffice tatsächlich für jeden Anwender frei?
----------------------------------------------------------------------

LibreOffice darf von jedem frei verwendet werden. Sie können diese Kopie von LibreOffice auf beliebig vielen Computern installieren und für beliebige Zwecke verwenden (einschließlich kommerzielle Nutzung, öffentliche Verwaltung und Bildung). Für weitere Informationen lesen Sie bitte den Lizenztext, der im LibreOffice-Download enthalten ist.

Warum ist LibreOffice für jeden Anwender frei?
----------------------------------------------------------------------

Sie können diese Kopie von LibreOffice kostenlos benutzen, weil einzelne Beitragende und Firmensponsoren die Software entwerfen, entwickeln, testen, übersetzen, dokumentieren, unterstützen, vermarkten und auf verschiedene Weise dazu beitragen, LibreOffice zu dem zu machen, was es heute ist - die führende Open Source Office-Software für Heim- und Firmenanwender.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Notes on Installation
----------------------------------------------------------------------

LibreOffice requires a recent version of Java Runtime Environment (JRE) for full functionality. JRE is not part of the LibreOffice installation package, it should be installed separately.

System Requirements
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Please be aware that administrator rights are needed for the installation process.

Registration of LibreOffice as default application for Microsoft Office formats can be forced or suppressed by using the following command line switches with the installer:

* REGISTER_ALL_MSO_TYPES=1 will force registration of LibreOffice as default application for Microsoft Office formats.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

Bitte stellen Sie sicher, dass genügend freier Speicherplatz im temporären Verzeichnis Ihres Systems vorhanden ist und dass Schreib-, Lese- und Ausführungsrechte gesetzt sind. Schließen Sie alle laufenden Programme, bevor Sie mit der Installation beginnen.

Installation von LibreOffice auf Debian/Ubuntu-basierten Linuxsystemen
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Dieses Verzeichnis enthält ein Unterverzeichnis "DEBS". Wechseln Sie in das Verzeichnis "DEBS".

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Dieses Verzeichnis enthält ein Unterverzeichnis "RPMS". Wechseln Sie in das Verzeichnis "RPMS".

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

For Fedora-based systems: sudo dnf install *.rpm

For Mandriva-based systems: sudo urpmi *.rpm

For other RPM-based systems (openSUSE, etc.): rpm -Uvh *.rpm

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Hinweise bezüglich der Desktopintegration für Linuxdistributionen, die in den Installationshinweisen nicht gesondert betrachtet wurden
----------------------------------------------------------------------

Es sollte recht einfach sein, LibreOffice auf hier nicht spezifisch betrachteten Linux-Distributionen zu installieren. Unterschiede könnten sich hauptsächlich bei der Desktopintegration ergeben.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Installation eines Sprachpakets
----------------------------------------------------------------------

Laden Sie das Sprachpaket für die gewünschte Sprache und Plattform herunter. Diese sind am gleichen Ort wie das Basis-Installationspaket verfügbar. Entpacken Sie das heruntergeladene Paket über einen Dateimanager in ein beliebiges Verzeichnis (zum Beispiel auf Ihren Arbeitsplatz). Beenden Sie alle LibreOffice-Anwendungen (einschließlich des Schnellstarters, falls gestartet).

Wechseln Sie in das Verzeichnis, in das Sie das Paket entpackt haben.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

Rechtsklicken Sie im Dateimanager im Verzeichnis und wählen "Im Terminal öffnen". Führen Sie in der Eingabeaufforderung den Befehl zum Installieren des Sprachpaketes aus (alle unten aufgeführten Kommandos werden wahrscheinlich nach Ihrem root-Passwort fragen):

Für Debian/Ubuntu-basierte Systeme: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

For Mandriva-based systems: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Nachdem Sie diese Einstellungen vorgenommen haben, klicken Sie OK. Der Dialog wird geschlossen und Sie sehen einen Hinweis, dass die Änderungen erst nach einem Neustart von LibreOffice aktiviert werden (denken Sie daran, auch den Schnellstarter zu beenden, sofern er aktiviert ist).

Beim nächsten Start von LibreOffice wird es in der gerade installierten Sprache starten.

----------------------------------------------------------------------
Problems During Program Startup
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

The location of the configuration file might vary on different versions of Windows.

----------------------------------------------------------------------
Shortcut Keys
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Important Accessibility Notes
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
Getting Involved
----------------------------------------------------------------------

The LibreOffice Community would very much benefit from your active participation in the development of this important open source project.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

How to Start
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Subscribe
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* Neuigkeiten: announce@de.libreoffice.org - Für alle Anwender empfohlen (niedriges Mailaufkommen)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* Generelle Entwicklerliste: libreoffice@lists.freedesktop.org (hohes Mailaufkommen, Englisch)

Einem oder mehreren Projekten beitreten
----------------------------------------------------------------------

You can make major contributions to this important open source project even if you have limited software design or coding experience. Yes, you!

We hope you enjoy working with the new LibreOffice 26.2 and will join us online.

Die LibreOffice-Community

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
