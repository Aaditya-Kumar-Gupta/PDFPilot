
======================================================================
LibreOffice 26.2 – Fontos információk
======================================================================


Ezen fájl frissítéseiért lásd: https://git.libreoffice.org/core/tree/master/README.md

Ez a fájl fontos információkat tartalmaz a LibreOffice programról. A program telepítése előtt alaposan tanulmányozza ezeket az információkat.

A LibreOffice közösség, amely ennek a terméknek a fejlesztéséért felelős, minden új tagnak örül. Ha Ön új felhasználó, a LibreOffice weboldalán rengeteg információt talál a LibreOffice projektről és a köré szerveződött közösségről. Látogasson el a https://www.libreoffice.org/ weboldalra.

A LibreOffice tényleg minden felhasználónak ingyenes?
----------------------------------------------------------------------

A LibreOffice mindenki számára szabadon használható. A LibreOffice jelen példányát annyi számítógépre telepíti, amennyire szeretné, és bármilyen célra felhasználhatja (beleértve a kereskedelmi, kormányzati, nyilvános vagy oktatási felhasználást). Bővebb információért olvassa el a LibreOffice termékhez kapott licencet.

Miért ingyenes a LibreOffice minden felhasználó számára?
----------------------------------------------------------------------

A LibreOffice-t azért használhatja ingyenesen, mert az egyéni hozzájárulók és vállalati szponzorok tervezték, fejlesztették, tesztelték, fordították, dokumentálták, támogatták, marketingelték és más módokon segítették. A LibreOffice ezért válhatott azzá, ami ma – a világ vezető nyílt forráskódú irodai szoftvere.

Hogyha értékeli az erőfeszítéseiket, és szeretné biztosítani, hogy a LibreOffice elérhető maradjon hosszan a jövőben is, kérjük fontolja meg a projekthez való hozzájárulást - látogassa meg a https://www.libreoffice.org/community/get-involved/ weboldalt a részletekért. Bárki hozzájárulhat valamilyen formában.

----------------------------------------------------------------------
Megjegyzések a telepítéshez
----------------------------------------------------------------------

LibreOffice egyes funkcióihoz Java futtatókörnyezet (JRE) szükséges. A JRE nem része a LibreOffice telepítőkészletének. Külön kell telepíteni.

Rendszerkövetelmények
----------------------------------------------------------------------

* Microsoft Windows 10 vagy magasabb

A telepítéshez rendszergazdai jogosultságokra van szükség.

A LibreOffice regisztrálása a Microsoft Office formátumok megnyitására használt alapértelmezett alkalmazásként a következő parancssori kapcsolókkal kényszeríthető, illetve tiltható:

* A REGISTER_ALL_MSO_TYPES=1 a LibreOffice szoftvert regisztrálja a Microsoft Office formátumok alapértelmezett alkalmazásaként.
* A REGISTER_NO_MSO_TYPES=1 a LibreOffice szoftvert nem regisztrálja a Microsoft Office formátumok alapértelmezett alkalmazásaként.

Ellenőrizze, hogy van-e elegendő szabad hely az ideiglenes könyvtárban, és ehhez a könyvtárhoz rendelkezik-e olvasási, írási és futtatási jogosultságokkal. A telepítés előtt célszerű kilépni minden egyéb programból.

A LibreOffice telepítése Debian- vagy Ubuntu-alapú Linux-rendszerekre
----------------------------------------------------------------------

A nyelvi csomag telepítésének lépéseit (a LibreOffice angol verziójának telepítése után) az alábbi, Nyelvi csomag telepítése szakaszban találja.

Amikor kibontja a letöltött archívumot, látni fogja hogy a tartalma ki lett csomagolva egy almappába. Nyisson egy fájlkezelő ablakot, és nyissa meg a mappát ami a "LibreOffice_"-al kezdődik, majd a verzió számmal és néhány platforminformációval követve.

Ebben a könyvtárban van egy „DEBS” alkönyvtár. Lépjen be a „DEBS” alkönyvtárba.

Kattintson a jobb egérgombbal, és a helyi menüből válassza a „Megnyitás terminálban” parancsot. Megnyílik egy terminálablak. A terminálablak parancssorába írja be a következő parancsot (a rendszer kérni fogja a rendszergazda jelszavát):

