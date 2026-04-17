
======================================================================
Llegiu-me del LibreOffice 26.2
======================================================================


Visiteu https://git.libreoffice.org/core/tree/master/README.md per a obtindre la versió més recent d'aquest fitxer.

Aquest fitxer conté informació important sobre el LibreOffice. Es recomana que llegiu aquesta informació atentament abans de començar la instal·lació.

La comunitat del LibreOffice és responsable del desenvolupament d'aquest producte, i vos convida a considerar participar com a membre de la comunitat. Si sou un usuari nou, podeu visitar el lloc web del LibreOffice, on hi trobareu molta informació sobre el projecte LibreOffice i les comunitats que existeixen al seu voltant. Aneu a https://www.libreoffice.org/.

El LibreOffice realment és gratuït per a tots els usuaris?
----------------------------------------------------------------------

Tothom pot utilitzar el LibreOffice gratuïtament. Podeu instal·lar aquesta còpia del LibreOffice en tants ordinadors com vulgueu i utilitzar-lo per a qualsevol propòsit (inclosos propòsits comercials, governamentals, d'administració pública i d'usos educatius). Podeu obtindre més detalls al text de llicència que s'inclou dins del paquet del LibreOffice.

Per què el LibreOffice és gratuït per a qualsevol usuari?
----------------------------------------------------------------------

Podeu utilitzar aquesta còpia del LibreOffice gratuïtament perquè col·laboradors individuals i patrocinadors corporatius han dissenyat, desenvolupat, provat, traduït, documentat, mantingut, promocionat i ajudat de moltes altres maneres per fer del LibreOffice allò que és hui: el líder mundial en programari lliure ofimàtic per a usuaris domèstics i d'oficina.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Notes d'instal·lació
----------------------------------------------------------------------

El LibreOffice necessita una versió actualitzada de l'entorn d'execució de Java (JRE) per a poder proporcionar tota la seua funcionalitat. El JRE no forma part del paquet d'instal·lació del LibreOffice i s'ha d'instal·lar per separat.

Requeriments del sistema
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Tingueu en compte que cal tindre drets d'administrador per al procés d'instal·lació.

El registre del LibreOffice com a aplicació per defecte per als formats del Microsoft Office es pot forçar o suprimir mitjançant les següents opcions de línia d'ordres de l'instal·lador:

* REGISTER_ALL_MSO_TYPES=1 forçarà el registre del LibreOffice com a aplicació per defecte per als formats del Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 suprimirà el registre del LibreOffice com a aplicació per defecte per als formats del Microsoft Office.

Assegureu-vos que teniu prou espai disponible al directori temporal del sistema i comproveu que teniu accés de lectura, escriptura i execució. Tanqueu tots els altres programes abans d'iniciar el procés d'instal·lació.

Instal·lació del LibreOffice en sistemes Linux basats en Debian/Ubuntu
----------------------------------------------------------------------

