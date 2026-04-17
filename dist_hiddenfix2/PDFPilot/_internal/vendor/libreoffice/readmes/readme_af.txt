
======================================================================
LibreOffice 26.2 Lees my
======================================================================


Die huidige weergawe van hierdie readme-lêer kan gevind word op  https://git.libreoffice.org/core/tree/master/README.md.

Hierdie lêer bevat belangrike inligting oor die sagteware $ {PRODUCTNAME}. Dit word aanbeveel dat u hierdie inligting sorgvuldig deurlees voordat u met die installasie begin.

Die LibreOffice-gemeenskap is verantwoordelik vir die verdere ontwikkeling van hierdie sagteware en nooi u om as lid van die gemeenskap by te dra. As u 'n nuwe gebruiker is, kan u meer vind oor die LibreOffice-projek en die gemeenskap rondom die projek op die LibreOffice-bladsy. Besoek  https://libreoffice.org/ .

Is LibreOffice vir almal gratis?
----------------------------------------------------------------------

LibreOffice is gratis vir almal om te gebruik. U kan hierdie kopie van LibreOffice op enige aantal rekenaars installeer en dit vir enige doel (insluitend kommersiële, openbare administrasie en onderwys) gebruik. Vir meer inligting, lees asseblief die lisensie-teks wat by die LibreOffice aflaai ingesluit is.

Waarom is LibreOffice vry vir elke gebruiker?
----------------------------------------------------------------------

U kan hierdie eksemplaar van LibreOffice gratis gebruik, want individuele bydraers en maatskappy borge ontwerp, ontwikkel, toets, vertaal, dokumenteer, ondersteun, bemark en doen verskillende dinge om LibreOffice te maak wat dit is Vandag is dit die toonaangewende Oopbron-kantoor-programmatuur vir tuis- en korporatiewe gebruik.

As u hulle inspanning waardeer en wil sorg dat LibreOffice ook in die toekoms beskikbaar bly, oorweeg dan om 'n bydrae te lewer aan die projek - sien https://www.libreoffice.org/community/get-involved/ vir meer informasie. Iedereen kan op die een of ander manier 'n bydrae lewer.

----------------------------------------------------------------------
Aantekeninge by installasie
----------------------------------------------------------------------

LibreOffice benodig 'n huidige weergawe van die Java Runtime Environment (JRE) vir volledige funksionaliteit. JRE is nie deel van die LibreOffice installasiepakket nie, dus moet dit afsonderlik geïnstalleer word.

Stelselvereistes
----------------------------------------------------------------------

* Microsoft Windows 10 or hoër

Let daarop dat administrateurregte benodig word vir die installasie.

Om LibreOffice as verstek toepassing vir Microsoft Office-formate te registreer, kan afgedwing of onderdruk word met die volgende bevelreël-skakelings by die installeerder:

*  REGISTER_ALL_MSO_TYPES = 1  dwing LibreOffice om te registreer as die standaardtoepassing vir Microsoft Office-lêerformate.
*  REGISTER_NO_MSO_TYPES = 1  verhoed dat LibreOffice geregistreer word as 'n verstek toepassing vir Microsoft Office-lêerformate.

Sorg dat daar voldoende vrye ruimte in die tydelike vouer op u stelsel is en dat die skryf-, lees- en uitvoeringsregte ingestel is. Sluit alle lopende programme voordat u met die installasie begin.

Installasie van LibreOffice op Debian / Ubuntu gebaseerde Linux-stelsels
----------------------------------------------------------------------

Vir instruksies oor hoe om 'n taalpakket te installeer (nadat u die Amerikaanse Engelse weergawe van LibreOffice geïnstalleer het), kyk na die afdeling met die naam Language Pack Installation hieronder.

Wanneer jy die afgelaaide argief uitpak, sal jy sien dat die inhoud uitgepak is na 'n sub-lêergids. Maak 'n lêerbestuurder-venster oop en verander lêergidsnaam na een wat begin met "LibreOffice_", gevolg deur die weergawe-nommer en platforminligting.

Hierdie gids bevat 'n sub-vouer "DEBS". Verander na die "DEBS"-vouer.

