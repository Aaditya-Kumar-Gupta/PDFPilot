
======================================================================
ملف LibreOffice 26.2 المعلوماتيّ
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

يحوي هذا الملف معلومات هامّة حول برمجيّة LibreOffice. من المستحسن قراءة هذه المعلومات بعناية قبل بدء التثبيت.

مجتمع LibreOffice مسؤول عن تطوير هذا المنتج، ويدعوك للنظر في المشاركة كعضو فيخ. إن كنت مستخدمًا جديدًا، يمكنك زيارة موقع LibreOffice حيث ستجد مجموعة من المعلومات حول مشروع LibreOffice والمجتمعات الموجودة وراءه. انتقل إلى https://www.libreoffice.org/.

أحقًّا LibreOffice مجّانيّ لأيّ شخص؟
----------------------------------------------------------------------

LibreOffice مجاني لخدمة الجميع. يمكنك أخذ نسخة من LibreOffice وتثبيتها على أي عدد من الأجهزة تريد، ويمكنك استخدامها لأي غرض (ويشمل ذلك الاستخدام التجاري والحكومي والإدارات المدنية والاستخدام التعليمي).لمزيد من المعلومات طالع نص الرخصة المرفق مع LibreOffice.

لمَ LibreOffice مجّانيّ لأيّ شخص؟
----------------------------------------------------------------------

يمكنك استخدام هذه النسخة من LibreOffice مجانا بِلا رسوم لأن المتطوعين والشركات الراعية قاموا بالتصميم، والتطوير، والاختبار، والترجمة، والتوثيق، والدعم، والتسويق، والمساعدة بطرق متعددة لجعل LibreOffice كما هو اليوم - زعيم البرمجيات الإنتاجية مفتوحة المصدر في العالم للمنزل والمكتب.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
ملاحظات حول التثبيت
----------------------------------------------------------------------

يحتاج LibreOffice إصدارة حديثة من بيئة عمل جافا (JRE) ليعمل بكامل خصائصه. ليست JRE جزءا من حزمة تثبيت LibreOffice، ويجب تثبيتها بشكل مستقل.

متطلبات النظام
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

يرجى تذكر أن صلاحيات المدير مطلوبة لعملية التثبيت.

يمكن فرض تسجيل LibreOffice كتطبيق مبدئي لتنسيقات ميكروسوفت أوفيس أو إيقاف تسجيله باستخدام تبديلات سطور الأوامر التالية مع المثبت:

* ‏REGISTER_ALL_MSO_TYPES=1 سيُجبر تسجيل LibreOffice كتطبيق مبدئي لأنساق ميكروسوفت أوفيس.
* ‏REGISTER_NO_MSO_TYPES=1 سيُزيل تسجيل LibreOffice كتطبيق مبدئي لأنساق ميكروسوفت أوفيس.

من فضلك تأكد من أنه لديك مساحة كافية من الذاكرة في الدليل المؤقت على جهازك ، و من فضلك تأكد من أن حقوق القراءة ، الكتابة ، التشغيل ممنوحة . أغلق كافة البرامج قبل البدء في عملية التثبيت.

تثبيت LibreOffice على الأنظمة القائمة على ديبيان/أبونتو لينكس
----------------------------------------------------------------------

للتعليمات حول كيفية تثبيت حزمة لغة (بعد تثبيت إصدار الولايات المتحدة الإنجليزي من LibreOffice)، يرجى قراءة القسم أدناه بعنوان تثبيت حزمة لغة.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

هذا الدليل يحتوى على دليل فرعي يدعى "DEBS". غير الدليل إلى "DEBS".

انقر بزر الفأرة اﻷيمن فى الدليل واختر "فتح في الطرفية". ستظهر الطرفية. من سطر اﻷوامر، اكتب هذا اﻷمر (سوف يطلب منك ادخال كلمة سر المستخدم المسؤول قبل تفعيل اﻷمر):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

اكتملت عملية التثبيت، ويفترض أن تكون لك أيقونات لجميع تطبيقات LibreOffice فى تطبيقات سطح المكتب فى قائمة تطبيقات/المكتب.