Per a les instruccions de com instal·lar un paquet de llengua (després d'haver instal·lat la versió en anglés EUA del LibreOffice), llegiu la secció següent titulada «Instal·lació d'un paquet de llengua».

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Aquest directori conté un subdirectori anomenat "DEBS". Canvieu el directori actual pel directori "DEBS".

Feu clic amb el botó secundari sobre el directori i seleccioneu «Obri en el Terminal». S'obrirà una finestra de terminal. Des de la línia d'ordes de la finestra de terminal, introduïu la següent orde (se vos preguntarà la contrasenya d'administrador abans d'executar-se):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

El procés d'instal·lació s'ha completat i heu de tindre les icones de totes les aplicacions del LibreOffice en el vostre menú d'escriptori d'Aplicacions/Ofimàtica.

Instal·lació del LibreOffice a Fedora, openSUSE, Mandriva i altres distribucions que utilitzen paquets RPM
----------------------------------------------------------------------

Per a les instruccions de com instal·lar un paquet de llengua (després d'haver instal·lat la versió en anglés EUA del LibreOffice), llegiu la secció següent titulada «Instal·lació d'un paquet de llengua».

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Aquest directori conté un subdirectori anomenat "RPMS". Canvieu el directori actual pel directori "RPMS".

Feu clic amb el botó secundari sobre el directori i seleccioneu «Obri en el Terminal». S'obrirà una finestra de terminal. Des de la línia d'ordes de la finestra de terminal, introduïu la següent orde (se vos preguntarà la contrasenya d'administrador abans d'executar-se):

Per a sistemes basats en Fedora: sudo dnf install *.rpm

Per a sistemes basats en Mandriva: sudo urpmi *.rpm

Per a altres sistemes que utilitzen RPM (openSUSE, etc.): rpm -Uvh *.rpm

El procés d'instal·lació s'ha completat i heu de tindre les icones de totes les aplicacions del LibreOffice en el vostre menú d'escriptori d'Aplicacions/Ofimàtica.

Alternativament, podeu usar l'script «install» ubicat al nivell superior del directori d'aquest arxiu per a fer una instal·lació com a usuari. L'script configurarà el LibreOffice per a tindre el seu propi perfil, separat del perfil normal del LibreOffice. Noteu que això no instal·larà la integració amb el sistema operatiu, com ara els elements del menú d'escriptori o els registres del tipus MIME.

Notes referents a la integració amb l'escriptori de les distribucions no mencionades en les instruccions anteriors
----------------------------------------------------------------------

Hauria de ser possible instal·lar fàcilment el LibreOffice en altres distribucions que no estan cobertes en aquestes instruccions. Les diferències principals seran en la integració amb l'escriptori.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Instal·lació d'un paquet de llengua
----------------------------------------------------------------------

Baixeu el paquet corresponent a la vostra llengua i plataforma. Aquests es troben disponibles en el mateix lloc que el fitxer d'instal·lació principal. Des del gestor de fitxers Nautilus, descomprimiu el fitxer baixat a un directori (el vostre escriptori, per exemple). Assegureu-vos també que heu eixit de totes les aplicacions del LibreOffice (inclòs l'inici ràpid, si està executant-se).

Canvieu de directori cap al directori on heu baixat el paquet de llengua.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Ara canvieu el directori actual pel directori que conté els paquets per instal·lar. En un sistema basat en Debian/Ubuntu el directori serà DEBS. En Fedora, openSUSE o Mandriva, el directori serà RPMS.

Des del gestor de fitxers Nautilus, feu clic amb el botó secundari sobre el directori i seleccioneu «Obri en el Terminal». S'obrirà una finestra de terminal. Des de la línia d'ordes de la finestra de terminal, introduïu la següent orde (se vos preguntarà la contrasenya d'administrador abans d'executar-se):

Per a sistemes basats en Debian/Ubuntu: sudo dpkg -i *.deb

Per a sistemes basats en Fedora: su -c 'dnf install *.rpm'

Per a sistemes basats en Mandriva: sudo urpmi *.rpm

Per a altres sistemes que utilitzen RPM (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Després d'ajustar aquests paràmetres, feu clic a «D'acord». El quadre de diàleg es tancarà i podreu veure un missatge d'informació que us informa que els canvis només s'activaran després d'eixir del LibreOffice i executar-lo una altra vegada (recordeu-vos també d'eixir de l'inici ràpid, si està activat).

La pròxima vegada que reinicieu el LibreOffice, s'iniciarà amb la llengua que heu instal·lat.

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

Només les tecles de drecera (combinacions de tecles) que no s'utilitzen en el sistema operatiu es poden utilitzar al LibreOffice. Si una combinació de tecles al LibreOffice no funciona tal com diu l'ajuda del LibreOffice, comproveu que no la utilitze ja el sistema operatiu. Per a resoldre aquests conflictes, podeu canviar les assignacions de tecles del sistema operatiu. Alternativament, podeu canviar gairebé qualsevol assignació de tecles a LibreOffice. Per a més informació, vegeu l'ajuda del LibreOffice o del sistema operatiu.

----------------------------------------------------------------------
Problemes en enviar documents com a correus electrònics des del LibreOffice
----------------------------------------------------------------------

En enviar un document a través de «Fitxer ▸ Envia ▸ Document de correu electrònic» o «Fitxer ▸ Envia ▸ Correu electrònic com a PDF» poden produir-se problemes (errors o bloquejos del programa). Això es deu al fitxer de sistema de Windows «Mapi» (Interfície de programació d'aplicacions de missatgeria), que causa problemes en algunes versions de fitxers. Lamentablement, el problema no pot reduir-se a un determinat número de versió. Per a obtindre més informació, visiteu https://www.microsoft.com per a cercar «mapi dll» en la base de coneixement de Microsoft.

----------------------------------------------------------------------
Notes importants quant a l'accessibilitat
----------------------------------------------------------------------

Per a més informació sobre les característiques d'accessibilitat del LibreOffice, visiteu https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Assistència a l'usuari
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Consulteu també la secció de preguntes més freqüents en el lloc web del LibreOffice.

----------------------------------------------------------------------
Notificació d'errors i problemes
----------------------------------------------------------------------

El nostre sistema actual per a reportar, seguir i resoldre errors és el Bugzilla, que es troba a https://bugs.documentfoundation.org/. Volem que tots els usuaris reportin errors que troben a la seua plataforma particular. Reportar errors és una de les contribucions més importants que la comunitat pot fer per a millorar el desenvolupament del LibreOffice.

----------------------------------------------------------------------
Com col·laborar
----------------------------------------------------------------------

La comunitat del LibreOffice es pot beneficiar en gran mesura de la vostra participació activa en el desenvolupament d'aquest important projecte de codi font obert.

Com a usuari ja sou ara mateix una part important del procés de desenvolupament i ens agradaria encoratjar-vos a tindre un paper encara més actiu tot sent un col·laborador a llarg termini de la comunitat. Uniu-vos a nosaltres i visiteu la pàgina al lloc web del LibreOffice.

Com començar
----------------------------------------------------------------------

La millor manera de començar a col·laborar-hi és subscriure-vos a una o més llistes de correu, llegir els missatges durant un temps i utilitzar gradualment els arxius de correu per a familiaritzar-vos amb els diversos temes que s'hi tracten des que es va alliberar el codi del LibreOffice l'octubre de 2000. Quan vos trobeu còmode, tot el que heu de fer és enviar un missatge de presentació i començar a treballar. Si teniu experiència amb altres projectes de programari lliure, consulteu la llista de coses per fer i mireu si hi ha res on voldríeu ajudar en el lloc web del LibreOffice.

Subscriviu-vos
----------------------------------------------------------------------

Ací teniu algunes de les llistes de correu a les quals vos podeu subscriure des de https://www.libreoffice.org/get-help/mailing-lists/

* Notícies: announce@documentfoundation.org *recomanada per a tots els usuaris* (poc trànsit)
* Llista d'usuaris principal: users@global.libreoffice.org *la manera fàcil d'assabentar-se dels temes que es debaten* (molt de trànsit)
* Projecte de màrqueting: marketing@global.libreoffice.org *més enllà del desenvolupament* (trànsit en augment)
* Llista general de desenvolupament: libreoffice@lists.freedesktop.org (molt de trànsit)

Apuntar-se a un o més projectes
----------------------------------------------------------------------

Podeu fer contribucions importants a aquest gran projecte de codi font obert fins i tot si la vostra experiència en programació i disseny de programari és limitada. No ho dubteu!

Esperem que gaudiu treballant amb el nou LibreOffice 26.2 i que us uniu a nosaltres en línia.

La comunitat LibreOffice

----------------------------------------------------------------------
Codi font utilitzat / modificat
----------------------------------------------------------------------

Parts amb copyright 1998, 1999 James Clark. Parts amb copyright 1996, 1998 Netscape Communications Corporation.
