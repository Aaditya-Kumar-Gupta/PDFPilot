
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

এ ফাইলে LibreOffice সফ্টওয়্যার সম্পর্কে গুরুত্বপূর্ণ তথ্য রয়েছে। ইনস্টলেশন শুরু করার পূর্বে এ তথ্য মনযোগ দিয়ে পড়ে নেয়ার জন্য আপনাকে সুপারিশ করা হচ্ছে।

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

LibreOffice কি আসলেই যেকোন ব্যবহারকারীর জন্য মুক্ত?
----------------------------------------------------------------------

LibreOffice সবার বিনামূল্যে ব্যবহারের জন্য। আপনি LibreOffice এর একটি অনুলিপি নিয়ে যতসংখ্যাক খুশি ততসংখ্যক কম্পিউটারে ইনস্টল করতে পারেন এবং আপনার পছন্দনানুসারে যেকোনো ক্ষেত্রে (বাণিজ্যিক, সরকারী, লোকপ্রশাসন বা শিক্ষাক্ষেত্রে)ব্যবহার করতে পারেন। আরও বিস্তারিত তথ্যের জন্য LibreOffice ডাউনলোডের সাথে দেয়া লাইসেন্স টেক্সট প্যাকেজ দেখুন।

কেন LibreOffice যেকোন ব্যবহারকারীর জন্য মুক্ত?
----------------------------------------------------------------------

LibreOffice এর অনুলিপি আপনার বিনামূল্যে ব্যবহারের জন্য কারণ প্রত্যেক অবদানকারী এবং কর্পোরেট স্পনসর যারা নকশা,উন্নয়ন, পরীক্ষা, অনুবাদ, নথিবদ্ধকরণ, সমর্থন, প্রচার এরকম আরও অনেক কিছু করেছে জন্যই LibreOffice আজকের এই অবস্থায় এসেছে - ঘর এবং অফিসের জন্য বিশ্বের নেতৃত্বদানকারী ওপেন সোর্স সফ্টওয়্য়ার প্রোডাক্টিভিটি।

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
ইনস্টলেশনের ব্যাপারে নোট
----------------------------------------------------------------------

LibreOffice requires a recent version of Java Runtime Environment (JRE) for full functionality. JRE is not part of the LibreOffice installation package, it should be installed separately.

সিস্টেমের আবশ্যকীয় বৈশিষ্ট্য
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Please be aware that administrator rights are needed for the installation process.

ইনস্টলারের নিম্নবর্ণিত কমান্ড লাইন সুইচগুলো ব্যবহার করে Microsoft Office ফরম্যাটের জন্য ডিফল্ট অ্যাপ্লিকেশন হিসেবে LibreOffice কে রেজিস্ট্রেশন করানো যায় বা বাদ দেয়া যায়।

* REGISTER_ALL_MSO_TYPES=1 will force registration of LibreOffice as default application for Microsoft Office formats.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

আপনার অস্থায়ী ডিরেক্টরি সিস্টেমে যথেষ্ট পরিমান মেমরি খালি আছে কিনা অনুগ্রহ করে তা নিশ্চিত করুন,এবং পড়া, লিখা ও চালানোর জন্য প্রবেশের অধিকার গ্রহণযোগ্য হবে তা নিশ্চিত করুন।  ইন্সটলেশন প্রক্রিয়া শুরু হওয়ার পূর্বেই বাকী সব প্রোগ্রাম বন্ধ করুন।

ডেবিয়ান/উবুন্টু ভিত্তিক লিনাক্স সিস্টেমের জন্য LibreOffice ইনস্টল প্রক্রিয়া
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

এই ডিরেক্টরিতে সাবডিরেক্টরি আছে যা "DEBS" নামে পরিচিত। ডিরেক্টরি "DEBS" এ পরিবর্তন করুন।

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

এই ডিরেক্টরিতে সাবডিরেক্টরি আছে যা "RPMS" নামে পরিচিত। ডিরেক্টরি "RPMS" এ পরিবর্তন করুন।

