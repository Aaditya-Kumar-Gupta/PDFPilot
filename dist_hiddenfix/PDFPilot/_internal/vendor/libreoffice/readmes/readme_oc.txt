
======================================================================
Legissètz-me LibreOffice 26.2
======================================================================


Consultatz  https://git.libreoffice.org/core/tree/master/README.md per obténer la version mai recenta d’aqueste fichièr

Aquel fichièr conten d'informacions importantas a prepaus del logicial LibreOffice. Gaitatz d' informacions abans de començar l'installacion.

The LibreOffice community is responsible for the development of this product, and invites you to consider participating as a community member. If you are a new user, you can visit the LibreOffice site, where you will find lots of information about the LibreOffice project and the communities that exist around it. Go to https://www.libreoffice.org/.

LibreOffice es vertadièrament liure per los utilizaires totes ?
----------------------------------------------------------------------

LibreOffice es liure d'utilizacion per totes e totas. Podètz prene aquela còpia de LibreOffice, l'installar sus tant d'ordenadors que desiratz e l'utilizar coma volètz (inclusent l'utilizacion comerciala, dins las administracions e las organisacions, atal coma dins l'educacion). Per pus de detalhs, veire lo tèxte de la licéncia provesit amb lo telecargament de LibreOffice.

Perqué LibreOffice  es gratuis per los utilizaires, utilizairas totes, totas ?
----------------------------------------------------------------------

Podètz utilizar aquela còpi de LibreOffice  gratuitament per çò que des contribuidors individuals e d'entrepresas sponsòrs an concebut, desvolopat, testat, traduit, documentat, susportat, promu e ajudat de mai d'autres biaisses encara per faire çò que LibreOffice es uèi - lo logicial de burotic Open Source leader mondial.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Nòtas sus l'installacion
----------------------------------------------------------------------

LibreOffice necessita una version recenta de l'environament d'execucion java (JRE) per l'utilizacion complèta de las foncionalitats. Lo JRE fa pas partida del paquet d'installacion LibreOffice, deu èsser installat separadament.

Configuracion necessària :
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Remarcatz que los dreits d'administrator son necessaris pel processus d'installacion.

Enregistrar LibreOffice coma aplicacion per defaut per legir los formats Microsoft Office pòt èsser parametrat amb la linha de comanda ligada amb l'installador :

* REGISTER_ALL_MSO_TYPES=1 forçarà l'enregistrament de LibreOffice coma aplicacion per defaut pels formats Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 suprimirà l'enregistrament de LibreOffice coma aplicacion per defaut pels formats Microsoft Office.

Asseguratz-vos que i pro d'espaci de memòria liura dins lo repertòri temporari del sistèma e que los dreits de lectura, d'escritura e d'execucion son acordats. Tampatz los autres programas abans de començar l'installacion.

Installacion de LibreOffice suls sistèmas Linux Ubuntu basats sus Debian/Ubuntu
----------------------------------------------------------------------

Per las instruccions a prepaus l'installacion d'un paquet de lengae (aprèp aver installat la version Anglés US de LibreOffice), legissètz la seccion çaijós intitulada Installar un paquet de lenga.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Aqueste repertòri conten un sosrepertòri nomenat "DEBS". Cambiatz de repertòri per lo de "DEBS".

