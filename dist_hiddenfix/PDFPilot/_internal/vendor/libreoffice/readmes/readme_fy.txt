
======================================================================
LibreOffice 26.2 Lêsmy
======================================================================


Foar de lêste fernijingen fan dit readme triem , sjoch https://git.libreoffice.org/core/tree/master/README.md

Dizze triem befettet wichtige ynformaasje oer it LibreOffice software. Der wurdt jo oanret om dizze ynformaasje mei soarch te lêzen foardat jo mei de ynstallaasje úteinsette.

De LibreOffice mienskip is ferantwurdlik foar de ûntwikkeling fan dit produkt, en nûget jo út om te oerwagen om mei de dwaan as lid fan de mienskip. As jo in nije brûker binne, dan kinne jo de webstee fan LibreOffice besykje, wêr jo ynformaasje fine kinne oer it LibreOffice projekt en de mienskippen der omhinne. Gean nei https://www.libreoffice.org/.

Is LibreOffice wier foar elkenien fergees te brûken?
----------------------------------------------------------------------

LibreOffice is fergees troch elkenien te brûken. Jo meie dizze kopy fan LibreOffice oannimme en it ynstallearje op safolle kompjûter as jo wolle, foar alle doeleinen meie jo it ek brûke (ynklusyf kommersjeel, oerheid, publyk bestjoer en ûnderwiis). Foar mear details sjoch de tekst fan de lisinsje dy't mei dizze ynlaad fan LibreOffice levere is.

Wêrom is LibreOffice fergees foar elke brûker?
----------------------------------------------------------------------

Jo kinne dizze kopy fan LibreOffice gehiel fergees brûke omdat yndividuele meidoggers en sponsoren, LibreOffice ûntwurpen, test, oerset, dokumintearre, stypje, en op de merk sette en op in soad oare manieren sadat it no is wat it is - de yn de wrâld meast foaroansteande Iepen Boarne produktiviteit software foar hûs en kantoar.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Taljochtingen by de ynstallaasje
----------------------------------------------------------------------

LibreOffice fereasket in resinte ferzje fan Java Runtime Environment (JRE) om folslein te funksjonearjen. JRE is gjin ûnderdiel fan it LibreOffice ynstallaasje pakket, en moat apart ynstallearre wurde.

Systeem fereasken
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Tink derom dat jo foech as systeembehearder nedich ha foar dit ynstallaasje proses.

Registraasje fan LibreOffice as standert programma foar Microsoft Office yndieling kin forsearre of ûnderdrukt wurde troch it brûken fan de folgjende skeakel opsjes foar opdrachtrigel mei it ynstallaasjeprogramma:

* REGISTER_ALL_MSO_TYPES=1 sil registraasje fan LibreOffice as standert programma ôftwinge foar Microsoft Office yndieling.
* REGISTER_NO_MSO_TYPES=1 sil registraasje fan LibreOffice as standert programma ûnderdrukke foar Microsoft Office yndieling.

Wês der wis fan dat jo genôch frije ûnthâld ha yn de tydlike map op jo systeem, en dat jo foech ha om hjiryn te skriuwen, te lêzen en út te fieren. Slút alle oare programma's ôf foardat jo mei de ynstallaasje úteinsette.

Ynstallaasje fan LibreOffice op Debian/Ubuntu basearre Linux systemen
----------------------------------------------------------------------

Foar ynstruksjes om in taal pakket te ynstallearjen (neidat jo de US Ingelske ferzje fan LibreOffice), lês de seksje hjirûnder mei as titel In taalpakket ynstallearje.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Dizze map befettet in sub-map neamd "DEBS". Feroarje de map nei de map "DEBS".

Rjochts klikke yn de map en kies "Iepenje yn in Terminal". Der iepenet in terminal finster. Op de opdrachtrigel fan it terminal finster fiere jo de folgjende opdracht yn (Jo sille frege wurde om it wachtwurd fan de root yn te fieren foardat de opdracht útfierd wurdt):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

It ynstallaasje proses is no foltôge, en jo soenen ikoanen moatte ha foar alle de LibreOffice programma's yn it menu Toepassingen/Kantoar fan jo buroblêd.

Ynstallaasje fan LibreOffice op Fedora, openSUSE, Mandriva en oare Linux systemen brûke RPM pakketten
----------------------------------------------------------------------

Foar ynstruksjes om in taal pakket te ynstallearjen (neidat jo de US Ingelske ferzje fan LibreOffice), lês de seksje hjirûnder mei as titel 'In taalpakket ynstallearje'.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Dizze map befettet in sub-map neamd "RPMS". Feroarje de map nei de "RPMS" map.

