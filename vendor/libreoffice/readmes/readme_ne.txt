
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


यस readme फाइलमा भएका नयाँ अपडेटहरु हेर्नका लागि https://git.libreoffice.org/core/tree/master/README.md हेर्नुहोस्

यो फाइलमा LibreOffice सफ्टवेयरको बारेमा महत्वपूर्ण सूचना समावेश छ । स्थापना गर्न अगि यो जानकारी ध्यानपूर्वक पढ्नुहोस् भनेर तपाईँलाई सिफारिस छ ।

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

के LibreOffice कुनै पनि प्रयोगकर्ताको लागि स्वतन्त्र छ ?
----------------------------------------------------------------------

LibreOffice प्रयोग गर्नलाई सबै प्रयोगकर्तालाई स्वतन्त्र छ । तपाईँले यस LibreOffice लाई कुनै पनि कम्प्युटरमा स्तापना गर्नुहोस्, अनि कुनै पनि कार्यको लागि (वाणिज्यिक, सरकारी, सार्वजनिक प्रशासन र शिक्षा को लागि) प्रयोग गर्नुहोस् । अझै धेरै जानकारीको लागि यस LibreOffice को इजाजतपत्र हेर्नुहोस् ।

यो LibreOffice कुनै पनि प्रयोगकर्ताको लागि स्वतन्त्र किन छ ?
----------------------------------------------------------------------

तपाईँले नि: शुल्क LibreOffice को उपयोग गर्न सक्नुहुन्छ किनभने व्यक्तिगत योगदानकर्ताहरू र कॉर्पोरेट प्रायोजहरूको डिजाइन, विकसित, परीक्षण, अनुवाद, कागजात, समर्थित, विपणन, र अरू प्रकारले LibreOffice लाई - संसारको घर र कार्यालय को लागि अग्रणी खुला स्रोत उत्पादकता सफ्टवेयर बनाउनलाई मद्दत गरेका छन् ।

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
स्थापना विषय टिप्पणी
----------------------------------------------------------------------

LibreOffice लाई पुरा प्रकार्यको निम्ति Java Runtime Environment (JRE) को हालैको संस्करण चाहिन्छ । JRE LibreOffice स्थापना प्याकेज संग उपलब्ध छैन, र अलगै स्थपना गर्नु पर्दछ ।

प्रणाली आवश्यकताहरू
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

कृपया याद राख्नुहोस् स्थापनाको लागि प्रशासक अधिकार हुन आवश्यक छ ।

Microsoft Office ढाँचाहरूको लागि पूर्वनिर्धारित अनुप्रयोगको रूपमा LibreOffice को दर्तालाई स्थापनाकर्तासँग निम्न आदेश लाइन स्विचहरू प्रयोग गरेर जबरजस्ती वा दबाउन सकिन्छ:

* REGISTER_ALL_MSO_TYPES=1 will force registration of LibreOffice as default application for Microsoft Office formats.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

कृपया सुनिश्चित गर्नुहोस् कि तपाइँसँग तपाइँको प्रणालीमा अस्थायी डाइरेक्टरीमा पर्याप्त खाली मेमोरी छ, र कृपया पढ्न, लेख्न र चलाउन पहुँच अधिकार प्रदान गरिएको छ भनेर सुनिश्चित गर्नुहोस्। स्थापना प्रक्रिया सुरु गर्नु अघि सबै अन्य कार्यक्रमहरू बन्द गर्नुहोस्।

डेबियन/उबुन्टु-आधारित लिनक्स प्रणालीहरूमा LibreOffice को स्थापना
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

यो डाइरेक्टरीले "DEBS" भनिने उपनिर्देशिका समावेश गर्दछ। डाइरेक्टरीलाई "DEBS" डाइरेक्टरीमा परिवर्तन गर्नुहोस्।

डाइरेक्टरी भित्र दायाँ क्लिक गर्नुहोस् र "टर्मिनलमा खोल्नुहोस्" छनौट गर्नुहोस्। एउटा टर्मिनल विन्डो खुल्नेछ। टर्मिनल सञ्झ्यालको कमाण्ड लाइनबाट, निम्न आदेश प्रविष्ट गर्नुहोस् (कमाण्ड कार्यान्वयन हुनु अघि तपाइँलाई तपाइँको रूट प्रयोगकर्ताको पासवर्ड प्रविष्ट गर्न प्रेरित गरिनेछ):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

