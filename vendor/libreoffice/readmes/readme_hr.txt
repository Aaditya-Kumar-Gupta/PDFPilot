
======================================================================
LibreOffice 26.2 PročitajMe
======================================================================


Pregledaj zadnje promjene ove readme-datoteke na https://git.libreoffice.org/core/tree/master/README.md

Ova datoteka sadrži bitne informacije o programskom paketu LibreOffice. Preporučujemo vam da pažljivo pročitate ove informacije prije pokretanja instalacije.

LibreOfficeova je zajednica odgovorna za razvoj ovoga proizvoda te poziva i tebe da postaneš članom zajednice. Ako si novi korisnik, posjeti LibreOfficeovu stranicu jer tamo možeš pronaći više informacija o LibreOfficeu i zajednicama oko ovoga projekta. Posjeti https://www.libreoffice.org/.

Je li LibreOffice stvarno besplatan za bilo kojeg korisnika?
----------------------------------------------------------------------

LibreOffice mogu slobodno koristiti svi. Ovu kopiju LibreOfficea možete instalirati na koliko god računala želite i koristiti u koju god svrhu želite (komercijalne, državne, administrativne i edukacijske). Za više informacija pogledajte tekst licence uklopljen u preuzetu inačicu LibreOfficea.

Zašto je LibreOffice besplatan za bilo kojeg korisnika?
----------------------------------------------------------------------

Ovu kopiju LibreOffice možete koristiti bez naplate jer su se pojedinci i korporativni sponzori udružili i dizajnirali, razvili, testirali, preveli, dokumentirali, podržali, reklamirali ili pomogli na druge načine u stvaranju današnje inačice LibreOffice paketa – vodećeg uredskog paketa otvorenog koda.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Zabilješke o instalaciji
----------------------------------------------------------------------

LibreOffice zahtjeva noviju inačicu Java Runtime Environment (JRE) za potpunu funkcionalnost. JRE nije dio LibreOffice instalacijskog paketa i treba se instalirati odvojeno.

Zahtjevi prema sustavu
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Potrebna su vam administratorska prava za proces instalacije.

Registracija LibreOffice kao zadanog programa za upravljanje Microsoft Office formatima može se prsiliti ili onemogućiti korištenjem sljedećih naredbi u instalaciji:

* REGISTER_ALL_MSO_TYPES=1 će registrirati LibreOffice kao zadani program za Microsoft Office datoteke.
* REGISTER_NO_MSO_TYPES=1 će ukloniti registraciju LibreOffice kao zadanog programa za Microsoft Office datoteke.

Provjerite imate li dovoljno slobodne memorije u privremenoj mapi na vašem sustavu, te se uvjerite da su vam odobrena prava čitanja, pisanja i izvršavanja. Zatvorite sve druge programe prije pokretanja instalacije.

Instalacija LibreOffice na sustave bazirane na Debian/Ubuntu
----------------------------------------------------------------------

Za upute kako instalirati jezični paket (nakon instalacije engleske SAD LibreOffice inačice), pročitajte niže navedeni odjeljak naslovljen Instalacija jezičnog paketa.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Ova mapa sadrži podmapu naziva „DEBS”. Promjenite mapu u „DEBS”.

Kliknite desnom tipkom miša u mapu i odaberite naredbu „Otvori u terminalu”. Otvorit će se prozor terminala. U naredbenom retku izvršite sljedeću naredbu (od Vas će biti zatražena root lozinka prije izvršenja naredbe):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Instalacijski proces je završen te biste trebali imati ikone svih LibreOffice modula u izborniku Programi/Ured.

Instalacija LibreOffice na Fodoru, openSUSE, Mandrivu i druge Linux sustave koristeći RPM pakete
----------------------------------------------------------------------

Za upute kako instalirati jezični paket (nakon instalacije engleske SAD LibreOffice inačice), pročitajte niže navedeni odjeljak naslovljen Instalacija jezičnog paketa.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Ova mapa sadrži podmapu naziva „RPMS”. Promjenite mapu u „RPMS”.

Kliknite desnom tipkom miša u mapu i odaberite naredbu „Otvori u terminalu”. Otvorit će se prozor terminala. U naredbenom retku izvršite sljedeću naredbu (od Vas će biti zatražena root lozinka prije izvršenja naredbe):

