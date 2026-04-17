
======================================================================
LibreOffice 26.2 LeguMin
======================================================================


Por la aktualaj ĝisdatigoj por ĉi tiu legumina dosiero, rigardu alhttps://git.libreoffice.org/core/tree/master/README.md

Ĉi tiu dosiero enhavas gravajn informojn pri la LibreOffice-programaro. Bonvolu detale legi ĉi tiujn informojn antaŭ ol ekinstali.

La LibreOffice-komunumo respondecas pri la evoluigo de ĉi tiu produkto, kaj invitas vin konsideri partopreni kiel komunumano. Se vi estas nova uzanto, vi povas viziti la retejon de LibreOffice, kie troviĝas multa informo pri la LibreOffice-projekto kaj la komunumoj kiuj ekzistas ĉirkaŭ ĝi. Iru al https://www.libreoffice.org/.

Ĉu LibreOffice vere estas libera por ĉiu uzanto?
----------------------------------------------------------------------

LibreOffice estas libere uzebla de ĉiu. Vi rajtas preni ĉi tiun kopion de LibreOffice kaj instali ĝin sur tiom ajn komputiloj kiom vi ŝatas, kaj uzi ĝin ial ajn kial vi ŝatas (inkluzive por komerca, registara, publikadministra kaj eduka uzo). Por pliaj detaloj vidu la permesilan tekston liveritan kune kun LibreOffice-elŝutaĵo.

Kial LibreOffice estas libera por ĉiu uzanto?
----------------------------------------------------------------------

Vi povas uzi ĉi tiun kopion de LibreOffice nuntempe sen kostoj ĉar individuaj kontribuantoj kaj kompaniaj sponsoroj planis, evoluigis, testis, tradukis, dokumentis, subtenis, enmerkatigis, kaj helpis multmaniere por fari de LibreOffice tion, kio ĝi estas hodiaŭ - la mondgvida liberfonta oficeja programaro.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Notoj pri instalado
----------------------------------------------------------------------

LibreOffice bezonas antaŭnelongan version de Ĝava-rultempa medio (JRE) por tuta funciado. JRE ne estas parto de la -instala pakaĵo de LibreOffice; necesas aparte instali ĝi.

Bezonoj de sistemo:
----------------------------------------------------------------------

* Microsoft Windows 10 aŭ pli freŝa

Noto: Bonvolu konscii ke administrantaj rajtoj estas bezonataj por la instalado.

Registrado de LibreOffice kiel apriora aplikaĵo por formatoj de Microsoft Office eblas igi aŭ ellasi uzante la jenajn komandliniajn parametrojn per la instalilo:

* REGISTER_ALL_MSO_TYPES=1 devigos registri je LibreOffice kiel la apriora aplikaĵo por formatoj de Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 preventos registri je LibreOffice kiel la apriora aplikaĵo por formatoj de Microsoft Office.

Bonvolu certigu ke vi havs sufiĉan liberan memoron en la dumtempa dosierujo sur via sistemo kaj ke legaj, skribaj kaj rulaj alirorajtoj estas ceditaj. Fermu ĉiujn aliajn programojn antaŭ startado de la instalo.

Instali je LibreOffice en Debian/Ubuntu-bazitaj Linuksaj sistemoj
----------------------------------------------------------------------

Por instrukcioj pri kiel instali lingvan pakaĵon (instalinte la usonanglan version de LibreOffice), bonvolu legi la sekvan sekcion nomitan Instali Lingvan Pakaĵon.

Kiam vi malpakas la elŝutitan arĥivon, vi vidos ke la enhavo estas maldensigita en subdosierujon. Malfermu fenestron de la dosiera mastrumilo, kaj ŝanĝu la dosierujon al tiu komencanta per  "LibreOffice_", sekvata de la versionumero kaj ia platforma informo.

Ĉi tiu dosierujo enhavas subdosierujon nomitan "DEBS". Ŝanĝu dosierujon al la dosierujo "DEBS".

Dekstre alklaku en la subdosierujo kaj elektu je "Malfermi en terminalo". Terminala fenestro malfermiĝos. En la komanda linio de la terminala fenestro, enigu la jenan komandon (ĝi invitos vin enigi vian ĉefuzantan pasvorton antaŭ ol la komando ruliĝos).

