
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

આ ફાઇલ LibreOffice સોફ્ટવેર વિશે મહત્વની જાણકારીને સમાવે છે. તમે સ્થાપનને શરૂ કરતા પહેલાં એકદમ ધ્યાનથી જાણકારીને વાંચવા આગ્રહ રાખે છે.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

શું કોઇપણ વપરાશકર્તા માટે ખરેખર LibreOffice મફત છે?
----------------------------------------------------------------------

LibreOffice એ દરેકને વાપરવા માટે મફત છે. તમે LibreOffice ની આ નકલ લઇ શકો છો અને તમને ગમે તે પ્રમાણે ઘણાબધા કમ્પ્યૂટરો પર તેને સ્થાપિત કરો, અને તમને ગમે તેવા કોઇપણ હેતુ માટે તેને વાપરો (વ્યાપારી, સરકારી, સાર્વજનિક વહીવટ અને અભ્યાસ વપરાશને સમાવી રહ્યા છે). આગળ વિગતો માટે આ LibreOffice ડાઉનલોડ સાથે પેકેજ થયેલ લાઇસન્સ લખાણને જુઓ.

શા માટે કોઇપણ વપરાશકર્તા માટે LibreOffice મફત છે?
----------------------------------------------------------------------

તમે મફતમાં LibreOffice ની આ નકલને વાપરી શકો છો કારણ કે વ્યક્તિગત ફાળક અને સંગઠિત પ્રાયોજકે LibreOffice ને બનાવવા માટે રચેલ, વિકસાવેલ, ચકાસેલ, અનુવાદ કરેલ, દસ્તાવેજીકરણ કરેલ, આધાર આપેલ, માર્કેટિંગ અને ઘણી બીજી રીતે મદદ કરેલ છે જે તે આજે છે - ઘર અને ઑફિસ માટે દુનિયાની  પ્રથમ ઓપન સોર્સ પ્રોડક્ટીવીટી સોફ્ટવેર.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
સ્થાપન માટેની નોંધ
----------------------------------------------------------------------

LibreOffice ને સંપૂર્ણ કાર્યક્ષમતા માટે Java Runtime Environment (JRE) ની તાજેતરની આવૃત્તિની જરૂર છે. JRE એ LibreOffice સ્થાપન પેકેજનો ભાગ નથી, તેને અલગ રીતે સ્થાપિત કરવુ જોઇએ.

સિસ્ટમ જરૂરિયાતો
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

મહેરબાની કરીને ધ્યાનમાં રાખો કે સંચાલકના મુદ્દાઓ સ્થાપનની પ્રક્રિયા માટે જરૂરી છે.

Microsoft Office બંધારણો માટે મૂળભૂત કાર્યક્રમ તરીકે LibreOffice નું રજીસ્ટ્રેશન એ સ્થાપનાર સાથે નીચેની આદેશ લીટી ની મદદથી દબાવુ અથવા દાબી શકાય છે:

* REGISTER_ALL_MSO_TYPES=1 એ Microsoft Office બંધારણો માટે મૂળભૂત કાર્યક્રમ તરીકે LibreOffice નાં રજીસ્ટ્રેશનનુ દબાણ કરશે.
* REGISTER_NO_MSO_TYPES=1 એ Microsoft Office બંધારણો માટે મૂળભૂત કાર્યક્રમ તરીકે LibreOffice નાં રજીસ્ટ્રેશ પર પ્રતિબંધ મૂકશે.

મહેરબાની કરીને ખાતરી કરો કે તમારી પાસે તમારી સિસ્ટમ પર કામચલાઉ ડિરેક્ટરીમાં પૂરતી મુક્ત મેમરી છે, અને મહેરબાની ખાતરી કરો કે વાંચવા, લખવા અને ચલાવવાનાં હકોની મંજૂરી આપેલ છે. સ્થાપન પ્રક્રિયાને શરૂ કરતા પહેલાં બધા બીજા કાર્યક્રમોને બંધ કરો.

Debian/Ubuntu-આધારિત Linux સિસ્ટમો પર LibreOffice નું સ્થાપન
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

આ ડિરેક્ટરી "DEBS" કહેવાતી ઉપડિરેક્ટરીને સમાવે છે. "DEBS" ડિરેક્ટરીમાં ડિરેક્ટરીને બદલો.

ડિરેક્ટરીમાં જમણી ક્લિક કરો અને "ટર્મિનલમાં ખોલો" ને પસંદ કરો. ટર્મિનલ વિન્ડો ખુલશે. ટર્મિનલ વિન્ડોની આદેશ વાક્યમાંથી, નીચેનાં આદેશને દાખલ કરો (આદેશ ચાલશે તે પહેલાં તમારા રુટ વપરાશકર્તાનાં પાસવર્ડને દાખલ કરવા માટે તમને પ્રોમ્પ્ટ કરશે):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

