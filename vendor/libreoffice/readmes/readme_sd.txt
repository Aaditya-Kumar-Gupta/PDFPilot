
======================================================================
LibreOffice 26.2 مونکي پڙهو
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

هن فائل ۾LibreOffice  سافٽ ويئر بابت اَهم معلومات مؤجود آهي۔ توهان کي صلاح ڏجي ٿي تە اِسٿاپن شروع ڪرڻ کان اَڳ پوري ڌيان سان اِها معومات پڙهو۔

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

ڇا LibreOffice ڪنهن بە اِستعمال ڪندڙ لاءِ سچ پچ مفت آهي؟
----------------------------------------------------------------------

LibreOfficeهرهڪ دواران اِستعمال ڪرڻ لاءِ مفت آهي۔ توهين LibreOffice  هي نقل کڻي سگهو ٿا ۽ جيترن ڪمپيوٽرن تي کپيو اِهو اِسٿاپت ڪري سگهو ٿا توهين جنهن بە مقصد لاءِ (تجارتي سرڪاري، عام اِنتظام ۽ تعليمي اِستعمال سميت) ڪتب آڻي سگهو ٿا۔ وڌيڪ تفصيل لاءِ هن LibreOffice ڊائون لوڊ سان ڏنل پئڪيج وارو ليسن جو متن ڏسو۔

LibreOffice ڪنهن نە اِستعمال ڪندڙ لاءِ مفت ڇو آهي؟
----------------------------------------------------------------------

توهين LibreOffice جو هي نقل مفت اِستعمال ڪري سگهو ٿا ڇو تە اِهو شخصي يوگدان ڏيندڙ ۽ ڪارپورٽ مالي مدد سان رچيل وڪست ڪيل، چڪاسيل، ترجمو ڪيل دستاويز تيار ڪيل سمرٿن ڏنل بازار ۾ آندل ۽ انيڪ ٻين طريقن سان مدد ڪيل LibreOffice جيڪو اَڄ گهر ۽ آفيس لاءِ دنيا جو تمام اَهم اوپن سورس اُپت وارو سافٽ ويئر آهي۔

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
اِسٿاپن تي ٽپڻيون
----------------------------------------------------------------------

LibreOffice requires a recent version of Java Runtime Environment (JRE) for full functionality. JRE is not part of the LibreOffice installation package, it should be installed separately.

سرستي لاءِ ضرورتون
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

مهرباني ڪري ڌيان رهي تە اِسٿاپن جي پرڪريا لاءِ منتظم جي حقن جي ضرورت آهي۔

مائڪرو سافٽ آفيس رچنائن لاءِ ڊيفالٽ درخواست جيانLibreOffice رجسٽريشن اِسٿاپن ڪندڙ سان هيٺئينءَ آديس جي سِٽ جي ڦيرائڻ سان عمل ۾ آڻي يا روڪي سگهجي ٿو۔

* REGISTER_ALL_MSO_TYPES=1 will force registration of LibreOffice as default application for Microsoft Office formats.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

مهرباني ڪري اِن ڳالهە جي پڪ ڪريو تە توهانجي سرشتي جي عارضي ڊائريڪٽريءَ ۾ ڪافي خالي ميموري مؤجود آهي ۽ مهرباني ڪري اِن ڳالهە جي پڪ ڪريو تە پڙهڻ لکڻ ۽ هلائڻ داخل ڪرڻ جا حق مؤجود آهن۔ اِسٿاپن پرڪريا شروع ڪرڻ کان اڳ ٻيا سڀ پروگرام بند ڪريو۔

ڊيبئن/يو بنٽو - آڌار وارن لينڪس سرشتن تي LibreOffice جو اِسٿاپن
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

هن ڊائريڪٽريءَ ۾  \DEBS\ نالي گؤڻ ڊائريڪٽري مؤجود آهي۔ ڊائريڪٽريء کي  \DEBS\ ڊائريڪٽريءَ ۾ بدلايو۔

