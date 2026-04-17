
======================================================================
ReadMe do LibreOffice 26.2
======================================================================


Para consultar as alterações mais recentes deste ficheiro, consulte https://git.libreoffice.org/core/tree/master/README.md

Este ficheiro contém informações relevantes sobre o LibreOffice. Recomenda-se a leitura exaustiva desta informação antes de instalar a aplicação.

A comunidade LibreOffice é responsável pelo desenvolvimento deste produto e incentiva todos os utilizadores a integrar a comunidade. Se é um novo utilizador, pode visitar o site LibreOffice, no qual encontra as informações sobre o projeto e sobre as comunidades do LibreOffice. Consulte https://www.libreoffice.org/.

O LibreOffice é realmente gratuito para os utilizadores?
----------------------------------------------------------------------

O LibreOffice é gratuito para todos os utilizadores. Você pode levar esta cópia do LibreOffice e instalá-la em quantos computadores quiser. É também livre para o utilizar como quiser (pode vender, instalar em instituições governamentais, na administração pública ou em estabelecimentos de ensino). Para saber mais detalhes, consulte a licença incluida no LibreOffice.

Porque é que o LibreOffice é gratuito?
----------------------------------------------------------------------

Pode utilizar esta cópia do LibreOffice gratutamente porque os colaboradores e os patrocinadores que o criaram, desenvolveram, testaram, traduziram, apoiaram, documentaram, publicitaram ou que de alguma forma ajudaram, são aqueles que tornam o LibreOffice aquilo que ele é - o líder das aplicações de produtividade para casa e escritórios em código livre.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Notas sobre a instalação
----------------------------------------------------------------------

O LibreOffice requer uma versão recente do Java Runtime Environment (JRE) para utilizar todas as funcionalidades. O JRE não faz parte do pacote de instalação do LibreOffice e deve ser instalado em separado.

Requisitos do sistema
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Tenha em atenção de que o processo de instalação requer direitos de administrador.

Pode recusar ou aceitar o registo do LibreOffice como aplicação padrão dos formatos Microsoft Office, utilizando as seguintes linhas de comandos durante a instalação:

* REGISTER_ALL_MSO_TYPES=1: o LibreOffice será a aplicação padrão para os formatos do Microsoft Office.
* REGISTER_NO_MSO_TYPES=1: o LibreOffice não será a aplicação padrão para formatos do Microsoft Office.

Certifique-se de que tem memória suficiente no diretório temporário do seu sistema e que possui permissão para escrever, ler e executar. Feche todos os programas antes de iniciar a instalação.

Instalação do LibreOffice nos sistemas baseados em Debian/Ubuntu
----------------------------------------------------------------------

Para mais informações sobre a instalação dos pacotes de idiomas (após instalar o LibreOffice na versão em inglês dos EUA), leia a seção abaixo intitulada Instalar um pacote de idioma.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Este diretório possui um subdiretório chamado "DEBS". Aceda ao diretório "DEBS".

Clique no botão direito do rato no diretório e escolha "Abrir no terminal". Um janela de terminal irá abrir. Na linha de comandos do terminal, digite o seguinte comando (será solicitada a palavra-passe de utilizador "root" antes do comando ser executado):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

O processo de instalação está completo, e deverá ter ícones para todas as aplicações LibreOffice no menu Aplicações/Escritório do seu sistema.

Instalação do LibreOffice nos sistemas Fedora, openSuse, Mandriva e outros que utilizem pacotes RPM
----------------------------------------------------------------------

Para mais informações sobre a instalação dos pacotes de idiomas (após instalar o LibreOffice na versão em inglês dos EUA), leia a seção abaixo intitulada Instalar um pacote de idioma.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

O diretório possui um subdiretório intitulado "RPMS". Aceda a esse diretório.

Clique no botão direito do rato no diretório e escolha "Abrir no terminal". Um janela de terminal irá abrir. Na linha de comandos do terminal, digite o seguinte comando (será solicitada a palavra-passe de utilizador "root" antes do comando ser executado):

