
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

या फाइलमध्ये LibreOffice सॉफ्टवेअरविषयी महत्वाची माहिती समाविष्टीत आहे. प्रतिष्ठापन सुरू करण्यापूर्वी ही माहिती वाचणे शिफारसीय आहे.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

खरच LibreOffice कुठल्याही वापरकर्त्याकरीता मोफत आहे?
----------------------------------------------------------------------

सर्वांच्या वापरकरीता LibreOffice मोफत आहे. तुम्ही LibreOffice चे प्रत घेऊ शकता व असंख्य संगणकावर प्रतिष्ठापीत करू शकता, तसेच कुठल्याही पसंतीच्या कारणास्तव वापर करू शकता (व्यापारिक, शासकिय, पब्लिक ॲडमिनिस्ट्रेशन व शैक्षणिक वापर समाविष्टीत). अधिक माहितीकरीता LibreOffice डाऊनलोडसह पॅकेज केलेले परवाना मजकूर पहा.

LibreOffice कुणत्याही वापरकर्त्यासाठी मोफत का आहे?
----------------------------------------------------------------------

तुम्ही LibreOffice प्रतचे मोफत वापर करू शकता कारण वैयक्तिक सहभागी व कॉरपोरेट स्पॉनसर्स् यांनी रचना, विकास, चाचणी, भाषांतरन, दस्तऐवजीकरण, सपोर्ट, मार्कटिंग केले आहे व तसेच LibreOffice ला आज जे आहे ते बनण्यास मदत पुरवले आहे - होम व ऑफिसकरीता जगातिल अग्रभागी Open Source प्रोडक्टिविटि सॉफ्टवेअर.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
स्थापना करण्याच्या टिपां
----------------------------------------------------------------------

LibreOfficeला संपूर्ण सुविधाकरीता जावा रनटाइम एंवार्यनमेंट (JRE)च्या सर्वान नविन आवृत्तीची आवश्यकता असते. JRE हे LibreOffice प्रतिष्ठापन संकुलचे भाग नाही, त्यास वेगळे प्रतिष्ठापीत करा.

पद्धती आवश्यकता
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

प्रतिष्ठापन प्रक्रियेकरीता प्रशासन हक्क आवश्यक आहे कृपया हे लक्षात ठेवा.

Microsoft Office स्वरूप करीता प्रतिष्ठापक सह खालिल आदेश ओळ स्वीचचा वापर करून LibreOffice ची नोंदणी जबरनरित्या किंवा दुर्लक्ष नुरूप केली जाऊ शकते:

* माइक्रोसॉफ्ट ऑफिस रूपणकरीता REGISTER_ALL_MSO_TYPES=1, LibreOffice याची नोंदणी पूर्वनिर्धारीत ॲप्लिकेशन म्हणून शक्य करतो.
* माइक्रोसॉफ्ट ऑफिस रूपणकरीता REGISTER_NO_MSO_TYPES=1, LibreOffice याची नोंदणी पूर्वनिर्धारीत ॲप्लिकेशन म्हणून अशक्य करतो.

कृपया प्रणालीवरील तात्पुर्ते डिरेक्ट्रीमध्ये अतिरीक्त मोकळी जागा आहे याची खात्री करा, व कृपया वाचन, लेखन व चालवायच्या परवानगी प्रदान केले आहे याची खात्री करा. प्रतिष्ठापन प्रक्रिया सुरू करण्यापूर्वी इतर सर्व प्रोग्राम्स् बंद करा.

Debian/Ubuntu-आधारीत Linux प्रणालींवरील LibreOffice चे प्रतिष्ठापन
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

या डिरेक्ट्रीमध्ये "DEBS" नावाची उपडिरेक्ट्री समाविष्टीत आहे. डिरेक्ट्रीला "DEBS" डिरेक्ट्रीकरीता बदला.

