param(
    [ValidateSet("desktop", "store")]
    [string]$Flavor = "desktop",
    [string]$Version = "1.0.0.0",
    [string]$PackageName = "PDFPilot",
    [string]$DisplayName = "PDFPilot",
    [string]$Publisher = "CN=REPLACE_WITH_PARTNER_CENTER_PUBLISHER",
    [string]$PublisherDisplayName = "PDFPilot",
    [string]$CertificatePath = "",
    [string]$CertificatePassword = "",
    [string]$TesseractInstallerPath = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$distRoot = Join-Path $repoRoot "dist\$Flavor"
$buildRoot = Join-Path $repoRoot "build\$Flavor"

$env:PDFPILOT_RELEASE_FLAVOR = $Flavor

Write-Host "Building PDFPilot flavor: $Flavor"
python -m PyInstaller --clean --noconfirm --distpath $distRoot --workpath $buildRoot "$repoRoot\PDFPilot.spec"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if ($Flavor -eq "store") {
    & "$PSScriptRoot\build_msix.ps1" `
        -BuildRoot (Join-Path $distRoot "PDFPilot") `
        -Version $Version `
        -PackageName $PackageName `
        -DisplayName $DisplayName `
        -Publisher $Publisher `
        -PublisherDisplayName $PublisherDisplayName `
        -CertificatePath $CertificatePath `
        -CertificatePassword $CertificatePassword
    exit $LASTEXITCODE
}

& "$PSScriptRoot\build_installer.ps1" `
    -BuildRoot (Join-Path $distRoot "PDFPilot") `
    -Version $Version `
    -TesseractInstallerPath $TesseractInstallerPath
exit $LASTEXITCODE
