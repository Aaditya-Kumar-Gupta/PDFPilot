
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

এই ফাইলয় LibreOffice চফ্টৱেৰৰ বিষয়ে গুৰুত্বপূৰ্ণ তথ্য অন্তৰ্ভুক্ত কৰে। আপোনাক ইনস্টল আৰম্ভ কৰাৰ আগত এই তথ্য সাৱধানেৰে পঢ়ি লোৱাৰ পৰামৰ্শ দিয়া হৈছে।

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

LibreOffice সঁচাকে যিকোনো ব্যৱহাৰকাৰীৰ কাৰণে বিনামূলীয়া নে?
----------------------------------------------------------------------

LibreOffice সকলোৰে ব্যৱহাৰৰ কাৰণে বিনামূলীয়াকে উপলব্ধ। আপুনি এই LibreOffice ৰ কপি লব পাৰে আৰু যিমান ইচ্ছা সিমান কমপিউটাৰত ইনস্টল কৰিব পাৰে, আৰু ইয়াক যিকোনো কাৰণত ব্যৱহাৰ কৰিব পাৰে যেনে (বানিজ্যিক, চৰকাৰী, ৰাজহুৱা, প্ৰশাসনীয় আৰু শিক্ষামূলক ব্যৱহাৰ)। অধিক জানিবলে এই LibreOffice ডাউনল'ডৰ লগত পেকেইজ্ড অনুজ্ঞা লিখনী চাওক।

LibreOffice যিকোনো ব্যৱহাৰকাৰীৰ কাৰণে বিনামূলিয়া কিয়?
----------------------------------------------------------------------

আপুনি LibreOffice ৰ এই কপি বিনামূলিয়াভাবে ব্যৱহাৰ কৰিব পাৰে কাৰণ সূকীয়া অৱদানকাৰী আৰু কৰপোৰেট অনুপালকসমূহে ৰূপাঙ্কন, উন্নয়ন, পৰিক্ষা, অনুবাদ, তথ্যচিত্ৰ লিখনী, সমৰ্থন, বিপণন আৰু বহু ধৰণে সহায় কৰিছে LibreOffice ক তাৰ বৰ্তমান ৰূপ দিবলে - বিশ্বৰ আগশাৰীৰ মুক্ত উৎস উৎপাদনকাৰী চফ্টৱেৰ ঘৰ আৰু অফিচৰ বাবে।

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
ইনস্টলেষণ টোকা
----------------------------------------------------------------------

LibreOffice ৰ সম্পূৰ্ণ কাৰ্যকৰিতাৰ বাবে Java চলনসময় পৰিৱেশ (JRE) ৰ এটা শেহতীয়া সংস্কৰণৰ প্ৰয়োজন। JRE LibreOffice ইনস্টল পেকেইজৰ এটা অংশ নহয়, ইয়াক পৃথকভাৱে ইনস্টল কৰিব লাগিব।

চিস্টেমৰ প্ৰয়োজনীয়তাবোৰ:
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

অনুগ্ৰহ কৰি মন কৰিব যে ইনস্টল প্ৰক্ৰিয়াৰ বাবে প্ৰশাসনীয় অধিকাৰসমূহৰ প্ৰয়োজন।

Microsoft Office ৰ কাৰণে LibreOffice অবিকল্পিত ৰূপে ন'হ'বলৈ ইনস্টলাৰৰ তলৰ কমান্ড শাৰী চুইচসমূহ বলবৎ কৰিব পাৰি:

* REGISTER_ALL_MSO_TYPES=1 এ LibreOffice ক Microsoft Office বিন্যাসসমূহৰ বাবে অবিকল্পিত এপ্লিকেচন হিচাপে ৰেজিস্ট্ৰেষণ বলৱৎ কৰিব।
* REGISTER_NO_MSO_TYPES=1 এ LibreOffice ক Microsoft Office বিন্যাসসমূহৰ বাবে অবিকল্পিত এপ্লিকেচন হিচাপে ৰেজিস্ট্ৰেষণ বলৱৎ কৰিব।

অনুগ্ৰহ কৰি সুনিশ্চিত হওক যে আপোনাৰ চিস্টেমত থকা অস্থায়ী ডাইৰেটৰিত পৰ্যাপ্ত খালি স্থান আছে, আৰু অনুগ্ৰহ কৰি সুনিশ্চিত কৰক যে পঢ়া, লিখা আৰু চলা অভিগম অধিকাৰসমূহৰ অনুমতি দিয়া হৈছে। ইনস্টল প্ৰক্ৰিয়া আৰম্ভ কৰাৰ আগত সকলো অন্য প্ৰগ্ৰাম বন্ধ কৰক।