डिरेक्ट्री अंतर्गत ऊजवी-क्लिक द्या व "टर्मिनलमध्ये उघडा" नीवडा. टर्मिनल पटल उघडले जाईल. टर्मिनल पटलच्या आदेश ओळपासून, खालील आदेश द्या (आदेश चालवण्यापूर्वी रूट वापरकर्त्याचे पासवर्ड देण्यास विनंती केली जाईल):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

प्रतिष्ठापन प्रक्रिया आत्ता पूर्ण झाली, व डेस्कटॉपमधील ॲप्लिकेशन्स्/ऑफिस मेन्यूतील सर्व LibreOffice ॲप्लिकेशन्सकरीता चिन्हे असायला हवे.

RPM संकुलांचा वापर करून Fedora, openSUSE, Mandriva व इतर Linux प्रणालींवरील LibreOfficeचे इंस्टॉलेशन
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

या डिरेक्ट्रीत "RPMS" नावाची उपडिरेक्ट्री समाविष्टीत आहे. डिरेक्ट्रीला "RPMS" डिरेक्ट्रीकरीता बदला.

डिरेक्ट्री अंतर्गत ऊजवी-क्लिक द्या व "टर्मिनलमध्ये उघडा" नीवडा. टर्मिनल पटल उघडले जाईल. टर्मिनल पटलच्या आदेश ओळपासून, खालील आदेश द्या (आदेश चालवण्यापूर्वी रूट वापरकर्त्याचे पासवर्ड देण्यास विनंती केली जाईल):

For Fedora-based systems: sudo dnf install *.rpm

Mandriva-आधारीत प्रणालींकरीता: sudo urpmi *.rpm

इतर RPM-आधारित प्रणालींकरिता (openSUSE, इत्यादि): rpm -Uvh *.rpm

प्रतिष्ठापन प्रक्रिया आत्ता पूर्ण झाली, व डेस्कटॉपमधील ॲप्लिकेशन्स्/ऑफिस मेन्यूतील सर्व LibreOffice ॲप्लिकेशन्सकरीता चिन्हे असायला हवे.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

वरील प्रतिष्ठापन सूचनांमध्ये Linux डिस्ट्रिब्यूशन्स् करीता डेस्कटॉप एकीकरण संबंधीत टिपण्णी समाविष्टीत नाही
----------------------------------------------------------------------

या प्रतिष्ठापन सूचनांमध्ये विशेषतया समाविष्ट नसलेल्या इतर Linux वितरणांवर LibreOffice प्रतिष्ठापीत करणे सहज शक्य व्हायला हवे. मुख्य पैलू ज्याकरीता मतभेद आढळू शकतात ते डेस्कटॉप एकीकरण आहे.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

लँगवेज पॅक प्रतिष्ठापीत करत आहे
----------------------------------------------------------------------

पसंतीच्या भाषा व प्लॅटफॉर्मकरीता लँगवेज पॅक डाऊनलोड करा. समान ठिकाणपासून मुख्य प्रतिष्ठापन आर्काइव्ह म्हणून उपल्बध होतात. Nautilus फाइल व्यवस्थापकातून, डाऊनलोड केलेल्या आर्काइव्हला डिरेक्ट्रीत काढा (उदाहरणार्थ, तुमचे डेस्कटॉप). सर्व LibreOffice ॲप्लिकेशन्स् बंद केल्याची खात्री करा (QuickStarter समाविष्टीत, सुरू केले असल्यास).

डिरेक्ट्रीला डाऊनलोड केलेल्या भाषा संकुलातील डिरेक्ट्रीकरीता बदलवा.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

आत्ता इंस्टॉलकरिता आवश्यक संकुल असणाऱ्या डिरेक्ट्रि ते डिरेक्ट्रिचा वापर करा. Debian किंवा Ubuntu-आधारीत प्रणालींवर, डिरेक्ट्रि DEBS असेल. Fedora, openSUSE किंवा Mandriva प्रणालींवर, डिरेक्ट्रि RPMS असेले.