ڊائريڪٽريءَ منجهە ساڄي پاسي - ڪلڪ ڪريو ۽ \آخر ۾ کوليو\ چونڊيو۔ آخريءَ جي ونڊو جي آديش جي سٽ مان هيٺيون آديش داخل ڪريو۔ (آديش تعميل ۾ اَچي اُن کان اڳ توهان کي پنهنجو مول اِستعمال ڪندڙ: جو ڳجهو لفظ داخل ڪرڻ جي ياد ڏياري ويندي۔

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

اِسٿاپن جي پرڪريا پوري ڪئي ويئي آهي، ۽ توهان وٽ پنهنجي ڊيسڪٽاپ پرڪريائن/ آفيس مينوءَ ۾ LibreOffice جي سڀني پرڪريائن لاءِ آئڪانس هڻڻ گهرجن۔

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

هن ڊائريٽريءَ ۾  \RPMS\ نالي گؤڻ ڊائريڪٽريءَ مؤجود آهي۔ ڊآئريڪٽري  \RPMS\ ڊائريڪٽريءَ ۾ بدلايو۔

ڊائريڪٽريءَ منجهە ساڄي پاسي - ڪلڪ ڪريو ۽ \آخر ۾ کوليو\ چونڊيو۔ آخريءَ جي ونڊو جي آديش جي سٽ مان هيٺيون آديش داخل ڪريو۔ (آديش تعميل ۾ اَچي اُن کان اڳ توهان کي پنهنجو مول اِستعمال ڪندڙ: جو ڳجهو لفظ داخل ڪرڻ جي ياد ڏياري ويندي۔

For Fedora-based systems: sudo dnf install *.rpm

مينڊريوا - آڌار وارن سرشتي لاءِ: sudo urpmi *.rpm

For other RPM-based systems (openSUSE, etc.): rpm -Uvh *.rpm

اِسٿاپن جي پرڪريا پوري ڪئي ويئي آهي، ۽ توهان وٽ پنهنجي ڊيسڪٽاپ پرڪريائن/ آفيس مينوءَ ۾ LibreOffice جي سڀني پرڪريائن لاءِ آئڪانس هڻڻ گهرجن۔

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

لينڪس ورهاستن لاءِ واسطو رکندڙ ڊيسڪٽاپ اِنٽيگريشن ٽپڻيون مٿين اِسٿاپن هدايتن ۾ شامل ناهن
----------------------------------------------------------------------

هن اِسٿاپن جي هدايتن ۾ جيڪي ٻين لينڪس ورهاستن ۾ خاص طور شامل ڪيل آهن اُنهن ۾  ${اُپت جو نالو} آسانيءَ سان اِسٿاپت ڪرڻ ممڪن هئڻ گهرجي۔ مکيە پهلو جنهن ۾ فرق جنهن سان دوبدو ٿيڻو پئجي سگهي ٿو اُهو آهي يڊيسڪٽاپ اِنٽيگزيشن۔

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

ٻولين جو پئڪ اِسٿاپت ڪري ٿو
----------------------------------------------------------------------

پنهنجي گهربل ٻوليءَ ۽ پليٽفارم لاءِ ٻوليءَ جو پئڪيج ڊائون لوڊ ڪريو۔ اِهي مکيە اِسٿاپن جي محفوظ سنگرهە جيان ساڳئي ٺڪاڻي مان مؤجود آهن نئٽيلڪس فائل اِنتظام مان ڊائون لوڊ ڪيل محفوظ سنگرهە ڊئريڪٽريءَ (مثال طور توهانجي ڊيسڪٽاپ) ۾ اختصار ڪڍي ٿو۔ اِن ڳالهە جي پڪ ڪريو تە توهان ${ايپت جو نالو} جون سڀ ڪاروايون (تيز شروع ڪندڙ سميت اَگر اُهو ڪيو ويو هجي) ڪڍي ڇڏيون آهن۔

ڊائريڪٽري اُن ڊائريڪٽريءَ ۾ بدلايو جنهن ۾ توهان پنهنجي ڊائون لوڊ ڪيل ٻوليءَ جي پئڪ جو اِختصار شامل ڪيو۔

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

نئٽيلس فائل اِنتظام ڪندڙ مان ڊائريڪٽريءَ ۾ ساڄي پاسي ڪلڪ ڪريو ۽  \آخريءَ ۾ کوليو \ آديش چونڊيو۔ توهان هاڻي جيڪا آخر جي ونڊو کولي اُن ۾ ٻوليءَ جو پئڪ (هيٺئين آديش سان، توهان کي پنهنجي مول جي سڀني اِستعمال ڪندڙ جو ڳجهو لفظ جي ياد ڏياري سگهي ٿو) اِسٿاپت ڪرڻ جو آديش تعميل ۾ آڻيو۔

ڊيبئن/يوبنٽو - آڌار وارن سرشتن لاءِ:  sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

مينڊريوا - آڌار وارن سرشتي لاءِ: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

اُهي طئە ڪيل ترتيبون ٺهڪائڻ بعد ٺيڪ تي ڪلڪ ڪريو۔ گفتن جو باڪس بند ٿي ويندو ۽ توهين معلومات جو سنديس ائين چوندي نظر ايندو تە تڏهن ئي توهانجو تبديليون متحرڪ ٿينديون۔ جڏهن توهين LibreOffice ٻاهر ڪڍي ڇڏيندا ۽ ان کي وري شروع ڪندا۔ (تيز اِسٽارٽر ڪڍي ڇڏڻ جي ڳالهە بە ياد رکو اگر اُها شروع ڪئي ويئي هجي۔)

ٻئي دفعي جڏهن توهين  LibreOffice شروع ڪندا تڏهن اُهو اُن ٻوليءَ ۾ شروع ٿيندو جيڪا توهان هاڻي اِسٿاپت ڪئي۔

----------------------------------------------------------------------
پروگرام جي شروعات ڪرڻ دوران مسئلا
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
ونڊوز ۾ ALPS/ سنيپٽڪ نوٽبوڪ جا ٽچپيڊس
----------------------------------------------------------------------

ونڊوز جي ڊرائيور جي مسئلي سبب توهين تڏهن  LibreOffice  دستاويزن ذريعي اِسڪرول نٿا ڪري سگهو جڏهن توهين ڪنهن ALPS/ سنيپٽڪس ٽچپيڊ جي آرپار پنهنجي آڱر گسڙيو ٿا۔

ٽچپيد اِسڪرولنگ سمرٿ نڻائڻ، \C:\Program Files\Synaptics\SynTP\SynTPEnh.ini\ رچنا فائل ۾ هيٺيون سٽون شامل ڪريو ۽ پنهنجو ڪمپيوٽر نئين سر شروع ڪريو:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

هن رچنا جي فائل جو ٺڪاڻو ونڊوز جي مختلف سنسڪرڻن ۾ علحدو ٿي سگهي ٿو۔

----------------------------------------------------------------------
آسان ڪنجيون
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
اهم داخل ڪرڻ جوڳيون ٽپڻيون
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
اِستعمال ڪندڙن جو سمرٿن
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
پروگرام جي چوڪن ۾ مسئلن جي رپورٽ ڪري پيو۔
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
مشغول ٿئي پيو
----------------------------------------------------------------------

هن اهم اوپن سورس پروجيڪٽ ۾ توهانجي سرگرم بهرو وٺڻ سان LibreOffice ڪميونٽيءَ کي تمام گهڻو فائدو ٿيندو۔

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

ڪئن شروع ڪجي
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Subscribe
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* خبرون: announce@documentfoundation.org *recommended to all users* (light traffic)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* عام تيار ڪندڙن جي ياداشت: libreoffice@lists.freedesktop.org (heavy traffic) ۾ شامل ٿئي پيو۔

هڪ يا وڌيڪ پروجيڪٽن ۾ شامل ٿئي پيو۔
----------------------------------------------------------------------

اگر توهانکي سافٽ ويئر ڊزائين يا ڪوڊنگ جو ٿورو بہ آزمودو هجي تہ توهين هن اَهم اوپن سورس پروجيڪٽ ۾ اهم يوگدان ڏيئي سگهو ٿا۔ ها، توهين!

اُميد تہ توهين نئين LibreOffice 26.2 سان ڪم ڪرڻ جي مؤج ماڻيو ٿا ۽ آن لائين تي اسان سان شامل ٿيندا۔

لبرا آفيس ڪميونٽي

----------------------------------------------------------------------
اِستعمال ڪيل/ڦيرڦار ڪيل مول ڪوڊ
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