स्थापना प्रक्रिया अब पूरा भएको छ, र तपाइँसँग तपाइँको डेस्कटपको एप्लिकेसन/अफिस मेनुमा सबै LibreOffice अनुप्रयोगहरूको लागि आइकनहरू हुनुपर्छ।

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

This directory contains a subdirectory called "RPMS". Change directory to the "RPMS" directory.

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

For Fedora-based systems: sudo dnf install *.rpm

For Mandriva-based systems: sudo urpmi *.rpm

For other RPM-based systems (openSUSE, etc.): rpm -Uvh *.rpm

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Notes Concerning Desktop Integration for Linux Distributions Not Covered in the Above Installation Instructions
----------------------------------------------------------------------

It should be easily possible to install LibreOffice on other Linux distributions not specifically covered in these installation instructions. The main aspect for which differences might be encountered is desktop integration.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Installing a Language Pack
----------------------------------------------------------------------

Download the language pack for your desired language and platform. They are available from the same location as the main installation archive. From the Nautilus file manager, extract the downloaded archive into a directory (your desktop, for instance). Ensure that you have exited all LibreOffice applications (including the QuickStarter, if it is started).

Change directory to the directory in which you extracted your downloaded language pack.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

From the Nautilus file manager, right-click in the directory and choose the command "Open in terminal". In the terminal window you just opened, execute the command to install the language pack (with all of the commands below, you may be prompted to enter your root user's password):

For Debian/Ubuntu-based systems: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

For Mandriva-based systems: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

After adjusting those settings, click on OK. The dialog box will close, and you will see an information message telling you that your changes will only be activated after you exit LibreOffice and start it again (remember to also exit the QuickStarter if it is started).

The next time you start LibreOffice, it will start in the language you just installed.

----------------------------------------------------------------------
कार्यक्रम सुरु गर्दा समस्याहरू
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
विन्डोजमा ALPS/Synaptics नोटबुक टचप्याडहरू
----------------------------------------------------------------------

Due to a Windows driver issue, you cannot scroll through LibreOffice documents when you slide your finger across an ALPS/Synaptics touchpad.

To enable touchpad scrolling, add the following lines to the "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" configuration file, and restart your computer:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

विन्डोजको विभिन्न संस्करणहरूमा कन्फिगरेसन फाइलको स्थान फरक हुन सक्छ।

----------------------------------------------------------------------
सर्टकट कुञ्जीहरू
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
LibreOffice बाट इमेलको रूपमा डकुमेन्टहरु पठाउँदा समस्याहरू
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
महत्त्वपूर्ण पहुँचयोग्यता नोटहरू
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
प्रयोगकर्ता सहयोग
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
बगहरू रिपोर्ट गर्दै & मुद्दाहरू
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
संलग्न हुँदैछ
----------------------------------------------------------------------

The LibreOffice Community would very much benefit from your active participation in the development of this important open source project.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

कसरी सुरु गर्ने
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

सवस्क्रिप्ट
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* समाचार: announce@documentfoundation.org *सबै प्रयोगकर्ताहरूलाई सिफारिस गरिएको* (हल्का ट्राफिक)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* सामान्य डेभलपर सूची: libreoffice@lists.freedesktop.org (भारी ट्रैफिक)

एक वा धेरै परियोजनाहरूमा सामेल हुदै
----------------------------------------------------------------------

तपाईंसँग सीमित सफ्टवेयर डिजाइन वा कोडिङ अनुभव भए तापनि तपाईंले यो महत्त्वपूर्ण खुला स्रोत परियोजनामा ठूलो योगदान गर्न सक्नुहुन्छ। हो तिमी!

We hope you enjoy working with the new LibreOffice 26.2 and will join us online.

लिब्रे अफिस समुदाय

----------------------------------------------------------------------
प्रयोग गरिएको / परिमार्जित स्रोत कोड
----------------------------------------------------------------------

अंश प्रतिलिपि अधिकार १९९८, १९९९ जेम्स क्लार्क। अंश प्रतिलिपि अधिकार १९९६, १९९८ Netscape Communications Corporation।
