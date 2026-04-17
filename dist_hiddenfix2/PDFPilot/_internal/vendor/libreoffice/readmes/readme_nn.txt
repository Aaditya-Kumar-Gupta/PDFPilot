
======================================================================
LibreOffice 26.2 LesMeg
======================================================================


Sjå https://git.libreoffice.org/core/tree/master/README.md for dei siste oppdateringane av denne skriveverna fila.

Denne fila inneheld viktig informasjon om LibreOffice. Du bør lesa denne informasjonen nøye før installasjon.

LibreOffice-fellseskapet er ansvarleg for utviklinga av dette produktet og inviterer deg til å verta ein del av samarbeidet som bidragsytar. Er du ein ny brukar, kan du kikka innom nettstaden til LibreOffice. Der vil du finna masse informasjon om prosjektet LibreOffice og miljøet rundt det. Gå til https://www.libreoffice.org/.

Er LibreOffice verkeleg gratis for alle?
----------------------------------------------------------------------

LibreOffice er gratis å bruka for alle. Du kan installera dette eksemplaret av LibreOffice på så mange datamaskiner du vil, og bruka det til kva du vil (gjeld også bruk i det offentlege, i næringslivet og innan utdanning). Du kan lesa meir om vilkåra i lisensteksten som følgjer med LibreOffice.

Kvifor er LibreOffice gratis for alle?
----------------------------------------------------------------------

Denne kopien av LibreOffice kan brukast gratis fordi einskilde bidragsytarar og korporative sponsorar har laga, utvikla, testa, omsett, dokumentert, støtta, marknadsført og hjelpt til på mange andre måtar for å gjere LibreOffice til det er i dag – verdas leiande kontorprogram med open kjeldekode for heim og kontor.

Dersom du verdset innsatsen deira og vil syta for at LibreOffice held fram med å vere tilgjengeleg langt inn i framtida, kan du vurdera å bidra til prosjektet. For nærare informasjon sjå: https://www.libreoffice.org/community/get-involved/. Alle kan bidra med noko.

----------------------------------------------------------------------
Merknadar om installasjonen
----------------------------------------------------------------------

LibreOffice brukar ein nyare versjon av Java køyretidsmiljø (JRE) for å kunna ta i bruk alle funksjonane. JRE er ikkje ein del av installasjonspakken for LibreOffice og må difor installerast ekstra.

Systemkrav
----------------------------------------------------------------------

* Microsoft Windows 10 eller høgare.

Du må ha administratorrettar for å kunna installera programmet.

Du kan velja LibreOffice som standardprogram når du opnar filer frå Microsoft Office-program. Under installasjonen gjer du dette ved å bruka desse kommandolinjevala:

* REGISTER_ALL_MSO_TYPES=1 gjer LibreOffice til standardprogrammet for Microsoft Office-format.
* REGISTER_NO_MSO_TYPES=1 gjer at LibreOffice ikkje vert standardprogram for Microsoft Office-format.

Kontroller at det er nok tilgjengeleg minne i mappa for mellomlagring i operativsystemet og at du har lese-, skrive- og køyrerettar på denne mappa. Lukk alle andre program før du startar installasjonen.

Installasjon av LibreOffice på Debian/Ubuntu-baserte Linux-system
----------------------------------------------------------------------

Les avsnittet «Installera språkpakke» nedanfor om korleis ei språkpakke skal installerast (etter at den US-engelske versjonen av LibreOffice er installert).

Når du pakkar ut det nedlasta arkivet, vil du sjå at innhaldet er dekomprimert til ein underkatalog. Opna eit filhandsamingsvindauge og byt katalog til den som byrjar med «LibreOffice_» og versjonsnummeret og plattforminformasjonen.

Denne mappa inneheld ei undermappe med namnet «DEBS». Bytt til denne mappa.