Debian/Ubuntu-ভিত্তিয় Linux চিস্টেমত LibreOffice ৰ ইনস্টল
----------------------------------------------------------------------

এটা ভাষা পেক ইনস্টল কৰিবলে সহায়ৰ বাবে (LibreOffice ৰ US ইংৰাজী সংস্কৰণ ইনস্টল কৰাৰ পিছত), অনুগ্ৰহ কৰি এটা ভাষা পেক ইনস্টল কৰা চিহ্নিত বিভাগ পঢ়ক।

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

ডাইৰেকটৰিয়ে "DEBS" নামৰ এটা উপ-ডাইৰেকটৰি অন্তৰ্ভুক্ত কৰে। ডাইৰেকটৰিক "DEBS" ডাইৰেকটিলে সলনি কৰক।

ডাইৰেকটৰিৰ ভিতৰত ৰাইট-ক্লিক কৰক আৰু বাছক "টাৰমিনেলত খোলক"। এটা টাৰমিনেল উইন্ডো খোল খাব। টাৰমিনেলৰ উইন্ডো কমান্ড শাৰীৰ পৰা, নিম্নলিখিত কমান্ড সুমুৱাওক (কমান্ডটো প্ৰেৰণ হোৱাৰ আগত আপোনাক আপোনাৰ ৰুট ব্যৱহাৰকাৰী পাছৱৰ্ড বিচৰা হব):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

ইনস্টল প্ৰক্ৰিয়া এতিয়া সম্পূৰ্ণ হৈছে, আৰু আপোনাৰ ডেস্কটপৰ এপ্লিকেচনসমূহ/অফিচ মেনুত থকা সকলো LibreOffice এপ্লিকেচনসমূহৰ বাবে আইকনসমূহ আপোনাৰ থাকিব লাগিব।

Fedora, openSUSE, Mandriva আৰু অন্য Linux চিস্টেমসমূহত RPM পেকেইজসমূহ ব্যৱহাৰ কৰি LibreOffice ৰ ইনস্টল
----------------------------------------------------------------------

এটা ভাষা পেক ইনস্টল কৰিবলে সহায়ৰ বাবে (LibreOffice ৰ US ইংৰাজী সংস্কৰণ ইনস্টল কৰাৰ পিছত), অনুগ্ৰহ কৰি এটা ভাষা পেক ইনস্টল কৰা চিহ্নিত বিভাগ পঢ়ক।

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

এই ডাইৰেকটৰিৰ এটা উপডাইৰেকটৰি "RPMS" ইনস্টল হৈ আছে। ডাইৰেকটৰিক "RPMS" ডাইৰেকটৰিলে সলনি কৰক।

ডাইৰেকটৰিৰ ভিতৰত ৰাইট-ক্লিক কৰক আৰু বাছক "টাৰমিনেলত খোলক"। এটা টাৰমিনেল উইন্ডো খোল খাব। টাৰমিনেলৰ উইন্ডো কমান্ড শাৰীৰ পৰা, নিম্নলিখিত কমান্ড সুমুৱাওক (কমান্ডটো প্ৰেৰণ হোৱাৰ আগত আপোনাক আপোনাৰ ৰুট ব্যৱহাৰকাৰী পাছৱৰ্ড বিচৰা হব):

For Fedora-based systems: sudo dnf install *.rpm

Mandriva-ভিত্তিয় চিস্টেমসমূহৰ বাবে: sudo urpmi *.rpm

অন্য RPM-ভিত্তিয় চিস্টেমসমূহ (openSUSE, ইত্যাদী) ৰ বাবে: rpm -Uvh *.rpm

ইনস্টল প্ৰক্ৰিয়া এতিয়া সম্পূৰ্ণ হৈছে, আৰু আপোনাৰ ডেস্কটপৰ এপ্লিকেচনসমূহ/অফিচ মেনুত থকা সকলো LibreOffice এপ্লিকেচনসমূহৰ বাবে আইকনসমূহ আপোনাৰ থাকিব লাগিব।