A következő parancsok telepíteni fogják a LibreOffice-t és az asztali integrációs csomagokat (elég csak bemásolni a terminálba őket, nem kell begépelni):

sudo dpkg -i *.deb

A telepítés ezzel kész, és a LibreOffice-alkalmazások ikonjainak meg kell jelenniük az Alkalmazások/Iroda menüben.

A LibreOffice telepítése Fedora, openSUSE, Mandriva vagy egyéb, RPM-csomagokat használó Linux-rendszerekre
----------------------------------------------------------------------

A nyelvi csomag telepítésének lépéseit (a LibreOffice angol verziójának telepítése után) az alábbi, Nyelvi csomag telepítése szakaszban találja.

Amikor kibontja a letöltött archívumot, látni fogja hogy a tartalma ki lett csomagolva egy almappába. Nyisson egy fájlkezelő ablakot, és nyissa meg a mappát ami a "LibreOffice_"-al kezdődik, majd a verzió számmal és néhány platforminformációval követve.

Ebben a könyvtárban van egy „RPMS” alkönyvtár. Lépjen be az „RPMS” alkönyvtárba.

Kattintson a jobb egérgombbal, és a helyi menüből válassza a „Megnyitás terminálban” parancsot. Megnyílik egy terminálablak. A terminálablak parancssorába írja be a következő parancsot (a rendszer kérni fogja a rendszergazda jelszavát):

Fedora-alapú rendszereken: sudo dnf install *.rpm

Mandriva-alapú rendszereken: sudo urpmi *.rpm

Egyéb RPM-alapú rendszereken (openSUSE stb.): rpm -Uvh *.rpm

A telepítés ezzel kész, és a LibreOffice-alkalmazások ikonjainak meg kell jelenniük az Alkalmazások/Iroda menüben.

Ennek alternatívájaként használhatja az „install” parancsfájlt az archívum felső szintjén a felhasználóként való telepítéshez. A parancsfájl úgy állítja be a(z) LibreOffice telepítését, hogy saját, a normál LibreOffice profiltól független profilt használjon. Ne feledje, hogy ez nem telepíti a rendszerintegrációs részeket, például az asztali menü elemeit és az asztali MIME-típus regisztrációkat.

Megjegyzések a munkaasztali integrációval kapcsolatban a fentiekben nem tárgyalt Linux-disztribúciók esetén
----------------------------------------------------------------------

A LibreOffice telepítése az ebben a dokumentumban nem említett Linux-diszribúciókra valószínűleg szintén egyszerűen elvégezhető. Egyedül a munkaasztali integrációban lehet eltérés.