Høgreklikk i mappa og vel «Opna i terminal». Eit terminalvindauge kjem fram. Skriv den følgjande kommandoen (du vert beden om å oppgje passordet til superbrukar/administrator før køyring av kommandoen) i kommandolinja i terminalvindauget:

Desse kommandoane vil installera LibreOffice og skrivebordsintegrasjonspakkene (du kan kopiera og lima dei inn i terminalen i staden for å prøva å skriva dei inn):

sudo dpkg -i *.deb

Installasjonprosessen er no fullført og ikon for alle programma i LibreOffice skal vera tilgjengelege i program-/kontormenyen på skrivebordet.

Installering av LibreOffice på Fedora, openSUSE, Mandriva og andre Linux-system ved hjelp av RPM-pakkar.
----------------------------------------------------------------------

Du finn rettleiing om installering av språkpakkar (etter å ha installert US engelsk-versjonen av LibreOffice) nedanfor i bolken med namnet «Installera språkpakkar».

Når du pakkar ut det nedlasta arkivet, vil du sjå at innhaldet er dekomprimert til ein underkatalog. Opna eit filhandsamingsvindauge og byt katalog til den som byrjar med «LibreOffice_» og versjonsnummeret og plattforminformasjonen.

Denne mappa inneheld ei undermappe kalla «RPMS». Bytt til denne mappa.

Høgreklikk i mappa og vel «Opna i terminal». Eit terminalvindauge kjem fram. Skriv den følgjande kommandoen (du vert beden om å oppgje passordet til superbrukar/administrator før køyring av kommandoen) i kommandolinja i terminalvindauget:

For Fedora-baserte system: sudo dnf install *.rpm

For Mandriva-baserte system: su -c urpmi *.rpm

For andre RPM-baserte system (openSuse osv.): rpm -Uvh *.rpm

Installasjonprosessen er no fullført, og ikon for alle programma i LibreOffice skal vera tilgjengelege i program-/kontormenyen på skrivebordet.

Alternativt kan du bruka «install»-skriptet som du finn øvst i denne arkivmappa for å installera som ein brukar. Skriptet vil setja opp LibreOffice med ein eigen profil for denne installasjonen, skild frå den normale LibreOffice-profilen. Merk at dette vil ikkje installera systemintegrasjonsdelar som skrivebordsmenyar og registrering av MIME-typar.

Merknadar for skrivebordsintegrasjon i Linux-distribusjonar som ikkje er dekka i installasjonsrettleiinga over
----------------------------------------------------------------------

Det er tolleg enkelt å installera LibreOffice på andre Linux-distribusjonar som ikkje vert dekka av installasjonsrettleiinga. Integrasjonen av programvaren på skrivebordet kan variera.

