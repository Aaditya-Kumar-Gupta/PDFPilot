
======================================================================
LibreOffice 26.2 రీడ్‌మీ
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

ఈ LibreOffice అనువర్తనం గురించి ముఖ్యమైన  వివరాలు ఈ ఫైల్ లో వున్నాయి. వాడటానికి ముందుముందు చాలా జాగ్రత్తగా ఈ వివరాలు చదవండి

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

LibreOffice ఎవరికైనా ఉచితమేనా? 
----------------------------------------------------------------------

LibreOffice అందరికి ఉచితం.  LibreOfficeనకలు తీసుకొని  మీకు కావలసినన్ని కంప్యూటర్లపై స్థాపించవచ్చు, మరియు ఏ అవసరానికైనా(వ్యాపార, ప్రభుత్వ, ప్రజాపాలన, విద్య తోపాటు). మరిన్ని వివరాలకు  LibreOffice తోజతచేసిన లైసెన్సు  పాఠ్యం చూడండి .

LibreOffice ఎందుకని ఎవరికైనా ఉచితం?
----------------------------------------------------------------------

LibreOffice ఉచితంగా వాడుకొనవచ్చు ఎందుకంటే , వ్యక్తులు, సంస్థ దాతలు దీని నిర్మాణానికి, పరీక్షకు, అనువాదాలకు, పుస్తకాలకు, సహాయానికి, ప్రచారానికి  చాలా రకాలుగా  ఈ  LibreOffice -  ప్రపంచపు  ప్రజాదరణ గల స్వేచ్ఛా మూలాల ఉత్పాదకత సాఫ్ట్వేర్ ఇంట్లోకి మరియు కార్యాలయానికి,  స్థాయి కి తీసుకొచ్చారు  

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
నోట్ లను నెలకొల్పడం
----------------------------------------------------------------------

పూర్తి ప్రమేయత కొరకు LibreOffice కు సరికొత్త జావా రన్‌టైమ్ యెన్విరాన్మెంట్ (JRE) అవసరం. JRE అనునది LibreOffice సంస్థాపన ప్యాకేజీ నందు బాగంకాదు, అది ప్రత్యేకంగా సంస్థాపించాలి.

వ్యవస్థ అవసరాలు:
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

సంస్థాపనా కార్యక్రమము కొరకు నిర్వహణాధికారి హక్కులు కావలెనని తెలుసుకోండి.

మైక్రోసాఫ్ట్ ఆఫీస్ ఫైళ్లకి LibreOffice అప్రమేయం అనువర్తనంగా చేయుట లేక తొలగించుటకు స్థాపనఆదేశ వరుసలో వాడే పరామితులు:

* Microsoft Office ఫార్మాట్స్ కొరకు REGISTER_ALL_MSO_TYPES=1 అనునది LibreOffice యొక్క నమోదీకరణ అప్రమేయ అనువర్తనంవలే చేయుటకు వత్తిడి చేయును.
* Microsoft Office ఫార్మాట్స్ కొరకు REGISTER_NO_MSO_TYPES=1 అనునది LibreOffice యొక్క నమోదీకరణ అప్రమేయ అనువర్తనంవలె చేయును.

మీ వ్యవస్థలోని తాత్కాలిక సంచయంలో  చాలినంత ఖాళీ మెమరీ   వున్నదని, మరియు రాయుట, చదువుట మరియు నడుపుట హక్కులు ఇవ్వబడినవని నిర్ధారించుకోండి.  స్థాపనాపద్ధతి   ప్రారంభించే  ముందు, అన్ని ఇతర ప్రోగ్రాములు మూయండి.

డెబియన్/ఉబుంటు అధారిత లినక్స్  వ్యవస్థలకొరకు LibreOffice స్థాపన 
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

ఈ సంచయంలో "DEBS" అనే ఉపసంచయం వుంటుంది. దానిలోకి మారండి.

సంచయం లో మౌస్ పై కుడి మీట నొక్కి "టర్మినల్ లో తెరుచు" ఎంచుకో. టర్మినల్ విండో తెరుచుకుంటుంది.ఆదేశం వరుస నుండి క్రింది ఆదేశం ప్రవేశపెట్టండి ( ఆదేశం నడిపేముందు మీ రూట్ వాడుకరి సంకేతపదం ప్రవేశపెట్టటానికి సందేశాలు కనబడతాయి):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

