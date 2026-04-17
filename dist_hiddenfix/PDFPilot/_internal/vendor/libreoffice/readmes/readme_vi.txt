
======================================================================
Tài liệu Đọc Đi LibreOffice 26.2
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

Tập tin này chứa thông tin về phần mềm LibreOffice. Bạn nên đọc kĩ trước khi cài đặt.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

Is LibreOffice Thực sự miễn phí?
----------------------------------------------------------------------

LibreOffice miễn phí cho mọi người. Có thể copy sản phẩm LibreOffice bao nhiêu bản tùy úy, dùng với bât kỳ mục đích nào (thương mại, danh mục công, giáo dục). Thông tin thêm xin xem trong giấy phép kèm theo LibreOffice.

Vì sao LibreOffice miễn phí cho mọi người?
----------------------------------------------------------------------

Bạn có quyền sao chép LibreOffice tự do không hạn chế vì rất nhiều cá nhân cũng như tổ chức đã thiết kế, phát triển, dịch, viết tài liệu, hỗ trợ, tiếp thị bằng nhiều cách khác nhau để LibreOffice thành công như ngày hôm nay - phần mềm văn phòng số một thế giới cho người dùng cá nhân cũng như doanh nghiệp.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Lưu ý khi cài đặt
----------------------------------------------------------------------

LibreOffice cần Java Runtime Environment (JRE) để có thể chạy đủ các chức năng. JRE không phài là một phần của gói cài đặt LibreOffice, do đó cần cài riêng.

Yêu cầu hệ thống
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Lưu ý rằng cần phải có quyền quản trị để chạy tiến trình cài đặt.

Chức năng đăng ký LibreOffice như là ứng dụng mặc định cho các định dạng MS Office cũng có thể được ép buộc hoặc thu hồi dùng những cái chuyển dòng lệnh theo đây với trình cài đặt:

* REGISTER_ALL_MSO_TYPES=1 will force registration of LibreOffice as default application for Microsoft Office formats.
* REGISTER_NO_MSO_TYPES=1 will suppress registration of LibreOffice as default application for Microsoft Office formats.

Bạn cần chuẩn bị đủ bộ nhớ và chỗ trống cho thư mục tạm cũng như quyền đọc/ghi. Hãy đóng các chương trình khác trước khi chạy trình cài đặt.

Cài đặt  LibreOffice vào Debian/Ubuntu
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Thư mục này chứa thư mục con "DEBS". Hãy chuyển đến thư mục "DEBS".

Nhấn chuột phải bên trong thư mục và chọn "Mở cửa sổ dòng lệnh". Cửa sổ dòng lệnh sẽ hiện ra. Nhập câu lệnh sau (bạn sẽ được yêu cầu nhập mật khẩu người dùng trước khi câu lệnh được thực thi):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Cài đặt hoàn tất, các biểu tượng của LibreOffice sẽ ở trong thực đơn Chương trình/Office.

Installation of LibreOffice on Fedora, openSUSE, Mandriva and other Linux systems using RPM packages
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Thư mục này chứa thư mục con "RPMS". Hãy chuyển đến thư mục "RPMS".

Nhấn chuột phải bên trong thư mục và chọn "Mở cửa sổ dòng lệnh". Cửa sổ dòng lệnh sẽ hiện ra. Nhập câu lệnh sau (bạn sẽ được yêu cầu nhập mật khẩu người dùng trước khi câu lệnh được thực thi):

For Fedora-based systems: sudo dnf install *.rpm

Với phiên bản Mandiva, dùng: sudo urpmi *.rpm

For other RPM-based systems (openSUSE, etc.): rpm -Uvh *.rpm

Cài đặt hoàn tất, các biểu tượng của LibreOffice sẽ ở trong thực đơn Chương trình/Office.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Chú ý về tích hợp với các phiên bản Linux không được đề cập tới trong hướng dẫn cài đặt ở trên
----------------------------------------------------------------------

LibreOffice có thể dễ dàng cài đặt trên các bản phân phối khác không liệt ở hướng dẫn cài đặt. Khó khăn có thể gặp phải chỉ là tích hợp với desktop.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Cài đặt gói ngôn ngữ
----------------------------------------------------------------------

Tải về gói ngôn ngữ cần thiết. Có thể tải về từ kho cài đặt chính. Với trình quản lý tệp Nautilus, giải nén kho đã tải về vào một thư mục nào đó (ví dụ, desktop). Trước khi cài đặt, đảm bảo rằng đã thoát khỏi  LibreOffice  (bao gồm cả quickstart).

Di chuyển tới thư mục đã giải nén gói ngôn ngữ.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Now change directory to the directory that contains the packages to install. On Debian/Ubuntu-based systems, the directory will be DEBS. On Fedora, openSUSE or Mandriva systems, the directory will be RPMS.

Từ trình quản lý tệp Nautilus, nhấp chuột phải vào thư mục và chọn "Mở bằng thiết bị đầu cuối". Trong cửa sổ thiết bị đầu cuối vừa được mở, thực hiện lệnh cài đặt gói ngôn ngữ (bằng dòng lệnh, và sẽ cần nhập mật khẩu của root):

Với Debian/Ubutun, dùng lệnh: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Với phiên bản Mandiva, dùng: sudo urpmi *.rpm

For other RPM-using systems (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Sau khi chỉnh các thiếp lập này, nhấn OK. Tắt hộp thoại, LibreOffice  sẽ thông báo rằng thay đổi chỉ có hiệu lực khi đã khởi động lại LibreOffice (Lưu ý rằng cần tắt Khởi động nhanh).

Ngôn ngữ đã cài đặt sẽ được dùng trong lần khởi động  LibreOffice  tiếp theo.

----------------------------------------------------------------------
Vấn đề trong khi khởi chạy chương trình
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Chuột lăn của máy tính xách tay ALPS/Synaptics cho Windows
----------------------------------------------------------------------

Do một vấn đề trình điều khiển Windows, bạn không thể cuộn qua tài liệu LibreOffice khi bạn trượt ngón tay qua một vùng sờ kiểu ALPS/Synaptics.

Để bật khả năng cuộn bằng chuột lăn, hãy thêm các dòng sau vào tập tin cấu hình "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini", sau đó khởi động lại máy tính:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Lưu ý: vaị trí của tập tin cấu hình có thể thay đổi tùy theo phiên bản của Windows.

----------------------------------------------------------------------
Phím tắt
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Ghi chú Khả năng Truy cập Quan trọng
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Hỗ trợ người dùng
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
Reporting Bugs & Issues
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
Tham gia 
----------------------------------------------------------------------

Cộng đồng LibreOffice sẽ rất biết ơn sự chủ động tham gia của bạn để việc phát triển dự án mã nguồn mở quan trọng này.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

How to Start
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Chỉ số dưới
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* Tin tức: announce@documentfoundation.org *khuyến nghị cho tất cả người dùng* (ít email)
* Main user list: users@global.libreoffice.org *easy way to lurk on discussions* (heavy traffic)
* Marketing project: marketing@global.libreoffice.org *beyond development* (getting heavy)
* Hộp thư phát triển nói chung libreoffice@lists.freedesktop.org (nhiều email)

Tham gia một hay nhiều dự án
----------------------------------------------------------------------

You can make major contributions to this important open source project even if you have limited software design or coding experience. Yes, you!

We hope you enjoy working with the new LibreOffice 26.2 and will join us online.

Cộng đồng LibreOffice

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