Para sistemas baseados em Fedora: sudo dnf install *.rpm

Para sistemas baseados em Mandriva: sudo urpmi *.rpm

Para outros sistemas que utilizem pacotes RPM (openSuse, etc.): rpm -Uvh *.rpm

O processo de instalação está completo, e deverá ter ícones para todas as aplicações LibreOffice no menu Aplicações/Escritório do seu sistema.

Alternativamente, pode utilizar o script de instalação, que pode encontrar no diretório principal deste arquivo para executar a instalação como utilizador. O script irá configurar o LibreOffice de modo a que tenha o seu perfil para esta instalação, separando-o do seu perfil habitual do LibreOffice. Tenha em conta que este método não instala os pacotes de integração nos menus e no ambiente de trabalho e também não regista os tipos MIME.

Notas relativas à integração no ambiente de trabalho para distribuições Linux não previstas nas instruções acima indicadas
----------------------------------------------------------------------

Deve ser fácil instalar o LibreOffice nos sistemas Linux que não estão abrangidos por estas instruções de instalação. As principais diferenças devem ocorrer na integração ao ambiente de trabalho.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Instalar um pacote de idioma
----------------------------------------------------------------------

Descarregue o pacote do idioma desejado. Estes pacotes estão disponíveis no mesmo local do pacote de instalação. Agora, no gestor de ficheiros Nautilus, extraia o arquivo descarregado para um diretório (ambiente de trabalho, por exemplo). Certifique-se de que encerrou todas as aplicações do LibreOffice (não se esqueça do Início rápido, se ativo).

Altere o diretório para aquele em que você extraiu o pacote de idioma descarregado.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Agora aceda ao diretório que contém os pacotes a instalar. Para sistemas Debian/Ubuntu, o diretório será DEBS. Para Fedora, openSuse ou Mandriva, o diretório será RPMS.

No gestor de ficheiros Nautilus, clique com o botão direito do rato e escolha "Abrir no terminal". Na janela de terminal que abriu, execute o comando para instalar o pacote (com todos os comandos em baixo, pode ser-lhe solicitada a palavra-passe de "root"):

Para sistemas baseados em Debian/Ubuntu: sudo dpkg -i *.deb

Para sistemas baseados em Fedora: su -c 'dnf install *.rpm'

Para sistemas baseados em Mandriva: sudo urpmi *.rpm

