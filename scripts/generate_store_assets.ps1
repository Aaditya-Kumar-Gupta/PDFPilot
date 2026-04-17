param(
    [string]$OutputRoot = ""
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceIcon = Join-Path $repoRoot "assets\app.ico"
if (-not (Test-Path $sourceIcon)) {
    throw "Source icon not found: $sourceIcon"
}

if (-not $OutputRoot) {
    $OutputRoot = Join-Path $repoRoot "packaging\msix\assets"
}

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

$assetMap = @{
    "Square44x44Logo.png" = 44
    "Square71x71Logo.png" = 71
    "Square150x150Logo.png" = 150
    "Square310x310Logo.png" = 310
    "Wide310x150Logo.png" = "310x150"
    "StoreLogo.png" = 50
}

$icon = [System.Drawing.Icon]::ExtractAssociatedIcon($sourceIcon)
if (-not $icon) {
    throw "Unable to load icon from $sourceIcon"
}

foreach ($entry in $assetMap.GetEnumerator()) {
    $outputPath = Join-Path $OutputRoot $entry.Key
    $width = 0
    $height = 0

    if ($entry.Value -is [string]) {
        $parts = $entry.Value.Split("x")
        $width = [int]$parts[0]
        $height = [int]$parts[1]
    } else {
        $width = [int]$entry.Value
        $height = [int]$entry.Value
    }

    $bitmap = New-Object System.Drawing.Bitmap $width, $height
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.Clear([System.Drawing.Color]::FromArgb(255, 15, 79, 107))
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

    $iconBitmap = $icon.ToBitmap()
    $padding = [Math]::Max([int]($width * 0.14), 8)
    $drawWidth = $width - ($padding * 2)
    $drawHeight = $height - ($padding * 2)
    if ($width -ne $height) {
        $drawWidth = [int]($width * 0.34)
        $drawHeight = $drawWidth
    }
    $x = [int](($width - $drawWidth) / 2)
    $y = [int](($height - $drawHeight) / 2)
    $graphics.DrawImage($iconBitmap, $x, $y, $drawWidth, $drawHeight)

    $bitmap.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $graphics.Dispose()
    $bitmap.Dispose()
    $iconBitmap.Dispose()
}

Write-Host "Store assets generated in: $OutputRoot"
