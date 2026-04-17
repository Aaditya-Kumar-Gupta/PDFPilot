
======================================================================
Darllen Fi LibreOffice 26.2
======================================================================


I gael diweddariadau diweddaraf y ffeil darllen fi, gweler  https://git.libreoffice.org/core/tree/master/README.md

Mae'r ffeil hon yn cynnwys gwybodaeth bwysig am y LibreOffice. Argymhellir eich bod yn darllen y wybodaeth yn ofalus iawn cyn dechrau gosod.

Mae cymuned LibreOffice yn gyfrifol am ddatblygu'r cynnyrch hwn, ac yn eich gwahodd i ystyried cymryd rhan fel aelod cymunedol. Os ydych chi'n ddefnyddiwr newydd, gallwch ymweld â gwefan LibreOffice, lle mae lawer o wybodaeth am brosiect LibreOffice a'r cymunedau sy'n bodoli o'i gwmpas. Ewch i https://www.libreoffice.org/.

A yw LibreOffice am ddim ar gyfer Unrhyw Defnyddiwr?
----------------------------------------------------------------------

Mae LibreOffice ar gael yn rhad ac am ddim i'w ddefnyddio gan bawb. Gallwch gymryd y copi hwn o LibreOffice a'i osod ar faint bynnag o gyfrifiaduron yr hoffech chi ei wneud, a'i ddefnyddio at ba bynnag bwrpas yr hoffech chi (gan gynnwys defnydd masnachol, llywodraeth, gweinyddiaeth gyhoeddus ac addysgol). Am wybodaeth bellach gweler y testun trwyddedu o fewn y pecyn llwytho i lawr LibreOffice.

Pam mae LibreOffice am ddim ar gyfer Unrhyw Ddefnyddiwr?
----------------------------------------------------------------------

Gallwch ddefnyddio'r copi hwn o LibreOffice yn rhad ac am ddim oherwydd bod cyfranwyr unigol a noddwyr corfforaethol wedi dylunio, datblygu, profi, cyfieithu, dogfennu, cefnogi, marchnata, a chynorthwyo mewn sawl ffordd arall i wneud LibreOffice yr hyn ydyw heddiw - meddalwedd cynhyrchu amlycaf y byd Cod Agored ar gyfer y cartref ac yn y swyddfa.

Os ydych yn gwerthfawrogi eu hymdrechion, ac yn dymuno i sicrhau fod LibreOffice yn parhau i fod ar gael ymhell i'r dyfodol, ystyriwch gyfrannu at y prosiect - gweler  https://www.libreoffice.org/community/get-involved/ am fanylion. Gall pawb wneud cyfraniad o ryw fath.

----------------------------------------------------------------------
Nodiadau Gosod
----------------------------------------------------------------------

Mae LibreOffice angen fersiwn diweddar o'r Java Runtime Environment (JRE) ar gyfer swyddogaethau llawn. Nid yw JRE yn rhan o becyn gosod LibreOffice, rhaid ei osod ar wahan.

Anghenion y System
----------------------------------------------------------------------

* Microsoft Windows 10 neu uwch

Byddwch yn ymwybodol fod angen hawliau gweinyddu ar gyfer y broses osod.

Mae modd gorfodi neu atal cofrestru LibreOffice fel y rhaglen rhagosodedig ar gyfer fformatau Microsoft Office drwy ddefnyddio'r newidynnau llinell orchymyn ganlynol gyda'r gosodwr:

* Bydd REGISTER_ALL_MSO_TYPES=1 yn gorfodi cofrestru LibreOffice fel y rhaglen ragosodedig ar gyfer fformatau Microsoft Office.
* Bydd REGISTER_NO_MSO_TYPES=1 yn rhwystro cofrestru LibreOffice fel y rhaglen ragosodedig ar gyfer fformatau Microsoft Office.

Gwnewch yn siŵr bod gennych ddigon o gof am ddim yn y cyfeiriadur dros dro ar eich system, a gwnewch yn siŵr bod hawl darllen, ysgrifennu a rhedeg wedi ei ganiatáu. Caewch bob rhaglen arall cyn dechrau ar y broses gosod.