સ્થાપન પ્રક્રિયા હવે સમાપ્ત થયેલ છે, અને તમારે ડેસ્કટોપનાં કાર્યક્રમો/ઑફિસ મેનુ માં બધા LibreOffice કાર્યક્રમો માટે તમારી પાસે ચિહ્નો હોવા જોઇએ.

RPM પેકેજોની મદદથી Fedora, openSUSE, Mandriva અને બીજી Linux સિસ્ટમો પર LibreOffice નું સ્થાપન
----------------------------------------------------------------------

For instructions on how to install a language pack (after having installed the US English version of LibreOffice), please read the section below entitled Installing a Language Pack.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

આ ડિરેક્ટરી "RPMS" તરીકે બોલાવાયેલ ઉપડિરેક્ટરીને સમાવે છે. "RPMS" ડિરેક્ટરીમાં ડિરેક્ટરીને બદલો.

ડિરેક્ટરીમાં જમણી ક્લિક કરો અને "ટર્મિનલમાં ખોલો" ને પસંદ કરો. ટર્મિનલ વિન્ડો ખુલશે. ટર્મિનલ વિન્ડોની આદેશ વાક્યમાંથી, નીચેનાં આદેશને દાખલ કરો (આદેશ ચાલશે તે પહેલાં તમારા રુટ વપરાશકર્તાનાં પાસવર્ડને દાખલ કરવા માટે તમને પ્રોમ્પ્ટ કરશે):

For Fedora-based systems: sudo dnf install *.rpm

Mandriva-આધારિત સિસ્ટમો માટે: sudo urpmi *.rpm

બીજી RPM-આધારિત સિસ્ટમો માટે (openSUSE, વગેરે.): rpm -Uvh *.rpm

સ્થાપન પ્રક્રિયા હવે સમાપ્ત થયેલ છે, અને તમારે ડેસ્કટોપનાં કાર્યક્રમો/ઑફિસ મેનુ માં બધા LibreOffice કાર્યક્રમો માટે તમારી પાસે ચિહ્નો હોવા જોઇએ.

Alternatively, you can use the 'install' script, located in the toplevel directory of this archive to perform an installation as a user. The script will set up LibreOffice to have its own profile for this installation, separated from your normal LibreOffice profile. Note that this will not install the system integration parts such as desktop menu items and desktop MIME type registrations.

Linux વિતરણો માટે નોંધોને લગતુ ડેસ્કટોપ એકત્રિકરણ ઉપર સ્થાપન સૂચનાઓમાં આવરેલ નથી
----------------------------------------------------------------------

બીજા Linux વિતરણો પર LibreOffice ને સ્થાપિત કરવાનું સરળ રીતે શક્ય હોવુ જોઇએ આ સ્થાપન સૂચનાઓ માટે વિશેષ રૂપે આવરેલ નથી મુખ્ય ઉદ્દેશ જેની માટે તફાવતોને શોધી શકાય તે ડેસ્કટોપ એકત્રિકરણ છે.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

ભાષા પેકેજને સ્થાપિત કરી રહ્યા છે
----------------------------------------------------------------------

તમારી ઇચ્છિત ભાષા અને પ્લેટફોર્મ માટે ભાષા પેકેજને ડાઉનલોડ કરો. મુખ્ય સ્થાપન પેટી તરીકે એજ સ્થાનમાંથી ઉપલબ્ધ છે. Nautilus ફાઇલ સંચાલકમાંથી, ડિરેક્ટરીમાં ડાઉનલોડ થયેલ પેટીનો અર્ક કાઢો (ઉદાહરણ માટે, તમારુ ડેસ્કટોપ). ખાતરી કરો કે તમે બધા LibreOffice કાર્યક્રમોમાંથી બહાર નીકળી ગયા છો (QuickStarter ને સમાવીને, જે તે શરૂ હોય તો).

ડિરેક્ટરીમાં ડિરેક્ટરીને બદલો જેમાં તમે તમારુ ડાઉનલોડ થયેલ ભાષા પેકેજનો અર્ક કાઢેલ છે.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

હવે ડિરેક્ટરીમાં ડિરેક્ટરીને બદલો કે જે સ્થાપિત કરવા માટે પેકેજોને સમાવે છે. Debian/Ubuntu-આધારિત સિસ્ટમો પર. ડિરેક્ટરી DEBS હશે. Fedora, openSUSE અથવા Mandriva સિસ્ટમો પર, ડિરેક્ટરી RPMS હશે.

Nautilus ફાઇલ સંચાલકમાંથી, ડિરેક્ટરીમાં જમણી ક્લિક કરો અને "ટર્મિનલમાં ખોલો" ને પસંદ કરો જે તમે હમણાં ખોલેલ છે. ભાષા પેકેજને સ્થાપિત કરવા માટે આદેશને ચલાવો (નીચે બધા આદેશો સાથે, તમે તમારાં રુટ વપરાશકર્તાનાં પાસવર્ડને દાખલ કરવા માટે તમને પ્રોમ્પ્ટ કરી શકે છે):