Clicatz amb lo boton dreit dins lo repertòri e causissètz "Dobrir un terminal". Una fenèstra de terminal se dobrís. picatz las comandas seguentas (vos serà demandat de picar vòstre senhal root abans que la comanda s'execute) :

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Lo processús d'installacion es ara acabat e avètz normalament las icònas de las aplicacions totas de LibreOffice dins lo menú de las aplicacions de l'environament de burèu.

Installacion de LibreOffice sus Fedora, openSUSE, Mandriva e autras sistèmas Linux qu'utilizan de paquetatges RPM
----------------------------------------------------------------------

Per las instruccions a prepaus de l'installacion d'un paquet de lenga (aprèp aver installat la version Anglés US de LibreOffice), legissètz la seccion çaijós intitulada Installar un paquet de lenga.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Lo repertòri conten un sosrepertòri nomenat "RPMS". Cambiatz de repertòri per aqueste repertòri.

Clicatz amb lo boton dreit dins lo repertòri e causissètz "Dobrir un terminal". Una fenèstra de terminal se dobrís. picatz las comandas seguentas (vos serà demandat de picar vòstre senhal root abans que la comanda s'execute) :

Pels sistèmas basats sus Fedora : sudo dnf install *.rpm

Pels sistèmas basats sus Mandriva : sudo urpmi *.rpm

Pels autres sistèmas basats sus RPM (openSUSE, etc.): rpm -Uvh *.rpm

Lo processús d'installacion es ara acabat e avètz normalament las icònas de las aplicacions totas de LibreOffice dins lo menú de las aplicacions de l'environament de burèu.

Alternativament, podètz utilizar l'escript 'install' situat dins lo repertòri superior d'aquesta archiu per executar una installacion en tant qu'utilizaire. L'escript va parametrar LibreOffice amb son pròpri perfil per aquesta installacion, separat del perfil LibreOffice normal. Remarcatz qu'aquò installarà pas las partidas d'integracion sistèma talas coma los elements de menú de l'environament e los enregistraments de tipe MIME de l'environament.

Nòtas concernent l'integracion dins l'environament de burèu per las distribucions Linux non previstas per las instruccions d'installacions çai-sota
----------------------------------------------------------------------

Normalament, es possible d'installar LibreOffice facilament sus d'autras distribucions Linus non especificadas. Lo principal aspècte que pòt faire problèma es l'integracion dins lo burèu.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Installacion d'un paquet de lenga
----------------------------------------------------------------------

Telecargatz lo paquet de lenga e de la platafòrma que volètz.Son disponibles al meteis endreit que los archius d'installacion principala. Del gestionari de fichièr Nautilus, descomprimissètz l'archiu telecargada dins un repertòri (lo vòstre burèu, per exemple). Asseguratz vos qu'avètz plan quitat totas las aplicacions LibreOffice (amb l'aviada rapida, s'es activada).

Cambiatz de repertòri per lo dins lo qual avètz descomprimit lo paquet de lenga telecargat.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Ara, cambiatz de repertòri per lo que conten los paquetatges d'installar. Sus de sistèmas basats sus Debian/Ubuntu, lo repertòri es DEBS. Sus de sistèmas Fedora, openSUSE o Mandriva, lo repertòri serà RPMS.

Del gestionari de fichièr Nautilus, vos cal clicar amb lo boton dreit dins lo repertòri e vos cal causir la comanda "Dobrir un terminal". Dins la fenèstra del terminal, cal executar la comanda per installar lo paquet de lenga (vos serà demandat de picar lo vòstre senhal)

Pels sistèmas Ubuntu/basats sus Debian : sudo dpkg -i *.deb

Pels sistèmas basats sus Fedora : su -c 'dnf install *.rpm'

Pels sistèmas basats sus Mandriva : sudo urpmi *.rpm

Pels autres sistèmas qu'utilizan RPM (openSUSE, etc.) : rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Aprèp lo reglatge d'aqueles paramètres, clicatz sus Òc. La brústia de dialòg se tamparà e veiretz un messatge per vos informar que la modificacions seràn presas en compte sonque aprèp la tampadura de LibreOffice  e sa reobertura (vos cal quitar, tanben l'aviada rapida s'es activa).

Lo còp que ven ont lançaretz LibreOffice, la lenga qu'avètz causida s'installarà.

----------------------------------------------------------------------
Problèmas a l'aviada del programa
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Pavat tactil notebook ALPS/Synaptics jos Windows
----------------------------------------------------------------------

En rason d'un problèma amb lo pilòt Windows, podètz pas far defilar un document LibreOffice quand fasètz lissar vòstre det sus un pavat tactil ALPS/Synaptics.

Per activar lo defilament amb lo pavat tactil, apondètz las linhas seguentas dins lo fichièr de configuracion "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" e tornatz amodar vòstre ordenador :

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Remarca : l'emplaçament del fichièr de configuracion pòt variar en foncion de las diferentas versions de Windows.

----------------------------------------------------------------------
Acorchis de clavièr
----------------------------------------------------------------------

Sols los acorchis de clavièr (combinason de tòcas) inutilizats pel sistèma operatiu pòdon èsser utilizats dins LibreOffice. Se una combinason de tòcas dins LibreOffice fonciona pas coma descrit dins l'ajuda LibreOffice, verificatz qu'aqueste acorchi de clavièr es pas ja utilizat pel sistèma operatiu. Per corregir aquela mena de conflictes, podètz modificar l'assignacion dels acorchis de clavièr del sistèma operatiu. Alternativament, podètz modificar practicament totas las assignacions de tòcas dins LibreOffice. Per mai d'entresenhas sus aquel subjècte, referissètz-vos a l'ajuda de LibreOffice o a la documentacion d'ajuda de vòstre sistèma operatiu.

----------------------------------------------------------------------
Problèmas en enviant documents a partir de LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Nòtas importantas sus l'accessibilitat
----------------------------------------------------------------------

For more information on the accessibility features in LibreOffice, see https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Ajuda als utilizaires
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Consultatz tanben la seccion FAQ sus lo site web LibreOffice.

----------------------------------------------------------------------
Raportar de disfonciaments & de problèmas
----------------------------------------------------------------------

Our system for reporting, tracking and solving bugs is currently Bugzilla, hosted at https://bugs.documentfoundation.org/. We encourage all users to feel entitled and welcome to report bugs that may arise on your particular platform. Energetic reporting of bugs is one of the most important contributions that the user community can make to the ongoing development and improvement of LibreOffice.

----------------------------------------------------------------------
Contribucion
----------------------------------------------------------------------

La Comunautat LibreOffice tirarà un grand benefici de vòstre participacion activa dins lo desvolopament d'aqueste projècte Open Source important.

As a user, you are already a valuable part of the suite's development process and we would like to encourage you to take an even more active role with a view to being a long-term contributor to the community. Please join and check out the contributing page at the LibreOffice website.

Per començar
----------------------------------------------------------------------

The best way to start contributing is to subscribe to one or more of the mailing lists, lurk for a while, and gradually use the mail archives to familiarize yourself with many of the topics covered since the LibreOffice source code was released back in October 2000. When you're comfortable, all you need to do is send an email self-introduction and jump right in. If you are familiar with Open Source Projects, check out our To-Dos list and see if there is anything you would like to help with at the LibreOffice website.

S'inscriure
----------------------------------------------------------------------

Here are a few of the mailing lists to which you can subscribe at https://www.libreoffice.org/get-help/mailing-lists/

* Novèlas : announce@fr.libreoffice.org *recomandada a totes utilizaires* (pauc de trafic)
* Lista principala d'utilizaires : users@fr.libreoffice.org *un biais aisit de seguir las discussions* (trafic mejan)
* Projècte Marketing : marketing@global.libreoffice.org *de delà del desvolopament* (en anglés, trafic elevat)
* Lista de desvolopament generala : libreoffice@lists.freedsktop.org (trafec important)

Participar a un o mai d'un projèctes
----------------------------------------------------------------------

Podètz far de contribucions màgers a aquel projècte Open Source important, quitament s'avètz una experiéncia limitada dins l'encodatge o lo dessenh del programa. Òc, vos !

Esperam que serètz content de trabalhar amb la version novèla de LibreOffice 26.2 e que nos rejonheretz lèu en linha.

La comunautat LibreOffice

----------------------------------------------------------------------
Còdi font utilizat / modificat
----------------------------------------------------------------------

Porcions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