La jenaj komandoj instalos je LibreOffice kaj la labortablajn integrigajn pakaĵojn (vi devas kopii kaj alglui ilin en la terminalan ekranon anstataŭ tajpi ilin):

sudo dpkg -i *.deb

La instalado nun estas finita, kaj vi devus havi bildsimbolojn por ĉiuj LibreOffice-aplkiaĵoj en la menuo Aplikaĵoj/Oficejo de via labortablo.

Instali je LibreOffice en Fedora, openSUSE, Mandriva kaj aliaj Linuksaj sistemoj kiuj utiligas RPM-pakaĵoj
----------------------------------------------------------------------

Por instrukcioj pri kiel instali lingvan pakaĵon (instalinte la usonanglan version de LibreOffice), bonvolu legi la sekvan sekcion nomitan Instali Lingvan Pakaĵon.

Kiam vi malpakas la elŝutitan arĥivon, vi vidos ke la enhavo estas maldensigita en subdosierujon. Malfermu fenestron de la dosiera mastrumilo, kaj ŝanĝu la dosierujon al tiu komencanta per "LibreOffice_", sekvata de la versionumero kaj ia platforma informo.

Ĉi tiu dosierujo enhavas subdosierujon nomitan "RPMS". Ŝanĝu dosierujon al la dosierujo "RPMS".

Dekstre alklaku en la subdosierujo kaj elektu je "Malfermi en terminalo". Terminala fenestro malfermiĝos. En la komanda linio de la terminala fenestro, enigu la jenan komandon (ĝi invitos vin enigi vian ĉefuzantan pasvorton antaŭ ol la komando ruliĝos).

Por Fedora-bazitaj sistemoj: sudo dnf install *.rpm

Por sistemoj bazitaj sur Mandriva: sudo urpmi *.rpm

Por aliaj RPM-bazitaj sistemoj (openSUSE, ktp.): rpm -Uvh *.rpm

La instalado nun estas finita, kaj vi devus havi bildsimbolojn por ĉiuj LibreOffice-aplkiaĵoj en la menuo Aplikaĵoj/Oficejo de via labortablo.

Aŭ, vi povas uzi la skripton 'install', kiu troviĝas en la plejaltnivela dsoierujo de ĉi tiu arĥivo, por instali kiel uzanto. La skripto agordos je LibreOffice havi sian profilon por ĉi tiu instalaĵo, aparte de via normala LibreOffice-profilo. Notu ke tio ne instalos la sistemintegrajn partojn, ekzemple la labortablajn menuerojn kaj labortablajn MIME-tipajn registrojn.

Notoj pri labortabla integrado por linuksaj distribuoj ne traktitaj en la supraj instrukcioj pri instalado.
----------------------------------------------------------------------

Devus ebli facile instali je LibreOffice en aliaj Linuksaj distribuoj ne specife traktitaj en ĉi tiuj instrukcioj. La ĉefa aspekto por kiu diferencoj eble troviĝos, temas pri labortabla integrado.

La RPMS (aŭ DEBS, respektive) dosierujo ankaŭ enhavas pakaĵon nomitan libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respektive, aŭ simile). Ĉi tiu estas pakaĵo por ĉiuj linuksaj distribuaĵoj kiuj subtenas la specifojn de Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), kaj estas liverata por instaliĝi sur aliaj distribuaĵoj ne kovritaj en la antaŭe menciitaj instrukcioj.

Instali lingvan pakaĵon
----------------------------------------------------------------------

Elŝutu la lingvan pakaĵon por via dezirataj lingvo kaj platformo. Ili disponeblas el la sama loko kiel la ĉefa instala arĥivo. De la dosieradministrilo Nautilus, eltiru la elŝutitan arĥivon en dosierujon (ekzemple via labortablo). Certigu ke vi eliris ĉiujn LibreOffice-aplikaĵojn (inkluzive QuickStarter, se ĝi estas startigita).

Ŝanĝu dosierujon al tiu dosierujo en kiu vi eltiris vian elŝutitan lingvan pakaĵon.

Nun ŝanĝu la dosierujon al la dosierujo kreita dum la ekstrakta procedo. Ekzemple, por la franca lingvopako por la 32-bita Debian/Ubuntu-bazita sistemo, la dosierujo estas nomita LibreOffice_, plus iu versia informo, plus Linux_x86_langpack-deb_fr.