Za sustave temeljene na Fedori: sudo dnf install *.rpm

Sustavi temeljeni na Mandriva: sudo urpmi *.rpm

Za ostale sustave bazirane na RPM (openSUSE, etc.): rpm -Uvh *.rpm

Instalacijski proces je završen te biste trebali imati ikone svih LibreOffice modula u izborniku Programi/Ured.

Alternativno, možete koristiti 'install' skriptu, koja se nalazi u vršnom direktoriju ove arhive kako biste napravili instalaciju kao korisnik. Skripta će postaviti vlastiti LibreOffice profil za ovu instalaciju, odvojeno od standardnog LibreOffice profila. Ovo neće instalirati dijelove sistemske integracije kao što su stavke izbornika radne površine i registracije MIME tipa radne površine.

Bilješke u vezi integracije u radnu površinu za Linux distribucije koje nisu naznačene u prethodnim uputstvima za instalaciju
----------------------------------------------------------------------

Trebalo bi biti moguće lako instalirati LibreOffice na druge Linux distribucije koje nisu pokrivene ovim uputstvima. Glavni dio u kojem se može naići na razlike je integracija sa radnom površinom.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Instalacija jezičnog paketa
----------------------------------------------------------------------

Preuzmite jezični paket vašeg željenog jezika i platforme. Paketi su dostupni na istom mjestu kao i glavna instalacijska arhiva. Iz upravitelja datotekama Nautilus, otpakirajte preuzetu arhivu u mapu (na primjer, radna površina). Provjerite jeste i isključili sve programe paketa LibreOffice (uključujući i Brzo pokretanje, ukoliko je pokrenut).

Otvorite mapu u kojoj je otpakiran preuzeti jezični paket.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Sada otvorite mapu koja sadrži instalacijske pakete. Na Debian/Ubuntu baziranim sustavima, postojat će mapa DEBS. Na Fedori, openSUSE-u ili Mandrivi, postojat će mapa RPMS.

Iz upravljača za datoteke Nautilus, izvršite desni klik na mapu i odaberite naredbu „Otvori u terminalu”. U prozoru terminala, koji se upravo otvorio, izvršite naredbu za instaliranje jezičnog paketa (sa svim dolje napisanim naredbama, biti ćete upitani za upis lozinke korisnika root):

Za sustave bazirane na Debian/Ubuntu: sudo dpkg -i *.deb

Za Fedora temeljene sustave: su -c 'dnf install *.rpm'

Sustavi temeljeni na Mandriva: sudo urpmi *.rpm

