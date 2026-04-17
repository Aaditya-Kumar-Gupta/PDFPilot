
======================================================================
LibreOffice 26.2 โปรดอ่าน (ReadMe)
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

ไฟล์นี้ประกอบด้วยข้อมูลสำคัญเกี่ยวกับซอฟต์แวร์ LibreOffice  กรุณาอ่านข้อมูลนี้อย่างละเอียดก่อนเริ่มติดตั้ง

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

LibreOffice ฟรีสำหรับผู้ใช้ใดๆ จริงหรือ?
----------------------------------------------------------------------

ผู้ใช้ทุกคนสามารถใช้ LibreOffice ได้ฟรี คุณสามารถนำเอาสำเนานี้ของ LibreOffice และติดตั้งลงในคอมพิวเตอร์กี่เครื่องก็ได้และใช้ตามวัตถุประสงค์ใดๆ (รวมถึงเพื่อการค้า งานราชการ การบริหารสาธารณะ และการศึกษา) สำหรับรายละเอียดเพิ่มเติมโปรดอ่านข้อความใบอนุญาตที่มาพร้อมกับ LibreOffice

ทำไม LibreOffice จึงฟรีสำหรับผู้ใช้ใดๆ ?
----------------------------------------------------------------------

คุณสามารถใช้สำเนานี้ของ LibreOffice วันนี้ได้ฟรีเพราะคนที่เป็นผู้ให้และหน่วยงานผู้สนับสนุนได้ออกแบบ พัฒนา ทดสอบ แปล ทำเอกสาร ให้สนับสนุน ทำการตลาดและช่วยเหลือในทางอื่นๆ อีกมากมายเพื่อทำให้ LibreOffice เป็นอย่างที่เป็นในวันนี้ คือเป็นผู้นำซอฟต์แวร์สผลิตภาพสำหรับบ้านและสำนักงานแบบโอเพ่นซอร์สของโลก

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
คำแนะนำการติดตั้ง
----------------------------------------------------------------------

LibreOffice ต้องใช้ Java Runtime Environment (JRE) เวอร์ชันใหม่ๆ เพื่อให้ทำงานได้อย่างเต็มที่ JRE ไม่ได้เป็นส่วนหนึ่งของแพ็คเกจการติดตั้ง LibreOffice  จึงต้องติดตั้งแยกกัน

ระบบที่ต้องการ
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

หมายเหตุ : โปรดทราบว่าสิทธิผู้ดูแลระบบจำเป็นสำหรับกระบวนการติดตั้ง

การลงทะเบียนให้ LibreOffice เป็นแอปพลิเคชันเริ่มต้นในการเปิดเอกสารรูปแบบของ Microsoft Office สามารถบังคับหรือห้ามได้โดยใช้คอมมานด์ไลน์สวิตช์ (command line switches) ต่อไปนี้กับโปรแกรมติดตั้ง:

* REGISTER_ALL_MSO_TYPES=1 จะบังคับให้ลงทะเบียน LibreOffice เป็นแอปพลิเคชันเริ่มต้นในการเปิดเอกสารรูปแบบของ Microsoft Office
* REGISTER_NO_MSO_TYPES=1 จะห้ามการลงทะเบียน LibreOffice เป็นแอปพลิเคชันเริ่มต้นในการเปิดเอกสารรูปแบบของ Microsoft Office

Please make sure you have enough free memory in the temporary directory on your system, and please ensure that read, write and run access rights have been granted. Close all other programs before starting the installation process.

Installation of LibreOffice on Debian/Ubuntu-based Linux systems
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

This directory contains a subdirectory called "DEBS". Change directory to the "DEBS" directory.

คลิกขวาภายในไดเร็คทอรีและเลือก "เปิดในเครื่องปลายทางหรือเทอร์มินัล" หน้าต่างเครื่องปลายทางจะเปิดขึ้น จากบรรทัดคำสั่งของหน้าต่างเครื่องปลายทาง ให้ป้อนคำสั่งต่อไปนี้ (คุณจะถูกบอกให้ป้อนรหัสผ่านของผู้ใช้รูทก่อนที่คำสั่งจะดำเนินการ):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