Regsklik met die muis in die vouer en kies "Open in Terminal". 'n Opdragreëlvenster word oopgemaak. Voer in die volgende opdrag op die opdragreël (u sal gevra word om die "root"-gebruiker wagwoord in te voer voordat die opdrag uitgevoer word):

Die volgende opdragte sal LibreOffice en die rekenaar-integrasie-pakkette installeer (jy kan dit kopieer en dan in die terminaal skerm plak eerder as om dit te probeer intik):

sudo dpkg -i *.deb

Die installasieproses is nou voltooi en daar moet ikone wees vir alle LibreOffice-toepassings in keuse-lys: Programme / Office-toepassings op u tafelrekenaar.

Installeer LibreOffice op Fedora, openSUSE, Mandriva en ander Linux-stelsels wat RPM-pakkette gebruik
----------------------------------------------------------------------

Vir instruksies oor hoe om 'n taalpakket te installeer (nadat u die Amerikaanse Engelse weergawe van LibreOffice geïnstalleer het), kyk na die afdeling hieronder met die naam "Language Pack Installation".

Wanneer jy die afgelaaide argief uitpak, sal jy sien dat die inhoud uitgepak is in 'n sub-lêergids. Maak 'n lêerbestuurder-venster oop en verander die gids na die een wat begin met "LibreOffice_", gevolg deur die weergawe-nommer en sommige platform-inligting.

Hierdie vouer bevat 'n subvouer "RPMS". Gaan na die "RPMS" -gids.

Regsklik met die muis in die vouer en kies "Open in Terminal". 'n Opdragreëlvenster word oopgemaak. Voer die volgende opdrag in op die opdragreël (u sal gevra word om die "root"-gebruiker wagwoord in te voer voordat die opdrag uitgevoer word):

Vir Fedora-gebaseerde stelsels: "sudo dnf install * .rpm"

Vir Mandriva-gebaseerde stelsels: sudo urpmi * .rpm

Vir ander RPM-gebaseerde stelsels (openSUSE en so aan): rpm -Uvh * .rpm

Die installeringsprosesse is nou gereed en u kan die ikone gebruik om alle LibreOffice-toepassingsin die kieslys "Toepassingen / Kantoor" te loop vanaf u tafelrekenaar.

Alternatiewelik kan u die 'install' -script, wat in die boonste vouer van hierdie argief is, gebruik om 'n installasie as gebruiker uit te voer. Die skrip sal LibreOffice opstel om sy eie profiel te hê vir hierdie installasie, wat apart is van u normale LibreOffice -profiel. Let daarop dat hierdie stelsel-integrasie dele nie geïnstalleer word nie, soos die inskrywings op die tafelrekenaar kieslys en die registrasie van die desktop-MIME-tipes.

Opmerkings oor tafelrekenaar-integrasie vir Linux-verspreidings wat nie in die installeringsinstruksies oorweeg is nie
----------------------------------------------------------------------

Dit moet redelik maklik wees om LibreOffice op Linux-distribusies te installeer wat nie spesifiek hier oorweeg word nie. Die belangrikste verskille kan wees in tafelrekenaar-integrasie.