Za ostale sustave koji koriste RPM (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Nakon prilagodbe ovih postavki, kliknite na 'U redu'. Dijaloški okvir će se zatvoriti i vidjet ćete poruku, da će vaše izmjene biti primjenjene tek nakon što izađete iz LibreOffice i ponovo ga pokrenete (nemojte zaboraviti isključiti Brzo pokretanje ukoliko je uključeno).

Sljedeći put kad pokrenete LibreOffice, pokrenuti će se jezik koj iste upravo instalirali.

----------------------------------------------------------------------
Problemi prilikom pokretanja programa
----------------------------------------------------------------------

Poteškoće s pokretanjem LibreOffice (npr. prekid programa) kao i problemi s ekranom često su uzrokovani upravljačkim programom grafičke kartice. Ako se ovi problemi pojave, aktualiziraj upravljački program grafičke kartice ili pokušaj koristiti grafički upravljački program tvog operacijskog sustava.

----------------------------------------------------------------------
ALPS/Synaptics dodirna ploča za prijenosna računala pod MS Windows
----------------------------------------------------------------------

Zbog problema s upravljačkim programom Windowsa, ne možete klizati kroz LibreOffice dokumente, kad pomićete prst preko taktilne ploče proizvođača ALPS/Synaptics.

Omogućite klizanje pomoću dodirne ploče, dodajući sljedeće retke u konfiguracijsku datoteku „C:\Program Files\Synaptics\SynTP\SynTPEnh.ini”, te ponovo pokrenite računalo:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Smještaj konfiguracijske datoteke može se razlikovati kod različitih inačica Windowsa.

----------------------------------------------------------------------
Prečice
----------------------------------------------------------------------

U LibreOfficeu se mogu koristiti samo tipkovničke kratice (kombinacije tipaka) koje ne koristi operativni sustav. Ako u LibreOfficeu kombinacija tipki ne radi kao što je opisano u LibreOffice Pomoći, provjerite ne koristi li već te kratice operativni sustav. Možete promjeniti kratice vašeg operativnog sustava kako biste ispravili ove konflikte. Uostalom, LibreOffice omogućuje promjenu gotovo svih tipkovničkih kratica. Radi više informacija pogledajte LibreOffice Pomoć ili Pomoć vašeg operativnog sustava.

----------------------------------------------------------------------
Problemi prilikom slanja dokumenata kao e-maila od LibreOffice
----------------------------------------------------------------------

Slanjem dokumenta kroz „Datoteka - Pošalji - Pošalji dokument e-poštom”, ili „Datoteka - Pošalji - Pošalji e-poštom kao PDF” može doći do problema (rušenja ili nereagiranje programa). Navedeno se događa zbog Windows sustavne datoteke „Mapi” (Messaging Application Programming Interface). Nažalost problem nije vezan uz konkretnu inačicu. Za više informacija posjetitehttps://www.microsoft.com i u Microsoftovoj bazi znanja potražite "mapi dll".

----------------------------------------------------------------------
Važne napomene o pristupačnosti
----------------------------------------------------------------------

Za više informacija o funkcijama za pristupačnost u LibreOffice, pogledajte na https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Podrška korisnicima
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Proverite FAQ odlomak na  LibreOffice web site-u.

----------------------------------------------------------------------
Prijavljivanje nedostataka i problema
----------------------------------------------------------------------

BugZilla je naš trenutačni sustav za prijavljivanje, praćenje i rješavanje grešaka host-ana je nahttps://bugs.documentfoundation.org/. Pozivamo sve korisnike da prijavljuju greške koje se mogu pojaviti na vašim platformama. Često prijavljivanje grešaka jedan je od najvažnijih doprinosa koji zajednica korisnika može napraviti za kontinuirani razvoj i napredak LibreOffice.

----------------------------------------------------------------------
Uključivanje u projekt
----------------------------------------------------------------------

LibreOffice zajednica može uvelike prosperirati vašim aktivnim doprinosom u razvoju ovog važnog open source projekta.

Kao korisnik, Vi ste već vrijedan član procesa razvijanja paketa i voljeli bismo vas potaknuti da se još aktivnije uključite i eventualno postanete dugoročni suradnik zajednice. Pridružite se i pogledajte stranicu doprinosa na  LibreOffice web site-u

Kako početi
----------------------------------------------------------------------

Želite li započeti pridonositi, najbolji je način pretplatiti se na jednu ili više pretplatničkih lista, neko vrijeme promatrati i kroz arhive se postupno upoznavati s temama aktualiziranima još otkako je objavljen izvorni kȏd LibreOffice u listopadu 2000. Kad se opustite, sve što trebate jest predstaviti se u poruci i – uključiti se. Ako ste upoznati s drugim projektima otvorenog koda, provjerite popis zadataka na LibreOffice web stranicama.

Pretplata
----------------------------------------------------------------------

Ovdje je nekoliko popisa skupnih e-poruka projekata na koje se možete prijaviti https://www.libreoffice.org/get-help/mailing-lists/

* Novosti: announce@documentfoundation.org *preporučeno svim korisnicima* (mali promet)
* Glavni korisnički popis primatelja: users@global.libreoffice.org *lagani način vrebanja rasprava* (veliki promet)
* Marketing projekt: marketing@global.libreoffice.org *iznad razvoja* (počinje imati veliki promet)
* Opći popis skupne e-pošte za razvijatelje: libreoffice@lists.freedesktop.org (velik promet)

Pridruživanje jednom ili više projekata
----------------------------------------------------------------------

I vi možete dati velik doprinos ovom važnom projektu otvorenog koda čak i ako imate malo iskustva u oblikovanju ili programiranju softvera. Da, vi!

Nadamo se da ste uživali u radu s novom LibreOffice 26.2 inačicom i da ćete nam se pridružiti na webu.

Zajednica LibreOffice

----------------------------------------------------------------------
Korišteni/promijenjeni izvorni kȏd
----------------------------------------------------------------------

Djelomično autorsko pravo 1998, 1999 James Clark. Djelomično autorsko pravo 1996, 1998 Netscape Communications Corporation.
