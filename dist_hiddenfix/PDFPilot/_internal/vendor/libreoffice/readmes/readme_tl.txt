
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


Para sa pinakabagong update sa readme file na ito, tingnan ang https://git.libreoffice.org/core/tree/master/README.md

Ang file na ito ay naglalaman ng mahalagang impormasyon tungkol sa LibreOffice software. Inirerekomenda mong basahin nang mabuti ang impormasyong ito bago simulan ang pag-install.

Ang komunidad ng LibreOffice ay responsable para sa pagbuo ng produktong ito, at iniimbitahan kang isaalang-alang ang paglahok bilang isang miyembro ng komunidad. Kung ikaw ay isang bagong user, maaari mong bisitahin ang LibreOffice site, kung saan makakahanap ka ng maraming impormasyon tungkol sa LibreOffice na proyekto at ang mga komunidad na umiiral sa paligid nito. Pumunta sa https://www.libreoffice.org/ .

Talagang Libre ba ang LibreOffice para sa Sinumang Gumagamit?
----------------------------------------------------------------------

Ang LibreOffice ay libre para gamitin ng lahat. Maaari mong kunin ang kopyang ito ng LibreOffice at i-install ito sa maraming computer hangga't gusto mo, at gamitin ito para sa anumang layunin na gusto mo (kabilang ang komersyal, pamahalaan, pampublikong pangangasiwa at paggamit ng edukasyon). Para sa karagdagang mga detalye tingnan ang teksto ng lisensya na nakabalot sa LibreOffice download na ito.

Bakit ang LibreOffice ay Libre para sa Sinumang Gumagamit?
----------------------------------------------------------------------

Magagamit mo ang kopyang ito ng LibreOffice nang walang bayad dahil ang mga indibidwal na nag-aambag at corporate sponsor ay nagdisenyo, bumuo, sumubok, nagsalin, nagdokumento, sumuporta, nag-market, at tumulong sa maraming iba pang mga paraan upang maging LibreOffice kung ano ito ngayon. - nangungunang Open Source productivity software sa mundo para sa bahay at opisina.

Kung pinahahalagahan mo ang kanilang mga pagsisikap, at gusto mong matiyak na ang LibreOffice ay patuloy na magiging available sa hinaharap, mangyaring isaalang-alang ang pag-ambag sa proyekto - tingnan ang https://www.libreoffice.org/community/get-involved/ para sa mga detalye. Ang bawat tao'y maaaring gumawa ng isang kontribusyon ng ilang uri.

----------------------------------------------------------------------
Mga Tala sa Pag-install
----------------------------------------------------------------------

Nangangailangan ang LibreOffice ng isang kamakailang bersyon ng Java Runtime Environment (JRE) para sa buong pagpapagana. Ang JRE ay hindi bahagi ng LibreOffice package ng pag-install, dapat itong i-install nang hiwalay.

Mga Kinakailangan sa System
----------------------------------------------------------------------

* Microsoft Windows 10 o mas mataas

Mangyaring magkaroon ng kamalayan na ang mga karapatan ng administrator ay kailangan para sa proseso ng pag-install.

Ang pagpaparehistro ng LibreOffice bilang default na application para sa mga format ng Microsoft Office ay maaaring pilitin o pigilan sa pamamagitan ng paggamit ng mga sumusunod na command line switch sa installer:

* Ang REGISTER_ALL_MSO_TYPES=1 ay pipilitin ang pagpaparehistro ng LibreOffice bilang default na application para sa mga format ng Microsoft Office.
* Ang REGISTER_NO_MSO_TYPES=1 ay pipigilan ang pagpaparehistro ng LibreOffice bilang default na application para sa mga format ng Microsoft Office.

Pakitiyak na mayroon kang sapat na libreng memorya sa pansamantalang direktoryo sa iyong system, at pakitiyak na ang mga karapatan sa pagbabasa, pagsulat at pagpapatakbo ay nabigyan ng access. Isara ang lahat ng iba pang mga programa bago simulan ang proseso ng pag-install.

Pag-install ng LibreOffice sa Debian/Ubuntu-based na Linux system
----------------------------------------------------------------------

Para sa mga tagubilin kung paano mag-install ng language pack (pagkatapos ma-install ang US English na bersyon ng LibreOffice), pakibasa ang seksyon sa ibaba na pinamagatang Pag-install ng Language Pack.

Kapag na-unpack mo ang na-download na archive, makikita mo na ang mga nilalaman ay na-decompress sa isang sub-directory. Magbukas ng window ng file manager, at baguhin ang direktoryo sa isang nagsisimula sa "LibreOffice_", na sinusundan ng numero ng bersyon at ilang impormasyon ng platform.

Ang direktoryo na ito ay naglalaman ng isang subdirectory na tinatawag na "DEBS". Baguhin ang direktoryo sa direktoryo ng "DEBS".

