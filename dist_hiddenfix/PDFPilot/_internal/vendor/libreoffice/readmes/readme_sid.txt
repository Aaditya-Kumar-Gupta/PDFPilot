
======================================================================
LibreOffice 26.2 Nabbawie
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

Tini fayle LibreOffice sofitiweere daafira horaamo mashalaqqe amaddinno. Tenne mashalaqqe Baysiisakkira albaanni wodanchite nabbawi.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

Isi LibreOffice Addinta ayee horonsi'raanora fanote?
----------------------------------------------------------------------

LibreOffice ayno horonsi'ra dandaanno. LibreOffice hinkiilo adhatenna dandaami geeshsha duucha kompiiterera baysiisanna, hasi'ni hajora (lawishshaho daddaloho, gashshooteho, dagate gashshootiranna rosu horora) horonsi'ra dandaatto/a. Gatino tittirshira LibreOffice baysiishshinni salloonnita fajjote borro lai.

LibreOffice ayee hororano mayra fano ikkino?
----------------------------------------------------------------------

Tenne hinkiilota LibreOffice baatoweelo horonsi'ra dandaatto/a korkaatuno fushshaanonna buusamaano irkisaano LibreOffice techora - alamete fanonna massagaancho buicho ikkitinota miniranna borrote minira qixxeessate sumiitino, uurrissino, jiffino, tirtino, maa'reekkitino, irkissino, dikko fushshitino, baca wole doogganni kaa'litino.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Baysiishshu Qaagiishsha
----------------------------------------------------------------------

LibreOffice muli attamoha Java Runtime Qarqarita (JRE) wo'ma kaa'lora hasi'ranno. JRE yaa LibreOffice baysiishshinni salo biso dikkitino.

Wodhote amuraate
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Gashshaanchu qoosso baysiishshu ha'rinshora hasiissannota afa hasiissannohe.

LibreOffice maareekkishshi hedeweelcho pirogiraame gede Microsoft Office formera wolqissanno woy aane nooha hajajote xuruura baysiisaanchu ledo ikkatenni gumulamanno:

* REGISTER_ALL_MSO_TYPES=1 , LibreOffice maareekkishsha Microsoft Office forme hedeweelcho pirogiraame gede wolqissanno.
* REGISTER_NO_MSO_TYPES=1 , LibreOffice maareekkishsha Microsoft Office forme hedeweelcho pirogiraame gede gumultanno.

Amuraatikkira ikkado fano qaaggo yannate geeshshi furchokkira nooheta buuxi'ri ballo, qoleno nabbawase, borreessasenna iillote qoosso agaramase hawaqi'ri ballo. Baysiishshu ha'rinsho hanafakkira albaanni wole pirogiraamma baala cufi.

Debian/Ubuntu-mereerso Linukisi amuraati aana assinanni LibreOffice baysiishsha
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Tini furcho "DEBS"yinannita cinaancho furcho amaddanno. Furcho "DEBS" widira soorri.