స్థాపించు పద్ధతి ఇప్పుడు పూర్తయింది. ఇప్పుడు LibreOffice  యొక్కఅన్ని అనువర్తనములకు చిహ్నాలురంగస్థలంలో అనువర్తనములు/కార్యాలయం  లో వుండాలి.

RPM  పాకేజీలు వాడి ఫెడోరా, ఓపెన్‌సూసె,  మాండ్రివా మరియు ఇతర  లినక్స్  వ్యవస్థలలో LibreOffice స్థాపన
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

ఈ సంచయంలో "RPMS" అనే ఉపసంచయం వుంటుంది. దానిలోకి మారండి.

సంచయం లో మౌస్ పై కుడి మీట నొక్కి "టర్మినల్ లో తెరుచు" ఎంచుకో. టర్మినల్ విండో తెరుచుకుంటుంది.ఆదేశం వరుస నుండి క్రింది ఆదేశం ప్రవేశపెట్టండి ( ఆదేశం నడిపేముందు మీ రూట్ వాడుకరి సంకేతపదం ప్రవేశపెట్టటానికి సందేశాలు కనబడతాయి):

For Fedora-based systems: sudo dnf install *.rpm

మాండ్రివ-అధార వ్యవస్థలకొరకు: sudo urpmi *.rpm

ఇతర RPM-అధార వ్యవస్థ (openSUSE, మొదల.): rpm -Uvh *.rpm

స్థాపించు పద్ధతి ఇప్పుడు పూర్తయింది. ఇప్పుడు LibreOffice  యొక్కఅన్ని అనువర్తనములకు చిహ్నాలురంగస్థలంలో అనువర్తనములు/కార్యాలయం  లో వుండాలి.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

పై స్థాపన  సూచనలు సరిపోని  వారి లినక్స్  పంపిణిలలో రంగస్థలం సమాకలనం కొరకు గమనికలు
----------------------------------------------------------------------

స్థాపన సూచనలలో లేని ఇతర  లినక్స్  పంపిణిలలో LibreOffice స్థాపించుట వీలవుతుంది. రంగస్థలం సమాకలనంలో  ప్రధాన తేడాలుండవచ్చు.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

భాష కవిలె (లాంగ్వేజ్ పాక్) స్థాపించు
----------------------------------------------------------------------

మీకు కావలసిన కంప్యూటర్ ప్లాట్ఫారం లో  మీ కిష్టమైన  భాష కొరకు భాష కవిలె (లాంగ్వేజ్ పాక్)  పొందండి.  ప్రధాన  స్థాపన ఆర్కైవు ఎక్కడ పొందారో అక్కడే  అవికూడా వుంటాయి. నాటిలస్ ఫైల్ నిర్వాహకి నుండి, పొందిన ఆర్కైవు మీకు కావలసిన సంచయంలో  (ఉదాహరణకు రంగస్థలం (desktop))  విప్పండి.  LibreOffice  అనువర్తనముల (QuickStarter తో సహా, అది ప్రారంభమైవుంటే)  నుండి నిష్క్రమించారని నిర్ధారించుకోండి

మీరు పొందిన  భాష కవిలె (లాంగ్వేజ్ పాక్) ఎక్కడ విప్పారో అ సంచయంలోకి మారండి

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

మీరు  ఏ సంచయంలో  స్థాపన కవిలెలు (పాకేజీలు)  వున్నాయో  అ సంచయంలోకి మారండి. ఉదాహరణకు  డెబియన్/ఉబుంటు అధార వ్యవస్థ లో  DEBS అనే సంచయం. ఫెడోరా, ఓపెన్‌సూసె,మాండ్రీవా వ్యవస్థలలో  సంచయం పేరు RPMS.

నాటిలస్ ఫైల్ నిర్వాహకిలో  మీకు కావలసిన సంచయం పై మౌస్  సూచికను వుంచి, కుడి మీట నొక్కి "టర్మినల్ లో తెరుచు" ఎంచుకో. టర్మినల్ విండో తెరుచుకుంటుంది.ఆదేశం వరుస నుండి భాష కవిలె (లాంగ్వేజ్ పాక్)   స్థాపన ఆదేశం నడపండి (  ఈ క్రింది ఆదేశాలన్నిటిని నడిపేముందు మీ రూట్ వాడుకరి సంకేతపదం ప్రవేశపెట్టటానికి సందేశాలు కనబడతాయి):