Mag-right-click sa loob ng direktoryo at piliin ang "Buksan sa Terminal". Magbubukas ang isang terminal window. Mula sa command line ng terminal window, ipasok ang sumusunod na command (isasabihan kang ipasok ang password ng iyong root user bago isagawa ang command):

Ang mga sumusunod na command ay mag-i-install ng LibreOffice at ang desktop integration packages (maaari mo na lang kopyahin at i-paste ang mga ito sa terminal screen sa halip na subukang i-type ang mga ito):

sudo dpkg -i *.deb

Nakumpleto na ang proseso ng pag-install, at dapat ay mayroon kang mga icon para sa lahat ng LibreOffice na application sa menu ng Applications/Office ng iyong desktop.

Pag-install ng LibreOffice sa Fedora, openSUSE, Mandriva at iba pang mga Linux system gamit ang RPM packages
----------------------------------------------------------------------

Para sa mga tagubilin kung paano mag-install ng language pack (pagkatapos ma-install ang US English na bersyon ng LibreOffice), pakibasa ang seksyon sa ibaba na pinamagatang Pag-install ng Language Pack.

Kapag na-unpack mo ang na-download na archive, makikita mo na ang mga nilalaman ay na-decompress sa isang sub-directory. Magbukas ng window ng file manager, at baguhin ang direktoryo sa isang nagsisimula sa "LibreOffice_", na sinusundan ng numero ng bersyon at ilang impormasyon ng platform.

Ang direktoryo na ito ay naglalaman ng isang subdirectory na tinatawag na "RPMS". Baguhin ang direktoryo sa direktoryo ng "RPMS".

Mag-right-click sa loob ng direktoryo at piliin ang "Buksan sa Terminal". Magbubukas ang isang terminal window. Mula sa command line ng terminal window, ipasok ang sumusunod na command (isasabihan kang ipasok ang password ng iyong root user bago isagawa ang command):

Para sa mga sistemang nakabase sa Fedora: sudo dnf install *.rpm

Para sa mga system na nakabatay sa Mandriva: sudo urpmi *.rpm

Para sa iba pang RPM-based system (openSUSE, atbp.): rpm -Uvh *.rpm

Nakumpleto na ang proseso ng pag-install, at dapat ay mayroon kang mga icon para sa lahat ng LibreOffice na application sa menu ng Applications/Office ng iyong desktop.

Bilang kahalili, maaari mong gamitin ang script na 'i-install', na matatagpuan sa toplevel na direktoryo ng archive na ito upang magsagawa ng pag-install bilang isang user. Ang script ay magse-set up ng LibreOffice upang magkaroon ng sarili nitong profile para sa pag-install na ito, na hiwalay sa iyong normal na LibreOffice na profile. Tandaan na hindi nito mai-install ang mga bahagi ng integration ng system tulad ng mga item sa desktop menu at mga pagpaparehistro ng uri ng MIME sa desktop.

Mga Tala Tungkol sa Pagsasama-sama ng Desktop para sa Mga Pamamahagi ng Linux na Hindi Saklaw sa Mga Tagubilin sa Pag-install sa Itaas
----------------------------------------------------------------------

Madaling posible na mag-install ng LibreOffice sa ibang mga pamamahagi ng Linux na hindi partikular na sakop sa mga tagubilin sa pag-install na ito. Ang pangunahing aspeto kung saan maaaring makatagpo ang mga pagkakaiba ay ang desktop integration.

