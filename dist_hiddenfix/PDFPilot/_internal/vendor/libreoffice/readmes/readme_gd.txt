
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

Tha fiosrachadh cudromach san fhaidhle seo mun bhathar-bhog LibreOffice. Mholamaid dhut am fiosrachadh seo a leughadh gu cùramach mus tòisich thu air an stàladh.

’S e coimhearsnachd LibreOffice a tha an urra ri leasachadh a' bhathar seo agus tha iad a’ cur fàilte ort pàirt a ghabhail sa choimhearsnachd seo. Mas e cleachdaiche ùr a tha annad, ’s urrainn dhut tadhal air làrach LibreOffice far am faigh thu torr fiosrachaidh mu phròiseact LibreOffice agus na coimhearsnachdan ’na lùib. Tadhail air https://www.libreoffice.org/.

A bheil LibreOffice saor an-asgaidh airson a h-uile duine gu dearbh?
----------------------------------------------------------------------

Tha LibreOffice saor an-asgaidh airson a h-uile duine. Tha cead agad an lethbhreac seo de LibreOffice a stàladh airson uiread a choimpiutairean a thogras tu agus a chùm rud sam bith a thogras tu (a’ gabhail a-steach cleachdadh malairteach, riaghaltais, rianachd phoblach agus oideachais). Thoir sùil air teacsa a’ cheadachais a fhuair thu an cois LibreOffice airson barrachd fiosrachaidh.

Carson a tha LibreOffice saor an-asgaidh airson a h-uile duine?
----------------------------------------------------------------------

Tha an lethbhreac seo de LibreOffice saor an-asgaidh dhut a chionn 's gun d' fhuair e taic dealbhaidh, deuchainnidh, eadar-theangachaidh, clàraidh, airgid is margaideachd o iomadh duine agus luchd-urrais corporra - a chuidich leinn air iomadh dòigh eile cuideachd - gus LibreOffice a thoirt gu buil agus 's e am bathar-bog le còd saor airson na dachaigh 's na h-oifis a tha air thoiseach air càch a tha ann an-diugh.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Nòtaichean stàlaidh
----------------------------------------------------------------------

Feumaidh LibreOffice tionndadh ùr de Java Runtime Environment (JRE) mus obraich e gu ceart. Chan eil JRE 'na phàirt dhen phacaid stàlaidh airson LibreOffice agus bidh agad ri stàladh leis fhèin.

Comasan an t-siostaim air a bheil feum
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Thoir an aire gu bheil feum air còraichean rianachd airson a stàladh.

'S urrainn dhut LibreOffice a chlàradh mar an aplacaid bhunaiteach airson faidhlichean Microsoft Office, no gun a chlàradh, leis na h-àitheantan a leanas on stàlaichear:

* Èignichidh REGISTER_ALL_MSO_TYPES=1 clàradh de LibreOffice mar an aplacaid bhunaiteach airson fòrmatan Microsoft Office.
* Bacaidh REGISTER_ALL_MSO_TYPES=1 clàradh de LibreOffice mar an aplacaid bhunaiteach airson fòrmatan Microsoft Office.

Dèan cinnteach gu bheil cuimhne shaor gu leòr agad sa phasgan sealach agad agus gu bheil cead leughaidh, sgrìobhaidh is ruith ann mar bu chòir. Dùin gach prògram eile mus tòisich thu air an stàladh.

Stàladh LibreOffice air siostaman Linux stèidhichte air Debian/Ubuntu
----------------------------------------------------------------------

Airson stiùireadh air stàladh pacaid cànain (as dèidh dhut an tionndadh Beurla de LibreOffice a stàladh), leugh an earrann gu h-ìosal air a bheil "A' stàladh pacaid cànain".

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Tha fo-phasgan san eòlaire seo air a bheil "DEBS". Thoir leum dhan phasgan "DEBS".

Dèan briogadh deas sa phasgan 's tagh "Open in Terminal". Fosglaidh uinneag tèirmineil. Cuir an àithne a leanas san loidhne àithne san uinneag tèirmineil (thèid iarraidh ort am facal-faire Root agad a chur a-steach mus dèid an àithne a chur an gnìomh):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Tha an stàladh deiseil agus bu chòir dha na h-ìomhaigheagan aig LibreOffice a bhith sa chlàr-taice Applications/Office air an deasg agad.

Stàladh de LibreOffice air Fedora, openSUSE, Mandriva agus siostaman Linux eile le pacaidean RPM
----------------------------------------------------------------------

Airson stiùireadh air stàladh pacaid cànain (as dèidh dhut an tionndadh Beurla de LibreOffice a stàladh), leugh an earrann gu h-ìosal air a bheil "A' stàladh pacaid cànain".

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Tha fo-phasgan san eòlaire seo air a bheil "RPMS". Thoir leum dhan phasgan "RPMS".