Debian/Ubuntu-આધારિત સિસ્ટમો માટે: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Mandriva-આધારિત સિસ્ટમો માટે: sudo urpmi *.rpm

બીજી RPM-વાપરતી સિસ્ટમો માટે (openSUSE, વગેરે.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

પેલા સુયોજનોને વ્યવસ્થિત કર્યા પછી. બરાબર પર ક્લિક કરો. સંવાદ બોક્સ બંધ થઇ જશે, અને તમે જાણકારી સંદેશો જોશો જે તમને કહી રહ્યો છે કે તમારા બદલાવો તમે LibreOffice માંથી બહાર નીકળો પછી જ સક્રિય થશે અને ફરીથી તેને શરૂ કરો (QuickStarter માંથી બહાર નીકળવાનું યાદ રાખો જો તે શરૂ થયેલ હોય તો).

આગળથી તમે LibreOffice ને શરૂ કરો, તે ભાષામાં શરૂ થશે જે તમે હમણાં જ સ્થાપિત કરેલ છે.

----------------------------------------------------------------------
પ્રક્રિયા શરૂ કરવા દરમ્યાન સમસ્યાઓ
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Windows માં ALPS/Synaptics નોટબુક ટચપેડ
----------------------------------------------------------------------

વિન્ડો ડ્રાઇવર સમસ્યા દરમ્યાન, LibreOffice દસ્તાવેજો મારફતે તમે સ્ક્રોલ કરી શકતા નથી જ્યારે ALPS/Synaptics ટચપેડ ની તરફ તમારી આંગળી ને ખસેડો.

ટચપેડ સરકાવવાનું સક્રિય કરવા માટે, નીચેની લીટીઓ "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" રૂપરેખાંકન ફાઈલમાં લખો, અને તમારું કમ્પ્યૂટર પુનઃશરૂ કરો:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

રૂપરેખાંકન ફાઈલનું સ્થાન Windows ની વિવિધ આવૃત્તિઓ પ્રમાણે બદલાઈ શકે છે.

----------------------------------------------------------------------
ટુંકાણ કળ
----------------------------------------------------------------------

Only shortcut keys (key combinations) not used by the operating system can be used in LibreOffice. If a key combination in LibreOffice does not work as described in the LibreOffice Help, check if that shortcut is already used by the operating system. To rectify such conflicts, you can change the keys assigned by your operating system. Alternatively, you can change almost any key assignment in LibreOffice. For more information on this topic, refer to the LibreOffice Help or the Help documentation of your operating system.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
મહત્વની ઉપલ્બધતા નોંધો
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
વપરાશકર્તા આધાર
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Also check the FAQ section at the LibreOffice website.

----------------------------------------------------------------------
અહેવાલીકરણ ભૂલો & મુદ્દાઓ
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
સાથે સંકળાઇ રહ્યા છે
----------------------------------------------------------------------

LibreOffice સમુદાય એ તેના વિકાસમાં તમારા સક્રિય ભાગમાંથી આ મહત્વના મુક્ત સ્રોત પ્રોજેક્ટમાં મોટો લાભ મેળવે છે.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

કેવી રીતે શરૂ કરવુ
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

ઉમેદવારી નોંધાવો
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* સમાચારો: announce@documentfoundation.org *બધા વપરાશકર્તાઓ માટે અગ્રહણીય* (ધીમો ટ્રાફિક)
* મુખ્ય વપરાશકર્તા યાદી: users@global.libreoffice.org *ચર્ચાઓ પર ધ્યાન રાખવાનું સરળ છે* (ભારે ટ્રાફિક)
* માર્કેટીંગ પ્રોજેક્ટ: marketing@global.libreoffice.org *વિકાસ હેઠળ* (ભારે થઇ રહ્યુ છે)
* સામાન્ય ડેવલપર યાદી: libreoffice@lists.freedesktop.org (વધારે ટ્રાફિક)

એક અથવા વધારે પ્રોજેક્ટો સાથે જોડાઇ રહ્યા છે
----------------------------------------------------------------------

તમે આ મહત્વના મુક્ત સ્રોત પ્રોજેક્ટ માટે પણ ફાળો આપી શકો છો જો તમે સોફ્ટવેરને બનાવવાનું અને તેનો કોડ લખવાનો અનુભવ કર્યો હોય. હા, તમે જ!

અમે આશા રાખીએ છીએ કે તમે નવા LibreOffice 26.2 સાથે કામ કરવામાં મજા આવી અને અમારી સાથે ઓનલાઈન જોડાશો.

LibreOffice સમુદાય

----------------------------------------------------------------------
વપરાયેલ / સુધારાયેલ સ્રોત કોડ
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
