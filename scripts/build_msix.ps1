param(
    [Parameter(Mandatory = $true)]
    [string]$BuildRoot,
    [string]$Version = "1.0.0.0",
    [string]$PackageName = "PDFPilot",
    [string]$DisplayName = "PDFPilot",
    [string]$Publisher = "CN=REPLACE_WITH_PARTNER_CENTER_PUBLISHER",
    [string]$PublisherDisplayName = "PDFPilot",
    [string]$Architecture = "x64",
    [string]$CertificatePath = "",
    [string]$CertificatePassword = ""
)

$ErrorActionPreference = "Stop"

function Find-Tool {
    param([string]$CommandName, [string[]]$FallbackPatterns)

    $command = Get-Command $CommandName -ErrorAction SilentlyContinue
    if ($command) {
        return $command.Source
    }

    foreach ($pattern in $FallbackPatterns) {
        $match = Get-ChildItem -Path $pattern -ErrorAction SilentlyContinue | Sort-Object FullName -Descending | Select-Object -First 1
        if ($match) {
            return $match.FullName
        }
    }

    throw "Unable to find $CommandName. Install the Windows SDK / MSIX tooling first."
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$msixRoot = Join-Path $repoRoot "packaging\msix"
$assetsRoot = Join-Path $msixRoot "assets"
$stagingRoot = Join-Path $repoRoot "out\msix-staging"
$packageRoot = Join-Path $stagingRoot "app"
$outputRoot = Join-Path $repoRoot "releases"
$manifestTemplate = Join-Path $msixRoot "AppxManifest.template.xml"
$manifestOutput = Join-Path $stagingRoot "AppxManifest.xml"
$packageOutput = Join-Path $outputRoot "PDFPilot-Store.msix"

New-Item -ItemType Directory -Force -Path $outputRoot | Out-Null
Remove-Item -Force $packageOutput -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force $stagingRoot -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force -Path $packageRoot | Out-Null

& "$PSScriptRoot\generate_store_assets.ps1" -OutputRoot $assetsRoot

Copy-Item -Path (Join-Path $BuildRoot "*") -Destination $packageRoot -Recurse -Force
Copy-Item -Path $assetsRoot -Destination $stagingRoot -Recurse -Force

# python-docx includes an exploded default template with bracketed filenames
# such as [Content_Types].xml that makeappx rejects. The packaged runtime
# still retains default.docx, which is the template python-docx uses.
$msixIncompatibleDocxTemplate = Join-Path $packageRoot "_internal\docx\templates\default-docx-template"
if (Test-Path $msixIncompatibleDocxTemplate) {
    Remove-Item -Recurse -Force $msixIncompatibleDocxTemplate
}

$manifest = Get-Content $manifestTemplate -Raw
$replacements = @{
    "__PACKAGE_NAME__" = $PackageName
    "__PUBLISHER__" = $Publisher
    "__VERSION__" = $Version
    "__DISPLAY_NAME__" = $DisplayName
    "__PUBLISHER_DISPLAY_NAME__" = $PublisherDisplayName
    "__ARCHITECTURE__" = $Architecture
}

foreach ($entry in $replacements.GetEnumerator()) {
    $manifest = $manifest.Replace($entry.Key, $entry.Value)
}

Set-Content -Path $manifestOutput -Value $manifest -Encoding UTF8

$makeappx = Find-Tool -CommandName "makeappx.exe" -FallbackPatterns @(
    "C:\Program Files (x86)\Windows Kits\10\bin\*\x64\makeappx.exe",
    "C:\Program Files\Windows Kits\10\bin\*\x64\makeappx.exe"
)

& $makeappx pack /d $stagingRoot /p $packageOutput /o
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if ($CertificatePath) {
    $signtool = Find-Tool -CommandName "signtool.exe" -FallbackPatterns @(
        "C:\Program Files (x86)\Windows Kits\10\bin\*\x64\signtool.exe",
        "C:\Program Files\Windows Kits\10\bin\*\x64\signtool.exe"
    )

    $signArgs = @("sign", "/fd", "SHA256", "/f", $CertificatePath)
    if ($CertificatePassword) {
        $signArgs += @("/p", $CertificatePassword)
    }
    $signArgs += $packageOutput
    & $signtool @signArgs
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}

Write-Host "MSIX package ready: $packageOutput"