Nun ŝanĝu dosierujon al la dosierujo kiu enhavas la pakaĵojn instalotajn. En Debian/Ubuntu-bazita sistemo, la dosierujo estos DEBS. En Fedora, Suse aŭ Mandriva-sistemo, la dosierujo estos RPMS.

En la dosieradministrilo Nautilus, dekstre alkalku la dosierujon kaj elektu la komandon "Malfermi en terminalo". En la ĵus malfermita terminala fenestro, rulu la komandon por instali la lingvan pakaĵon (kun ĉiuj subaj komandoj, ĝi eble invitos vin enigi vian ĉefuzantan pasvorton):

Por Debian/Ubuntu-bazitaj sistemo: sudo dpkg -i *.deb

Por sistemoj bazitaj sur Fedora: su -c 'dnf install *.rpm'

Por sistemoj bazitaj sur Mandriva: sudo urpmi *.rpm

Por aliaj RPM-uzantaj sistemoj (openSUSE, etc.): rpm -Uvh *.rpm

Nun startigu iun el la LibreOffice aplikaĵoj - Verkilo, ekzemple. Iru al la menuero Iloj kaj elektu je Agordoj. En la agorda dialogo, alklaku al "Lingvoj kaj lokaĵaroj" kaj alklaku al "Ĝenerale". Faligu la liston "Uzula interfaco" kaj elektu la lingvon ĵus instalita. Se vi volas, faru same por la "Lokaĵara agordaro", la "Apriora valuto", kaj "Aprioraj lingvoj por dokumentoj".

Modifinte tiujn agordojn, alklaku al Akcepti. La dialogo fermiĝos, kaj vi vidos mesaĝon informi vin ke viaj ŝanĝoj aktiviĝos nur post fermo kaj remalfermo de LibreOffice (memoru eliri el QuickStarter, se ĝi estas startigita).

Je la sekva fojo kiam vi startigos je LibreOffice, ĝi komenciĝos en a lingvo kiun vi ĵus instalis.

----------------------------------------------------------------------
Problemoj dum programlanĉo
----------------------------------------------------------------------

Malfacilaĵojn startigi je LibreOffice (ekzemple, aplikaĵoj paraliziĝas) kaj problemojn pri la ekrana vidigo ofte kaŭzas la pelilo de la grafika karto. Se tiaj problemoj okazas, bonvolu ĝisdatigi la pelilon de via grafika karto, aŭ provi uzi la pelilon liveritan kun via operaciumo.

----------------------------------------------------------------------
ALPS/Synaptics tekkomputila tuŝtabulo en Vindozo
----------------------------------------------------------------------

Pro problemo pri vindoza pelilo, oni ne povas rulumi tra dokumentoj de LibreOffice kiam oni glitigas fingron trans la tuŝkuseneto de ALPS/Synaptics.

Por enŝalti tuŝtabulan rulumadon, aldonu la sekvajn liniojn al la agorda dosiero "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini", kaj restartigu vian komputilon:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

La loko de la agorda dosiero eble varias ĉe diversaj versioj de Vindozo.

----------------------------------------------------------------------
Fulmklavoj
----------------------------------------------------------------------

Nur fulmklavoj (klavaj kombinaĵoj) neuzataj de la mastruma sistemo estas uzeblaj en LibreOffice. Se klava kombinaĵo en LibreOffice ne funkcias kiel priskribita en la Helpo de LibreOffice, kontrolu ĉu tiu kombinaĵo jam estas uzata de la mastruma sistemo. Por solvi tiajn konfliktojn, vi povas ŝanĝi la klavojn atribuitajn de via mastruma sistemo. Alie, vi povas ŝanĝi preskaŭ iun ajn klavan agordon en LibreOffice. Por plia informo tiutema, vidu la Helpon de LibreOffice aŭ de via mastruma sistemo.

----------------------------------------------------------------------
Problemoj dum sendado de dokumentoj kiel retpoŝtoj el LibreOffice
----------------------------------------------------------------------

Sendante dokumenton per 'Dosiero - Sendi - Dokumento kiel retpoŝto' aŭ 'Dosiero - Sendi -Dokumento kiel PDF', eble okazos problemoj (programaj haltoj). Tio ŝuldas al la sistema dosiero "Mapi" (Mesaĝa Aplikaĵa Programa Interfaco) de Vindozo, kiu kaŭzas problemojn ĉe iuj dosieraj versioj. Bedaŭrinde, la problemo ne limiĝas al specifa versionumero. Por plua informo vizitu al https://www.microsoft.com por serĉi tra la datumbazo Microsoft Knowledge Base por "mapi dll".