Ang direktoryo ng RPMS (o DEBS, ayon sa pagkakabanggit) ay naglalaman din ng package na pinangalanang libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (o libreoffice26.2- debian-menus_26.2.0.1-1_all.deb, ayon sa pagkakabanggit, o katulad). Ito ay isang pakete para sa lahat ng distribusyon ng Linux na sumusuporta sa mga detalye/rekomendasyon ng Freedesktop.org (https://en.wikipedia.org/ wiki/Freedesktop.org), at ibinibigay para sa pag-install sa iba pang mga distribusyon ng Linux na hindi sakop sa mga nabanggit na tagubilin.

Pag-install ng Language Pack
----------------------------------------------------------------------

I-download ang language pack para sa iyong gustong wika at platform. Available ang mga ito mula sa parehong lokasyon bilang pangunahing archive ng pag-install. Mula sa Nautilus file manager, i-extract ang na-download na archive sa isang direktoryo (halimbawa, ang iyong desktop). Tiyaking lumabas ka na sa lahat ng LibreOffice na application (kabilang ang QuickStarter, kung ito ay nagsimula).

Baguhin ang direktoryo sa direktoryo kung saan mo kinuha ang iyong na-download na pack ng wika.

Ngayon baguhin ang direktoryo sa direktoryo na nilikha sa panahon ng proseso ng pagkuha. Halimbawa, para sa French language pack para sa isang 32-bit na Debian/Ubuntu-based system, ang direktoryo ay pinangalanang LibreOffice_, kasama ang ilang impormasyon sa bersyon, at Linux_x86_langpack-deb_fr.

Ngayon baguhin ang direktoryo sa direktoryo na naglalaman ng mga pakete na i-install. Sa mga sistemang nakabatay sa Debian/Ubuntu, ang direktoryo ay magiging DEBS. Sa Fedora, openSUSE o Mandriva system, ang direktoryo ay magiging RPMS.

Mula sa Nautilus file manager, i-right-click sa direktoryo at piliin ang command na "Buksan sa terminal". Sa terminal window na kakabukas mo lang, isagawa ang command na i-install ang language pack (kasama ang lahat ng command sa ibaba, maaari kang i-prompt na ipasok ang password ng iyong root user):

Para sa Debian/Ubuntu-based system: sudo dpkg -i *.deb

Para sa mga sistemang nakabase sa Fedora: su -c 'dnf install *.rpm'

Para sa mga system na nakabatay sa Mandriva: sudo urpmi *.rpm

Para sa iba pang mga system na gumagamit ng RPM (openSUSE, atbp.): rpm -Uvh *.rpm

Ngayon simulan ang isa sa mga LibreOffice application - Writer, halimbawa. Pumunta sa Tools menu at piliin ang Options. Sa dialog box ng Mga Pagpipilian, mag-click sa "Mga Wika at Lokal" at pagkatapos ay mag-click sa "Pangkalahatan". I-dropdown ang listahan ng "User interface" at piliin ang wikang kaka-install mo lang. Kung gusto mo, gawin ang parehong bagay para sa "Setting ng lokal", ang "Default na pera", at ang "Mga default na wika para sa mga dokumento."

Pagkatapos ayusin ang mga setting na iyon, mag-click sa OK. Magsasara ang dialog box, at makakakita ka ng mensahe ng impormasyon na nagsasabi sa iyo na ang iyong mga pagbabago ay isaaktibo lamang pagkatapos mong lumabas sa LibreOffice at simulan itong muli (tandaang lumabas din sa QuickStarter kung ito ay nagsimula).

Sa susunod na simulan mo ang LibreOffice, magsisimula ito sa wikang kaka-install mo lang.

----------------------------------------------------------------------
Mga Problema sa Pagsisimula ng Programa
----------------------------------------------------------------------

Ang mga paghihirap sa pagsisimula ng LibreOffice (hal. ang mga application ay nakabitin) pati na rin ang mga problema sa display ng screen ay kadalasang sanhi ng driver ng graphics card. Kung mangyari ang mga problemang ito, mangyaring i-update ang driver ng iyong graphics card o subukang gamitin ang driver ng graphics na inihatid kasama ng iyong operating system.

----------------------------------------------------------------------
ALPS/Synaptics notebook touchpads sa Windows
----------------------------------------------------------------------

Dahil sa isyu sa driver ng Windows, hindi ka makakapag-scroll sa LibreOffice na mga dokumento kapag na-slide mo ang iyong daliri sa isang ALPS/Synaptics touchpad.

Upang paganahin ang pag-scroll ng touchpad, idagdag ang mga sumusunod na linya sa configuration file na " C:\Program Files\Synaptics\SynTP\SynTPEnh.ini ", at i-restart ang iyong computer:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Maaaring mag-iba ang lokasyon ng configuration file sa iba't ibang bersyon ng Windows.

----------------------------------------------------------------------
Mga Shortcut Key
----------------------------------------------------------------------

Tanging ang mga shortcut key (mga kumbinasyon ng key) na hindi ginagamit ng operating system ang maaaring gamitin sa LibreOffice. Kung ang kumbinasyon ng key sa LibreOffice ay hindi gumana tulad ng inilarawan sa LibreOffice Help, tingnan kung ang shortcut na iyon ay ginagamit na ng operating system. Upang maitama ang mga naturang salungatan, maaari mong baguhin ang mga key na itinalaga ng iyong operating system. Bilang kahalili, maaari mong baguhin ang halos anumang pangunahing pagtatalaga sa LibreOffice. Para sa higit pang impormasyon sa paksang ito, sumangguni sa LibreOffice Help o ang Help documentation ng iyong operating system.

----------------------------------------------------------------------
Mga Problema Kapag Nagpapadala ng Mga Dokumento bilang Mga Email Mula sa LibreOffice
----------------------------------------------------------------------

Kapag nagpapadala ng dokumento sa pamamagitan ng 'File - Send - Email Document' o 'File - Send - Email as PDF' maaaring mangyari ang mga problema (nag-crash o nag-hang ang program). Ito ay dahil sa Windows system file na "Mapi" (Messaging Application Programming Interface) na nagdudulot ng mga problema sa ilang bersyon ng file. Sa kasamaang palad, ang problema ay hindi maaaring paliitin sa isang tiyak na numero ng bersyon. Para sa karagdagang impormasyon bisitahin ang https://www.microsoft.com upang maghanap sa Microsoft Knowledge Base para sa "mapi dll".

----------------------------------------------------------------------
Mahalagang Mga Tala sa Accessibility
----------------------------------------------------------------------

Para sa higit pang impormasyon sa mga feature ng accessibility sa LibreOffice, tingnan ang https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Suporta sa Gumagamit
----------------------------------------------------------------------

Ang pangunahing pahina ng suporta ay nag-aalok ng iba't ibang mga posibilidad para sa tulong sa LibreOffice. Maaaring nasagot na ang iyong tanong - tingnan ang Community Forum sa https://ask.libreoffice.org/ o hanapin ang mga archive ng 'users@libreoffice.org' mailing list sa https://www.libreoffice.org/lists/users/. Bilang kahalili, maaari mong ipadala ang iyong mga tanong sa users@libreoffice.org. Kung gusto mong mag-subscribe sa listahan (upang makakuha ng mga tugon sa email), magpadala ng walang laman na mail sa: users+subscribe@libreoffice.org.

Suriin din ang seksyong FAQ sa website ng LibreOffice .

----------------------------------------------------------------------
Pag-uulat ng Mga Bug & Mga isyu
----------------------------------------------------------------------

Ang aming system para sa pag-uulat, pagsubaybay at paglutas ng mga bug ay kasalukuyang Bugzilla, na naka-host sa https://bugs.documentfoundation.org/ . Hinihikayat namin ang lahat ng mga gumagamit na pakiramdam na may karapatan at malugod na mag-ulat ng mga bug na maaaring lumitaw sa iyong partikular na platform. Ang masiglang pag-uulat ng mga bug ay isa sa pinakamahalagang kontribusyon na magagawa ng komunidad ng user sa patuloy na pag-unlad at pagpapabuti ng LibreOffice.

----------------------------------------------------------------------
Pagiging Kasangkot
----------------------------------------------------------------------

Ang LibreOffice Community ay lubos na makikinabang sa iyong aktibong pakikilahok sa pagbuo ng mahalagang open source na proyektong ito.

Bilang isang user, isa ka nang mahalagang bahagi ng proseso ng pag-develop ng suite at gusto ka naming hikayatin na gumawa ng mas aktibong tungkulin na may layuning maging isang pangmatagalang kontribyutor sa komunidad. Mangyaring sumali at tingnan ang nag-aambag na pahina sa LibreOffice website .

Paano Magsisimula
----------------------------------------------------------------------

Ang pinakamahusay na paraan upang magsimulang mag-ambag ay ang mag-subscribe sa isa o higit pa sa mga mailing list, magtago sandali, at dahan-dahang gamitin ang mga archive ng mail upang maging pamilyar ang iyong sarili sa marami sa mga paksang sakop mula noong ang LibreOffice source code ay inilabas pabalik sa Oktubre 2000. Kapag kumportable ka na, ang kailangan mo lang gawin ay magpadala ng email na pagpapakilala sa sarili at tumalon kaagad. Kung pamilyar ka sa Open Source Projects, tingnan ang aming listahan ng Mga Gagawin at tingnan kung mayroon kang anumang gagawin gustong tumulong sa LibreOffice website .

Mag-subscribe
----------------------------------------------------------------------

Narito ang ilan sa mga mailing list kung saan maaari kang mag-subscribe sa https://www.libreoffice.org/get-help/mailing-lists/

* Balita: announce@documentfoundation.org *inirerekomenda sa lahat ng user* (light traffic)
* Pangunahing listahan ng user: users@global.libreoffice.org *madaling paraan para magtago sa mga talakayan* (mabigat na trapiko)
* Proyekto sa marketing: marketing@global.libreoffice.org *beyond development* (nagpapabigat)
* Pangkalahatang listahan ng developer: libreoffice@lists.freedesktop.org (mabigat na trapiko)

Pagsali sa isa o higit pang Mga Proyekto
----------------------------------------------------------------------

Maaari kang gumawa ng malalaking kontribusyon sa mahalagang open source na proyektong ito kahit na mayroon kang limitadong disenyo ng software o karanasan sa coding. Oo, ikaw!

Umaasa kaming masisiyahan kang magtrabaho kasama ang bagong LibreOffice 26.2 at sasali sa amin online.

Ang LibreOffice Community

----------------------------------------------------------------------
Ginamit / Binagong Source Code
----------------------------------------------------------------------

Mga Bahagi Copyright 1998, 1999 James Clark. Mga Bahagi Copyright 1996, 1998 Netscape Communications Corporation.
