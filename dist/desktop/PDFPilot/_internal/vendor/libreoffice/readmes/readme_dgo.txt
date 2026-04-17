
======================================================================
LibreOffice 26.2 रीडमी
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

इस फाइल च LibreOfficeसाफ्टवेअर दे बारे च म्हत्तवपूर्ण जानकारी ऐ.तुसेंगी सुझाया जंदा ऐ जे इंस्टालेशन शुरू करने शा पैह्‌लें इस जानकारी गी बड़े ध्यानै कन्नै पढ़ी लैओ.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

क्या LibreOffice वाक्या-ई कुसै बी बरतूनी आस्तै मुख्त ऐ?
----------------------------------------------------------------------

LibreOffice हर कुसै दे बरतने आस्तै मुख्त ऐ. तुस LibreOffice दी कापी लेई सकदे  ओ ते  ते इस्सी जिन्ने चाहो उन्ने  कंप्यूटरें पर इंस्टाल करी सकदे ओ, ते अपने कुसै बी मकसद  आस्तै इस्सी बरती सकदे ओ(बनजी, सरकारी, सार्वजनिक प्रशासन ते शैक्षणिक उपयोग). अग्गें होर मती जानकारी आस्तै LibreOffice डाउनलोड दे पैकेज दा इबारत लाइसैंस दिक्खो.

एह् LibreOffice कुसै  बी बरतूनी आस्तै मुख्त की ऐ?
----------------------------------------------------------------------

तुस इस LibreOffice दी कापी गी  मुख्त बरती सकदे ओ की जे  बक्खरे-बक्खरे योगदानकर्ताएं ते कार्पोरेट प्रायोजकें इस्सी डिजायन, विकसत, जांच, अनूदत, दस्तावेजत, मार्केटिङ करियै ते एह् LibreOfficeअज्ज जे किश  बी है,इसदे इस रूप गी बनाने च केइयें चाल्लियें दी मदद कीती.अज्ज एह्  घरें ते दफ्तरें आस्तै दुनिया दा आगू मुक्त स्रोत उत्पादकता साफ्टवेअर ऐ.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
प्रस्थापना पर नोट
----------------------------------------------------------------------

LibreOffice requires a recent version of Java Runtime Environment (JRE) for full functionality. JRE is not part of the LibreOffice installation package, it should be installed separately.

सिस्टम लोड़ां
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

कृपा करियै एह् जानी लैओ जे इंस्टालेशन प्रक्रिया आस्तै प्रशासक अधिकार लोड़चदे न.

इंस्टाल-कर्ता कन्नै निम्नलिखत कमांड लाइन स्विचें गी बरतियै माइक्रोसाफ्ट आफिस फार्मैटें आस्तै डिफाल्ट ऐपलीकेशन दे तौर परLibreOfficeदी रजिस्ट्रेशन गी जरूरी बनाया जां सप्रैस्स कीता जाई सकदा ऐ :

* REGISTER_ALL_MSO_TYPES=1 will force registration of LibreOffice as default application for Microsoft Office formats.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

कृपा करियै  एह् पक्का करी  लैओ जे थुआढ़े सिस्टम  च आरजी डायरैक्टरी च काफी मैमरी बाकी ऐ, ते  कृपा करियै  एह् पक्का करी  लैओ जे पढ़ने, लिखने ते चलाने दे पुज्ज-अधिकार दित्ते जाई चुके न. इंस्टालेशन प्रक्रिया गी शुरू करने शा पैह्‌लें  सब्भै बाकी प्रोग्राम बंद करो.

LibreOffice दा डेबियन/उबंटू आधारत लिनक्स सिस्टमें उप्पर इंस्टालेशन
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

इस डायरैक्टरी च "DEBS" नांऽ दी उप- डायरैक्टरी होंदी ऐ. डायरैक्टरी गी "DEBS" डायरैक्टरी च बदलो.

डायरैक्टरी दे अंदर सज्जा क्लिक करो ते "Open in Terminal"चुनो.इक टर्मिनल विंडो खुʼल्लग. टर्मिनल विंडो दी कमांड लाइन थमां एह् कमांड प्रविश्ट करो(कमांड दे अमल च औने शा पैह्‌लें तुसेंगी अपना बुनेआदी बरतूनी पासवर्ड पर्विश्ट करने आस्तै आखेआ जाह्‌ग ):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

इंस्टालेशन प्रक्रिया हून पूरी होई गेई ऐ, ते थुआढ़ी डैस्कटाप दियें ऐपलीकेशनें/आफिस मेन्यु च सभनेंLibreOffice ऐपलीकेशनें आस्तै आइकन होने चाहिदे.

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

इस डायरैक्टरी च "RPMS". नांऽ दी उप- डायरैक्टरी होंदी ऐ. डायरैक्टरी गी "RPMS". डायरैक्टरी च बदलो.

डायरैक्टरी दे अंदर सज्जा क्लिक करो ते "Open in Terminal"चुनो.इक टर्मिनल विंडो खुʼल्लग. टर्मिनल विंडो दी कमांड लाइन थमां एह् कमांड प्रविश्ट करो(कमांड दे अमल च औने शा पैह्‌लें तुसेंगी अपना बुनेआदी बरतूनी पासवर्ड पर्विश्ट करने आस्तै आखेआ जाह्‌ग ):

For Fedora-based systems: sudo dnf install *.rpm

मैनद्रिव अधारत सिस्टमें आस्तै: sudo urpmi *.rpm

For other RPM-based systems (openSUSE, etc.): rpm -Uvh *.rpm

