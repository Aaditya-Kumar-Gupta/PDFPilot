
======================================================================
Llegiu-me del LibreOffice 26.2
======================================================================


Visiteu https://git.libreoffice.org/core/tree/master/README.md per a obtenir la versió més recent d'aquest fitxer.

Aquest fitxer conté informació important sobre el LibreOffice. Es recomana que llegiu aquesta informació atentament abans de començar la instal·lació.

La comunitat del LibreOffice és responsable del desenvolupament d'aquest producte, i us convida a considerar participar com a membre de la comunitat. Si sou un usuari nou, podeu visitar el lloc web del LibreOffice, on hi trobareu molta informació sobre el projecte LibreOffice i les comunitats que existeixen al seu voltant. Aneu a https://www.libreoffice.org/.

El LibreOffice realment és gratuït per a tots els usuaris?
----------------------------------------------------------------------

Tothom pot utilitzar el LibreOffice gratuïtament. Podeu instal·lar aquesta còpia del LibreOffice a tants ordinadors com vulgueu i utilitzar-lo per a qualsevol a qualsevol propòsit (inclosos propòsits comercials, governamentals, d'administració pública i d'usos educatius). Podeu obtenir més detalls al text de llicència que s'inclou dins del paquet del LibreOffice.

Per què el LibreOffice és gratuït per a qualsevol usuari?
----------------------------------------------------------------------

Podeu utilitzar aquesta còpia del LibreOffice gratuïtament perquè col·laboradors individuals i patrocinadors corporatius han dissenyat, desenvolupat, provat, traduït, documentat, mantingut, promocionat i ajudat de moltes altres maneres per a fer del LibreOffice allò que és avui: el líder mundial en programari lliure ofimàtic per a usuaris domèstics i d'oficina.

Si aprecieu l'esforç i voleu que el LibreOffice segueixi estant disponible en el futur, considereu la possibilitat de contribuir al projecte. Visiteu www.libreoffice.org/community/get-involved per a obtenir més detalls. Tothom pot contribuir-hi d'alguna manera.

----------------------------------------------------------------------
Notes d'instal·lació
----------------------------------------------------------------------

El LibreOffice necessita una versió actualitzada de l'entorn d'execució de Java (JRE) per a poder proporcionar tota la seva funcionalitat. El JRE no forma part del paquet d'instal·lació del LibreOffice i s'ha d'instal·lar per separat.

Requisits del sistema
----------------------------------------------------------------------

* Microsoft Windows 10 o posterior

Tingueu en compte que cal tenir drets d'administrador per al procés d'instal·lació.

El registre del LibreOffice com a aplicació per defecte per als formats del Microsoft Office es pot forçar o suprimir mitjançant les següents opcions de línia d'ordres de l'instal·lador:

* REGISTER_ALL_MSO_TYPES=1 forçarà el registre del LibreOffice com a aplicació per defecte per als formats del Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 suprimirà el registre del LibreOffice com a aplicació per defecte per als formats del Microsoft Office.

Assegureu-vos que teniu prou espai disponible al directori temporal del sistema i comproveu que teniu accés de lectura, escriptura i execució. Tanqueu tots els altres programes abans d'iniciar el procés d'instal·lació.

Instal·lació del LibreOffice en sistemes Linux basats en Debian/Ubuntu
----------------------------------------------------------------------

