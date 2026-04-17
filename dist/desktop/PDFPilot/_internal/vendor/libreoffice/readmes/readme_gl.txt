
======================================================================
Ficheiro Léame do LibreOffice 26.2
======================================================================


Para as actualizacións máis recentes deste ficheiro, vexa https://git.libreoffice.org/core/tree/master/README.md

Este ficheiro contén información importante sobre o software LibreOffice. Recoméndaselle ler atentamente esta información antes de comezar a instalación.

A comunidade de LibreOffice é responsábel do desenvolvemento deste produto e convida a que vostede participe nel. Se é un usuario novo pode visitar o sitio de LibreOffice, no cal poderá atopar moita información sobre o proxecto LibreOffice e as comunidades que existen ao seu arredor. Vaia a http://www.libreoffice.org/.

LibreOffice é realmente libre para calquera usuario?
----------------------------------------------------------------------

LibreOffice é de uso libre para todos. Pode utilizar esta copia de LibreOffice para instalala en todos os computadores que desexe, e utilizala para calquera propósito que teña (o que inclúe a utilización comercial, gobernamental, na Administración pública e na educación). Para máis detalles, consulte o texto da licenza incluída na descarga de LibreOffice.

Por que LibreOffice é libre para todas as persoas?
----------------------------------------------------------------------

Pode utilizar esta copia de LibreOffice libre de cargas grazas a persoas que colaboran individualmente e a entidades financiadores que deseñaron, traduciron, documentaron, apoiaron, promoveron e axudaron de moitas outras formas para facer de LibreOffice o que ela é hoxe - a mellor suite do mundo de programas de produtividade ofimática de código aberto tanto para uso persoal como profesional.

Se aprecia os esforzos e lle gustaría que o LibreOffice continúe dispoñíbel no futuro, considere achegar a súa contribución ao proxecto - para máis detalles vexa https://www.libreoffice.org/community/get-involved/. Todo o mundo pode contribuír dalgunha maneira.

----------------------------------------------------------------------
Notas sobre a instalación
----------------------------------------------------------------------

O LibreOffice require unha versión recente do Java Runtime Environment (JRE) para unha funcionalidade completa. O JRE non é parte do paquete de instalación do LibreOffice, debe instalarse á parte.

Requisitos do sistema
----------------------------------------------------------------------

* Microsoft Windows 10 ou superior

Advírtese de que cómpre ter dereitos de administrador para o proceso de instalación.

O rexistro do LibreOffice como aplicación predeterminada para os formatos do Office da Microsoft pódese forzar ou rexeitar usando os seguintes modificadores co instalador na liña de ordes:

* REGISTER_ALL_MSO_TYPES=1 forzará o rexistro da LibreOffice como aplicación predeterminada para os formatos do Office da Microsoft.
* REGISTER_NO_MSO_TYPES=1 rexeitará o rexistro do LibreOffice como aplicación predeterminada para os formatos do Office da Microsoft.

Asegúrese de que hai espazo abondo no cartafol temporal do seu sistema e de que ten permisos de lectura, escritura e execución. Peche calquera outro programa antes de iniciar o proceso de instalación.

Instalación da LibreOffice en sistemas Linux baseados en Debian/Ubuntu
----------------------------------------------------------------------

Para obter instrucións sobre como instalar un paquete de idioma (despois de ter instalada a versión en inglés US de LibreOffice), lea a sección seguinte titulada Instalación dun paquete de idioma.

Cando desempaquete o arquivo descargado, verá que o contido se descomprimiu nun subcartafol. Abra unha xanela do xestor de ficheiros e vaia ao cartafol que comece por «LibreOffice_», seguido polo número de versión e algún tipo de información sobre a plataforma.

Este cartafol contén un subcartafol chamado «DEBS». Entre no cartafol «DEBS».

Prema sobre o botón dereito do rato e seleccione "Abrir un terminal". Abrirase unha xanela do terminal. Na liña de ordes da xanela do terminal, escriba a seguinte orde (preguntaráselle previamente polo seu contrasinal de usuario root antes de que se execute a orde):

As ordes seguintes instalan LibreOffice e os paquetes para a integración no escritorio (pode simplemente copialas e pegalas na pantalla do terminal no canto de tentar escribilas):

sudo dpkg -i *.deb

O proceso de instalación completouse e xa debería ter as iconas para todas as aplicacións do LibreOffice no seu menú Aplicacións/Ofimática.

Instalación de LibreOffice en Fedora, Suse, Mandriva e outros sistemas Linux que usan paquetes RPM
----------------------------------------------------------------------

Para obter instrucións sobre como instalar un paquete de idioma (despois de ter instalada a versión en inglés US de LibreOffice), lea a sección seguinte titulada Instalación dun paquete de idioma.

Cando desempaquete o arquivo descargado, verá que o contido se descomprimiu nun subcartafol. Abra unha xanela do xestor de ficheiros e vaia ao cartafol que comece por «LibreOffice_», seguido polo número de versión e algún tipo de información sobre a plataforma.

Este cartafol contén un subcartafol chamado "RPMS". Cámbiese ao cartafol "RPMS".