বিকল্পভাৱে, আপুনি ইনস্টলেষণক এজন ব্যৱহাৰকাৰী ৰূপে পৰিৱেশন কৰিবলে, এই আৰ্কাইভৰ ওপৰ স্তৰৰ ডাইৰেকটৰিত অৱস্থিত, 'install' স্ক্ৰিপ্ট ব্যৱহাৰ কৰিব পাৰিব। স্ক্ৰিপ্টে এই ইনস্টলেষণৰ বাবে তাৰ নিজস্ব আলেখ্য ৰাখিবলে LibreOffice সংস্থাপন কৰিব, যি আপোনাৰ স্বাভাৱিক LibreOffice আলেখ্যৰ পৰা পৃথক থাকিব। মন কৰিব যে ই চিস্টেমৰ অনূকলন অংশবোৰ যেনে ডেস্কটপ মেনু বস্তু আৰু ডেস্কটপ MIME ধৰণ ৰেজিস্ট্ৰেষণ ইনস্টল নকৰে।

Linux বিতৰনসমূহৰ বাবে ডেস্কটপ অনুকলন উদ্বেগীয় টোকাসমূহ উপৰত থকা ইনস্টল নিৰ্দেশসমূহত অন্তৰ্ভুক্ত নহয়
----------------------------------------------------------------------

LibreOffice ক এই ইনস্টল নিৰ্দেশসমূহত ধাৰ্য্যত নহোৱা অন্য Linux বিতৰনসমূহত ইনস্টল কৰা অতি সহজভাৱে সম্ভব হব লাগে। মূখ্য কাৰণ যাৰ কাৰণে ভিন্নতাৰ সন্মুখিন হব পাৰে হল ডেস্কটপ অনুকলন।

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

এটা ভাষা পেক ইনস্টল কৰা হৈ আছে
----------------------------------------------------------------------

আপোনাৰ পছন্দৰ ভাষা আৰু প্লেটফৰ্মৰ কাৰণে ভাষা পেক ডাউনল'ড কৰক। ইহত মূখ্য ইনস্টল আৰকাইভ যি অৱস্থানৰ আছে তাতে উপলব্ধ। Nautilus ফাইল ব্যৱস্থাপকৰ পৰা, ডাউনল'ড কৰা আৰকাইভক এটা ডাইৰেকটৰি (যেনে আপোনাৰ ডেস্কটপ) লে এক্সস্ট্ৰেক্ট কৰক। সুনিশ্চিত কৰক যে আপুনি সকলো LibreOffice এপ্লিকেচন (QuickStarter কে ধৰি, যদি ইয়াক আৰম্ভ কৰা হৈছে) প্ৰস্থান কৰিছে।

যিটো ডাইৰেকটৰিলে আপুনি ডাউনল'ড কৰা ভাষা পেক এক্সস্ট্ৰেক্ট কৰিছে তালৈকে ডাইৰেকটৰি সলনি কৰক।

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

এতিয়া ডাইৰেকটৰিক সেই ডাইৰেকটৰিলে সলনি কৰক যি ইনস্টল কৰিব লগিয়া পেকেইজসমূহ অন্তৰ্ভুক্ত কৰে। Debian/Ubuntu-ভিত্তিয় চিস্টেমসমূহত, ডাইৰেকটৰি DEBS হব। Fedora, openSUSE অথবা Mandriva চিস্টেমসমূহত, ডাইৰেকটৰি RPMS হব।

Nautilus ফাইল ব্যৱস্থাপকৰ পৰা, ডাইৰেকটৰিত ৰাইট-ক্লিক কৰক আৰু বাছক "টাৰমিনেলত খোলক"। টাৰমিনেল উইন্ডো যিটো আপুনি এইমাত্ৰ খোলিছে, ভাষা পেক ইনস্টল কৰিবলে কমান্ড প্ৰেৰণ কৰক (তলত থকা সকলো কমান্ডৰ সৈতে, আপোনাক আপোনাৰ ৰুট ব্যৱহাৰকাৰী পাছৱৰ্ড বিচৰা হব পাৰে):

Debian/Ubuntu-ভিত্তিয় চিস্টেমসমূহৰ বাবে: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Mandriva-ভিত্তিয় চিস্টেমসমূহৰ বাবে: sudo urpmi *.rpm

অন্য RPM-ব্যৱহাৰকাৰী চিস্টেমসমূহ (openSUSE,ইত্যাদী) ৰ বাবে: rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

