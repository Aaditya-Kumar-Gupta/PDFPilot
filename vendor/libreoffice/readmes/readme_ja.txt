
======================================================================
LibreOffice 26.2 ReadMe
======================================================================


最新版のこの readme ファイルはこちらから参照できます。https://git.libreoffice.org/core/tree/master/README.md

このファイルはソフトウェアLibreOfficeについての重要な情報を含んでいます。インストールを始める前に十分注意してこれを読むことをお勧めします。

LibreOfficeコミュニティはこの製品の開発に対して責任を負い、あなたにコミュニティメンバーとして参加することを考えていただくようご案内します。あなたが新しい利用者なら、LibreOfficeのサイトを訪れることができます。そこで LibreOfficeプロジェクトやその周りに存在するコミュニティについての多くの情報を見つかります。https://www.libreoffice.org/ へどうぞ。

LibreOfficeは本当にどの利用者に対してもフリーですか？
----------------------------------------------------------------------

LibreOfficeは誰でも自由に利用できます。LibreOfficeのコピーを用意して、それを好きなだけたくさんのコンピューターにインストールし、そしてそれを（商用や政府向け、行政向け、教育での利用などを含む）好きな目的で使ってかまいません。さらなる詳細についてはこのLibreOfficeダウンロードに同梱されているライセンスの文面を見てください。

なぜLibreOfficeはどの利用者に対してもフリーなのですか？
----------------------------------------------------------------------

あなたはLibreOfficeのこのコピーを無償で利用することができます。なぜなら、個人の貢献者や企業スポンサーが設計し、開発し、検証し、翻訳し、文書化し、サポートし、マーケティングをし、その他の多くの方法で助けることによって、LibreOfficeは今日あるような形 - 世界で最も優れた家庭およびオフィス向けのオープンソースプロダクティビティソフトウェアになっているからです。

If you appreciate their efforts, and would like to ensure that LibreOffice continues to be available far into the future, please consider contributing to the project - see https://www.libreoffice.org/community/get-involved/ for details. Everyone can make a contribution of some kind.

----------------------------------------------------------------------
インストールに関する注記
----------------------------------------------------------------------

LibreOfficeのすべての機能を使うにはJava実行環境（JRE）の最近のバージョンが必要です。JREはLibreOfficeには含まれていないので、別途インストールする必要があります。

システム要件
----------------------------------------------------------------------

* Microsoft Windows 10 or higher

注: インストールを実行するには、管理者権限が必要です。

Microsoft Office形式のデフォルトアプリケーションとしてLibreOfficeを登録するか否かは、次のようにコマンドラインでインストーラーのオプションを使用して指定できます:

* REGISTER_ALL_MSO_TYPES=1を指定すると、強制的にLibreOfficeをMicrosoft Officeフォーマットの既定アプリケーションとして登録します。
* REGISTER_NO_MSO_TYPES=1を指定すると、LibreOfficeをMicrosoft Officeフォーマットの既定アプリケーションとして登録しません。

システムの一時ディレクトリに十分なメモリーがあることを確認してください、そして読み込み、書き込み、および実行権限があることを確認してください。インストール処理を開始する前に他の全てのプログラムを閉じてください。

LibreOfficeをDebian/UbuntuベースのLinuxシステムにインストールする方法
----------------------------------------------------------------------

言語パックを（英語版のLibreOfficeのインストール後に）インストールする場合は、次の「言語パックのインストール」セクションを参考にしてください。

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

このディレクトリは"DEBS"と呼ばれるサブディレクトリを含みます。"DEBS"ディレクトリへ現在のディレクトリを変更してください。

そのディレクトリで右クリックをし、"ターミナルを開く"を選択してください。ターミナルウィンドウが開きます。ターミナルウィンドウのコマンドラインから、以下のコマンドを入力してください(コマンドが実行される前に root ユーザーのパスワードを入力するよう促されます):

The following commands will install LibreOffice and the desktop integration packages (you may just copy and paste them into the terminal screen rather than trying to type them):

sudo dpkg -i *.deb

これでインストールのプロセスが完了しました、デスクトップのアプリケーション/オフィスのメニューに全てのLibreOfficeアプリケーションのアイコンがあるはずです。

LibreOfficeを Fedora, openSUSE, Mandrivaや他のRPMを採用したLinuxシステムにインストールする方法
----------------------------------------------------------------------

言語パックを（英語版のLibreOfficeのインストール後に）インストールする場合は、次の「言語パックのインストール」セクションを参考にしてください。

When you unpack the downloaded archive, you will see that the contents have been decompressed into a sub-directory. Open a file manager window, and change directory to the one starting with "LibreOffice_", followed by the version number and some platform information.

このディレクトリは"RPMS"と呼ばれるサブディレクトリを含みます。"RPMS"ディレクトリへ現在のディレクトリを変更してください。