Gosod LibreOffice ar systemau Linux yn seiliedig ar Debian/Ubuntu
----------------------------------------------------------------------

I gael cyfarwyddiadau ar sut i osod pecyn iaith (ar ôl gosod y fersiwn Saesneg UDA o LibreOffice), darllenwch yr adran isod o'r enw Gosod Pecyn Iaith.

Pan fyddwch yn dadbacio archif wedi'i lwytho i lawr, byddwch yn gweld y cynnwys sydd wedi'i ddatgywasgu i is-gyfeiriadur. Agorwch ffenestr rheolwr ffeiliau a newid cyfeiriadur i un yn cychwyn gyda "LibreOffice_", ac yna rhif y fersiwn a rhywfaint o fanylion y platfform.

Mae'r cyfeiriadur hwn yn cynnwys is-gyfeiriadur o'r enw "DEBS". Newidiwch y cyfeiriadur i gyfeiriadur "DEBS".

Rhowch glic de o fewn y cyfeiriadur a dewis "Agor mewn Terfynell". Bydd ffenestr terfynell yn agor. O linell orchymyn y ffenestr derfynell, rhowch y gorchymyn canlynol (byddwch yn cael eich annog i gynnig eich cyfrinair defnyddiwr gwraidd cyn bydd y gorchymyn gweithredu):

Bydd y gorchymyn canlynol yn gosod LibreOffice  a'r pecynnau integreiddio bwrdd gwaith (gallwch gopïo a gludo nhw i sgrin y derfynell yn lle ceisio'u teipio nhw):

sudo dpkg -i *.deb

Mae'r broses gosod nawr wedi ei chwblhau, a dylai bod eiconau ar gyfer yr holl raglenni LibreOffice ar ddewislen Rhaglenni/Swyddfa eich bwrdd gwaith.

Gosod LibreOffice ar Fedora, openSUSE, Mandriva a systemau Linux eraill sy'n defnyddio pecynnau RPM
----------------------------------------------------------------------

I gael cyfarwyddiadau ar sut i osod pecyn iaith (ar ôl gosod y fersiwn Saesneg UDA o LibreOffice), darllenwch yr adran isod o'r enw Gosod Pecyn Iaith.

Pan fyddwch yn dadbacio archif wedi'i lwytho i lawr, byddwch yn gweld y cynnwys sydd wedi'i ddatgywasgu i is-gyfeiriadur. Agorwch ffenestr rheolwr ffeiliau a newid cyfeiriadur i un yn cychwyn gyda "LibreOffice_", ac yna rhif y fersiwn a rhywfaint o fanylion y platfform.

Mae'r cyfeiriadur hwn yn cynnwys is-gyfeiriadur o'r enw "RPMS". Newidiwch y cyfeiriadur i gyfeiriadur "RPMS".

Rhowch glic de o fewn y cyfeiriadur a dewis "Agor mewn Terfynell". Bydd ffenestr terfynell yn agor. O linell orchymyn y ffenestr derfynell, rhowch y gorchymyn canlynol (byddwch yn cael eich annog i gynnig eich cyfrinair defnyddiwr gwraidd cyn bydd y gorchymyn gweithredu):

Ar gyfer systemau sy'n seiliedig ar Fedora : sudo dnf install *.rpm'

Ar gyfer systemau sy'n seiliedig ar Mandriva : sudo urpmi *.rpm

Ar gyfer systemau eraill yn seiliedig ar RPM (openSUSE, ac ati.): rpm -Uvh *.rpm

Mae'r broses gosod nawr wedi ei chwblhau, a dylai bod eiconau ar gyfer yr holl raglenni LibreOffice ar ddewislen Rhaglenni/Swyddfa eich bwrdd gwaith.

