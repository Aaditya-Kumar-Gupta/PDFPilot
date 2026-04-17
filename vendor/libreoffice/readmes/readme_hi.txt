
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

यह फ़ाइल LibreOffice सॉफ्टवेयर के बारे में महत्वपूर्ण सूचना समाहित किए है. आपको इस सूचना को बहुत ध्यान से संस्थापन आरंभ करने के पहले पढ़ने की जरूरत है.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

क्या LibreOffice वाकई किसी उपयोक्ता के लिए निःशुल्क है?
----------------------------------------------------------------------

LibreOffice हर किसी के लिए उपयोग के लिए निःशुल्क है. आप LibreOffice के इस नक़ल को ले सकते हैं और मनचाहे संख्या में कंप्यूटरों पर संस्थापित कर सकते हैं, और अपने किसी उद्देश्यों के लिए इसे उपयोग कर सकते हैं (वाणिज्यिक, सरकारी, सार्वजनिक प्रशासन और शैक्षणिक उपयोग). आगे और विवरण के लिए संकुलित लाइसेंस इस LibreOffice डाउनलोड के साथ पाठ देखें.

क्यों LibreOffice किसी उपयोक्ता के लिए निःशुल्क है?
----------------------------------------------------------------------

आप इस LibreOffice की कॉपी को बिना किसी शुल्क के उपयोग कर सकते हैं क्योंकि अलग-अलग योगदानकर्ताओं और कॉरपोरेट प्रायोजकों ने इसे डिजायन, विकसित, जाँच, अनुवाद, दस्तावेज़ित, मार्केटिंग और मदद कई रूपों में किया है जिससे LibreOffice बन पाया है जो यह आज है - घर और कार्यालयों के लिए दुनिया का अग्रणी मुक्त स्रोत उत्पादकता सॉफ्टवेयर.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
संस्थापन पर टिप्पणी
----------------------------------------------------------------------

LibreOffice के लिए जावा रनटाइम वातावरण (JRE) का हालिया संस्करण पूर्ण कार्यशीलता के लिए चाहिए. JRE LibreOffice संस्थापन संकुल का हिस्सा नहीं है, इसे अलग से संस्थापित किया जाना चाहिए.

तंत्र जरूरत
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

नोट: जानें कि प्रशासक अधिकार संस्थापन प्रक्रिया के लिए जरूरी है.

माइक्रोसॉफ़्ट ऑफ़िस प्रारूप के लिए बतौर तयशुदा अनुप्रयोग LibreOffice का पंजीयन संस्थापक के साथ निम्नलिखित कमांड लाइन स्विच के साथ बाध्य किया या रोका जा सकता है:

* REGISTER_ALL_MSO_TYPES=1 LibreOffice को माइक्रोसॉफ्ट ऑफिस प्रारूप के लिए बतौर तयशुदा अनुप्रयोग पंजीयन के लिए बाध्य करेगा.
* REGISTER_NO_MSO_TYPES=1 की पंजीयन को माइक्रोसॉफ़्ट ऑफिस प्रारूप के लिए तयशुदा अनुप्रयोग के रूप में दबाएगा.

कृपया सुनिश्चित करें कि आपके पास आपके तंत्र में अस्थायी निर्देशिका में निःशुल्क स्मृति है, और कृपया सुनिश्चित करें कि पढ़ें, लिखें और चलाएँ पहुँच अधिकार दिए जा चुके हैं. संस्थापन प्रक्रिया को आरंभ करने के पहले सभी अन्य प्रोग्राम बंद करें.

LibreOffice का डेबियन/उबन्टू आधारित लिनक्स तंत्र पर संस्थापन
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

यह निर्दशिका "DEBS" नामक उपनिर्देशिका समाहित करती है. निर्देशिका को "DEBS" निर्देशिका में बदलें.

निर्देशिका के अंदर दाहिना क्लिक करें और "टर्मिनल में खोलें" चुनें. एक टर्मिनल विंडो खुलेगा. टर्मिनल विंडो की कमांड लाइन से, निम्नलिखित कमांड दर्ज करें (आपको अपना रूट उपयोक्ता का कूटशब्द दर्ज करना होगा इससे पहले कि कमांड चलेगा):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

संस्थापन प्रक्रिया अब पूरी हो गई है, और आपके पास सभी LibreOffice अनुप्रयोग हैं आपके डेस्कटॉप के अनुप्रयोग/ऑफिस मेन्यू में.

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

यह निर्दशिका "RPMS" नामक उपनिर्देशिका समाहित करती है. निर्देशिका को "RPMS" निर्देशिका में बदलें.

निर्देशिका के अंदर दाहिना क्लिक करें और "टर्मिनल में खोलें" चुनें. एक टर्मिनल विंडो खुलेगा. टर्मिनल विंडो की कमांड लाइन से, निम्नलिखित कमांड दर्ज करें (आपको अपना रूट उपयोक्ता का कूटशब्द दर्ज करना होगा इससे पहले कि कमांड चलेगा):

For Fedora-based systems: sudo dnf install *.rpm

मंद्रिवा आधारित तंत्र के लिए: sudo urpmi *.rpm

For other RPM-based systems (openSUSE, etc.): rpm -Uvh *.rpm