そのディレクトリで右クリックをし、"ターミナルを開く"を選択してください。ターミナルウィンドウが開きます。ターミナルウィンドウのコマンドラインから、以下のコマンドを入力してください(コマンドが実行される前に root ユーザーのパスワードを入力するよう促されます):

Fedoraベースのシステムでは: sudo dnf install *.rpm

Mandrivaベースのシステム向け: sudo urpmi *.rpm

他のRPMを使用するシステム(openSUSE等)向け: rpm -Uvh *.rpm

これでインストールのプロセスが完了しました、デスクトップのアプリケーション/オフィスのメニューに全てのLibreOfficeアプリケーションのアイコンがあるはずです。

代わりに、このアーカイブを伸張したフォルダーの直下にある「インストール」スクリプトを使用し、ユーザー権限でインストールすることもできます。このスクリプトは通常のLibreOfficeプロファイルとは別のLibreOffice独自のプロファイルを作成します。注意として、この方法ではデスクトップメニューアイテムとデスクトップMIMEタイプ登録といったシステム統合部分はインストールされません。

ここまでのインストールガイドでカバーされなかった、Linuxディストリビューションのデスクトップ統合環境に関しての注意
----------------------------------------------------------------------

これらのインストールの説明で明示的に扱っていない他のLinuxディストリビューションでLibreOfficeをインストールするのは簡単にできるはずです。違いが見つかる主な面はデスクトップインテグレーションです。