تثبيت LibreOffice على فيدورا، أوبن سوزي، ماندريفا وأنظمة لينكس الأخرى باستخدام حزم RPM
----------------------------------------------------------------------

للتعليمات حول كيفية تثبيت حزمة لغة (بعد تثبيت إصدار الولايات المتحدة الإنجليزي من LibreOffice)، يرجى قراءة القسم أدناه بعنوان تثبيت حزمة لغة.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

هذا الدليل يحتوي على دليل فرعي يدعى "RPMS". غير الدليل إلى دليل "RPMS".

انقر بزر الفأرة اﻷيمن فى الدليل واختر "فتح في الطرفية". ستظهر الطرفية. من سطر اﻷوامر، اكتب هذا اﻷمر (سوف يطلب منك ادخال كلمة سر المستخدم المسؤول قبل تفعيل اﻷمر):

For Fedora-based systems: sudo dnf install *.rpm

للأنظمة القائمة على ماندريفا: sudo urpmi *.rpm

للأنظمة الأخرى القائمة على RPM (أوبن سوزي، إلخ): rpm -Uvh *.rpm

اكتملت عملية التثبيت، ويفترض أن تكون لك أيقونات لجميع تطبيقات LibreOffice فى تطبيقات سطح المكتب فى قائمة تطبيقات/المكتب.

إضافة إلى ذلك، يمكنك استخدام سكرِبت 'install' الموجود في الدليل فوق مستوى هذا الأرشيف للتثبيت كمُستخدِم. سيضبط هذا السكرِبت LibreOffice ليملك ملف تعريف لهذا التثبيت منفصلًا عن ملف التعريف الطبيعي لـ LibreOffice. لاحظ أن هذا لن يثبّت أجزاء تكامل النظام مثل عناصر القائمة وتسجيلات نوع MIME لسطح المكتب.

الملاحظات المتعلقة بالتكامل مع سطح المكتب لتوزيعات اللينكس غير مغطاة في تعليمات التثبيت بالأعلى
----------------------------------------------------------------------

ينبغي أن يكون تنزيل LibreOffice ممكنا بسهولة على توزيعات لينكس الأخرى التي لم تغطى بالتحديد في تعليمات التثبيت هذه. الجانب الرئيسي في الاختلافات ربما يواجه في التكامل مع سطح المكتب.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

تنزيل حزمة لغة
----------------------------------------------------------------------

نزل حزمة اللغة للّغة والمنصة المرغوبة. تلك الحزم متوفرة من نفس مكان أرشيف التثبيت الرئيسي. من مدير ملفات Nautilus، استخرج الأرشيف المنزّل إلى دليل ملفات (في سطح المكتب، مثلاٌ). تأكد من أنك خرجت من كل تطبيقات LibreOffice (بما في ذلك التشغيل السريع، إذا كان قد بدأ).

غير الدليل إلى الدليل الذي استخرجت فيه حزمة اللغة المنزلة.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

الآن غير الدليل إلى الدليل المحتوي على حزم التنزيل. في الأنظمة المعتمدة على ديبيان/أبونتو، الدليل سيكون DEBS. على أنظمة فيدورا، أوبن سوزي أو ماندريفا، الدليل سيكون RPMS.

من مدير ملفات Natilus، انقر بالزر الأيمن على الدليل واختر الأمر "افتح في الطرفية". في نافذة الطرفية التي فتحتها للتو، نفذ الأمر لتثبيت حزمة اللغة (مع كل الأوامر التي بالأسفل، ربما يطلب منك إدخال كلمة سر مسؤول النظام):

للأنظمة المعتمدة على ديبيان/أبونتو: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

للأنظمة القائمة على ماندريفا: sudo urpmi *.rpm

للأنظمة الأخرى التي تستخدم RPM (أوبن سوزي، إلخ): rpm -Uvh *rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

بعد ضبط هذه الإعدادات، انقر على حسنًا. صندوق الحوار سوف يغلق، وسترى رسالة معلومة تخبرك بأن التعديلات سيتم تفعيلها فقط عندما تغلق LibreOffice وتعيد تشغيله مرة أخرى (تذكر أن تخرج من التشغيل السريع إذا كان قد بدأ).