Rjochts klikke yn de map en kies "Iepenje yn in Terminal". Der iepenet in terminal finster. Op de opdrachtrigel fan it terminal finster fiere jo de folgjende opdracht yn (Jo sille frege wurde om it wachtwurd fan de root yn te fieren foardat de opdracht útfierd wurdt):

Foar Fedora basearre systemen: sudo dnf install *.rpm

Foar Mandriva basearre systemen: sudo urpmi *.rpm

Foar oare RPM basearre systemen (openSUSE, ensfh.): rpm -Uvh *.rpm

It ynstallaasje proses is no foltôge, en jo soenen ikoanen moatte ha foar al de LibreOffice programma's yn it menu Toepassingen/Kantoar fan jo buroblêd.

As alternatyf, kinne brûkme meitsje fan it 'ynstallaasje' skript, dat te finen is yn de heechste map fan dit argyf om in ynstallaasje te dwaan as brûker. De skript sil LibreOffice opsette mei in eigen profyl foar dizze ynstallaasje, skieden fan jo normale LibreOffice profyl. Tink derom dat dit net de systeem yntegraasje ûnderdielen ynstallearret lykas de buroblêd menu items en buroblêd MIME-type registraasjes.

Taljochtingen oer buroblêd yntegraasje foar Linux distribúsjes dy Net dekt wurde yn de boppesteande ynstallaasje ynstruksjes
----------------------------------------------------------------------

It soe maklik wêze moatte om LibreOffice te ynstallearjen op oare Linux distribúsjes dy net spesifyk opnaam binne yn dizze ynstallaasje ynstruksjes. It haad aspekt wêrby jo ferskillen kin tsjinkomme is buroblêd yntegraasje.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

In taal pakket ynstallearje
----------------------------------------------------------------------

Laad it taal pakket yn foar de troch jo winske taal en platfoarm. Se binne beskikber op deselde lokaasje as it haad ynstallaasje argyf. Mei de triembehearder Nautilus pakke jo it ynladen argyf út yn in map (Bygelyks jo buroblêd). Besjoch of alle LibreOffice programma's ôfsluten binne (ynklusyf Fluchstarter, as dizze úteinsetten is).

Feroarje de map nei de map wêryn jo it ynladen taal pakket útpakt ha.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Feroarje no de map nei de map dy it ynstallaasje pakket befettet. Op Debian/Ubuntu basearre systemen is de map DEBS. Op Fedora, Suse of Mandriva systemen is de map RPMS.

Fanút de Nautilus triembehearder, rjochts klik yn de map en kies de opdracht "Iepenje yn terminal". Yn de terminal finster dy't jo krekt iepene ha, fiere jo de opdracht út om it taal pakket te ynstallearjen (mei alle ûndersteande opdrachten, kin der frege wurde om it wachtwurd fan de root yn te fieren):

Foar Debian/Ubuntu basearre systemen: sudo dpkg -i *.deb

Foar Fedora basearre systemen: su -c 'dnf install *.rpm'

Foar Mandriva basearre systemen: sudo urpmi *.rpm