Yn lle hynny, gallwch ddefnyddio sgript 'gosod', sydd wedi ei leoli yn y cyfeiriadur lefel uchaf yr archif ar gyfer cyflawni gosod fel defnyddiwr. Bydd y sgript yn gosod LibreOffice i gael ei broffil ei hun ar gyfer y gosodiad hwn, ar wahân i'ch proffil LibreOffice arferol. Sylwch na fydd hyn yn gosod darnau integreiddio system megis eitemau dewislen bwrdd gwaith a chofrestriadau bwrdd gwaith math MIME.

Nodiadau Ynghylch Integreiddio'r Bwrdd Gwaith ar gyfer dosbarthiadau Linux sydd Heb eu cynnwys yn y Cyfarwyddiadau Gosod Uchod
----------------------------------------------------------------------

Dylai fod yn eithaf hawdd gosod LibreOffice ar ddosbarthiadau Linux eraill heb eu cynnwys yn benodol yn y cyfarwyddiadau gosod. Y prif wahaniaethau all fod mewn integreiddio’r bwrdd gwaith.

Mae cyfeiriadur RPMS (neu DEBS, yn ôl eu trefn ) hefyd yn cynnwys pecyn o'r enw libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, yn ôl eu trefn neu debyg). Mae hwn yn becyn ar gyfer yr holl dosbarthiadau Linux sy'n cynnal manylion/argymhellion Freedesktop.org (https://en.wikipedia.org/wiki/Freedesktop.org), ac mae ar gael ar gyfer ei osod ar ddosbarthiadau Linux eraill sydd heb eu cynnwys yn y cyfarwyddiadau hyn.

Gosod Pecyn Iaith
----------------------------------------------------------------------

Llwythwch i lawr y pecyn iaith ar gyfer eich dewis iaith a phlatfform. Maent ar gael oddi ar yr un lleoliad a'r prif archif gosod. O'r trefnydd ffeiliau Nautilus, dynnwch yr archif i mewn i gyfeiriadur (eich bwrdd gwaith, er enghraifft). Sicrhewch eich bod allan o bob rhaglen LibreOffice (gan gynnwys CychwynCyflym, os yw wedi ei gychwyn).

Newidiwch gyfeiriadur i'r cyfeiriadur yr ydych wedi echdynnu eich pecyn iaith iddo.

Nawr newidiwch gyfeiriadur i'r cyfeiriadur a grëwyd yn ystod y broses echdynnu. Er enghraifft, ar gyfer y pecyn iaith Ffrangeg ar gyfer system sy'n seiliedig ar 32-did Debian/Ubuntu, enw'r cyfeiriadur yw LibreOffice_, a hefyd peth manylion fersiwn, a Linux_x86_langpack-deb_fr.

Nawr newidiwch gyfeiriadur i'r cyfeiriadur sy'n cynnwys y pecynnau i'w gosod. Ar systemau Debian/Ubuntu y cyfeiriadur fydd DEBS. Ar systemau Fedora, openSUSE neu Mandriva RPMS fydd y cyfeiriadur.

O'r rheolwr ffeiliau Nautilus, rhowch glic de yn y cyfeiriadur a dewis y gorchymyn "Agor mewn terfynell". Yn y ffenest derfynell rydych newydd ei hagor, gweithredwch yr orchymyn i osod y pecyn iaith (gyda'r holl orchmynion isod, efallai y byddwch yn derbyn cais i roi eich cyfrinair defnyddiwr gwraidd):

Ar gyfer systemau sy'n seiliedig ar Debian/Ubuntu: sudo-i dpkg *.deb

Ar gyfer systemau sy'n seiliedig ar Fedora : su -c 'dnf install *.rpm'

Ar gyfer systemau sy'n seiliedig ar Mandriva : sudo urpmi *.rpm

Ar gyfer systemau eraill yn seiliedig ar RPM (openSUSE, ac ati.): rpm -Uvh *.rpm

Nawr cychwynnwch un o raglenni LibreOffice - Writer, er enghraifft. Ewch i'r ddewislen Offer a dewiswch Dewisiadau. Yn y blwch deialog Dewisiadau, cliciwch ar "Ieithoedd a Locales" ac yna cliciwch ar "Cyffredinol". Agorwch y rhestr "Rhyngwyneb Defnyddiwr" a dewiswch yr iaith newydd ei gosod. Os ydych yn dymuno, gwnewch yr un peth ar gyfer y "Gosodiadau Locale", yr "Arian rhagosodedig", a'r "Ieithoedd Rhagosodedig ar gyfer dogfennau".