Nautilus फाइल व्यवस्थापकापासून, डिरेक्ट्रीमध्ये ऊजवी-क्लिक द्या व आदेश "टर्मिनलमध्ये उघडा" नीवडा. नकतेच उघडलेल्या टर्मिनल पटलात लँगवेज पॅक प्रतिष्ठापीत करण्यासाठी आदेश चालवा (सर्व खालील आदेशांसह, रूट वापरकर्त्याचे पासवर्ड देण्यास विनंती केली जाईल):

Debian/Ubuntu-आधारीत प्रणालींकरीता: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Mandriva-आधारीत प्रणालींकरीता: sudo urpmi *.rpm

इतर RPM-आधारित प्रणालींकरिता (openSUSE, इत्यादि): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

संरचना समायोजीत केल्यानंतर, OK वर क्लिक करा. संवाद पेटी बंद होईल, व LibreOffice पासून बाहेर पडल्यावर व पुन्हा सुरू केल्यावरच बदल लागू होतील असा माहिती संदेश आढळेल (QuickStarter सुरू असल्यास बंद करायला विसरू नका).

LibreOffice ला पुढे सुरू केल्यास, ते नुकतेच प्रतिष्ठापीत केलेल्या भाषेत सुरू होईल.

----------------------------------------------------------------------
आज्ञावलीं सुरू होतेवेळी समस्या
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
विन्डोजमधील ALPS/सिनॅपटीक वही टचपॅड
----------------------------------------------------------------------

विन्डोजच्या ड्राईवर मुद्दयामुळे, जेव्हा आपण आपले बोट ALPS/सिनॅपटीक टचपॅडमधून हलवता तेव्हा LibreOffice दस्तऐवजांमधून आपण सरकवू शकत नाही.

टचपॅड स्क्रोलिंगला सक्षम करण्यासाठी, पुढील ओळींना "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" संयोजना फाइलमध्ये समाविष्ट करा, व संगणकाला पुनः सुरू करा:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

संरचना फाइलचे स्थान Windows वरील वेगळ्या आवृत्तींकरीता वेगळे असू शकतात.

----------------------------------------------------------------------
जवळच्या मार्गाच्या कीज
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
महत्वाचे सुलभता टिप
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
वापरकर्त्याचा आधार
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
बग्स् & अडचणी कळवत आहे
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
सहभागी व्हा
----------------------------------------------------------------------

LibreOffice समुदायास या महत्वाच्या खुल्या स्त्रोत प्रकल्पाच्या विकासात आपल्या सक्रिय सहभाग घेण्याचा खूपच फायदा होईल.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

सुरू कसे करायचे
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

सभासद व्हा
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* समाचार: announce@documentfoundation.org *सर्व वापरकर्त्यांसाठी शिफारसीय* (हलके ट्राफिक)
* मुख्य वारकर्ता सूची: users@global.libreoffice.org *चर्चासह जुडण्याचे सोपे पर्याय* (जास्त ट्राफिक)
* व्यापार प्रकल्प: marketing@global.libreoffice.org *विकासाच्या पलिकडे* (जास्त ट्राफिक)
* सर्वसाधारण डेव्हलपर सूची: libreoffice@lists.freedesktop.org (जास्त ट्राफिक)

एक किंवा त्यापेक्षा जास्त प्रकल्पांमध्ये सामिल होत आहे
----------------------------------------------------------------------

मर्यादीत सॉफ्टवेअर रचना किंवा कोडींग अनुभव असल्यावरही तुम्हील या महत्वाचे ओपन सोअर्स प्रकल्पात मुख्य योगदान करू शकता. होय, तुम्ही!

नवीन LibreOffice 26.2 बरोबर काम करताना आपल्याला आनंद वाटला अशी आम्ही आशा करतो आणि आपण चालू असताना आमच्यात सामिल व्हाल.

LibreOffice समूह

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