Right-click within the directory and choose "Open in Terminal". A terminal window will open. From the command line of the terminal window, enter the following command (you will be prompted to enter your root user's password before the command will execute):

For Fedora-based systems: sudo dnf install *.rpm

For Mandriva-based systems: sudo urpmi *.rpm

For other RPM-based systems (openSUSE, etc.): rpm -Uvh *.rpm

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

লিনাক্স ডিস্ট্রিবিউশনের জন্য ডেস্কটপ ইন্টিগ্রেশন উপরোক্ত ইনস্টলেশন অনুসরণ করে না
----------------------------------------------------------------------

LibreOffice কে অন্যান্য লিনাক্স ডিস্ট্রিবিউশনে ইনস্টল করা সহজ হবে। ডেস্কটপ ইন্টিগ্রেশনে এসব পরিবর্তনগুলো প্রয়োগ হবে।

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

ভাষা প্যাক ইনস্টল করা হচ্ছে
----------------------------------------------------------------------

আপনার পছন্দনীয় ভাষা এবং প্লাটফরমের জন্য ভাষা প্যাকটি ডাউনলোড করুন। এটি মূল ইন্সটলেশন আর্কাইভের একই অবস্থানে বিদ্যমান। নটিলাস ফাইল ব্যবস্থাপক হতে, ডাউনলোডকৃত আর্কাইভকে ডিরেক্টরিতে (উদাহরণস্বরূপ-আপনার ডেস্কটপ) সম্প্রসারণ করুন। আপনি সব LibreOffice এপ্লিকেশন (যদি QuickStarter শুরু হয়, তবে এটি অন্তর্ভুক্ত হবে ) হতে প্রস্থান নিশ্চিত করুন।

ডাউনলোডকৃত ডিরেক্টরিটি যেখানে আনপ্যাক করেছেন সে ডিরেক্টরিতে ডিরেক্টরি পরিবর্তন করুন।

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

নটিলাস ফাইল ব্যবস্থাপক হতে, ডিরেক্টরিতে ডান-ক্লিক করুন এবং "টার্মিনালে খোলা" কমান্ডটি নির্বাচন করুন। এইমাত্র উন্মুক্তকৃত টার্মিনাল উইন্ডোতে, ভাষা প্যাকটি ইনস্টল করতে কমান্ডটি কার্যকর করুন(নিম্নে বর্ণিত সব কমান্ডসহ, আপনাকে মূল ব্যবহারকারী পাসওয়ার্ডটি প্রবেশ করাতে হতে পারে)।

ডেবিয়ান/উবুন্টু ভিত্তিক সিস্টেমের জন্য: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

For Mandriva-based systems: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

এই সেটিংগুলো সমন্বিত করার পর, ঠিক আছে তে ক্লিক করুন। সংলাপ বাক্সটি বন্ধ হয়ে যাবে এবং একটি তথ্য বার্তা দেখতে পাবেন তাতে লিখা থাকবে LibreOffice প্রস্থান করে আবার  শুরু করলে ( মনে রাখবেন, যদি QuickStarter শুরু থাকে তবে তাও প্রস্থান করতে হবে) পরিবর্তনগুলো সক্রিয় হবে।

পরবর্তীতে LibreOffice চালালে, এটি আপনার ইনস্টলকৃত ভাষায় চালু হবে।

----------------------------------------------------------------------
প্রোগ্রাম শুরুর সময় ত্রুটি
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Windows ALPS/Synaptics নোটবই টাচপ্যাড
----------------------------------------------------------------------

একটি Windows ড্রাইভার বিষয়ের কারনে, ALPS/Synaptics টাচপ্যাডে আঙুল চালানোর সময় আপনি LibreOffice নথির মধ্যে স্ক্রল করতে পারবেন না।

টাচপ্যাড স্ক্রলিং সক্রিয় করতে, কনফিগারেশন ফাইলে নিচের লাইনটি যুক্ত করুন "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" , এবং কম্পিউটার রিটার্ট করুন:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

কনফিগারেশন ফাইলের অবস্থান উইন্ডোজের সংস্করণ ভেদে ভিন্ন হয়।

----------------------------------------------------------------------
শর্টকাট কী
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
জরুরি অ্যাক্সেসিবিলিটি নোট
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
ব্যবহারকারী সহায়তা
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
বাগ এবং ইস্যু রিপোর্টিং
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
সংযুক্ত হোন
----------------------------------------------------------------------

LibreOffice কমিউনিটি এই জরুরী ওপেন সোর্স প্রোজেক্ট উন্নয়নে আপনার কার্যকর অংশগ্রহনে অত্যন্ত উপকৃত হবে।

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

কিভাবে শুরু করতে হবে
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

সাবস্ক্রাইব
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* খবর: announce@documentfoundation.org *recommended to all users* (light traffic)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* সাধারণ ডেভেলপার তালিকা: libreoffice@তালিকাs.freedesktop.org (heavy traffic)

এক বা একাধিক প্রোজেক্টে অংশগ্রহন করুন
----------------------------------------------------------------------

যদি আপনার খুব কম সফটওয়্যার ডিজাইন বা কোডিং অভিজ্ঞতা থাকে তাহলেও আপনি এই জরুরী মুক্ত সোর্স প্রোজেক্টে বড় অবদান রাখতে পারেন। হ্যাঁ, আপনি!

আশা করি আপনি নতুন LibreOffice 26.2 এর সাথে কাজ করে আনন্দ পাচ্ছেন এবং অনলাইনে আমাদের সাথে যুক্ত হবেন।

লিবার অফিস কমিউনিটি

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