في المرة القادمة التي تبدأ فيها LibreOffice، سيبدأ باللغة التي قمت بتنزيلها مؤخرًا.

----------------------------------------------------------------------
المشكلات التي تحدث أثناء بدء تشغيل البرنامج
----------------------------------------------------------------------

صعوبات بدء LibreOffice (مثلا علوق التطبيقات) وكذا مشاكل عَرض الشاشة يسببها غالبًا مشغّل بطاقة الرسوميات. إذا حصلت هذه المشاكل فالرجاء تحديث مشغّل بطاقة الرسوميات لديك أو محاولة استخدام مشغّل الرسوميات المُعطى مع نظام التشغيل لديك.

----------------------------------------------------------------------
لوحات لمس الحاسوب المحمول ALPS/Synaptics في ويندوز
----------------------------------------------------------------------

بسبب وجود مشكلة في برنامج تشغيل ويندوز، لا يمكنك التمرير عبر مستندات LibreOffice عند وضع إصبعك على لوحة لمس ALPS/Synaptics.

لتمكين تمرير لوحة اللمس، قم بإضافة السطور التالية إلى ملف التكوين "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" وأعد تشغيل الحاسوب.

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

قد يختلف موقع ملف التكوين على الإصدارات المختلفة من ويندوز.

----------------------------------------------------------------------
اختصارات المفاتيح
----------------------------------------------------------------------

يمكن استخدام مفاتيح الاختصار (مجموعات المفاتيح) غير المستخدمة بواسطة نظام التشغيل فقط في LibreOffice. إذا لم تعمل مجموعة مفاتيح في LibreOffice كما هو موضح في تعليمات LibreOffice، فتحقق مما إذا كان هذا الاختصار قيد الاستخدام بالفعل بواسطة نظام التشغيل. لتصحيح هذه التعارضات، يمكنك تغيير المفاتيح المعينة بواسطة نظام التشغيل. وبدلًا من ذلك، يمكنك تغيير أي تعيين مفتاح تقريبًا في LibreOffice. للاطلاع على مزيد من المعلومات حول هذا الموضوع، راجع مساعدة LibreOffice أو وثائق المساعدة الخاصة بنظام التشغيل.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
ملاحظات مهمة عن قابلية الوصول
----------------------------------------------------------------------

لمزيد من المعلومات عن ميزات قابلية الوصول في LibreOffice، انظر https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
دعم المستخدم
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
الإبلاغ عن العلل و المشاكل
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
المشاركة
----------------------------------------------------------------------

قد يستفيد مجتمع LibreOffice بشكل كبير من المشاركة النشطة في تطوير مشروع المصدر المفتوح المهم هذا.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

كيفية البدء
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

اشترك
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* الأخبار: announce@documentfoundation.org *ينصح بها لكل المستخدمين* (خفيفة النشاط)
* قائمة المستخدمين الرئيسية: users@global.libreoffice.org *طريقة سهلة لمتابعة النقاش* (عالية النشاط)
* مشروع التسويق: marketing@global.libreoffice.org *ما بعد التطوير* (متوسطة النشاط)
* قائمة المطورين العامة: libreoffice@lists.freedesktop.org (عالية النشاط)

الانظمام لواحد أو أكثر من المشاريع
----------------------------------------------------------------------

يمكنك عمل مساهمات كبيرة بمشروع المصدر المفتوح المهم هذا حتى لو كانت خبرتك بتصميم البرنامج أو الترميز محدودة. نعم، أنت!

نأمل أن تستمتع بالعمل على LibreOffice 26.2 الجديد وأن تنضم إلينا عبر الشابكة.

مجتمع ليبرأوفيس

----------------------------------------------------------------------
كود مصدري مستخدم / معدل
----------------------------------------------------------------------

حقوق محفوظة جزئيا 1998، 1999 جيمس كلارك. حقوق محفوظة جزئيا 1996، 1998 شركة نِت‌سكيب للاتصالات.