డెబియన్/ఉబుంటుఅధార వ్యవస్థలకు: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

మాండ్రివ-అధార వ్యవస్థలకొరకు: sudo urpmi *.rpm

ఇతర RPM-వినియోగ వ్యవస్థలు (openSUSE, మొదల.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

అమర్పులు మార్చినతరువాత,  సరే నొక్కండి. సంవాద పెట్టె మూయబడుతుంది.  మీరు చేసిన మార్పులు LibreOffice  ను నిష్క్రమించి  మరల ప్రారంభించితేనే  చేతనమవుతాయనే సందేశం కనబడుతుంది. (QuickStarter  ప్రారంభమైవుంటే దానిని కూడా నిష్క్రమించాలని గుర్తుంచుకోండి) 

తరువాత సారి LibreOffice     ప్రారంభించినపుడు , మీరు స్థాపించిన భాషతో ప్రారంభమవుతుంది.

----------------------------------------------------------------------
ప్రోగ్రామ్ స్టార్టప్‌నందు సమస్యలు
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
పాడులువిండోలలో ALPS/సినాప్టిక్ నోట్బుక్ టచ్పాడులు
----------------------------------------------------------------------

విండోస్ డ్రైవర్ సమస్య కారణంగా, మీరు మీ వ్రేలును ALPS/Synaptics టచ్‌పాడ్ గుండా జరుపుతున్నప్పుడు మీరు LibreOffice పత్రముల గుండా స్క్రాలు చేయలేరు.

టచ్ ప్యాడు ద్వారా జరుపుటకు, "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" వాక్యమును configuration ఫైల్ నకు జత చేసి, మీ కంప్యూటర్ ను పునఃప్రారంభించండి:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

గమనిక: కానిఫిగరేషన్ ఫైల్  యొక్కా స్థానం వివిధ గావాక్షాల విడుదల లో వేరుగా ఉండవచ్చు

----------------------------------------------------------------------
అడ్డ దారి మీటలు
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
ముఖ్యమైన అనుకూలపరచు  గమనికలు
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
వాడుకరికి సహకరించు 
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
బగ్ & సమస్యలు నివేదన
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
తీసుకొని చిక్కుకున్న
----------------------------------------------------------------------

LibreOffice సముదాయం ఈ ముఖ్యమైన స్వేచ్ఛా మూల పథకంలో మీ క్రియాశీలక భాగస్వామ్యంతో చాలా లాభపడుతుంది. 

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

ప్రారంభముకు దారి
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

చందాదారుకండి
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* వార్తలు: announce@documentfoundation.org *అన్ని వాడుకరులకు సిఫారస్ చేయబడినది* (కొద్దిపాటి సంభాషణలు)
* ముఖ్య వాడుకరి జాబితా: users@global.libreoffice.org *చర్చలలో పాల్గొనుటకు సులువైన మార్గం* (అధిక ట్రాఫిక్)
* ప్రచార పథకం: marketing@global.libreoffice.org *అభివృద్ధి తర్వాత* (అత్యంత ఎక్కువ సంభాషణల స్థాయికి చేరుతోంది)
* సాధారణ  అభివృద్ధికారి జాబితా: libreoffice@lists.freedesktop.org  (అత్యంత ఎక్కువ సంభాషణలు)

ఒకటి లేక ఎక్కువ పథకములు చేర్చు
----------------------------------------------------------------------

పెద్దవైన సహాయాన్ని మీకు సాఫ్ట్వేర్ అనుభవం అంతగాలేకపోయినా చేయవచ్చు. అవును. మీరే!

మీరు  కొత్త LibreOffice 26.2 తో పనిచేయుటను అనందిస్తున్నారని మరియు ఆన్‌లైన్ నందు మాతో చేరుతారని ఆశిస్తున్నాము.

 లిబ్రెఆఫీస్ సముదాయం

----------------------------------------------------------------------
Used / Modified Source Code
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
