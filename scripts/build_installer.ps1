param(
    [Parameter(Mandatory = $true)]
    [string]$BuildRoot,
    [string]$Version = "1.0.0",
    [string]$TesseractInstallerPath = ""
)

$ErrorActionPreference = "Stop"

function Resolve-TesseractInstaller {
    param([string]$BuildOverride)

    if ($BuildOverride -and (Test-Path $BuildOverride)) {
        return (Resolve-Path $BuildOverride).Path
    }

    $repoRoot = Split-Path -Parent $PSScriptRoot
    $candidates = @(
        (Join-Path $repoRoot "vendor\installers\tesseract-ocr.exe"),
        (Join-Path $repoRoot "temp\tesseract-ocr-w64-setup-5.4.0.20240606.exe")
    )

    foreach ($candidate in $candidates) {
        if (Test-Path $candidate) {
            return (Resolve-Path $candidate).Path
        }
    }

    return ""
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$outputRoot = Join-Path $repoRoot "releases"
$issFile = Join-Path $repoRoot "packaging\installer\PDFPilot.iss"
$iscc = Get-Command iscc.exe -ErrorAction SilentlyContinue

if (-not $iscc) {
    throw "Inno Setup Compiler (iscc.exe) was not found on PATH."
}

$resolvedTesseractInstaller = Resolve-TesseractInstaller -BuildOverride $TesseractInstallerPath
New-Item -ItemType Directory -Force -Path $outputRoot | Out-Null

$defines = @(
    "/DMyBuildDir=$BuildRoot",
    "/DMyAppVersion=$Version",
    "/DMyOutputDir=$outputRoot"
)

if ($resolvedTesseractInstaller) {
    $defines += "/DMyTesseractInstaller=$resolvedTesseractInstaller"
}

& $iscc.Source @defines $issFile
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
Write-Host "Installer ready in: $outputRoot"