Prema sobre o botón dereito do rato e escolla «Abrir un terminal». Abrirase unha xanela do terminal. Na liña de ordes da xanela do terminal, escriba a seguinte orde (preguntaráselle previamente polo seu contrasinal de usuario root antes de que se execute a orde):

Para sistemas baseados en Fedora: sudo dnf install *.rpm

Para sistemas Mandriva: sudo urpmi *.rpm

Para os demais sistemas RPM (openSuse, etc.): rpm -Uvh *.rpm

O proceso de instalación completouse e xa debería ter as iconas para todas as aplicacións do LibreOffice no seu menú Aplicacións/Ofimática.

Alternativamente, pode utilizar o script de instalación «install» existente no cartafol superior deste arquivo para instalar como usuário. O script configurará o LibreOffice co seu perfil, sen interferir co perfil normal de LibreOffice. Saiba que así non instalará as partes de integración no sistema tales como menús de escritorio e os rexistros de escritorio de tipos MIME.

Notas sobre a integración do escritorio para distribucións Linux non mencionadas nas instrucións de instalación anteriores
----------------------------------------------------------------------

Debería ser doado instalar LibreOffice noutras distribucións Linux non especificadas nestas instrucións de instalación. O principal aspecto das diferenzas podería estar na integración co escritorio.