Foar oare RPM basearre systemen (openSUSE, ensfh.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Nei it oanpassen fan dizze ynstellingen, klik op Okee. It dialoochskerm sil ôfslute en jo sjogge in ynformaasje berjocht dy't jo ferteld dat jo oanpassingen allinne aktivearre wurde sille neidat jo LibreOffice ôfslute en op 'e nei úteinsetten ha (tink derom om ek de fluchstarter te sluten as dizze start is).

De folgjende kear as jo LibreOffice starte, sille dizze úteinsette yn de taal dy't jo krekt ynstallearre ha.

----------------------------------------------------------------------
Swierrigens ûnder it úteinsetten fan programma
----------------------------------------------------------------------

Swierrigens by it úteinsetten fan LibreOffice (lykas programma's dy't fêst rinne) ek swierrigens mei de skerm werjefte wurdt faaks feroarsake troch it stjoerprogramma fan de grafyske kaart. As dizze swierrigens barre, fernij dan it stjoerprogramma fan jjo grafyske kaart of besykje it grafyske stjoerprogramma te brûken dat by jo bestjoeringssysteem levere is.

----------------------------------------------------------------------
ALPS/Synaptics skoatkompjûter taastskerm yn Windows
----------------------------------------------------------------------

Troch in Windows stjoerprogramma swierrigens, kinne jo net skowe troch LibreOffice dokuminten as jo glydzje mei jo finger oer in ALPS/Synaptics taastskerm.

Foar it ynskeakeljen fan taastskerm skowen, heakje de folgjende rigels ta oan de "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" konfiguraasje triem, en werstart jo kompjûter:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

De lokaasje fan it konfiguraasje triem kin ferskille op de ferskillende ferzjes fan Windows.

----------------------------------------------------------------------
Fluchtoetsen
----------------------------------------------------------------------

Allinne fluchtoetsen (toets kombinaasjes) dy net brûkt wurde kin troch it bestjoeringssysteem yn LibreOffice. As in toets kombinaasje yn LibreOffice net wurket lykas beskreaun yn de help fan LibreOffice, kontrolearje dan of dy fluchtoets net al brûkt wurdt troch it bestjoeringssysteem. Jo kinne de troch jo systeem tawiisde toetsen feroarje om sokke konflikten op te lossen. As alternatyf kinne jo hast elke tawizing fan toetsen yn LibreOffice feroarje. Foar mear ynformaasje oer dit ûnderwerp sjogge jo yn de help fan LibreOffice of de Help dokumintaasje fan jo bestjoeringssysteem.

----------------------------------------------------------------------
Swierrigens by it ferstjoeren fan dokuminten as e-post fan út LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Wichtige taljochtingen oer tagonklikens
----------------------------------------------------------------------

Foar mear ynformaasje oer de tagonklikens mooglikheden yn LibreOffice, sjoch https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Brûkers stipe
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Besjoch ek it diel Faaks Frege Fragen the LibreOffice website.

----------------------------------------------------------------------
Brekken & swierrigens rapportearje
----------------------------------------------------------------------

Us systeem foar it melden, folgjen en oplossen fan brekken is op it stuit BugZilla, hosted op https://bugs.documentfoundation.org/. Wy trúnje al ús brûkers oan om brekken,dy har foardogge op beskate platfoarms, te melden. Energetyske rapportaazje fan brekken is ien fan de wichtichste bydragen dy de brûkers mienskip leverje kin oan de fierdere ûntwikkeling en ferbettering fan LibreOffice.

----------------------------------------------------------------------
Wurdt belutsen
----------------------------------------------------------------------

De LibreOffice mienskip soe in soad profitearje kinne fan jo aktive partisipaasje yn de ûntwikkeling fan dit wichtich iepen boarne projekt.

As in brûker binne jo al in weardefol ûnderdiel fan it ûntwikkeling proses fan it pakket en wy wolle jo oantrúnje om in noch aktivere rol yn te nimmen om op in langere termyn in bydrage te jaan oan de mienskip. Doch mei en besjoch de side oer de bydragen op de LibreOffice webstee.

Hoe te begjinnen
----------------------------------------------------------------------

De bêste manier om mei it bydragen te begjinnen is om yn te skriuwen by ien of mear ferstjoerlisten, en folgje dissen foar in tiid om fertroud te reitsjen mei de ferskate ûnderwerpen dy, sûnt de boarnekoade fan LibreOffice útkaam is yn oktober 2000, behannele is. Wannear jo fertroud fiele, kinne jo in e-post stjoere wêryn jo je foarstelle en begjin kalm oan. As jo fertroud binne mei Iepenboarne projekten, sjoch dan ris op de Takenlist en sjoch of der wat is wêrmei jo helpe wolle op the LibreOffice website.

Ynskriuwe
----------------------------------------------------------------------

Hjir binne in pear ferstjoerlisten wêr jo op ynskriuwe kinne op https://www.libreoffice.org/get-help/mailing-lists/

* Nijs: announce@documentfoundation.org *oanrekommandearre oan alle brûkers* (bytsje ferkear)
* Wichtichste brûkerslist: users@global.libreoffice.org *maklik manier om diskusjes te folgjen* (soad ferkear)
* Marketing projekt: marketing@global.libreoffice.org *faorby ûntwikkeling* (yn it ingelsk, wurdt drokker)
* Algemiene list foar ûntwikkelders: libreoffice@lists.freedesktop.org (soad ferkear)

Meidwaan mei ien of mear projekten
----------------------------------------------------------------------

Jo kinne wichtige bydragen dwaan oan dit iepenboarne projekt, sels as jo beheinde of gjin ûnderfining ha mei software ûntwerp of kodearring. Ja jo!

Wy hoopje dat it wurkjen mei de nije LibreOffice 26.2 jo befalt en by ús oanslute op it ynternet.

De LibreOffice mienskip

----------------------------------------------------------------------
Brûkte / Oanpaste boarnekoade
----------------------------------------------------------------------

Part Copyright 1998, 1999 James Clark. Part Copyright 1996, 1998 Netscape Communications Corporation.
