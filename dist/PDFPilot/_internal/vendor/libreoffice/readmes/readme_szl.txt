
======================================================================
Zbiōr ReadMe programu LibreOffice 26.2
======================================================================


For the latest updates to this readme file, see https://git.libreoffice.org/core/tree/master/README.md

Tyn zbiōr zawiyro ważne informacyje ô ôprogramowaniu LibreOffice. Przeczytej go pozornie przed zaczyńciym instalacyje.

Społeczność LibreOffice je ôdpedzialno za budowanie tego programu i zaproszo cie do zastanowiynio sie nad ôstaniym jednym z jeji czōnkōw. Jeźli używosz programu, nawiydź strōna LibreOffice, kaj znojdziesz informacyje ô projekcie LibreOffice jak tyż jego społeczności. Nawiydź http://www.libreoffice.org/.

Je LibreOffice naprowda darmowy dlo wszyjskich?
----------------------------------------------------------------------

Program LibreOffice je darmowy dlo wszyjskich. Możesz używać tyj kopije LibreOffice i instalować jōm na tylu kōmputrach, wielu ino chcesz, jak tyż używać jij w kożdym cylu (kōmercyjnym, regyrōnkowym, edukacyjnym i w instytucyjach administracyje publicznyj). Wiyncyj informacyji idzie znojść w licyncyji przidanyj do pobranego LibreOffice.

Czymu program LibreOffice je darmowy dlo kożdego?
----------------------------------------------------------------------

Możesz używać tyj kopije LibreOffice bez płacynio, bo moc spōłpracownikōw i spōnsorōw go projektowało, tworziło, testowało, ôpisowało, spiyrało, reklamowało i pōmogało na siyła inkszych spusobōw, żeby LibreOffice bōł tym, czym je dzisiej – liderym postrzōd paketōw biurowych zorty Open Source na świecie, do użytku w dōma i we firmie.

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
Informacyje ô instalacyji
----------------------------------------------------------------------

LibreOffice wymogo nojnowszyj wersyje strzodowiska Java Runtime Environment (JRE) dlo połnego fungowanio. JRE to niyma tajla paketu instalacyjnego LibreOffice i winiyn być zainstalowany ekstra.

Wymogania systymowe
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

Do przekludzynio instalacyje potrzebne sōm uprawniynia administratora.

Registracyjo systymu LibreOffice za wychodno aplikacyjo do formatōw Microsoft Office idzie wymusić abo zastawićbez użycie instalatora z dalij pokozanymi szaltrami linije kōmynd:

* REGISTER_ALL_MSO_TYPES=1 wymusi registracyjo LibreOffice za wychodno aplikacyjo dlo formatōw Microsoft Office.
* REGISTER_NO_MSO_TYPES=1 strzimie registracyjo LibreOffice za wychodno aplikacyjo dlo formatōw Microsoft Office.

Trzeba dać pozōr, czy styko wolnego placu w katalogu tymczasowym, i czy ôstały prziznane uprawniynia ôdczytu, zopisu i sztartowanio. Przed zaczyńciym procesu instalacyje trzeba zawrzić inksze programy.

Instalacyjo LibreOffice w systymie Linux ôpartym ô dystrybucyjo Debian/Ubuntu
----------------------------------------------------------------------

Coby dostać instrukcyje, jak zainstalować paket jynzykowy (po instalacyji anglojynzycznej wersyje LibreOffice), przeczytej sekcyjo niżyj, zatytułowano Instalacyjo paketu jynzykowego.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Tyn katalog zawiyro podkatalog ze mianym „DEBS”. Zmiyń katalog na „DEBS”.

Kliknij prawym kneflym myszy na katalogu i ôbier z myni „Ôtwōrz w Terminalu”. Ôkno terminala ôtworzi sie. We liniji kōmynd trzeba wpisać ta kōmynda (pokoże sie pytanie ô hasło używocza root, podwiela kōmynda bydzie wykōnano):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

Proces instalacyje je teroz skōńczōny a ikōny wszyjskich aplikacyji LibreOffice winny sie pokazować w myni Programy/Biōro.

Instalacyjo LibreOffice dlo Fedory, openSUSE, Mandriwy i inkszych dystrybucyji Linuksa, co używajōm paketōw RPM
----------------------------------------------------------------------

Coby dostać instrukcyje, jak zainstalować paket jynzykowy (po instalacyji anglojynzycznej wersyje LibreOffice), przeczytej sekcyjo niżyj, zatytułowano Instalacyjo paketu jynzykowego.

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

Tyn katalog zawiyro podkatalog ze mianym „RPMS”. Zmiyń katalog na „RPMS”.