Die RPMS (of onderskeidelik DEBS) lêergids bevat ook 'n pakket genaamd libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (of libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, of iets soortgelyk). Dit is 'n pakket vir alle Linux-verspreidings wat die Freedesktop.org spesifikasies/aanbevelings ondersteun (https://en.wikipedia.org/wiki/Freedesktop.org), en word voorsien vir installasie op ander Linux-verspreidings wat nie in die bogenoemde instruksies gedek is nie.

Installeer 'n Taal Pakket
----------------------------------------------------------------------

Laai die taalpakket af vir die taal en platform wat u verkies. Dit is beskikbaar op dieselfde plek as die basiese installeringspakket. Pak die afgelaaide pakket in 'n vouer van u keuse via 'n lêerverkenner (byvoorbeeld op u tafelrekenaar). Sluit alle LibreOffice-toepassings af (insluitend die QuickStarter as dit begin).

Verander na die vouer waar u die taalpakket uitgevou het.

Verander nou die gids na die lêergids wat tydens die uitpakproses geskep is. Byvoorbeeld, vir die Franse taalpakket vir 'n 32-bis Debian/Ubuntu-gebaseerde stelsel, is die lêergids-naam LibreOffice_, plus nog weergawe-inligting, plus Linux_x86_langpack-deb_fr.

Verander nou na die vouer met die pakkette wat geïnstalleer moet word. Op Debian / Ubuntu-gebaseerde stelsels is dit die DEBS-vouer. Op Fedora, openSuse of Mandriva-stelsels is dit RPMS.

Regsklik met die muis in die lêerverkenner in die vouer en kies "Open in terminale". Voer die opdrag uit om die taalpakket te installeer by die opdrag (al die opdragte hieronder vra waarskynlik vir u "root'-gebruiker wagwoord):

Vir Debian/Ubuntu gebaseerde stelsels: sudo dpkg -i *.deb

Vir Fedora-gebaseerde stelsels: "su -c 'dnf install * .rpm' "

Vir Mandriva gebaseerde stelsels: sudo urpmi *.rpm

Vir ander stelsels, wat RPM gebruik (Suse, etc.): rpm -Uvh *.rpm

Begin nou een van die LibreOffice-toepassings - Writer, byvoorbeeld. Gaandie Nutsprogramme-kieslys en kies Opsies. Klik in die Opsies dialoogkassie op "Tale en lokaliteit" en klik dan op "Algemeen". Wip-af die "Gebruikerskoppelvlak" lys en kies die taal wat jy sopas geïnstalleer het. As jy wil, doen dieselfde ding vir die "Lokaliteitsinstelling",  die "Verstek geldeenheid" en die "Verstek tale vir dokumente".

Nadat u hierdie instellings gemaak het, klik op OK. Die dialoogvenster sluit en u sal sien dat die veranderinge eers geld sal word na die herbegin van LibreOffice (onthou om ook QuickStarter te stop as dit begin het).

Die volgende keer dat LibreOffice begin word, sal dit begin in die taal wat u pas geïnstalleer het.

----------------------------------------------------------------------
Probleme tydens programbegin
----------------------------------------------------------------------

Probleme met LibreOffice (bv. Programme hang) sowel as probleme met die vertoonskerm word dikwels veroorsaak deur die grafiese kaart se drywer. As hierdie probleme opduik, moet u die grafiese kaart se drywer opdateer of gebruik u bedryfstelsel se grafiese drywer.

----------------------------------------------------------------------
ALPS/Synaptics-notaboek-streelpanele in Windows
----------------------------------------------------------------------

As gevolg van 'n probleem met 'n Windows-drywer kan u nie deur LibreOffice-dokumente rol wanneer u met u vinger op 'n ALPS/Synaptics-streelpaneel streel nie.

Om die rol met die aanraakskerm te laat rol, voeg die volgende reëls by die lêer " C: \ Program Files \ Synaptics \ SynTP \ SynTPEnh.ini " en herbegin u rekenaar:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Die ligging van die konfigurasielêer kan afhang van die Windows-weergawe.

----------------------------------------------------------------------
Snelsleutels
----------------------------------------------------------------------

Slegs sleutelkombinasies wat nie deur die bedryfstelsel gebruik word nie, kan in LibreOffice gebruik word. As 'n sleutelkombinasie in LibreOffice nie werk soos beskryf in die hulp van LibreOffice nie, moet daar gekyk word of hierdie kombinasie reeds deur die bedryfstelsel gebruik word. Om hierdie konflik op te los, kan die toewysing van die bedryfstelsel herdefinieer of verwyder word. Alternatiewelik kan byna elke sleutelborduitleg in LibreOffice verander word. Bykomende inligting oor hierdie onderwerp kan gevind word in die LibreOffice-hulp en die hulp van die bedryfstelsel.

----------------------------------------------------------------------
Probleme met versending van dokumente as e-Posse vanuit LibreOffice
----------------------------------------------------------------------

Wanneer 'n dokument via 'Lêer - Stuur - E-pos dokument' of 'Lêer - Stuur - E-pos as PDF' gestuur word, kan probleme opduik (program crash of hang). Dit is as gevolg van die Windows-stelsel lêer "Mapi" (Messaging Application Programming Interface) wat probleme in sommige lêer weergawes veroorsaak. Ongelukkig kan die probleem nie tot 'n sekere weergawenommer beperk word nie. Vir meer inligting besoek https://www.microsoft.com om die Microsoft Knowledge Base vir "mapi dll" te deursoek.

----------------------------------------------------------------------
Belangrike toeganklikheidsaantekeninge
----------------------------------------------------------------------

Verdere inligting oor toeganklikheid in LibreOffice kan gevind word op  https://libreoffice.org/get-help/accessibility / .

----------------------------------------------------------------------
Gebruikersteun
----------------------------------------------------------------------

Die  hoof bladsy vir hulp bied verskeie geleenthede vir hulp met  LibreOffice. U vraag is moontlik alreeds beantwoord - bekyk die Gemeenskapsforum by https://ask.libreoffice.org/ of deursoek argiewe van  'users@libreoffice.org' poslys by https://www.libreoffice.org/lists/users/. Alternatiewelik, kan u vrae instuur na users@libreoffice.org. Sou u verkies om in te skrywe na die lys (om epos antwoorde te kry), stuur 'n leë epos na: users+subscribe@libreoffice.org.

Kyk ook na die gereelde vrae op die  LibreOffice-webwerf .

----------------------------------------------------------------------
Foute & Probleme rappporteer
----------------------------------------------------------------------

Ons stelsel om foute aan te meld, op te spoor en op te los, is tans BugZilla en is geleë op  https://bugs.documentfoundation.org/ beskikbaar. Ons moedig almal aan om self foute aan te meld wat op die platform mag voorkom. Die aktiewe rapportering van foute is een van die belangrikste bydraes wat die gebruikersgemeenskap kan lewer om die verdere ontwikkeling van LibreOffice te ondersteun.

----------------------------------------------------------------------
Raak Betrokke
----------------------------------------------------------------------

Die LibreOffice-gemeenskap sou graag wou voordeel trek uit jou aktiewe deelname in die ontwikkeling van hierdie belangrike oopbronprojek.

As gebruiker is u reeds 'n waardevolle deel van die ontwikkelingsproses van die Office Suite en wil ons u aanmoedig om op die langtermyn aan die gemeenskap deel te neem. Besoek ons webwerf by  https://libreoffice.org/community/  .

Hoe om te begin
----------------------------------------------------------------------

Die maklikste manier om aan die gang te kom, is om in te teken op een of meer e-poslyste, 'n rukkie te lees en die onderwerpe in die e-posargiewe te bespreek wat bespreek is sedert die LibreOffice-projek in Oktober 2000 van stapel gestuur is. Sodra u gereed is, stuur 'n e-pos met 'n kort self-inleiding en raak direk betrokke. As u reeds vertroud is met open source-projekte, kyk dan na  https://libreoffice.org/community/developers/  volgens die vraag of daar 'n taak vir u is.

Teken in
----------------------------------------------------------------------

Hier is 'n paar van die poslyste waarop u kan inteken:  https://libreoffice.org/get -help / poslyste / 

* Nuus: announce@de.libreoffice.org - * Aanbeveel vir alle gebruikers * (lae posvolume)
* Gebruikershulp: users@de.libreoffice.org - * Gebruikersondersteuning vir LibreOffice * (hoë volume pos)
* Bemarking: marketing@global.libreoffice.org - * Adverteer LibreOffice * (groot hoeveelheid pos, Engels)
* Algemene lys ontwikkelaars: libreoffice@lists.freedesktop.org (groot hoeveelheid pos, Engels)

Sluit aan by een of meer projekte
----------------------------------------------------------------------

U kan groot bydraes lewer tot hierdie oopbronprojek selfs al het u beperkte sagtewareontwerp- of koderingservaring. Ja, u kan!

Ons hoop u geniet dit om met die nuwe LibreOffice 26.2 te werk en dat u aanlyn by ons sal aansluit.

Die LibreOffice-gemeenskap

----------------------------------------------------------------------
Gebruikte / gewysigde bronkode
----------------------------------------------------------------------

Gedeeltes van kopiereg 1998, 1999 deur James Clark. Gedeeltes van kopiereg 1996, 1998 Netscape Communications Corporation.