Per a les instruccions de com instal·lar un paquet de llengua (després d'haver instal·lat la versión en anglès EUA del LibreOffice), llegiu la secció següent titulada «Instal·lació d'un paquet de llengua».

En descomprimir el fitxer baixat, veureu que els continguts es descomprimeixen en un subdirectori. Obriu una finestra del gestor de fitxers i canvieu el directori actual al que comença per «LibreOffice_», tot seguit pel número de versió i informació sobre la plataforma.

Aquest directori conté un subdirectori anomenat «DEBS». Canvieu el directori actual pel directori «DEBS».

Feu clic amb el botó secundari sobre el directori i seleccioneu «Obre en el Terminal». S'obrirà una finestra de terminal. Des de la línia d'ordres de la finestra de terminal, introduïu la següent ordre (se us preguntarà la contrasenya d'administrador abans d'executar-se):

Les ordres següents instal·laran el LibreOffice i els paquets d'integració amb l'escriptori (podeu copiar-les i enganxar-les a una finestra del terminal en comptes d'intentar teclejar-les):

sudo dpkg -i *.deb

El procés d'instal·lació s'ha completat i heu de tenir les icones de totes les aplicacions del LibreOffice en el vostre menú d'escriptori d'Aplicacions/Ofimàtica.

Instal·lació del LibreOffice a Fedora, openSUSE, Mandriva i altres distribucions que utilitzen paquets RPM
----------------------------------------------------------------------

Per a les instruccions de com instal·lar un paquet de llengua (després d'haver instal·lat la versión en anglès EUA del LibreOffice), llegiu la secció següent titulada «Instal·lació d'un paquet de llengua».

En descomprimir el fitxer baixat, veureu que els continguts es descomprimeixen en un subdirectori. Obriu una finestra del gestor de fitxers i canvieu el directori actual al que comença per «LibreOffice_», tot seguit pel número de versió i informació sobre la plataforma.

Aquest directori conté un subdirectori anomenat «RPMS». Canvieu el directori actual pel directori «RPMS».

Feu clic amb el botó secundari sobre el directori i seleccioneu «Obre en el Terminal». S'obrirà una finestra de terminal. Des de la línia d'ordres de la finestra de terminal, introduïu la següent ordre (se us preguntarà la contrasenya d'administrador abans d'executar-se):

Per a sistemes basats en Fedora: sudo dnf install *.rpm

Per a sistemes basats en Mandriva: sudo urpmi *.rpm

Per a altres sistemes que utilitzen RPM (openSUSE, etc.): rpm -Uvh *.rpm

El procés d'instal·lació s'ha completat i heu de tenir les icones de totes les aplicacions del LibreOffice en el vostre menú d'escriptori d'Aplicacions/Ofimàtica.

Alternativament, podeu usar l'script «install» ubicat al nivell superior del directori d'aquest arxiu per a fer una instal·lació com a usuari. L'script configurarà el LibreOffice per a tenir el seu propi perfil, separat del perfil normal del LibreOffice. Noteu que això no instal·larà la integració amb el sistema operatiu, com ara els elements del menú d'escriptori o els registres del tipus MIME.

Notes referents a la integració amb l'escriptori de les distribucions no mencionades en les instruccions anteriors
----------------------------------------------------------------------

Hauria de ser possible d'instal·lar fàcilment el LibreOffice en altres distribucions que no estan cobertes en aquestes instruccions. Les diferències principals seran en la integració amb l'escriptori.

El directori RPMS (o DEBS, respectivament) també conté un paquet anomenat libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (o libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectivament, o similar). Aquest paquet és per a totes les distribucions de Linux que implementen les especificacions o recomanacions de Freedesktop (https://ca.wikipedia.org/wiki/Freedesktop.org), i es proporciona per a permetre la instal·lació en distribucions Linux que no estan mencionades en les instruccions.

Instal·lació d'un paquet de llengua
----------------------------------------------------------------------

Baixeu el paquet corresponent a la vostra llengua i plataforma. Aquests es troben disponibles en el mateix lloc que el fitxer d'instal·lació principal. Des del gestor de fitxers Nautilus, descomprimiu el fitxer baixat a un directori (el vostre escriptori, per exemple). Assegureu-vos també que heu sortit de totes les aplicacions del LibreOffice (inclòs l'inici ràpid, si està executant-se).

Canvieu de directori cap al directori on heu baixat el paquet de llengua.

Ara canvieu el directori actual pel directori que s'ha creat durant el procés d'extracció. Per exemple, pel codi de llengua catalana pels sistema Debian/Ubuntu de 32 bits, el directori s'anomena LibreOffice_, més informació sobre la versió, més Linux_x86_langpack-deb_ca.

Ara canvieu el directori actual pel directori que conté els paquets per instal·lar. En un sistema basat en Debian/Ubuntu el directori serà DEBS. En Fedora, openSUSE o Mandriva, el directori serà RPMS.

Des del gestor de fitxers Nautilus, feu clic amb el botó secundari sobre el directori i seleccioneu «Obre en el Terminal». S'obrirà una finestra de terminal. Des de la línia d'ordres de la finestra de terminal, introduïu la següent ordre (se us preguntarà la contrasenya d'administrador abans d'executar-se):

Per a sistemes basats en Debian/Ubuntu: sudo dpkg -i *.deb

Per a sistemes basats en Fedora: su -c 'dnf install *.rpm'

Per a sistemes basats en Mandriva: sudo urpmi *.rpm

Per a altres sistemes que utilitzen RPM (openSUSE, etc.): rpm -Uvh *.rpm

Ara inicieu una de les aplicacions del LibreOffice, per exemple el Writer. Aneu al menú Eines i trieu Opcions. En el quadre de diàleg Opcions, feu clic a «Llengües i opcions regionals» i, a continuació, feu clic a «General». Deixeu anar la llista «Interfície d'usuari» i seleccioneu la llengua que acabeu d'instal·lar. Si voleu, feu el mateix amb la configuració «Opcions regionals», la «Divisa per defecte» i les «Llengües per defecte per als documents».

Després d'ajustar aquests paràmetres, feu clic a «D'acord». El quadre de diàleg es tancarà i podreu veure un missatge d'informació dient-vos que els canvis només s'activaran després de sortir del LibreOffice i executar-lo un altre cop (recordeu-vos també de sortir de l'inici ràpid, si està activat).

El següent cop que reinicieu el LibreOffice, s'iniciarà amb la llengua que heu instal·lat.

----------------------------------------------------------------------
Problemes en iniciar el programa
----------------------------------------------------------------------

Les dificultats per iniciar LibreOffice (p.e., les aplicacions es pengen) i els problemes amb la visualització de la pantalla solen ser causades pel controlador de la targeta gràfica. Si es produeixen aquests problemes, actualitzeu el controlador de la targeta gràfica o proveu d'utilitzar el controlador de gràfics subministrat amb el vostre sistema operatiu.

----------------------------------------------------------------------
Ratolins tàctils ALPS/Synaptics de portàtils al Windows
----------------------------------------------------------------------

A causa d'un problema amb el controlador del Windows, no us podeu desplaçar a través de documents del LibreOffice en arrossegar el dit per un ratolí tàctil ALPS/Synaptics.

Per a habilitar el desplaçament amb el ratolí tàctil, afegiu les línies següents al fitxer de configuració "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini"  i reinicieu l'ordinador:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

La ubicació del fitxer de configuració pot variar en diferents versions del Windows.

----------------------------------------------------------------------
Tecles de drecera
----------------------------------------------------------------------

Només les tecles de drecera (combinacions de tecles) que no s'utilitzen en el sistema operatiu es poden utilitzar al LibreOffice. Si una combinació de tecles al LibreOffice no funciona tal com diu l'ajuda del LibreOffice, comproveu que no la utilitzi ja el sistema operatiu. Per resoldre aquests conflictes, podeu canviar les assignacions de tecles del sistema operatiu. Alternativament, podeu canviar gairebé qualsevol assignació de tecles a LibreOffice. Per a més informació, vegeu l'ajuda del LibreOffice o del sistema operatiu.

----------------------------------------------------------------------
Problemes en enviar documents com a correus electrònics des del LibreOffice
----------------------------------------------------------------------

En enviar un document a través de «Fitxer ▸ Envia ▸ Document de correu electrònic» o «Fitxer ▸ Envia ▸ Correu electrònic com a PDF» poden produir-se problemes (errors o bloquejos del programa). Això es deu al fitxer de sistema de Windows «Mapi» (Interfície de programació d'aplicacions de missatgeria), que causa problemes en algunes versions de fitxers. Lamentablement, el problema no pot reduir-se a un determinat número de versió. Per a obtenir més informació, visiteu https://www.microsoft.com per a cercar «mapi dll» en la base de coneixement de Microsoft.

----------------------------------------------------------------------
Notes importants quant a l'accessibilitat
----------------------------------------------------------------------

Per a més informació sobre les funcionalitats d'accessibilitat del LibreOffice, visiteu https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Assistència als usuaris
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Consulteu també la secció de preguntes més freqüents en el lloc web del LibreOffice.

----------------------------------------------------------------------
Notificació d'errors i problemes
----------------------------------------------------------------------

El nostre sistema actual per a reportar, seguir i resoldre errors és el Bugzilla, que es troba a https://bugs.documentfoundation.org/. Volem que tots els usuaris reportin errors que trobin a la seva plataforma particular. Reportar errors és una de les contribucions més importants que la comunitat pot fer per a millorar el desenvolupament del LibreOffice.

----------------------------------------------------------------------
Com col·laborar
----------------------------------------------------------------------

La comunitat del LibreOffice es pot beneficiar en gran mesura de la vostra participació activa en el desenvolupament d'aquest important projecte de codi font obert.

Com a usuari ja sou ara mateix una part important del procés de desenvolupament i ens agradaria encoratjar-vos a tenir un paper encara més actiu tot sent un col·laborador a llarg termini de la comunitat. Uniu-vos a nosaltres i visiteu la pàgina al lloc web del LibreOffice.

Com començar
----------------------------------------------------------------------

La millor manera de començar a col·laborar-hi és subscriure-us a una o més llistes de correu, llegir els missatges durant un temps i utilitzar gradualment els arxius de correu per a familiaritzar-vos amb els diversos temes que s'hi tracten des que es va alliberar el codi del LibreOffice l'octubre de 2000. Quan us trobeu còmode, tot el que heu de fer és enviar un missatge de presentació i començar a treballar. Si teniu experiència amb altres projectes de programari lliure, consulteu la llista de coses per fer i mireu si hi ha res on voldríeu ajudar en el lloc web del LibreOffice.

Subscriviu-vos
----------------------------------------------------------------------

Aquí teniu algunes de les llistes de correu a les quals us podeu subscriure des de https://www.libreoffice.org/get-help/mailing-lists/

* Notícies: announce@documentfoundation.org *recomanada per a tots els usuaris* (poc trànsit)
* Llista d'usuaris principal: users@global.libreoffice.org *la manera fàcil d'assabentar-se dels temes que es debaten* (molt trànsit)
* Projecte de màrqueting: marketing@global.libreoffice.org *més enllà del desenvolupament* (trànsit en augment)
* Llista general de desenvolupament: libreoffice@lists.freedesktop.org (molt trànsit)

Apuntar-se a un o més projectes
----------------------------------------------------------------------

Podeu fer contribucions importants a aquest gran projecte de codi font obert fins i tot si la vostra experiència en programació i disseny de programari és limitada. No ho dubteu!

Esperem que gaudiu treballant amb el nou LibreOffice 26.2 i que us uniu a nosaltres en línia.

La comunitat LibreOffice

----------------------------------------------------------------------
Codi font utilitzat / modificat
----------------------------------------------------------------------

Parts amb copyright 1998, 1999 James Clark. Parts amb copyright 1996, 1998 Netscape Communications Corporation.