Para outros sistemas que utilizem pacotes RPM (openSuse, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Após ajustar todas as definições pretendidas, clique Aceitar. A janela vai ser fechada e você vai receber uma mensagem a alertar que a interface do utilizador foi atualizada e que será aplicada na próxima vez que iniciar o LibreOffice (não se esqueça de fechar o Início rápido, se ativo).

Da próxima vez que executar o LibreOffice, a interface será exibida no idioma instalado.

----------------------------------------------------------------------
Problemas durante o arranque do programa
----------------------------------------------------------------------

As dificuldades em iniciar o LibreOffice (por exemplo, a aplicação bloqueia), bem como problemas com a exibição do ecrã são, normalmente, causados pelo controlador da placa gráfica. Se esses problemas ocorrerem, atualize o controlador da placa gráfica ou tente usar o controlador disponibilizado nativamente no sistema.

----------------------------------------------------------------------
Painéis tácteis para portáteis ALPS/Synaptics no Windows
----------------------------------------------------------------------

Devido a um problema do controlador do Windows, não é possível percorrer documentos do LibreOffice deslizando com o dedo no painel táctil ALPS/Synaptics.

Para ativar a deslocação, adicione as seguintes linhas ao ficheiro de configuração "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" e reinicie o computador:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

A localização do ficheiro de configuração pode variar nas diversas versões do Windows.

----------------------------------------------------------------------
Teclas de atalho
----------------------------------------------------------------------

Apenas as teclas de atalho (combinação de teclas) que não são utilizadas pelo sistema operativo podem ser utilizadas no LibreOffice. Se uma combinação de teclas do LibreOffice não funcionar como descrito na ajuda do LibreOffice, verifique se o atalho está a ser utilizado pelo sistema operativo. Para resolver os conflitos, pode alterar as teclas atribuídas pelo seu sistema operativo. Alternativamente, pode alterar quase todas as teclas de atalho do LibreOffice. Para mais informações, consulte a ajuda do LibreOffice ou a documentação do seu sistema operativo.

----------------------------------------------------------------------
Problemas ao enviar documentos como e-mail a partir do LibreOffice
----------------------------------------------------------------------

Ao enviar um documento através de "Ficheiro - Enviar - Documento por e-mail" ou "Ficheiro - Enviar - Documento como PDF anexo", podem ocorrer problemas (falha ou bloqueio do programa). Isto, porque, o sistema de ficheiros "Mapi" (Messaging Application Programming Interface) do Windows pode causar problemas em algumas versões de ficheiros. Infelizmente, não foi possível restringir o problema a uma versão específica. Para mais informações, consulte https://www.microsoft.com e pesquise na base de conhecimento da Microsoft por "mapi.dll".

----------------------------------------------------------------------
Notas importantes de acessibilidade
----------------------------------------------------------------------

Para mais informações sobre as funções de acessibilidade do LibreOffice, consulte https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Suporte técnico
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Verifique também a secção FAQ no site do LibreOffice.

----------------------------------------------------------------------
Comunicar erros & problemas
----------------------------------------------------------------------

O nosso sistema de reporte, acompanhamento e solução de erros é o BugZilla e está alojado em https://bugs.documentfoundation.org/. Encorajamos todos os utilizadores a reportarem os erros encontrem. O reporte de erros é a contribuição mais importante que os utilizadores podem dar, pois só assim é que a comunidade pode continuar a desenvolver e melhorar o LibreOffice.

----------------------------------------------------------------------
Envolvimento
----------------------------------------------------------------------

A comunidade do LibreOffice beneficiará bastante com a sua participação ativa no desenvolvimento deste importante projeto de código aberto.

Enquanto utilizador, você já é uma parte importante do processo de desenvolvimento. No entanto, gostaríamos de o incentivar a ter um papel mais ativo, oferecendo o seu contributo na comunidade. Veja como pode contribuir no site do LibreOffice.

Como começar
----------------------------------------------------------------------

A melhor forma de participar é subscrevendo as listas de correio, verificar o método de trabalho e utilizar os arquivos de mensagens para se acostumar aos diversos tópicos abrangidos, desde que o código fonte do LibreOffice foi disponibilizado, em outubro de 2000. Quando se sentir à vontade, só precisa de enviar uma mensagem para a lista de correio, apresentar-se e começar a interagir com os membros. Se souber como funcionam os projetos de código livre, verifique as listas de elementos a desenvolver (TODO) e verifique se existe algo em que acha que pode participar no site do LibreOffice.

Subscrever
----------------------------------------------------------------------

As listas de correio a que o utilizador pode subscrever estão disponíveis em https://www.libreoffice.org/get-help/mailing-lists/

* Novidades: announce@documentfoundation.org *recomendado para todos os utilizadores* (comunicação ligeira)
* Lista de correio dos utilizadores: users@global.libreoffice.org *local para debater diversos assuntos* (comunicação intensa)
* Departamento de marketing: marketing@global.libreoffice.org *em desenvolvimento* (comunicação a aumentar todos os dias)
* Lista dos programadores: libreoffice@lists.freedesktop.org (comunicação intensa)

Integrar um ou mais projetos
----------------------------------------------------------------------

Pode contribuir de forma significativa para este importante projeto de código livre, mesmo se a sua experiência de programação seja limitada. Sim, você mesmo!

Esperamos que o novo LibreOffice 26.2 corresponda às suas expectativas e aguardamos a sua integração na equipa.

A comunidade LibreOffice

----------------------------------------------------------------------
Código fonte utilizado/modificado
----------------------------------------------------------------------

Partes com direitos de autor 1998, 1999 James Clark. Partes com direitos de autor 1996, 1998 Netscape Communications Corporation.