Furchotenni qiniite-qiphi assite ka'e "Open in Terminal" doodhi. Gawalote Hule fa'nantanno. Gawalote Hulera hajajote xuruurinni, aantanno hajajo eessi (hajajo loosu aana hosate albaanni kaimu horonsi'raanchikki saiqaale eessate deerra ledatto/a):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

suudo dpkg -i *.deb

Baysiishshu ha'rinsho xa gumulantinona, deskitoppekki Pirpgiraamma/Ofiisete mayno giddo noohetera baalante LibreOffice pirogiraammara bido heedhahera hasiisanno.

RPM usurra horonsi'ratenni Fedora, Suse, Mandriva nna woleno Linukisi amuraatta aanaLibreOffice baysiisa
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Tini furcho "RPMS"yinannita cinaancho furcho amaddanno. Furcho "RPMS" widira soorri.

Furchotenni qiniite-qiphi assite ka'e "Open in Terminal" doodhi. Gawalote Hule fa'nantanno. Gawalote Hulera hajajote xuruurinni, aantanno hajajo eessi (hajajo loosu aana hosate albaanni kaimu horonsi'raanchikki saiqaale eessate deerra ledatto/a):

For Fedora-based systems: sudo dnf install *.rpm

Mandriva-mereerso amuraattara: sudo urpmi *.rpm

Woloota RPM-mereerso amuraattara (Suse, wkl.): rpm -Uvh *.rpm

Baysiishshu ha'rinsho xa gumulantinona, deskitoppekki Pirpgiraamma/Ofiisete mayno giddo noohetera baalante LibreOffice pirogiraammara bido heedhahera hasiisanno.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Linukisi Tuqishshira Deskitoppete Karsiishsha La'anno Xawishshuwa Aliidi Baysiishshu Biddissuwa giddo Diworantino
----------------------------------------------------------------------

Tenne murantino baysiishshu biddissuwa giddo ikkikkinni wolootu Linukisi tuqishshuwa aana LibreOffice shotunni baysiisa dandiinanni. Badooshshu kalaqamate qara kaima ikkara dandaannohu deskitoppete karsiishshaati.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Afuu Usura baysiisa
----------------------------------------------------------------------

Hasiisannohe afiinna assootu amuraattira afuu usura dirrisi'ri. Qara baysiishshu mareekkimmanni mittu baychinni afantanno. Nautilus faylete gashshaanchinni, dirritino maareekko furchote giddo kalaqi (lawishshaho, deskitoppekkira). Baalanta LibreOffice pirogiraamma (hanafiha ikkiro, QuickStarter mitteenni) agurte fulakki hawaqi'ri.

Furcho dirrisi'rootto afuu usurira kalaqi'rootto furchora qolte soorri.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Xa furcho baysiisate usurra amaddino furchora soorri. Debian/Ubuntu-mereerso amuraatta aana, furcho ikkannohu DEBS. Fedora, Suse woy Mandriva amuraatta aana furcho ikkannohu RPMS.

Nautilus faylete gashshaanchinni, furchote giddo qiniite-qiphi assite ka'e "Open in terminal" hajajo doodhi. Fa'nootto/ate gawalote Hule giddo, afuu usura baysiisate hajajo loosiisi (baalante woriidi hajajuwa ledo, kaimu horonsi'raanchikki saiqaale eessate deerra lexxoottoha ikkanno):

Debian/Ubuntu-mereerso amuraattara: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Mandriva-mereerso amuraattara: sudo urpmi *.rpm

Woloota RPM-horonsi'rate amuraattara (Suse, wkl.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Hakkuri mamiwaro rageesso gedensaanni, OK aana qiphi assi. Hasaawu saaxine cufanteenna, soorrokki baqqeessantannohu LibreOfficenni fulitto/aronna marro qolte hanafitto/aro calla ikkinota mashalaqqissannohe sokka la"atto/a (QuickStarter hanafinoha ikkiro isono agurte fulakki buuxi'ri).

Aantanno yannara LibreOffice hanafatto/a, hanaffannohuno baysiisi'rootto/a afiinniiti.

----------------------------------------------------------------------
Pirogiraame Hanaffanno Woyti Mitiimmuwa
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
ALPS/Synaptics qaagishshumaaxaafi Hullo giddo
----------------------------------------------------------------------

Hulete oofaanchi widoonni, qubbichokki ALPS/Synaptics touchpad widoonni qolte islaydisatto/a woyte LibreOffice bortajubba giddoonni goshoosha didandaatto/a.

Goshoonshe touchpad ta dandeessate, woroonni noo xuruurra "C:\Pirogiraamete Faylla\Synaptics\SynTP\SynTPEnh.ini" qinoote faylera ledatenni, compiiterekki marro hanafi:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Qinoote fayle ofolla babbaxxinohu Hulete laalchi garinni soorrantara dandiitanno.

----------------------------------------------------------------------
Muraasu Qulfubba
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Hasiisannore Injeessammete Qaagishsha
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Horonsi'raanchu Irko
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
Bugise Rippoorte assate & Hajubba
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
Getting Involved
----------------------------------------------------------------------

LibreOffice Dagoomi tenne hasiissanno xawado buicho pirojekite latishshira assatto/a baqqitte beeqqokkinni addinta xaabbata horo afi'ranno.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

Hiittooni Hananfanni
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

Miiloo'mi
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* Odoo: announce@documentfoundation.org *baalante horonsi'raanora* (light traffic)
* Qara horonsi'raanchu dirto: users@global.libreoffice.org *hasaawa taxxi assate shota doogooti* (heavy traffic)
* Dikki'rote pirijekte: marketing@global.libreoffice.org *lophote aleenni* (getting heavy)
* Xaphooma lossaancho dirto: libreoffice@lists.freedesktop.org (heavy traffic)

Mitte woy roore Pirojektuwa Xaada
----------------------------------------------------------------------

Qara fushsho tenne hasiissino xawado buicho pirojektera assa dandaatto/a bikkancho softiweerete akeekishshi woy kooddisate rosichi hee'riherono. Maahoyye, Atinni!

Haaro LibreOffice 26.2nni loosakkinni hagiidhatto/a gedenna xaadooshshu giddoonni xaadattonke gede handeemmo. 

LibreOffice Dagitte

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