संस्थापन प्रक्रिया अब पूरी हो गई है, और आपके पास सभी LibreOffice अनुप्रयोग हैं आपके डेस्कटॉप के अनुप्रयोग/ऑफिस मेन्यू में.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

ऊपर के संस्थापन निर्देश में कवर नहीं हुए लिनक्स वितरण के डेस्कटॉप एकीकरण के संबंध में नोट्स
----------------------------------------------------------------------

LibreOffice को अन्य लिनक्स वितरण पर संस्थापित करना आसानी से संभव था जो कि इन संस्थापन निर्देश में विशेष रूप से कवर नहीं किया गया था. मुख्य पहलू जिनके लिए अंतर हो सकता है वह है डेस्कटॉप एकीकरण.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

भाषा पैक का संस्थापन
----------------------------------------------------------------------

अपने वांछित भाषा और प्लेटफॉर्म के लिए भाषा पैक डाउनलोड करें. मुख्य संस्थापन अभिलेख की तरह उसी स्थान से वे उपलब्ध हैं. नॉटिलस फ़ाइल प्रबंधक से, डाउनलोड किए अभिलेख को निर्देशिका (उदाहरण के लिए आपका डेस्कटॉप) निकालें. सुनिश्चित करें कि आप सभी LibreOffice अनुप्रयोगों से निकल (QuickStarter के साथ, यदि यह आरंभ हो चुका है) चुके हैं.

निर्देशिका को उन निर्देशिका में बदलें जिसमें आफने अपने डाउनलोड किए गए भाषा पैक को निकाला है.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

नॉटिलस फ़ाइल प्रबंधक से, निर्देशिका पर दाहिना क्लिक करें और "टर्मिनल में खोलें" कमांड चुनें. टर्मिनल विंडो में जिसे आपने हाल में खोला है, भाषा पैक को संस्थापित करने के लिए कमांड चलाएँ (नीचे के सभी कमांड के साथ, आपको अपना रूट कूटशब्द दर्ज करने के लिए प्रांप्ट किया जाएगा):

डेबियन/उबन्टू आधारित तंत्र के लिए: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

मंद्रिवा आधारित तंत्र के लिए: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

उन सेटिंग को समायोजित करके, ठीक पर क्लिक करें. संवाद पेटी बंद हो जाएगी, और आप एक सूचना संदेश देखें आपको बताते हुए कि आपके परिवर्तन तभी सक्रिय किए जाएँगे जब LibreOffice से छोड़ते हैं और इसे फिर आरंभ करते हैं (क्विकस्टार्टर से निकलना याद रखें यदि यह आरंभ होता है).

अगली बार जब आप LibreOffice शुरू करते हैं, तो यह आपके द्वारा संस्थापित भाषा में आरंभ होगा.

----------------------------------------------------------------------
गनोम पर प्रोग्राम आरंभ होने के दौरान समस्या
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
विंडोज में ALPS/Synaptics नोटबुक टचपैड
----------------------------------------------------------------------

एक Windows ड्राइवर मुद्दा के कारण, आप LibreOffice दस्तावेज़ से हो कर स्क्रॉल नहीं कर सकते हैं जब कि अपनी अंगुली को एक ALPS/Synaptics टचपैड के आर-पार ले जाते हैं.

टचपैड स्क्रॉलिंग सक्रिय करने के लिए "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" विन्यास फ़ाइल में ये पंक्ति जोड़ें और अपना कंप्यूटर फिर शुरू करें:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

नोट: विन्यास फ़ाइल की अवस्थिति Windows के भिन्न संस्करण के साथ भिन्न रहता है.

----------------------------------------------------------------------
शार्टकट कुंजी
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
महत्वपूर्ण पहुंचयोग्य नोट्स
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
उपयोक्ता समर्थन
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
बग रिपोर्टिंग व मुद्दे
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
शामिल हो रहा है
----------------------------------------------------------------------

LibreOffice समुदाय को आपके सक्रिय सहभागिता से बहुत लाभ मिलेगा इस मुक्त स्रोत प्रोजेक्ट के विकास में.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

आरंभ करने का तरीका
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

सदस्यता
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* समाचार: announce@documentfoundation.org *सभी उपयोक्ता के लिए अनुशंसित* (हल्की ट्रैफिक)
* प्रधान उपयोक्ता सूची: users@global.libreoffice.org *परिचर्चा से जुड़ने का आसान तरीका* (बहुत अधिक आवाजाही)
* विपणन परियोजना: marketing@global.libreoffice.org *beyond development* (ट्रैफिक बढ़ रहा है)
* सामान्य विकासकर्ता सूची: libreoffice@lists.freedesktop.org (बहुत ट्रैफिक)

एक या अधिक परियोजनाओं में शामिल हों
----------------------------------------------------------------------

आप इस महत्वपूर्ण मुक्त स्रोत प्रोजेक्ट में तभी अच्छा योगदान दे सकते हैं जब आपको कम सॉफ्टवेयर डिजायन अथवा कोडिंग अनुभव है. हां, आप!

हम आशा करते हैं कि आप नए LibreOffice 26.2 के साथ कार्य करने का आनंद लें और हमें ऑनलाइन शामिल करें.

LibreOffice समुदाय

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