The installation process is now completed, and you should have icons for all the LibreOffice applications in your desktop's Applications/Office menu.

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

This directory contains a subdirectory called "RPMS". Change directory to the "RPMS" directory.

คลิกขวาภายในไดเร็คทอรีและเลือก "เปิดในเครื่องปลายทางหรือเทอร์มินัล" หน้าต่างเครื่องปลายทางจะเปิดขึ้น จากบรรทัดคำสั่งของหน้าต่างเครื่องปลายทาง ให้ป้อนคำสั่งต่อไปนี้ (คุณจะถูกบอกให้ป้อนรหัสผ่านของผู้ใช้รูทก่อนที่คำสั่งจะดำเนินการ):

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

หลังจากที่ปรับการตั้งค่าแล้ว คลิกตกลง กล่องโต้ตอบจะปิดลงและคุณจะเห็นข้อความที่บอกว่าการเปลี่ยนแปลงของคุณจะมีผลหลังจากที่ออกจาก LibreOffice และเริ่มต้นใหม่อีกครั้ง (อย่าลืมออกจาก QuickStarter ด้วยถ้ามันทำงานอยู่)

The next time you start LibreOffice, it will start in the language you just installed.

----------------------------------------------------------------------
ปัญหาเกิดขึ้นระหว่างโปรแกรมเริ่มการทำงาน
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
แผ่นสัมผัส ALPS/Synaptics touchpads ที่ใช้กับเครื่องโน้ตบุ๊คในระบบ Windows
----------------------------------------------------------------------

เนื่องจากปัญหาไดรเวอร์ของ Windows คุณไม่สามารถเลื่อนหน้าจอของเอกสาร LibreOffice เมื่อคุณสไลด์นิ้วผ่านแป้นสัมผัส ALPS/Synaptics

ในการเปิดการทำงานของการเลื่อนหน้าจอด้วยทัชแพด ให้เพิ่มบรรทัดต่อไปนี้เข้าไปยังไฟล์โครงแบบ "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" และรีสตาร์ทคอมพิวเตอร์ใหม่:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

ตำแหน่งของไฟล์กำหนดค่าอาจจะแตกต่างกันตามรุ่นของ Windows

----------------------------------------------------------------------
คีย์ลัด 
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
หมายเหตุสำคัญเกี่ยวกับการเข้าถึง
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
ช่วยเหลือผู้ใช้
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
การรายงานบั๊ก & ประเด็นปัญหา
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
ได้มีส่วนร่วม
----------------------------------------------------------------------

ชุมชน LibreOffice จะได้รับประโยชน์มากมายมายจากการมีส่วนร่วมของคุณในการพัฒนาของโครงงานโอเพ่นซอร์สที่สำคัญนี้

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

เริ่มต้นอย่างไร
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

ลงนาม
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* ข่าว: announce@documentfoundation.org *แนะนำสำหรับผู้ใช้ทั้งหมด* (การจราจรเบาบาง)
* เวทีอภิปรายหลักของผู้ใช้: users@global.libreoffice.org *วิธีง่ายๆ ในการดูว่าเขาหารืออะไรกัน* (จราจรหนาแน่น) 
* โครงการด้านการตลาด: marketing@global.libreoffice.org *ถัดไปจากการพัฒนา* (การจราจรเริ่มหนาแน่น)
* บัญชีจ่าหน้าทั่วไปของผู้พัฒนา: libreoffice@lists.freedesktop.org (จราจรหนาแน่น)

การเข้าร่วมโครงการหนึ่งหรือมากกว่า
----------------------------------------------------------------------

คุณสามารถเป็นผู้ช่วยสนับสนุนหลักในโครงงานโอเพนซอร์สที่สำคัญนี้แม้ว่าคุณจะมีประสบการณ์ในการออกแบบซอฟต์แวร์หรือเขียนโปรแกรมอย่างจำกัด 

เราหวังว่าคุณคงจะทำงานสนุกกับ LibreOffice 26.2 ใหม่และจะเข้าร่วมกับเราทางออนไลน์

ชุมชนลิเบอร์ออฟฟิศ

----------------------------------------------------------------------
ใช้/แก้ไข  ซอร์สโค้ด
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