O directorio de RPM (ou DEB, segundo corresponda) tamén contén un paquete chamado libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (ou libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectivamente, ou semellante). Consiste nun paquete para todas as distribucións que admiten as especificacións de Freedesktop.org (https://gl.wikipedia.org/wiki/Freedesktop.org), e fornécese para permitir a instalación noutras distribucións de Linux non cubertas nas instrucións mencionadas.

Instalación dun paquete de idioma
----------------------------------------------------------------------

Descargue o paquete de idioma do idioma, país e plataforma desexado. Están dispoñíbeis no mesmo lugar do arquivo de instalación principal. Dentro do xestor de ficheiros Nautilus, extraia o arquivo descargado nun cartafol (no seu escritorio, por exemplo). Asegúrese de ter saído de todas as aplicacións do LibreOffice (incluíndo o Iniciador rápido, caso de se estar executando).

Cámbiese ao cartafol no que extraeu o paquete de idioma descargado.

Cámbiese ao cartafol que se creou durante o proceso de extracción. Por exemplo, para o paquete de idioma galego dun sistema Debian ou Ubuntu de 32 bits, o cartafol chámase LibreOffice_, máis a información sobre a versión, seguido por Linux_x86_langpack-deb_gl.

Agora, cámbiese ao cartafol que contén os paquetes para instalar. Nos sistemas baseados en Debian ou Ubuntu, o cartafol chámase DEBS. Nos sistemas Fedora, openSuse ou Mandriva, o cartafol chámase RPMS.

Desde o xestor de ficheiros Nautilus, prema o botón dereito no cartafol e escolla a orde «Abrir nun terminal». Na xanela do terminal que se acaba de abrir, execute a orde de instalar o paquete de idioma (en todas as ordes seguintes, solicitaráselle escribir o contrasinal do usuario root):

Para sistemas Debian/Ubuntu: sudo dpkg -i *.deb

Para sistemas baseados en Fedora: su -c 'dnf install *.rpm'

Para sistemas Mandriva: sudo urpmi *.rpm

Para outros sistemas RPM (openSuse, etc.): rpm -Uvh *.rpm

Inicie agora unha das aplicacións de LibreOffice - por exemplo o Writer. Vaia ao menú Ferramentas e escolla Opcións. Na caixa de diálogo Opcións, prema en «Idiomas e configuración local» e prema en «Xeral». Na lista despregábel «Interface de usuario» seleccione o idioma que acaba de instalar. Se quere, faga o mesmo con «Configuración local», a «Moeda predeterminada», e «Idiomas predeterminados para documentos».

Despois de axustar esa configuración, prema en Aceptar. O cadro de diálogo pecharase e verá unha mensaxe informativa que avisa de que os cambios se activarán despois de saír do LibreOffice e de reinicialo (lembre pechar o inicio rápido, se estiver en execución).

A próxima vez que incie LibreOffice, arrincará no idioma que acaba de instalar.

----------------------------------------------------------------------
Problemas ao iniciar o programa
----------------------------------------------------------------------

As dificultades ao iniciar o LibreOffice (p. ex. as aplicacións bloquéanse), así como os problemas coa presentación na pantalla prodúcense con frecuencia por causa do controlador da tarxeta gráfica. Se estes problemas ocorreren, actualice o controlador da tarxeta gráfica ou tente usar o controlador gráfico fornecido co sistema operativo.

----------------------------------------------------------------------
Superficies sensíbeis ALPS e Synaptics de notebooks en Windows
----------------------------------------------------------------------

Debido a un problema cos controladores de Windows, non é posíbel desprazar documentos a través de LibreOffice pasando o dedo por unha superficie sensíbel ALPS ou Synaptic.

Para activar a súa superficie sensíbel, engada as liñas que se indican á ruta de configuración "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" e despois reinicie o seu computador:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Obs.: A localización do ficheiro de configuración pode variar segundo as diferentes versións de Windows.

----------------------------------------------------------------------
Teclas de atallo
----------------------------------------------------------------------

As únicas teclas de atallo (combinacións de teclas) que se poden utilizar en LibreOffice son aquelas non utilizadas polo sistema operativo. Se algunha combinación de teclas non funciona en LibreOffice conforme se describe na Axuda de LibreOffice, comprobe se o sistema operativo xa usa ese atallo. Para corrixir eses conflitos, mude as teclas asignadas polo seu sistema operativo. Alternativamente, modifique as asignacións de teclas de LibreOffice. Para obter máis información sobre este asunto, consulte a Axuda de LibreOffice ou a documentación de axuda do seu sistema operativo.

----------------------------------------------------------------------
Problemas ao enviar documentos como correo electrónico desde o LibreOffice
----------------------------------------------------------------------

Ao enviar documentos a través de «Ficheiros – Enviar - Documento como correo electrónico» ou «Ficheiro - Enviar - Correo electrónico como PDF» poden xurdir problemas (por exemplo, o bloqueo do programa). Isto débese a que o ficheiro «Mapi» (Messaging Application Programming Interface) do Windows causa problemas nalgunhas das súas versións. Desgraciadamente, o problema non se pode restrinxir a unha versión determinada. Para máis información, visite https://www.microsoft.com para buscar «mapi dll» en Microsoft Knowledge Base.

----------------------------------------------------------------------
Notas importantes de accesibilidade
----------------------------------------------------------------------

Para obter máis información sobre as características de accesibilidade de LibreOffice consulte https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Asistencia do usuario
----------------------------------------------------------------------

A páxina principal de axuda ofrece varias posibilidades de axuda para o LibreOffice. Pode que a súa pregunta xa fose respondida — mire no Foro da Comunidade en https://ask.libreoffice.org/ ou busque nos arquivos da lista de correo «users@libreoffice.org» de https://www.libreoffice.org/lists/users/. Como alternativa, pode envíar as súas preguntas a users@libreoffice.org. Se desexa subscribirse á lista (para recibir respostas por correo), envíe unha mensaxe en branco a: users+subscribe@libreoffice.org.

Consulte tamén a sección de preguntas frecuentes do sitio web do LibreOffice.

----------------------------------------------------------------------
Informar de fallos & incidencias
----------------------------------------------------------------------

O noso sistema de informe, seguimento e resolución de fallos é o Bugzilla, hospedado en https://bugs.documentfoundation.org/. Convidamos a todos os usuarios a informaren de fallos que poidan ter aparecido nunha plataforma en particular. O informe de fallos é unha das máis importantes colaboracións da comunidade de usuarios para o desenvolvemento continuado e a mellora do LibreOffice.

----------------------------------------------------------------------
Participación
----------------------------------------------------------------------

A Comunidade LibreOffice sairía moi beneficiada da súa participación activa no desenvolvemento deste importante proxecto de software libre.

Como usuario, xa é parte valiosa do proceso de desenvolvemento da suite e gustaríanos convidalo a ter un papel máis activo co fin de converter a súa participación en colaboración de longo prazo coa comunidade. Únase á nosa comunidade e consulte a páxina de colaboracións do sitio web do LibreOffice.

Como comezar
----------------------------------------------------------------------

A mellor maneira de colaborar é subscribirse a unha ou máis de nosas listas de correo, observar durante algún tempo e gradualmente utilizar os arquivos de correo para se familiarizar cos varios temas abordados desde que o código fonte da LibreOffice foi liberado en outubro de 2000. Se estiver familiarizado cos proxectos de código aberto, consulte a nosa lista de tarefas por facer e vexa se hai algo no que lle interese axudar no sitio web do LibreOffice.

Subscribirse
----------------------------------------------------------------------

Aquí se detallan algunha das listas de correo ás que se pode subscribir en https://www.libreoffice.org/get-help/mailing-lists/

* Novas: announce@documentfoundation.org *recomendada para todos os usuarios* (tráfico leve)
* Lista principal de usuarios: users@global.libreoffice.org *un xeito fácil de seguir as discusión* (tráfico intenso)
* Proxecto de Mercadotecnia: marketing@global.libreoffice.org *alén do desenvolvemento* (tráfico en aumento)
* Lista xeral de desenvolvedores: libreoffice@lists.freedesktop.org (tráfico pesado)

Unirse a un ou máis proxectos
----------------------------------------------------------------------

Pode facer grandes contribucións a este proxecto de software libre mesmo sen ter moita experiencia con manexo do código ou co deseño de software. Si, vostede mesmo!

Esperamos que aprecie traballar co novoLibreOffice 26.2 e que se una a nós na rede.

A comunidade LibreOffice

----------------------------------------------------------------------
Código fonte usado / modificado
----------------------------------------------------------------------

Partes dos dereitos de autor pertencen a James Clark do 1998 ao 1999. Partes dos dereitos de autor pertencen a Netscape Communications Corporation do 1996 a 1998.