Kliknij prawym kneflym myszy na katalogu i ôbier z myni „Ôtwōrz w Terminalu”. Ôkno terminala ôtworzi sie. We liniji kōmynd trzeba wpisać ta kōmynda (pokoże sie pytanie ô hasło używocza root, podwiela kōmynda bydzie wykōnano):

For Fedora-based systems: sudo dnf install *.rpm

Dlo systymōw opartych na dystrybucyji Mandriva: sudo urpmi *.rpm

Dlo inkszych systymōw opartych na paketach RPM (openSUSE, itp.): rpm -Uvh *.rpm

Proces instalacyje je teroz skōńczōny a ikōny wszyjskich aplikacyji LibreOffice winny sie pokazować w myni Programy/Biōro.

Możesz tyż użyć skryptu „install”, co je na nojwyższym poziōmie foldera archiwum, coby sztartnōńć instalacyjo za używocza. Skrypt skōnfiguruje LibreOffice z włosnym profilym, ôddzielōnym ôd twojigo normalnego profilu LibreOffice. Dej pozōr, iże to niy bydzie instalacyjo elymyntōw, co integrujōm ze systymym, takich jak pozycyje w myni biōrka i wpisy w regeście MIME.

Zopiski ô integracyji z biōrkym dlo dystrybucyji Linuksa niy wymianowanych w powyższyj instrukcyji instalacyje
----------------------------------------------------------------------

Instalacyjo LibreOffice winna być blank prosto w dystrybucyjach Linuksa, kere były pōminiynte w tyj instrukcyji instalacyje. Jedyno rōżnica może sie zdarzić w integracyji z biōrkym.

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

Instalacyjo paketu jynzykowego
----------------------------------------------------------------------

Trzeba pobrać paket jynzykowy dlo ôdpednij godki i platformy. Pakety dostympne sōm w tym samym miyjscu, co bazowe archiwum instalacyjne. Ze pōmocōm mynedżera zbiorōw trzeba rozpakować pobrane archiwum do katalogu (bp. na biōrko). Trzeba tyż dać pozōr, żeby żodyn z programōw paketu LibreOffice niy bōł sztartniynty (społym z modułym gibkigo sztartowanio QuickStarter).

Trzeba przejść do katalogu, kaj pobrany paket jynzykowy bōł rozpakowany.

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

Teroz przejdź do katalogu, co zawiyro pakety instalacyjne. Dlo systymōw ôpartych ô dystrybucyjo Debian/Ubuntu tyn katalog nazywo sie DEBS. Dlo systymōw Fedora, openSUSE i Mandriva tyn katalog nazywo sie RPMS.

Kliknij prawym kneflym myszy na katalogu i ôbier z myni „Ôtwōrz w Terminalu”. Ôkno terminala ôtworzi sie. Coby zainstalować paket jynzykowy, w wierszu nakozań trzeba wpisać ta kōmynda (pokoże sie prośba ô hasło używocza root, podwiela kōmynda bydzie wykōnano):

Dlo systymōw, co bazujōm na Debianie/Ubuntu: sudo dpkg -i *.deb

For Fedora-based systems: su -c 'dnf install *.rpm'

Dlo systymōw ôpartych na dystrybucyji Mandriva: sudo urpmi *.rpm

Dlo inkszych systymōw, co używajōm RPM (openSUSE, etc.): rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

Po zmianie tych sztelōnkōw trzeba naciś knefel OK. Ôkno dialogowe zawrzi sie i bydzie pokozano informacyjo ô tym, iże dokōnane zmiany ôdniesōm skutek dopiyro po sztartniyńciu na nowo LibreOffice (pamiyntej ô zawarciu modułu gibkigo sztartowanio QuickStarter).

Zainstalowany i ôbrany jynzyk bydzie aktywny przi nastympnym ôtwarciu LibreOffice.

----------------------------------------------------------------------
Problymy w czasie sztartowanio programu
----------------------------------------------------------------------

Difficulties starting LibreOffice (e.g. applications hang) as well as problems with the screen display are often caused by the graphics card driver. If these problems occur, please update your graphics card driver or try using the graphics driver delivered with your operating system.

----------------------------------------------------------------------
Touchpady w kōmputrach mobilnych ALPS/Synaptics w Windows
----------------------------------------------------------------------

Skirz kludzocza systymu Windows niy idzie przewijać dokumyntōw LibreOffice, jak sie przejyżdżo palcym po touchpadach kōmputrōw mobilnych ALPS/Synaptics.

