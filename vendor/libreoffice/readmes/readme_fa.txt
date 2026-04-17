
======================================================================
LibreOffice 26.2 مرا بخوان
======================================================================


برای مشاهده آخرین به روز رسانی پرونده مرا بخوان، بروید به https://git.libreoffice.org/core/tree/master/README.md

این پرونده حاوی اطلاعات مهمی درباره نرم‌افزار LibreOffice است. توصیه می‌شود که قبل از نصب کردن این اطلاعات را با دقت بخوانید.

اجتماع LibreOffice مسؤولیت پیشرفت این محصول را برعهده دارد, و از شما دعوت می کند به عنوان عضوی از این مجموعه مشارکت داشته باشید. اگر شما کاربر جدیدی هستید, می توانید از سایت LibreOffice دیدن فرمایید, جایی که می توانید اطلاعات بسیاری درباره پروژه LibreOffice و اجتماعات موجود حول آن بیاید. بروید به  https://fa.libreoffice.org/.

آیا LibreOffice واقعاً برای همه کاربران رایگان است؟
----------------------------------------------------------------------

LibreOffice برای استفاده همگان رایگان است. شما می‌توانید یک رو‌نوشت از LibreOffice بردارید و آن را روی هر تعداد رایانه‌ای که دوست دارید نصب کنید، و آن را برای هر هدفی که دوست دارید استفاده کنید (شامل استفاده تجاری، حکومتی، مدیریت همگانی و آموزشی). برای جزئیات بیشتر متن اجازه‌نامه را که همراه بار‌گیری این LibreOffice بسته‌بندی‌ شده است ببینید.

چرا LibreOffice برای همه کاربران رایگان است؟
----------------------------------------------------------------------

شما می‌توانید به‌رایگان از رونوشتی از LibreOffice استفاده کنید؛ زیرا مشارکت‌کنندگان فردی و حامیان مالی متعددی در طراحی، توسعه، آزمایش، مستندسازی و بازاریابی این محصول تلاش کرده و با یاری آن‌ها بهترین بسته نرم‌افزاری تولید محتوای در دنیای نرم‌افزار آزاد، LibreOffice تولید شده است که در خانه و اداره در دسترس شماست.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
نکاتی درباره نصب
----------------------------------------------------------------------

LibreOffice requires a recent version of Java Runtime Environment (JRE) for full functionality. JRE is not part of the LibreOffice installation package, it should be installed separately.

نیازمندی های سامانه
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Please be aware that administrator rights are needed for the installation process.

Registration of LibreOffice as default application for Microsoft Office formats can be forced or suppressed by using the following command line switches with the installer:

* REGISTER_ALL_MSO_TYPES=1 will force registration of LibreOffice as default application for Microsoft Office formats.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

لطفاً مطمئن شوید که در شاخه موقت رایانه خود به اندازه کافی حافظه‌ی آزاد دارید، و لطفاً مطمئن شوید که دسترسی‌های خواندن، نوشتن و اجرا شدن اعطا شده باشد. قبل از آغاز فرایند نصب تمام برنامه‌های دیگر را ببندید.

Installation of LibreOffice on Debian/Ubuntu-based Linux systems
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

این شاخه حاوی یک زیر‌شاخه به‌نام "DEBS" است. به شاخه "DEBS" تغییر شاخه بدهید.

داخل شاخه کلیک راست کرده و «باز کردن در پایانه» را برگزینید. پنجره پایانه باز خواهد شد. از خط فرمان پنجره پایانه، دستور زیر را وارد کنید (از شما خواسته خواهد شد که گذر‌واژه کاربر ریشه را قبل از اجرا شدن دستور وارد کنید):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

This directory contains a subdirectory called "RPMS". Change directory to the "RPMS" directory.

داخل شاخه کلیک راست کرده و «باز کردن در پایانه» را برگزینید. پنجره پایانه باز خواهد شد. از خط فرمان پنجره پایانه، دستور زیر را وارد کنید (از شما خواسته خواهد شد که گذر‌واژه کاربر ریشه را قبل از اجرا شدن دستور وارد کنید):

For Fedora-based systems: sudo dnf install *.rpm

برای سیستم‌های مبتنی بر مندریوا: sudo urpmi *.rpm

برای دیگر سیستم‌هایی که از RPM استفاده می‌کنند (اوپن‌سوسه و غیره): rpm -Uvh *.rpm

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Notes Concerning Desktop Integration for Linux Distributions Not Covered in the Above Installation Instructions
----------------------------------------------------------------------

It should be easily possible to install LibreOffice on other Linux distributions not specifically covered in these installation instructions. The main aspect for which differences might be encountered is desktop integration.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Installing a Language Pack
----------------------------------------------------------------------

Download the language pack for your desired language and platform. They are available from the same location as the main installation archive. From the Nautilus file manager, extract the downloaded archive into a directory (your desktop, for instance). Ensure that you have exited all LibreOffice applications (including the QuickStarter, if it is started).

به شاخه‌ای که بسته زبان‌تان را در آن استخراج کرده‌اید تغییر شاخه بدهید.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

از مدیر پرونده ناتیلوس، در شاخه کلیک راست کرده و دستور «باز کردن در پایانه» را برگزینید. در پنجره پایانه‌ای که تنها آن را باز کرده‌اید، دستور را اجرا کنید تا بسته زبان نصب شود (با تمام دستورات زیر، به شما اعلان خواهد شد که گذر‌واژه کاربر ریشه را وارد کنید):

برای سیستم‌های مبتنی بر دبین/اوبونتو: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

برای سیستم‌های مبتنی بر مندریوا: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

After adjusting those settings, click on OK. The dialog box will close, and you will see an information message telling you that your changes will only be activated after you exit LibreOffice and start it again (remember to also exit the QuickStarter if it is started).

بار بعد که LibreOffice را آغاز کنید، در زبانی که نصبش کرده‌اید آغاز خواهد شد.

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

* News: announce@documentfoundation.org *recommended to all users* (light traffic)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* General developer list: libreoffice@lists.freedesktop.org (heavy traffic)

ملحق شدن به یک طرح یا بیشتر
----------------------------------------------------------------------

You can make major contributions to this important open source project even if you have limited software design or coding experience. Yes, you!

We hope you enjoy working with the new LibreOffice 26.2 and will join us online.

انجمن لیبره‌آفیس

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