Ar ôl addasu'r gosodiadau hynny, cliciwch ar Iawn. Bydd y blwch deialog yn cau, ac fe welwch neges yn dweud wrthych y bydd eich newidiadau ond yn cael eu gweithredu ar ôl i chi adael LibreOffice a dechrau eto (cofiwch hefyd adael CychwynCyflym os ydyw wedi dechrau).

Y tro nesaf y byddwch yn dechrau LibreOffice, bydd yn cychwyn yn yr iaith rydych wedi ei osod.

----------------------------------------------------------------------
Anawsterau wrth Gychwyn y Rhaglen
----------------------------------------------------------------------

Mae anawsterau cychwyn LibreOffice  (e.e. rhaglenni’n stopio) yn ogystal â phroblemau gyda'r dangosydd sgrin yn aml wedi';u achosi gan yrwyr cardiau graffig. Os yw'r anawsterau hyn yn digwydd, diweddarwch eich gyrrwr neu ceisiwch ddefnyddio'r gyrrwr ddaeth gyda'ch system weithredu.

----------------------------------------------------------------------
Pad cyffwrdd gliniaduron ALPS/Synaptics Windows
----------------------------------------------------------------------

Oherwydd anhawsterau gyrrwyr Windows, nid oes modd sgrolio drwy ddogfennau LibreOffice documents wrth lithro eich bys ar draws pad cyffwrdd ALPS/Synaptics.

I alluogi sgrolio pad cyffwrdd, ychwanegwch y llinellau canlynol i ffeil ffurfweddu "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" , ac ailgychwyn eich cyfrifiadur:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Gall leoliad y ffeil ffurfweddu amrywio yn ôl y fersiwn o Windows.

----------------------------------------------------------------------
Bysellau Llwybr Byr
----------------------------------------------------------------------

Dim ond bysellau (cyfuniad bysellau) nad ydynt yn cael eu defnyddio gan y system weithredu mae modd eu defnyddio yn LibreOffice. Os nad yw cyfuniad bysellau'n gweithio yn LibreOffice fel y disgrifir yn Cymorth LibreOffice, gwiriwch fod y llwybr byr yn cael ei ddefnyddio eisoes gan y system. I gywiro'r gwrthdaro, mae modd newid y bysellau neilltuwyd gan eich system weithredu. Fel arall, mae modd newid bron unrhyw un o'r bysellau neilltuwyd gan LibreOffice. Am ragor o wybodaeth ar y pwnc, ewch i Cymorth LibreOffice neu ddogfennaeth Cymorth eich system weithredu.

----------------------------------------------------------------------
Anawsterau wrth Anfon Dogfennau fel E-byst o LibreOffice
----------------------------------------------------------------------