Coby włōnczyć przewijanie, przidej nastympujōnce linije do zbioru konfiguracyjnego "C:\Program Files\Synaptics\SynTP\SynTPEnh.ini" i sztartnij na nowo kōmputer:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Położynie zbioru może sie rōżnić w zależności ôd wersyje systymu Windows.

----------------------------------------------------------------------
Skrōty tastatury
----------------------------------------------------------------------

W programie LibreOffice mogōm być używane ino te skrōty tastaturowe (kōmbinacyje knefli), co niy sōm używane ôd systymu ôperacyjnego. Jeźli skrōt w programie LibreOffice niy funguje w spusōb ôpisany w pōmocy LibreOffice, trzeba wybadać, eli niyma ôn używany ôd systymu ôperacyjnego. Jeźli tak je, możesz skasować tyn kōnflikt bez zmiyniynie skrōtōw używane ôd systymu. Możesz tyż zmiynić hned kożdy skrōt używany w produkcie LibreOffice. Wiyncyj informacyji na tyn tymat je w pōmocy do produktu LibreOffice i w dokumyntacyji używanego systymu ôperacyjnego.

----------------------------------------------------------------------
Problems When Sending Documents as Emails From LibreOffice
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
Ważne informacyje ô dostympności
----------------------------------------------------------------------

Wiyncyj informacyji na tymat dostympności w LibreOffice idzie znojś pod adresōm https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Sparcie używocza
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

Wybadej tyż sekcyjo FAQ na strōnie LibreOffice .

----------------------------------------------------------------------
Report błyndōw & problymōw
----------------------------------------------------------------------

Bugzilla je naszym systymym do raportowanio, śledzynio i rozwiōnzowanio błyndōw, dostympno pod adresōm http://bugs.documentfoundation.org/. Zachyncōmy wszyjskich używoczy do raportowanio błyndōw, jake mogōm sie ukozać na jejich platformach. Ynergiczne raportowanie błyndōw je jednym z nojważniyjszych fungowań, jake społeczność używoczy może wniyść do dalszego rozrostu i poprawy LibreOffice.

----------------------------------------------------------------------
Prziłōncz sie
----------------------------------------------------------------------

Społeczność LibreOffice miała by wielki użytek z twojigo aktywnego udziału w rozroście tego ważnego projektu open source.

Jak kożdy używocz, je żeś już wertownōm tajlōm procesu rozrostowego i chcieliby my zachyńcić cie do podyjmniyńcio barzij aktywnyj role w dugoterminowyj spōłprace ze społecznościōm. Nawiydź i wybadej strōna z informacyjami ô możliwych spusobach spōłprace pod adresōm Strōny LibreOffice.

Jak zaczōńć spōłpraca?
----------------------------------------------------------------------

Nojlepszym spusobym na zaczyńcie spōłprace je zapisanie sie na jedna abo wiyncyj list mailingowych, przeglōndanie archiwum i stopniowe zapoznowanie sie z tymatami tam poruszōnymi. Bez to, iże kod zdrzōdłowy LibreOffice ôstoł wydany w Październiku 2000, zakres tymatycznych list je doś przestrōnny. Jak bydziesz sie czuć kōmfortowo, jedyne co musisz zrobić, to wysłać email w kerym krōtko sie przedstawisz i wskoczysz na głymboko woda. Jeźli projekty Open Source niy sōm cudze do ciebie, wybadej nasza lista TODO i zobocz, czy tam je coś, przi czym chcesz pōmōc. Wiyncyj informacyji pod adresōm Strōny LibreOffice/.

Subskrybuj
----------------------------------------------------------------------

Niżyj je pora list mailingowych, co na nie możesz sie zapisać pod adresōmhttps://www.libreoffice.org/get-help/mailing-lists/

* Nowości: announce@documentfoundation.org *zalycano dlo wszyjskich* (mały ruch)
* Bazowo lista używoczy: users@global.libreoffice.org *prosto podpatrzisz dyskusyjo* (srogi ruch)
* Marketing: marketing@global.libreoffice.org *beyond development* (coroz ciynżyjszy)
* Ôgōlno lista programistōw: libreoffice@lists.freedesktop.org (srogi ruch)

Prziwstowanie do jednego abo wiyncyj projektōw
----------------------------------------------------------------------

Możesz mieć srogi wkłod w tyn ważny projekt open source, nawet jeźli mosz niysroge doświadczynie w projektowaniu i tworzyniu ôprogramowanio. Ja, ty!

Mōmy nadzieja, iże podobo ci sie nowe LibreOffice 26.2 i prziłōnczysz sie dō nos w internecie.

Społeczność LibreOffice

----------------------------------------------------------------------
Użyty / Zmodyfikowany kod zdrzōdłowy
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