সেই সংহতিসমূহ সংগঠিত কৰাৰ পিছত, ঠিক আছেত ক্লিক কৰক। ডাইলগ বাকচ বন্ধ হব, আৰু আপুনি এটা তথ্য বাৰ্তা দেখা পাব যি আপোনাক কব যে আপোনাৰ পৰিৱৰ্তনসমূহ LibreOffice প্ৰস্থান কৰি আৰু পুনৰ ইয়াক আৰম্ভ কৰাৰ (QuickStarter প্ৰস্থান কৰিব মনত ৰাখিব যদি আৰম্ভ হৈ আছে) পিছত সক্ৰিয় হব।

আকৌ যেতিয়া আপুনি LibreOffice আৰম্ভ কৰিব, ই আপুনি এইমাত্ৰ ইনস্টল কৰা ভাষাত আৰম্ভ হব।

----------------------------------------------------------------------
প্ৰগ্ৰাম আৰম্ভ কৰোঁতে সমস্যা
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Windows ত ALPS/Synaptics নোটবহী টাচপেডসমূহ
----------------------------------------------------------------------

এটা Windows ড্ৰাইভাৰ সমস্যাৰ কাৰণে, আপুনি LibreOffice দস্তাবেজত গমন কৰিব নোৱাৰে যেতিয়া আপুনি ALPS/Synaptics টাচপেড ব্যৱহাৰ কৰে।

টাচপেড স্ক্ৰ'লিং সক্ষম কৰিবলৈ, "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" সংৰূপ ফাইলটোলৈ তলত দিয়া শাৰীবোৰ যোগ কৰক, আৰু কমপিউটাৰটো পুনাৰম্ভ কৰক:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

টোকা: ৰূপৰেখা ফাইলটোৰ স্থানটো বিভিন্ন Windows ৰ সংস্কৰণবোৰত বেলেগ হ'ব পাৰে।

----------------------------------------------------------------------
চৰ্টকাট কি'সমূহ
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
গুৰুত্বপূৰ্ণ অভিগমৰ টোকা
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
ব্যৱহাৰকৰ্তাৰ সমৰ্থন
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
বাগসমূহ & সংবাদ দিয়া হৈ আছে; বিষয়সমূহ
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
জড়িত হৈ আছে
----------------------------------------------------------------------

এই গুৰুত্বপূৰ্ণ মুক্ত উৎসৰ পৰিকল্পনাত LibreOffice সম্প্ৰদায় বহুতো লাভ পাব আপোনাৰ সক্ৰিয় অংশ গ্ৰহণৰ পৰা।

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

কেনেকৈ আৰম্ভ কৰিব
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

স্বাক্ষৰ কৰক
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* বাতৰি: announce@documentfoundation.org *সকলো ব্যৱহাৰকাৰীৰ কাৰণে উপদেশিত* (পাতল ট্ৰাফিক)
* মূখ্য ব্যৱহাৰকাৰী তালিকা: users@global.libreoffice.org *আলোচনাসমূহত অংশগ্ৰহন কৰিবলে সহজ উপায়* (ডাঠ ট্ৰাফিক)
* বিপণন প্ৰকল্প: marketing@global.libreoffice.org *উন্নয়ন পাৰ হৈ* (ভাৰি হৈ আছে)
* সাধাৰণ উন্নয়ক তালিকা: libreoffice@lists.freedesktop.org (ডাঠ ট্ৰাফিক)

এটা অথবা অধিক প্ৰকল্পত অংশগ্ৰহন লৈ আছে
----------------------------------------------------------------------

যদিও আপোনাৰ ছফটৱেৰ ডিজাইন অথবা ক'ডিং অভিজ্ঞতা সীমিত এই গুৰুত্বপূৰ্ণ অপেন উৎস প্ৰজেক্টটোলৈ আপুনি অধিক পৰিমাণৰ বৰঙণি আগবঢ়াব পাৰে. হয়, আপুনি!

নতুন LibreOffice 26.2 ৰ লগত কাম কৰি আপুনি ভাল পাব বুলি ভাবিছো আৰু আমাক অনলাইন লগ ধৰিব।

LibreOffice সম্প্ৰদায়

----------------------------------------------------------------------
ব্যৱহৃত/পৰিবৰ্তিত উৎস ক'ড
----------------------------------------------------------------------

Portions স্বত্বাধিকাৰ1998, 1999 James Clark. Portions স্বত্বাধিকাৰ 1996, 1998 Netscape সংযোগ সংঘঠন।