Pan yn anfon dogfen drwy 'Ffeil - Anfon - Dogfen fel E-bost' neu 'Dogfen fel Atodiad PDF' gall anawsterau ddigwydd (rhaglen yn chwalu neu'n peidio). Mae hyn oherwydd ffeil system Windows "Mapi" (Messaging Application Programming Interface) sy'n achosi anawsterau i rai fersiynau o ffeiliau. Yn anffodus, nid oes modd cyfyngu'r anhawster i rhai fersiynau penodol. Am ragor o wybodaeth ewch i  https://www.microsoft.com a chwilio'r Microsoft Knowledge Base am "mapi dll".

----------------------------------------------------------------------
Nodiadau Hygyrchedd Pwysig
----------------------------------------------------------------------

Am ragor o wybodaeth am nodweddion hygyrchedd o fewn LibreOffice, gweler https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Cefnogaeth i Ddefnyddwyr
----------------------------------------------------------------------

Mae'r prif dudalennau cefnogaeth offers various possibilities for help with LibreOffice.Efallai bod eich cwestiynau eisoes wedi'u hateb - check the Community Forum at https://ask.libreoffice.org/ neu chwiliwch archifau rhestr e-bostio 'users@libreoffice.org' yn https://www.libreoffice.org/lists/users/. Fel arall, gallwch anfon eich cwestiynau at users@libreoffice.org. Os hoffech chi danysgrifio i'r rhestr (i gael ymatebion e-bost), anfonwch e-bost gwag: users+subscribe@libreoffice.org.

Hefyd ewch i'n hadran Cwestiynnau Cyffredin yng ngwefan LibreOffice.

----------------------------------------------------------------------
Adrodd Gwallau a Materion
----------------------------------------------------------------------

Bugzilla yw ein system ar gyfer adrodd, olrhain a datrys bygiau ar hyn o bryd, sy'n cael ei gynnal, diolch i  https://bugs.documentfoundation.org/. Rydym yn annog pob defnyddwyr i feddu'r hawl a bod croeso i roi gwybod am wallau a all godi ar eich platfform penodol. Mae adrodd egnïol ar wallau yn un o'r cyfraniadau pwysicaf y gall y gymuned ddefnyddwyr ei wneud i ddatblygiad a gwelliant parhaus LibreOffice.

----------------------------------------------------------------------
Ymuno
----------------------------------------------------------------------

Hoffai Cymuned LibreOffice fanteisio ar eich ymwneud gweithgar yn natblygiad y project cod agored hwn.

Fel defnyddiwr, rydych eisoes yn rhan werthfawr o'r broses ddatblygu'r rhaglenni a hoffem eich annog i gymryd rhan hyd yn oed yn fwy gweithgar gyda golwg ar fod yn gyfrannwr tymor hir i'r gymuned. Ymunwch a darllen y dudalen cyfrannu yng ngwefan LibreOffice.

Sut i Gychwyn
----------------------------------------------------------------------

Y ffordd orau i ddechrau cyfrannu yw drwy danysgrifio i un neu fwy o'r rhestrau e-bostio, llechu am ychydig, ac yn raddol ddefnyddio'r post archifau i ymgyfarwyddo â llawer o'r pynciau sy'n cael eu trafod ers i'r cod ffynhonnell LibreOffice gael ei rhyddhau yn ôl yn Hydref 2000. Pan fyddwch yn gyfforddus, dim ond angen i chi gyflwyno eich hun sydd ei angen ac ymuno'r gwaith. Os ydych yn gyfarwydd â Phrosiectau Cod Agored, edrychwch ar ein rhestr Gwneud a gweld os oes unrhyw beth yr hoffech chi gyfrannu tuag ato yngngwefan LibreOffice.

Tanysgrifo
----------------------------------------------------------------------

Dyma rai o'r rhestrau e-bostio at y gallwch danysgrifio iddynt https://www.libreoffice.org/get-help/mailing-lists/

* Newyddion: announce@documentfoundation.org *ar gyfer pob defnyddwyr* (traffig ysgafn)
* Rhestr prif ddefnyddiwr: users@global.libreoffice.org *ffordd hawdd i wrando ar drafodaethau* (defnydd trwm)
* Project marchnata: marketing@global.libreoffice.org *datblygiad+* (trymhau)
* Rhestr cyffredinoldatblygwr: libreoffice@lists.freedesktop.org (traffig trwm)

Ymuno gydag un neu fwy o Brojectau
----------------------------------------------------------------------

Mae modd i chi wneud cyfraniad sylweddol i'r project cod agored pwysig hwn hyd yn oed os mai dim ond profiad bychan o gynllunio meddalwedd neu godio sydd gennych. Ie, chi!

Gobeithio y byddwch yn mwynhau gweithio gyda LibreOffice 26.2 ac y gwnewch ymuno gyda ni ar-lein.

Cymuned LibreOffice

----------------------------------------------------------------------
Cod Ffynhonnell Defnyddwyr / Addaswyd
----------------------------------------------------------------------

Hawlfraint Cyfrannau 1998, 1999 James Clark. Hawlfraint Cyfrannau 1996, 1998 Netscape Communications Corporation.