Dèan briogadh deas sa phasgan 's tagh "Open in Terminal". Fosglaidh uinneag tèirmineil. Cuir an àithne a leanas san loidhne àithne san uinneag tèirmineil (thèid iarraidh ort am facal-faire Root agad a chur a-steach mus dèid an àithne a chur an gnìomh):

For Fedora-based systems: sudo dnf install *.rpm

Airson siostaman stèidhichte air Mandriva: sudo urpmi *.rpm

Airson siostaman eile stèidhichte air RPM (openSUSE is msaa.): rpm -Uvh *.rpm

Tha an stàladh deiseil agus bu chòir dha na h-ìomhaigheagan aig LibreOffice a bhith sa chlàr-taice Applications/Office air an deasg agad.

No 's urrainn dhut an sgriobt "install" a chleachdadh a tha ann am pasgan as àirde na tasg-lainn seo gus a stàladh mar chleachdaiche. Suidhichidh an sgriobt LibreOffice air dòigh 's gum bi a' phròifil fa leth aige airson an stàlaidh seo, fa leth on phròifil LibreOffice àbhaisteach agad. Thoir an aire nach stàlaich seo pìosan innteagrachadh an t-siostaim mar buill clàr-taice an deasga agus MIME Type Registrations.

Nòtaichean mun Desktop Integration air sgaoilidhean Linux nach deach a mhìneachadh gu h-àrd san treòir stàlaidh
----------------------------------------------------------------------

Chan eil dùil gum biodh e doirbh LibreOffice a stàladh air sgaoilidhean eile de Linux nach deach a mhìneachadh san treòir stàlaidh seo. 'S e an Desktop Integration an rud a tha dualach a bhith eadar-dhealaichte.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Mar a stàlaicheas tu pacaid cànain
----------------------------------------------------------------------

Luchdaich a-nuas a' phacaid cànain airson do chànain 's an ùrlair agad. Gheibh thu iad san dearbh àite a fhuair thu am prìomh thasg-lann stàlaidh. Fosgail am manaidsear fhaidhlichean Nautilus, dì-dhùmhlaich an tasg-lann a fhuair thu air an lìon do dh'eòlaire (an deasg agad, mar eisimpleir). Dèan cinnteach gun do dhùin thu gach aplacaid LibreOffice (a' gabhail a-steach an grad-thòisiche, ma tha e a' dol).

Thoir leum dhan phasgan far an do dhì-dhùmhlaich thu a' phacaid cànain a fhuair thu on lìon.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Thoir leum dhan phasgan a-nis far a bheil na pacaidean a tha ri an stàladh. Air siostaman Debian/Ubuntu, 's e DEBS a bhios air a' phasgan. Air siostaman Fedora, openSUSE no Mandriva, 's e RPMS a bhios air a' phasgan.

Ann am manaidsear fhaidhlichean Nautilus, dèan briogadh deas sa phasgan 's tagh "Open in terminal". Fosglaidh uinneag tèirmineil. Cuir an àithne airson stàladh na pacaid cànain san loidhne àithne san uinneag tèirmineil (leis na h-àitheantan a chì thu gu h-ìosal; faodaidh gun dèid iarraidh ort am facal-faire Root agad a chur a-steach):

Airson siostaman stèidhichte air Debian/Ubuntu : sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Airson siostaman stèidhichte air Mandriva: sudo urpmi *.rpm

Airson siostaman eile a chleachdas RPM (openSUSE is msaa.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Briog air "Ceart ma-thà" as dèidh dhut na roghainnean seo a chur air gleus. Dùinidh bogsa a' chòmhraidh agus chì thu teachdaireachd fiosrachaidh a dh'innseas dhut nach dèid na dh'atharraich thu a chur an sàs ach as dèidh dhut LibreOffice fhàgail agus a thòiseachadh a-rithist (cuimhnich gum bi agad an grad-thòisiche fhàgail cuideachd ma tha e a' dol).

Thèid LibreOffice a thòiseachadh sa chànan a stàlaich thu an-dràsta an ath-thuras.

----------------------------------------------------------------------
Duilgheadasan rè tòiseachadh a' phrògraim
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Padaichean-beantainn ALPS/Synaptics Notebook ann am Windows
----------------------------------------------------------------------

Air sgàth mearachd le draibhear Windows, chan urrainn dhut sgroladh tro sgrìobhainnean LibreOffice ma ghluaiseas tu do chorrag thairis air pada-beantainn ALPS/Synaptics.

Gus sgroladh air pada-beantainn a chur an comas, cuir na loidhnicheach a leanas ris an fhaidhle rèiteachaidh "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" agus tòisich an coimpiutair agad a-rithist:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Faodaidh gum bi am faidhle rèiteachaidh ann an àitichean eadar-dhealaichte air na diofar tionndaidhean de Windows.

----------------------------------------------------------------------
Iuchraichean nan ath-ghoiridean
----------------------------------------------------------------------