इंस्टालेशन प्रक्रिया हून पूरी होई गेई ऐ, ते थुआढ़ी डैस्कटाप दियें ऐपलीकेशनें/आफिस मेन्यु च सभनेंLibreOffice ऐपलीकेशनें आस्तै आइकन होने चाहिदे.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

उप्परली इंस्टालेशन हिदायतें च  लिनक्स बंडांदरें आस्तै डैस्कटाप एकीकरण कन्नै सरबंधत नोट नेईं दित्ते गेदे.
----------------------------------------------------------------------

इʼनें इंस्टालेशन हिदायतें च  चेचे तौर उप्पर नेईं दित्ती गेदी हिदायतें दे बावजूद बाकी दुए लिनक्स बंडांदरें पर LibreOfficeगी इंस्टाल करना सौखे गै मुमकन होई जाह्‌ग.जिस पक्ख लेई फर्क-भेद पेश आई सकदा ऐ ओह् ऐ -डैस्कटाप-एकीकरण.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

भाशा पैक इंस्टाल कीता जा करदा ऐ
----------------------------------------------------------------------

अपनी इच्छत भाशा ते प्लेटफार्म आस्तै भाशा पैक डाउनलोड  करो. ओह् ,मुक्ख इंस्टालेशन आर्काइव दे रूप च उस्सै स्थान पर उपलब्ध न. नाटिलस फाइल मैनजर थमां कुसै डायरैक्टरी ( मसाल दे तौर पर थुआढ़ा डैस्कटाप)च डाउनलोड  आर्काइव कड्ढो.एह् पक्का करी लैओ जे तुसें सभनें LibreOfficeऐपलीकेशनें(तुर्तशुरूकर्ता सनैं , जेकर शुरू ऐ).  चा निकास करी लेदा ऐ.

डायरैक्टरी गी उस डायरैक्टरी च बदलो जित्थै तुसें अपना डाउनलोड  भाशा पैक कड्ढियै आंह्‌दा ऐ.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

नाटिलस फाइल मैनजर थमां डायरैक्टरी दे अंदर सज्जा क्लिक करो ते "Open in Terminal" कमांड चुनो. इक टर्मिनल विंडो खुʼल्लग. भाशा पैक गी इंस्टाल करने आस्तै कमांड गी  अमल च आह्‌न्नो( खʼल्ल दित्ती दियें सभनें कमांडें सनै, तुसेंगी अपना बुनेआदी बरतूनी पासवर्ड प्रविश्ट करने आस्तै आखेआ जाह्‌ग ):

डेवियन/उबंटू-अधारत सिस्टमें आस्तै:: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

मैनद्रिव अधारत सिस्टमें आस्तै: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

उʼनें सैट्टिङें गी अड्जस्ट करने दे बाद, OK पर क्लिक करो. संवाद बाक्स बंद होई जाह्‌ग,ते तुसें गी इक जानकारी सनेहा नजरी औग जेह्‌ड़ा दस्सग जे थुआढ़ियां तब्दीलियां तां गै  सक्रिय कीतियां जाङन जिसलै तुस LibreOffice चा निकास करदे ओ ते  इस्सी परतियै शुरू करदे ओ (तुर्त शुरूकर्ता चा निकास करने दा चेता रक्खो जेकर ओह् शुरू ऐ).

अगली बारी जिसलै तुस LibreOffice शुरू करदे ओ, तां एह् थुआढ़े आसेआ हुनै इंस्टाल कीती दी भाशा च शुरू होग.

----------------------------------------------------------------------
प्रोग्राम दे शुरू दरान समस्यां
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
विंडोज़ च ALPS/ सिन्पटिक्स नोटबुक टचपैड
----------------------------------------------------------------------

जिसलै तुस अपनियां औंगलियां ALPS/ सिन्पटिक्स टचपैड दे आरपार फेरदे ओ, विंडोज चालक मुद्दे कारण तुस   LibreOffice दस्तावेजें चा स्क्रोल नेईं करी सकदे  .

टच-पैड स्क्रोलिङ गी समर्थ करने आस्तै संरूपण फाइल च एह् लाइनां जोड़ो ते कंप्यूटर परतियै शुरू करो: "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini"

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

विंडोज़ दे बक्खरे-बक्खरे सरूपें पर संरूपण फाइल दी स्थिति बक्खरी होई सकदी ऐ.

----------------------------------------------------------------------
शार्टकट कीआं
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
म्हत्त्वपूर्ण समर्थन लेई नोट
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
बरतूनी समर्थन
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
Reporting Bugs & Issues
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
शामल होआ करदा ऐ
----------------------------------------------------------------------

इस म्हत्तवपूर्ण खु’ल्ले स्रोत प्राजैक्ट दे विकास च थुआढ़ी क्रियाशील भागीदारी थमां LibreOffice  समुदाय गी बड़ा फायदा होग.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

शुरू करने दा तरीका
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Subscribe
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* खबर: announce@documentfoundation.org *सभनें बरतूनियें आस्तै सफारशशुदा  * (घट्ट ट्रैफिक)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* सामान्य विकासक सूची: libreoffice@lists.freedesktop.org (मती ट्रैफिक)

इक जां मते प्रोजैक्टें च शामल होआ करदा ऐ
----------------------------------------------------------------------

तुस इस म्हत्तवपूर्ण खु’ल्ले स्रोत प्राजैक्ट च बड़ा सैहयोग देई सकदे ओ, भामें थुआढ़े कोल साफ्टवेअर डजैन जां कोडीकरण तजर्बा सीमत ऐ.हां, तुस.

अस मेद करने आं जे नमें LibreOffice 26.2  साथें कम्म करने च तुसें गी नंद औंदा ऐ ते तुस आनलाइन साढ़े कन्नै शामल होगेओ.

लिब्रे आफिस समुदाय

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