The RPMS (or DEBS, respectively) directory also contains a package named libreoffice26.2-freedesktop-menus-26.2.0.1-1.noarch.rpm (or libreoffice26.2-debian-menus_26.2.0.1-1_all.deb, respectively, or similar). This is a package for all Linux distributions that support the Freedesktop.org specifications/recommendations (https://en.wikipedia.org/wiki/Freedesktop.org), and is provided for installation on other Linux distributions not covered in the aforementioned instructions.

言語パックのインストール
----------------------------------------------------------------------

お望みの言語およびプラットフォームの言語パックをダウンロードしてください。それらは主要なインストールアーカイブとして同じ場所から取得できます。Nautilusファイルマネージャーから、ダウンロードしたアーカイブを1つのディレクトリ（例えば、デスクトップ）に展開してください。LibreOfficeのアプリケーション(もし開始していれば、クイックスターターも含め)すべてを終了していることを確認してください。

現在のディレクトリをダウンロードした言語パックを展開したディレクトリに変更してください。

Now change directory to the directory that was created during the extraction process. For instance, for the French language pack for a 32-bit Debian/Ubuntu-based system, the directory is named LibreOffice_, plus some version information, plus Linux_x86_langpack-deb_fr.

ここで現在のディレクトリをインストールするパッケージを含むディレクトリに変更してください。Debian/Ubuntu ベースのシステムでは、このディレクトリは DEBS です。Fedora や openSUSE、Mandriva システムでは、RPMS です。

Nautilus ファイルマネージャーから、そのディレクトリで右クリックしてコマンド"ターミナルを開く"を選択してください。そこで開いたターミナルウィンドウで、言語パックをインストールするコマンドを実行してください(以下の全てのコマンドについて、root ユーザーのパスワードを入力するよう促されることがあります):

Debian/Ubuntu ベースのシステム向け: sudo dpkg -i *.deb

Fedoraベースのシステムでは: su -c 'dnf install *.rpm'

Mandrivaベースのシステム向け: sudo urpmi *.rpm

他のRPMを使用するシステム(openSUSE等)向け: rpm -Uvh *.rpm

Now start one of the LibreOffice applications - Writer, for instance. Go to the Tools menu and choose Options. In the Options dialog box, click on "Languages and Locales" and then click on "General". Dropdown the "User interface" list and select the language you just installed. If you want, do the same thing for the "Locale setting", the "Default currency", and the "Default languages for documents".

これらの設定を調整した後、OK をクリックしてください。ダイアログボックスが閉じて、LibreOfficeを終了して再度起動した（もし起動していれば、クイックスターターも終了することを忘れないでください）ときに初めて変更が有効になるということを知らせる情報メッセージが出てくるでしょう。

次回にLibreOfficeを起動させると、インストールした言語で開始されます。

----------------------------------------------------------------------
プログラム起動時の問題
----------------------------------------------------------------------

LibreOfficeが起動しない場合や画面表示に関する問題の多くは、グラフィックカードドライバーが原因となって発生しています。これらの問題が発生した場合は、グラフィックカードドライバーを更新するか、OS付属のグラフィックドライバーに変更してみてください。

----------------------------------------------------------------------
Windows上でのALPS/Synaptics製のノートブックPCタッチパッド
----------------------------------------------------------------------

Windowsドライバーに問題があるため、ALPS/Synaptics製のタッチパッド上で指を動かしてもLibreOfficeのドキュメントをスクロールすることはできません。

タッチパッドでスクロールできるようにするには、下記の行を C:\Program Files\Synaptics\SynTP\SynTPEnh.ini 設定ファイルに追加して、コンピューターを再起動してください:

[LibreOffice]

FC = "SALFRAME"

SF = 0x10000000

SF |= 0x00004000

注意事項: この設定ファイルの場所は、Windows のバージョンによって異なる場合があります。

----------------------------------------------------------------------
ショートカットキー
----------------------------------------------------------------------

LibreOfficeで使用できるショートカットキー（キーの組み合わせ）は、オペレーティングシステムで使用されていないものだけです。LibreOfficeのショートカットキーがLibreOffice ヘルプの記述どおりに動作しない場合は、そのショートカットキーがすでにオペレーティングシステムで使用されているかどうかを確認してください。このような競合を解決するには、オペレーティングシステムによって割り当てられているキーを変更してください。または、LibreOffice側でキーの割り当てを変更します (ほとんどのキー割り当ては変更が可能です)。詳細については、LibreOfficeのヘルプまたはオペレーティングシステムのヘルプを参照してください。

----------------------------------------------------------------------
LibreOfficeから文書をメール送信する際に問題が発生しました
----------------------------------------------------------------------

When sending a document via 'File - Send - Email Document' or 'File - Send - Email as PDF' problems might occur (program crashes or hangs). This is due to the Windows system file "Mapi" (Messaging Application Programming Interface) which causes problems in some file versions. Unfortunately, the problem cannot be narrowed down to a certain version number. For more information visit https://www.microsoft.com to search the Microsoft Knowledge Base for "mapi dll".

----------------------------------------------------------------------
重要な利用を手助けするためのノート
----------------------------------------------------------------------

LibreOfficeでのアクセシビリティの機能についてのさらなる情報は、https://www.libreoffice.org/accessibility/ をご覧ください

----------------------------------------------------------------------
ユーザーサポート
----------------------------------------------------------------------

The main support page offers various possibilities for help with LibreOffice. Your question may have already been answered - check the Community Forum at https://ask.libreoffice.org/ or search the archives of the 'users@libreoffice.org' mailing list at https://www.libreoffice.org/lists/users/. Alternatively, you can send in your questions to users@libreoffice.org. If you like to subscribe to the list (to get email responses), send an empty mail to: users+subscribe@libreoffice.org.

また、LibreOfficeのwebサイトの「よくある質問」のセクションを確認してください。

----------------------------------------------------------------------
バグと問題の報告
----------------------------------------------------------------------

バグを報告し追跡し解決するための私たちのシステムは現在Bugzillaであり、https://bugs.documentfoundation.org/ でホストされています。全てのユーザーに対し個別のプラットフォームで生じるバグを報告する資格があり歓迎されているとお考えください。バグの精力的な報告はユーザーコミュニティがLibreOfficeの進行中の開発や改善に対してできる最も重要な貢献の1つです。

----------------------------------------------------------------------
コミュニティへの参加
----------------------------------------------------------------------

LibreOfficeコミュニティでは、この重要なオープンソースプロジェクトの発展への積極的な参加をお待ちしています。

利用者として、あなたは既にこのスイートの開発プロセスの価値のある一部分であり、コミュニティにとって長期に渡る貢献者となるように、一層のアクティブな役割を果たすことを勧めます。ぜひ参加して、LibreOfficeのWebサイトを調べてみてください。

始め方
----------------------------------------------------------------------

貢献を始めるために最善の方法は、1つまたはそれ以上のメーリングリストを購読し、しばらく様子を見て、徐々にメールのアーカイブを使って2000年10月まで遡るLibreOfficeのソースコードがリリースされて以来出てきているたくさんの話題に親しむことです。良い状態になれば、あとは自己紹介のメールを送って飛び込むだけです。オープンソースプロジェクトに慣れているなら、LibreOfficeのWebサイトで私たちの To-Do リストを調べて手伝いたいと思うものがないか見てください。

購読
----------------------------------------------------------------------

購読できるメーリングリストが次の場所にあります: https://www.libreoffice.org/get-help/mailing-lists/

* お知らせ: announce@documentfoundation.org *すべてのユーザーに推奨* (小流量)
* メインのユーザー向けリスト: users@global.libreoffice.org *議論を簡単に見守ることができます* (多流量)
* マーケティングプロジェクト: marketing@global.libreoffice.org *開発を越えて* (流量が増えつつあります)
* 一般的な開発者向けリスト: libreoffice@lists.freedesktop.org (多流量)

一つ以上のプロジェクトに参加
----------------------------------------------------------------------

ソフトウェアの設計やコーディングの経験が少なくても、この重要なオープンソースプロジェクトに貢献する方法はあります。

新しいLibreOffice 26.2をどうぞお楽しみください。そして、オンラインコミュニティに参加していただけることを願っています。

LibreOffice コミュニティ

----------------------------------------------------------------------
使用された / 修正されたソースコード
----------------------------------------------------------------------

Portions Copyright 1998, 1999 James Clark. Portions Copyright 1996, 1998 Netscape Communications Corporation.