Chan urrainn dhut iuchraichean ath-ghoiridean (sreathan sònraichte de dh’iuchraichean) a chleachdadh ann an LibreOffice ach an fheadhainn nach eil an siostam obrachaidh a’ cleachdadh. Mur eil ath-ghoirid ann an LibreOffice ag obair mar a tha Cobhair LibreOffice ag innse dhut, thoir sùil ach a bheil e ’ga chleachdadh leis an t-siostam obrachaidh agad mu thràth. Air neo ’s urrainn dhut cha mhòr gach ath-ghoirid ann an LibreOffice atharrachadh. Airson barrachd fiosrachaidh mun chuspair seo, leugh Cobhair LibreOffice no na sgrìobhainnean cobharach am broinn an t-siostaim obrachaidh agad.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Nòtaichean cudromach mu sho-ruigsinneachd
----------------------------------------------------------------------

Airson barrachd fiosrachaidh a thaobh gleusan so-ruigsinneachd ann an LibreOffice, thoir sùil air https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Taic nan cleachdaichean
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Thoir sùil air na CÀBHA air làrach-lìn LibreOffice.

----------------------------------------------------------------------
Ag aithris air bugaichean ⁊ is duilgheadasan
----------------------------------------------------------------------

’S e Bugzilla an siostam a tha sinn a’ cleachdadh airson aithris, tracadh is fuasgladh nam bugaichean air https://bugs.documentfoundation.org/. Tha sinn a’ toirt brosnachadh dhan a h-uile cleachdaiche a thighinn ann agus aithris a dhèanamh air bugaichean a dh’fhaodadh a bhith ann air an ùrlar agad-sa. ’S e aithriseadh beothail nam buga aon dhe na rudan as cudromaiche as urrainn dhan choimhearsnachd a dhèanamh gus taic a chumail ruinn ann an leasachadh LibreOffice.

----------------------------------------------------------------------
Gabh pàirt ann
----------------------------------------------------------------------

B' fheairrde coimhearsnachd LibreOffice do com-pàirteachas gnìomhach ann an leasachadh a' phròiseict chudromach seo ann an saoghal bathar-bog le còd fosgailte.

Mar chleachdaiche, tha thu ’nad bhall cudromach ann am pròiseas leasachaidh a’ bhathair seo mu thràth agus bu toigh leinn brosnachadh a thoirt dhut fiù pàirt nas motha a ghabhail, gu h-àraid air an ùine fhada. Nach gabh thu pàirt ann ’s tu a’ toirt sùil air duilleag a’ chom-pàirteachais aig làrach-lìn LibreOffice.

Toiseach tòiseachaidh
----------------------------------------------------------------------

’S e fo-sgrìobhadh do chuid dhe na liostaichean puist aon dhe na h-àitichean as fhearr airson toiseach tòiseachaidh. Cum sùil orra fad greis agus cleachd tasg-lannan a’ phuist gus am fàs thu nas eòlaiche air an iomadh chuspair a dhèilig sinn ris on a chaidh còd LibreOffice a shaoradh san Dàmhair 2000. Nuair a bhios tu cofhurtail leis, cha leig thu leas an uairsin ach post-d a chur dhan liosta ’s fàilte a chur air daoine agus bidh thu an teis-mheadhan na cùise an uairsin. Ma tha thu eòlach air pròiseactan còd fosgailte, thoir sùil air liostaichean nan rudan a tha ri dhèanamh ach a bheil dad ann as urrainn dhut cuideachadh leinn aig làrach-lìn LibreOffice.

Fo-sgrìobh
----------------------------------------------------------------------

Seo cuid dhe na liostaichean puist as urrainn dhut fo-sgrìobhadh thuca air https://www.libreoffice.org/get-help/mailing-lists/

* Naidheachd: announce@documentfoundation.org *molar seo do chleachdaiche sam bith* (post beag)
* Prìomh-liosta an luchd-chleachdaidh: users@global.libreoffice.org *dòigh fhurasta gus sùil a chumail air na deasbadan (torr mòr puist)
* Am pròiseact margaideachd: marketing@global.libreoffice.org *seachad air an leasachadh fhèin* (a' fàs trang)
* Liosta choitcheann an luchd-dealbhaidh: libreoffice@lists.freedesktop.org (post mòr)

A' dol an sàs pròiseict no phròiseactan
----------------------------------------------------------------------

'S urrainn dhut taic mhòr a chumail ris a' phròiseict chudromach seo ann an saoghal bathar-bog le còd fosgailte, fiù mur eil ach beagan eòlais agad air dealbhadh bathar-bog no còdachadh. Seadh, thusa!

Tha sinn an dòchas gun gabh thu tlachd 'nad obair le LibreOffice 26.2 agus gum faic sinn thu air loidhne.

Coimhearsnachd LibreOffice

----------------------------------------------------------------------
Còd tùsail air cleachdadh/atharrachadh
----------------------------------------------------------------------

Cuid dhen chòir-lethbhreac 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