RPMS-katalogen (høvesvis DEBS) inneheld òg ein pakke kalla libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (eller libreoffice26.2- debian-menus_26.2.0.1-1_all.deb, høvesvis eller liknande). Dette er ein pakke for alle Linux-distribusjonar som støttar Freedesktop.org-spesifikasjonane/tilrådingane (https://en.wikipedia.org/wiki/Freedesktop.org) og vert levert for installasjon på andre Linux-distribusjonar som ikkje vert dekte av dei nemnde instruksjonane.

Installera ei språkpakke
----------------------------------------------------------------------

Last ned språkpakken for det ønskte språket og den ønskte plattforma. Dei er tilgjengelege frå den same staden som standardinstallasjonen. Bruk filhandsamaren og pakk ut det nedlasta arkivet i ei mappe (for eksempel skrivebordet). Syt for at du har avslutta alle program i LibreOffice (også snøggstartaren dersom denne er slått på.)

Byt til mappa der den nedlasta språkpakken vart pakka ut.

Endra no katalog til katalogen som vart oppretta under utvinningsprosessen. For eksempel, for den franske språkpakken for eit 32-bitars Debian/Ubuntu-basert system, heiter katalogen LibreOffice_, pluss litt versjonsinformasjon, pluss Linux_x86_langpack-deb_fr.

Byt til mappa som inneheld pakkene som skal installerast. På Debian/Ubuntu-baserte system vil katalogen heita DEBS. På Fedora-, openSUSE- og Mandriva-baserte system vil katalogen heita RPMS.

Frå filhandsamaren, høgreklikk i mappa og vel kommandoen «Opna i terminal». I terminalvindauget, køyr kommandoen for å installera språkpakkene (kommandoane nedføre vil kanskje krevja passordet til superbrukar):

For Debian/Ubuntu-baserte system: sudo dpkg -i *.deb

For Fedora-basertesystem: su -c 'dnf install *.rpm'

For Mandriva-baserte system: su -c urpmi *.rpm

For andre RPM-baserte system (openSuse, osv.): rpm -Uvh *.rpm

Opna eit av programma i LibreOffice, for eksempel Writer. Gå til menyen «Verktøy» og vel «Innstillingar». I dialogvindauget «Innstillingar», trykk på «Språk og regionale tilpassingar» og vel «Generelt». Vel lista i rullegardinmenyen «Brukargrensesnittet» og språket som vart installert. Dersom det er ønskjeleg, gjer det same med «Lokale innstillingar», «Standard valuta» og «Standardspråk for dokument».

Etter å ha justert innstillingane, trykk på OK. Dialogvindauget vert lukka og ei melding om at innstillingane vert slått på ved neste oppstart av LibreOffice vert vist. Start programmet på nytt (hugs også å lukka snøggstarten.)

Neste gong LibreOffice startar, vil det starta i det språket du nettopp installerte.

----------------------------------------------------------------------
Problem ved programoppstart
----------------------------------------------------------------------

Vanskar med å starta LibreOffice (for eksempel program som heng seg opp) og problem med skjermvisinga kjem ofte frå grafikkortdrivaren. Viss du får desse problema, oppdater grafikkortdrivaren eller prøv å bruka grafikkdrivaren som følgjer med operativsystemet.

----------------------------------------------------------------------
ALPS/Synaptics-styreplater i Windows
----------------------------------------------------------------------

På grunn av ein drivarfeil i Windows kan du ikkje rulle i eit LibreOffice-dokument når du brukar ei styreplate frå ALPS/Synaptics.

For å kunna rulla med ei styreplate, legg inn desse linjene i oppsettfila C:\Program Files\Synaptics\SynTP\SynTPEnh.iniog start datamaskinen på nytt:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

Plasseringa av oppsettfila kan variera på ulike versjonar av Windows.

----------------------------------------------------------------------
Snartastar
----------------------------------------------------------------------

Berre snøggtastar (tastekombinasjonar) som ikkje er brukte i operativsystemet kan brukast i LibreOffice. Dersom ein tastekombinasjon i LibreOffice ikkje verkar som det står i hjelpetekstane for LibreOffice, sjå etter om snartastane er i bruk av operativsystemet. For å løysa slike konfliktar, kan du endra tastetilordningane i operativsystemet. Du kan også endra nesten alle tastekombinasjonane i LibreOffice. For meir informasjon om dette emnet, sjå hjelpa i LibreOffice eller dokumentasjonen for operativsystemet.

----------------------------------------------------------------------
Problem med å senda dokument som e-post frå LibreOffice
----------------------------------------------------------------------

Når du sender eit dokument via «Fil → Send → E-postdokument» eller «Fil → Send → Ei pdf-fil som e-postvedlegg», kan det oppstå problem (programmet krasjar eller heng seg opp). Dette kjem av Windows-systemfila «Mapi» (Messaging Application Programming Interface) som lagar problem i nokre filversjonar. Diverre kan problemet ikkje avgrensast til eit bestemt versjonsnummer. Viss du vil ha meir informasjon, kan du gå til https://www.microsoft.com for å søkja i Microsoft Knowledge Base etter «mapi dll».

----------------------------------------------------------------------
Viktig informasjon om tilgjenge
----------------------------------------------------------------------

For meir informasjon om tilgjengestøtte i LibreOffice, sjå https://www.libreoffice.org/accessibility/

----------------------------------------------------------------------
Brukarstøtte
----------------------------------------------------------------------

Hovudstøttesida tilbyr ulike måtar for hjelp med LibreOffice. Spørsmålet ditt kan alt vera svara på – kontroller difor fellesskapsforumet på https://ask.libreoffice.org eller søk i arkiva til e-postlista «users@libreoffice.org» påhttps://www.libreoffice.org. Alternativt kan du senda inn spørsmåla dine til users@libreoffice.org (engelsk). Viss du vil abonnera på lista (for å få e-postsvar), send ein tom e-post til users+subscribe@libreoffice.org. Alle desse er på engelsk, men svært få av brukarane har engelsk som førstespråk, så dei er vane med stotrande språk.

Sjå også FAQ på the LibreOffice website.

----------------------------------------------------------------------
Rapportar inn feil & problem
----------------------------------------------------------------------

Systemet for rapportering, sporing og løysing av feil er no Bugzilla, som ligg på https://bugs.documentfoundation.org/. Vi oppfordrar alle brukarane til å rapportera (på engelsk) feil som måtte dukke opp på den plattforma dei brukar. Aktiv feilrapportering er eit av dei mest verdifulle bidraga brukarmiljøet kan koma med i høve til den stadig pågåande utviklinga og forbetringa av LibreOffice.

----------------------------------------------------------------------
Engasjer deg
----------------------------------------------------------------------

LibreOffice-fellesskapet vil ha stor hjelp av at du deltek i utviklinga av dette viktige fri programvare-prosjektet.

Som brukar er du alt ein verdifull del av utviklingsprosessen og me vil oppmuntra deg til å ta ei aktiv rolle som bidragsytar i miljøet. Les meir på sida for bidragsytarar the LibreOffice website og meld deg på.

Korleis kome i gang
----------------------------------------------------------------------

Denne beste måten å bidra på er å abonnera på ei eller fleire av e-postlistene og følgja med ei stund for så å ta gradvis i bruk e-postarkiva for å gjera deg kjend med mange av dei temaa som er dekkja etter at kjeldekoden til LibreOffice vart gjort tilgjengeleg i oktober 2000. Når du føler deg klar, treng du berre å senda ein e-post der du introduserer deg sjølv og hoppa i det. Kjenner du open kjeldekode-prosjekta frå før, ta ein kikk på lista over oppgåver på the LibreOffice website og sjå om det er noko du kan hjelpa til med.

Abonner
----------------------------------------------------------------------

Her er nokre av e-postlistene du kan abonnera på https://www.libreoffice.org/get-help/mailing-lists/.

* Nyheitar: announce@documentfoundation.org *tilrådd for alle brukarar* (liten trafikk)
* Hovudliste for brukarar: users@libreoffice.org *enkelt å følgje med på diskusjonar* (mykje trafikk)
* Marknadsføringprosjekt: marketing@libreoffice.org *utover utvikling* (er i ferd med å verta tung.
* Generell utviklarliste: libreoffice@lists.freedesktop.org (høg trafikk)

Gå med i eitt eller fleire prosjekt
----------------------------------------------------------------------

Du kan gjera mykje for prosjektet sjølv om du ikkje har erfaring med programvareutvikling og programmering. Ja, nettopp du!

Me vonar du har glede av å arbeida med LibreOffice 26.2 og at me snart møtar deg på nettet.

LibreOffice-miljøet

----------------------------------------------------------------------
Brukt/endra kjeldekode
----------------------------------------------------------------------

Deler av opphavsrett 1998, 1999 James Clark. Deler av opphavsrett 1996, 1998 Netscape Communications Corporation.
