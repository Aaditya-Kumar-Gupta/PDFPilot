#ifndef MyBuildDir
  #error MyBuildDir must be defined.
#endif

#ifndef MyAppVersion
  #define MyAppVersion "1.0.0"
#endif

#ifndef MyOutputDir
  #define MyOutputDir "."
#endif

#define MyAppName "PDFPilot"
#define MyAppExeName "PDFPilot.exe"

[Setup]
AppId={{C193FEB0-20CE-449D-AE0F-8055D6C52370}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher=PDFPilot
DefaultDirName={autopf}\PDFPilot
DefaultGroupName=PDFPilot
OutputDir={#MyOutputDir}
OutputBaseFilename=PDFPilot-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Files]
Source: "{#MyBuildDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
#ifdef MyTesseractInstaller
Source: "{#MyTesseractInstaller}"; DestDir: "{tmp}"; DestName: "tesseract-setup.exe"; Flags: deleteafterinstall
#endif

[Icons]
Name: "{group}\PDFPilot"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\PDFPilot"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
#ifdef MyTesseractInstaller
Filename: "{tmp}\tesseract-setup.exe"; Parameters: "/S"; StatusMsg: "Installing Tesseract OCR prerequisite..."; Flags: waituntilterminated
#endif
Filename: "{app}\{#MyAppExeName}"; Description: "Launch PDFPilot"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