Az RPMS (vagy DEBS) mappa tartalmaz egy libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (vagy libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, vagy hasonló) nevű csomagot is. Ez azokra a Linux disztribúciókra van, amik támogatják a Freedesktop.org specifikációit/ajánlásait (https://en.wikipedia.org/wiki/Freedesktop.org), és biztosítva van telepítéshez más Linux disztribúciókhoz, amik nem kerültek említésre az előbbi instrukciókban.

Nyelvi csomag telepítése
----------------------------------------------------------------------

Töltse le a kívánt nyelvhez és platformhoz való nyelvi csomagot. Ezek ugyanonnan elérhetők, ahonnan a fő telepítőkészlet. A Nautilus fájlkezelő segítségével bontsa ki a letöltött archívumot egy könyvtárba (például az asztalra). Lépjen ki minden LibreOffice-alkalmazásból (a Gyorsindítóból is, ha el volt indítva).

Lépjen be abba a könyvtárba, amelybe a letöltött nyelvi csomagot kicsomagolta.

Most nyissa meg a mappát, ami a kicsomagolás közben lett létrehozva. Például, a magyar nyelvcsomaghoz egy 32-bites Debian/Ubuntu alapú rendszeren, a mappa neve LibreOffice_, plusz néhány verzió információ, plusz Linux_x86_langpack-deb_hu.

Ezután lépjen be a telepítendő csomagokat tartalmazó könyvtárba. Debian- vagy Ubuntu-alapú rendszeren ez a DEBS könyvtár. Fedora, openSUSE vagy Mandriva rendszereken ez az RPMS könyvtár.

A Nautilus fájlkezelőben kattintson a jobb egérgombbal, és a helyi menüből válassza a „Megnyitás terminálban” parancsot. Megnyílik egy terminálablak. A terminálablak parancssorába írja be a következő parancsot (a rendszer kérni fogja a rendszergazda jelszavát):

Debian- és Ubuntu-alapú rendszereken: sudo dpkg -i *.deb

Fedora-alapú rendszereken: su -c 'dnf install *.rpm'

Mandriva-alapú rendszereken: sudo urpmi *.rpm

Egyéb RPM-alapú rendszereken (openSUSE stb.): rpm -Uvh *.rpm

Ezután indítsa el az egyik LibreOffice-alkalmazást, például a Writert A Tools menüből válassza az Options lehetőséget. Az Options párbeszédablakban kattintson a „Languages and Locales” lehetőségre, majd kattintson a „General” elemre. A „User interface” legördülő listából kiválaszthatja az imént telepített nyelvet. Ha szeretné, beállíthatja ezt a nyelvet a „Locale setting”, a „Default currency” és a „Default languages for documents” lehetőségeknél is.

A beállítások végeztével nyomja meg az OK gombot. A párbeszédablak bezáródik, és egy figyelmeztető üzenet jelenik meg, hogy a változások csak a LibreOffice újraindítása után fognak életbe lépni. Ne felejtsen el a Gyorsindítóból is kilépni, ha az el volt indítva.

A LibreOffice következő indításakor a kiválasztott nyelven fog megjelenni a felhasználói felület.

----------------------------------------------------------------------
Programindítási problémák
----------------------------------------------------------------------

A LibreOffice indításával (például lefagyás) valamint a képernyőn való megjelenítéssel kapcsolatos nehézségeket gyakran a videokártya illesztőprogramja okozza. Ha ilyeneket tapasztal, frissítse a videokártya illesztőprogramját, vagy próbálja használni az operációs rendszerhez kapott illesztőprogramot.

----------------------------------------------------------------------
ALPS/Synaptics noteszgépek tapipadja Windows rendszerben
----------------------------------------------------------------------

A Windows illesztőprogramjának hibája miatt nem tudja görgetni a LibreOffice-dokumentumok, amikor átcsúsztatja az ujját az APLS/Synaptic tapipadján.

A tapipados görgetés engedélyezéséhez adja a következő sorokat a „C:\Program Files\Synaptics\SynTP\SynTPEnh.ini” konfigurációs fájlhoz, és indítsa újra a számítógépet:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

A konfigurációs fájl helye a különböző Windows-verzióban más-más lehet.

----------------------------------------------------------------------
Gyorsbillentyűk
----------------------------------------------------------------------

A LibreOffice programjain belül csak olyan gyorsbillentyű-kombinációkat lehet használni, amelyeket az operációs rendszer még nem foglalt le. Amennyiben egy billentyűkombináció nem úgy működne a LibreOffice programban, mint ahogyan az le van írva a LibreOffice súgójában, ellenőrizze, hogy nem foglalt-e a billentyűkombináció. Az ütközések elkerüléséhez két lehetőség van. Módosíthatja az operációs rendszer (grafikus felület) gyorsbillentyű-kombinációit vagy a LibreOffice kombinációit. A gyorsbillentyűk beállításához tekintse meg a LibreOffice súgóját, vagy használja az operációs rendszer súgórendszerét.

----------------------------------------------------------------------
Lehetséges problémák, amikor a LibreOffice-ból egy dokumentumot e-mailként szeretne elküldeni
----------------------------------------------------------------------

Hibák léphetnek fel (a program elszáll vagy lefagy), amikor e-mailként el szeretne küldeni egy dokumentumot a „Fájl - Küldés - Dokumentum e-mailként” vagy „Fájl - Küldés - Dokumentum PDF-mellékletként” menüpontot kiválasztva. Ennek oka a Windows „MAPI” rendszerfájlja (Messaging Application Programming Interface), amelynek bizonyos verziói problémákat okoznak. Sajnos a probléma nincs egyértelműen egy verzióhoz kötve. További információkért látogasson el a https://www.microsoft.com honlapra, és keressen a Microsoft tudásbázisában a „mapi dll” kulcsszavakra.

----------------------------------------------------------------------
Fontos megjegyzések a kisegítő lehetőségekkel kapcsolatosan
----------------------------------------------------------------------

A LibreOffice kisegítő lehetőségeiről bővebben a https://www.libreoffice.org/accessibility/ oldalon olvashat.

----------------------------------------------------------------------
Felhasználói támogatás
----------------------------------------------------------------------

A fő támogatási oldal különféle lehetőségeket kínál a LibreOffice használatához nyújtott segítséghez. Lehet, hogy kérdésére már megszületett a válasz – nézze meg a Közösségi fórumot itt: https://ask.libreoffice.org/, vagy keressen a users@libreoffice.org levelezőlista archívumában: https://www.libreoffice.org/lists/users/. Másik lehetőségként elküldheti kérdéseit a következő címre: users@libreoffice.org. Ha szeretne feliratkozni a listára (és így e-mail-ben megkapni a válaszokat), küldjön egy üres levelet erre a címre: users+subscribe@libreoffice.org.

Olvassa el a gyakran ismételt kérdéseket is a LibreOffice weboldalán.

----------------------------------------------------------------------
Hibák és problémák bejelentése
----------------------------------------------------------------------

A programhibák bejelentésére, nyomon követésére és kijavítására jelenleg egy Bugzilla rendszert használunk, amely a https://bugs.documentfoundation.org/ címen érhető el. Szeretnénk bátorítani minden felhasználót, hogy jelentse azokat a hibákat, amelyekkel a rendszerében találkozik. A hibajelentések elküldése az egyik legnagyobb hozzájárulás, amelyet a felhasználói közösség tehet a LibreOffice folyamatos fejlesztése érdekében.

----------------------------------------------------------------------
Részvétel a projektben
----------------------------------------------------------------------

A LibreOffice-közösség számára igen hasznos, ha Ön aktívan részt vesz ennek a nyílt forráskódú projektnek a fejlesztésében.

Mint felhasználó, máris értékes résztvevője a szoftvercsomag fejlesztésének. Azonban arra bátorítjuk, hogy vállaljon aktívabb szerepet, járuljon hozzá akár Ön is a közösség erőfeszítéseihez. Kérjük, csatlakozzon hozzánk, és tekintse meg a hozzájárulói oldalunkat.

Hogyan kezdje?
----------------------------------------------------------------------

Ha tenni szeretne valamit a LibreOffice projektért, annak az a legjobb módja, hogy feliratkozik egy vagy több levelezőlistára. Figyelje a hozzászólásokat, és használja az archívumot, hogy betekintést szerezzen azokba a témákba, amelyekről a listán a LibreOffice forráskódjának megjelenése, 2000 októbere óta szó volt. Ha úgy érzi, hogy képben van, küldjön egy rövid bemutatkozást a listára, és vegyen részt Ön is az aktív levelezésben. Ha már van tapasztalata nyílt forráskódú projektekkel, tekintse meg a tennivalók listáját a LibreOffice weboldalán.

Feliratkozás
----------------------------------------------------------------------

Íme a projekt néhány levelezőlistája, amelyekre az alábbi címen iratkozhat fel: https://www.libreoffice.org/get-help/mailing-lists/

* Hírek (angolul): announce@documentfoundation.org *minden felhasználó számára ajánlott* (kis forgalom)
* Fő felhasználói fórum (angolul): users@global.libreoffice.org (nagy forgalom)
* Marketing projekt: marketing@global.libreoffice.org *a fejlesztésen túl* (nagy forgalom)
* Általános fejlesztői levelezőlista: libreoffice@lists.freedesktop.org (nagy forgalom)

Csatlakozás valamelyik projekthez
----------------------------------------------------------------------

Ön is sokat hozzátehet ehhez a fontos nyílt forráskódú projekthez, akkor is, ha csak kevéssé ért a szoftverfejlesztéshez vagy a programozáshoz. Igen, pont Ön!

Reméljük, élvezni fogja a munkát az új LibreOffice 26.2 szoftvercsomaggal, és csatlakozik hozzánk az interneten.

A LibreOffice Közösség

----------------------------------------------------------------------
Használt / módosított forráskód
----------------------------------------------------------------------

Egyes részek Copyright 1998, 1999 James Clark. Egyes részek Copyright 1996, 1998 Netscape Communications Corporation.