----------------------------------------------------------------------
Gravaj notoj pri alireblo
----------------------------------------------------------------------

Por plua informo pri la aliraj funkcioj en LibreOffice, legu je https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Subteno de uzantoj
----------------------------------------------------------------------

La ĉefa subtena paĝo  prezentas diversajn eblojn por helpi pri LibreOffice. Via demando eble jam estas respondita - kontrolu la Komunuman Forumon ĉe https://ask.libreoffice.org/ aŭ serĉu la arĥivojn de la retpoŝta listo 'users@libreoffice.org' https://www.libreoffice.org/lists/users/. Aŭ, vi povas sendi vian demandon al users@libreoffice.org. Se vi volas aliĝi al la listo (por ricevi retpoŝtajn respondojn), sendu vakan retpoŝton al: users+subscribe@libreoffice.org.

Ankaŭ kontrolu la FAQ (oftajn demandojn) ĉe la retejo de LibreOffice.

----------------------------------------------------------------------
Raporti erarojn kaj problemojn
----------------------------------------------------------------------

Nia sistemo por raporti, spuri kaj solvi cimojn aktuale estas Bugzilla, gastigata ĉe https://bugs.documentfoundation.org/. Ni rekomendas al ĉiuj uzantoj senti sin rajtigita kaj bonvena por raporti problemojn kiuj ekestas ĉe via specifa platformo. Energia raportado de problemoj estas iu el la plej gravaj kontribuoj kiujn la uzantkomunumo povas fari al la daŭra evoluo kaj plibonigo de LibreOffice.

----------------------------------------------------------------------
Ekokupiĝi
----------------------------------------------------------------------

La Komunumo de LibreOffice tre avantaĝus de via aktiva partopreno en la evoluo de ĉi tiu grava liberfonta projekto.

Kiel uzanto, vi jam estas valora parto de la evoluiga procedo de la programaro, kaj plaĉas al ni kuraĝigi vin preni eĉ pli aktivan rolon cele al fariĝi longdaŭra kontribuanto al la komunumo. Bonvolu aliĝi kaj rigardi la paĝon por uzantoj ĉe: la retejo de LibreOffice.

Kiel komenci
----------------------------------------------------------------------

La plej bona maniero por ekkontribui estas aboni al unu aŭ pluraj el la dissendolistoj, spekti dum periodo, kaj iom post iom uzi la retpoŝtajn arĥivojn por alkutimiĝi al multaj el la temoj kovritaj ekde kiam la fonta kodo de LibreOffice liberiĝis en oktobro 2000. Kiam vi estos komforta, kion vi bezonos fari, estos sendi retpoŝtan mem-prezenton kaj simple ensalti. Se vi konas malfermfontajn projektojn, inspektu nian liston de farendaĵoj ĉe la retejo de LibreOffice.

Aboni
----------------------------------------------------------------------

Jen kelkaj dissendolistoj al kiuj vi povas aliĝi https://www.libreoffice.org/get-help/mailing-lists/

* Novaĵoj: announce@openoffice.org *rekomendita por ĉiuj uzantoj* (nedensa trafiko)
* Ĉefa uzantolisto: users@global.libreoffice.org *facilas aŭskulti diskutojn* (peza trafiko)
* Merkatado: marketing@global.libreoffice.org *preter evoluigado* (fariĝas pli peza)
* Ĝenerala listo por programistoj: libreoffice@lists.freedesktop.org (multa trafiko)

Aliĝi al unu aŭ pluraj projektoj
----------------------------------------------------------------------

Vi povas fari grandajn kontribuojn al ĉi tiu grava malfermfonta projekto, eĉ se vi havas limigitan programaran dezajnan aŭ kodigan sperton. Jes, vi!

Ni esperas, ke vi ĝojos labori per la nova LibreOffice 26.2 kaj kuniĝu kun ni interrete.

La komunumo de LibreOffice

----------------------------------------------------------------------
Uzita / modifita fontkodo
----------------------------------------------------------------------

Partoj kopirajto 1998, 1999 James Clark. Partoj kopirajto 1996, 1998 Netscape Communications Corporation.
