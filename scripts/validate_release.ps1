param(
    [string]$MsixPath = "releases\PDFPilot-Store.msix",
    [string]$InstallerPath = "releases\PDFPilot-Setup.exe",
    [string]$PythonPath = ".venv\Scripts\python.exe",
    [string]$ReportRoot = "releases\validation",
    [switch]$AllowUnsigned,
    [switch]$SkipFunctionalSmoke
)

$ErrorActionPreference = "Stop"

function New-CheckResult {
    param(
        [string]$Name,
        [bool]$Passed,
        [string]$Message,
        [object]$Details = $null
    )

    [pscustomobject]@{
        name = $Name
        status = if ($Passed) { "passed" } else { "failed" }
        message = $Message
        details = $Details
    }
}

function Resolve-RequiredPath {
    param([string]$PathValue)

    if (-not (Test-Path $PathValue)) {
        throw "Required path not found: $PathValue"
    }
    return (Resolve-Path $PathValue).Path
}

function Get-FileEvidence {
    param([string]$PathValue)

    $item = Get-Item $PathValue
    $signature = Get-AuthenticodeSignature $PathValue
    $hash = Get-FileHash -Algorithm SHA256 $PathValue
    [pscustomobject]@{
        path = $item.FullName
        length = $item.Length
        lastWriteTime = $item.LastWriteTime.ToString("o")
        sha256 = $hash.Hash
        signatureStatus = [string]$signature.Status
        signatureMessage = $signature.StatusMessage
        signerSubject = if ($signature.SignerCertificate) { $signature.SignerCertificate.Subject } else { "" }
        signerThumbprint = if ($signature.SignerCertificate) { $signature.SignerCertificate.Thumbprint } else { "" }
        versionInfo = [pscustomobject]@{
            fileVersion = $item.VersionInfo.FileVersion
            productVersion = $item.VersionInfo.ProductVersion
            productName = $item.VersionInfo.ProductName
            companyName = $item.VersionInfo.CompanyName
        }
    }
}

function Read-MsixManifest {
    param([string]$PathValue)

    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $archive = [System.IO.Compression.ZipFile]::OpenRead($PathValue)
    try {
        $entry = $archive.GetEntry("AppxManifest.xml")
        if (-not $entry) {
            throw "MSIX does not contain AppxManifest.xml"
        }
        $reader = [System.IO.StreamReader]::new($entry.Open())
        try {
            [xml]$manifest = $reader.ReadToEnd()
        }
        finally {
            $reader.Dispose()
        }

        $entries = @($archive.Entries | ForEach-Object { $_.FullName })
        [pscustomobject]@{
            manifest = $manifest
            entries = $entries
        }
    }
    finally {
        $archive.Dispose()
    }
}

function Test-MsixPackage {
    param([string]$PathValue)

    $checks = [System.Collections.Generic.List[object]]::new()
    $package = Read-MsixManifest -PathValue $PathValue
    $manifest = $package.manifest
    $entries = $package.entries
    $packageNode = $manifest.Package
    $identity = $packageNode.Identity
    $application = $packageNode.Applications.Application
    $visuals = $application.VisualElements
    $capabilities = @($packageNode.Capabilities.ChildNodes | ForEach-Object { $_.Name })

    $checks.Add((New-CheckResult "msix_manifest_identity" ($identity.Name -eq "PDFPilot") "MSIX package identity name is PDFPilot." @{
        name = $identity.Name
        publisher = $identity.Publisher
        version = $identity.Version
        architecture = $identity.ProcessorArchitecture
    }))
    $checks.Add((New-CheckResult "msix_manifest_version" ($identity.Version -match '^\d+\.\d+\.\d+\.\d+$') "MSIX version uses four-part package version format." $identity.Version))
    $checks.Add((New-CheckResult "msix_manifest_architecture" ($identity.ProcessorArchitecture -eq "x64") "MSIX architecture is x64." $identity.ProcessorArchitecture))
    $checks.Add((New-CheckResult "msix_manifest_executable" ($application.Executable -eq "app\PDFPilot.exe") "MSIX executable points at app\PDFPilot.exe." $application.Executable))
    $checks.Add((New-CheckResult "msix_manifest_full_trust" ($application.EntryPoint -eq "Windows.FullTrustApplication" -and $capabilities -contains "runFullTrust") "MSIX declares full-trust desktop app capability." @{
        entryPoint = $application.EntryPoint
        capabilities = $capabilities
    }))

    $requiredAssets = @(
        "assets/StoreLogo.png",
        "assets/Square44x44Logo.png",
        "assets/Square71x71Logo.png",
        "assets/Square150x150Logo.png",
        "assets/Square310x310Logo.png",
        "assets/Wide310x150Logo.png"
    )
    $missingAssets = @($requiredAssets | Where-Object { $entries -notcontains $_ })
    $checks.Add((New-CheckResult "msix_store_assets" ($missingAssets.Count -eq 0) "MSIX contains required Store visual assets." @{
        missing = $missingAssets
        displayName = $visuals.DisplayName
    }))

    $containsLibreOffice = @($entries | Where-Object { $_ -like "*vendor/libreoffice*" -or $_ -like "*vendor\libreoffice*" }).Count -gt 0
    $containsTesseract = @($entries | Where-Object { $_ -match "(?i)tesseract" }).Count -gt 0
    $containsDocxTemplateFolder = @($entries | Where-Object { $_ -like "*default-docx-template*" }).Count -gt 0
    $checks.Add((New-CheckResult "msix_excludes_bundled_libraries" (-not $containsLibreOffice -and -not $containsTesseract) "Store package excludes bundled LibreOffice and Tesseract payloads." @{
        containsLibreOffice = $containsLibreOffice
        containsTesseract = $containsTesseract
    }))
    $checks.Add((New-CheckResult "msix_excludes_incompatible_docx_template" (-not $containsDocxTemplateFolder) "MSIX excludes python-docx exploded template files that makeappx rejects." @{
        containsDefaultDocxTemplate = $containsDocxTemplateFolder
    }))

    return $checks
}

function Test-InstallerPayload {
    param([string]$RepoRoot)

    $checks = [System.Collections.Generic.List[object]]::new()
    $desktopRoot = Join-Path $RepoRoot "dist\desktop\PDFPilot"
    $exePath = Join-Path $desktopRoot "PDFPilot.exe"
    $sofficePath = Join-Path $desktopRoot "_internal\vendor\libreoffice\program\soffice.exe"
    $issPath = Join-Path $RepoRoot "packaging\installer\PDFPilot.iss"
    $iss = Get-Content $issPath -Raw

    $checks.Add((New-CheckResult "installer_desktop_build_root_exists" (Test-Path $desktopRoot) "Desktop build root exists for installer payload validation." $desktopRoot))
    $checks.Add((New-CheckResult "installer_contains_app_exe" (Test-Path $exePath) "Desktop installer payload contains PDFPilot.exe." $exePath))
    $checks.Add((New-CheckResult "installer_contains_bundled_libreoffice" (Test-Path $sofficePath) "Desktop installer payload includes bundled LibreOffice renderer." $sofficePath))
    $checks.Add((New-CheckResult "installer_admin_privileges" ($iss -match "PrivilegesRequired=admin") "Installer requires admin privileges as expected." "PrivilegesRequired=admin"))
    $checks.Add((New-CheckResult "installer_shortcuts_configured" ($iss -match "\{group\}\\PDFPilot" -and $iss -match "\{autodesktop\}\\PDFPilot") "Installer defines Start menu and optional desktop shortcuts." $null))
    $checks.Add((New-CheckResult "installer_uninstall_cleanup_configured" ($iss -match "\[UninstallDelete\]" -and $iss -match "\{app\}") "Installer has uninstall cleanup for app directory." $null))

    return $checks
}

function Invoke-CheckedCommand {
    param(
        [string]$Name,
        [string]$FilePath,
        [string[]]$Arguments,
        [string]$WorkingDirectory,
        [string]$LogPath
    )

    $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
    $startInfo.FileName = $FilePath
    $escapedArguments = @($Arguments | ForEach-Object {
        $argument = [string]$_
        if ($argument -notmatch '[\s"]') {
            $argument
        }
        else {
            '"' + $argument.Replace('\', '\\').Replace('"', '\"') + '"'
        }
    })
    $startInfo.Arguments = $escapedArguments -join " "
    $startInfo.WorkingDirectory = $WorkingDirectory
    $startInfo.UseShellExecute = $false
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true

    $process = [System.Diagnostics.Process]::new()
    $process.StartInfo = $startInfo
    [void]$process.Start()
    $stdout = $process.StandardOutput.ReadToEnd()
    $stderr = $process.StandardError.ReadToEnd()
    $process.WaitForExit()
    $exitCode = $process.ExitCode
    @(
        "COMMAND: $FilePath $($Arguments -join ' ')",
        "EXIT CODE: $exitCode",
        "",
        "STDOUT:",
        $stdout,
        "",
        "STDERR:",
        $stderr
    ) | Out-File -FilePath $LogPath -Encoding UTF8
    return (New-CheckResult $Name ($exitCode -eq 0) "$FilePath $($Arguments -join ' ')" @{
        exitCode = $exitCode
        logPath = (Resolve-Path $LogPath).Path
    })
}

function Write-MarkdownReport {
    param(
        [string]$PathValue,
        [object]$Payload
    )

    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add("# PDFPilot Release Validation Report")
    $lines.Add("")
    $lines.Add("- Created UTC: $($Payload.createdUtc)")
    $lines.Add("- Overall status: $($Payload.status)")
    $lines.Add("- Unsigned artifacts allowed: $($Payload.allowUnsigned)")
    $lines.Add("")
    $lines.Add("## Artifacts")
    $lines.Add("")
    foreach ($artifact in $Payload.artifacts.PSObject.Properties) {
        $value = $artifact.Value
        $lines.Add("### $($artifact.Name)")
        $lines.Add("")
        $lines.Add("- Path: ``$($value.path)``")
        $lines.Add("- Bytes: $($value.length)")
        $lines.Add("- SHA256: ``$($value.sha256)``")
        $lines.Add("- Signature: $($value.signatureStatus)")
        $lines.Add("- Signer: $($value.signerSubject)")
        $lines.Add("")
    }
    $lines.Add("## Checks")
    $lines.Add("")
    $lines.Add("| Check | Status | Message |")
    $lines.Add("| --- | --- | --- |")
    foreach ($check in $Payload.checks) {
        $message = [string]$check.message
        $lines.Add("| $($check.name) | $($check.status) | $($message.Replace('|', '/')) |")
    }
    $lines.Add("")
    $lines.Add("## VM Validation")
    $lines.Add("")
    $lines.Add("Complete the clean-machine checklist in ``docs\RELEASE_TESTING.md`` before release. This local report is not a substitute for Windows 10 and Windows 11 VM validation.")
    Set-Content -Path $PathValue -Value ($lines -join [Environment]::NewLine) -Encoding UTF8
}

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$reportRootPath = Join-Path $repoRoot $ReportRoot
New-Item -ItemType Directory -Force -Path $reportRootPath | Out-Null

$msixFullPath = Resolve-RequiredPath (Join-Path $repoRoot $MsixPath)
$installerFullPath = Resolve-RequiredPath (Join-Path $repoRoot $InstallerPath)
$pythonFullPath = Resolve-RequiredPath (Join-Path $repoRoot $PythonPath)

$checks = [System.Collections.Generic.List[object]]::new()
$artifacts = [pscustomobject]@{
    msix = Get-FileEvidence -PathValue $msixFullPath
    installer = Get-FileEvidence -PathValue $installerFullPath
}

$signatureOk = $AllowUnsigned -or (($artifacts.msix.signatureStatus -eq "Valid") -and ($artifacts.installer.signatureStatus -eq "Valid"))
$checks.Add((New-CheckResult "production_signatures" $signatureOk "Both release artifacts must have valid production signatures unless -AllowUnsigned is supplied." @{
    msix = $artifacts.msix.signatureStatus
    installer = $artifacts.installer.signatureStatus
}))

$unitLog = Join-Path $reportRootPath "unit-tests.log"
$checks.Add((Invoke-CheckedCommand -Name "unit_tests" -FilePath $pythonFullPath -Arguments @("-m", "unittest", "discover", "-s", "tests") -WorkingDirectory $repoRoot -LogPath $unitLog))

if (-not $SkipFunctionalSmoke) {
    $functionalLog = Join-Path $reportRootPath "functional-smoke.log"
    $functionalJson = Join-Path $reportRootPath "functional-smoke.json"
    $functionalMarkdown = Join-Path $reportRootPath "functional-smoke.md"
    $checks.Add(
        (Invoke-CheckedCommand `
            -Name "functional_smoke" `
            -FilePath $pythonFullPath `
            -Arguments @("scripts\release_functional_smoke.py", "--output-root", (Join-Path $reportRootPath "functional"), "--json-report", $functionalJson, "--markdown-report", $functionalMarkdown) `
            -WorkingDirectory $repoRoot `
            -LogPath $functionalLog)
    )
}

foreach ($check in (Test-MsixPackage -PathValue $msixFullPath)) {
    $checks.Add($check)
}

foreach ($check in (Test-InstallerPayload -RepoRoot $repoRoot)) {
    $checks.Add($check)
}

$failed = @($checks | Where-Object { $_.status -ne "passed" })
$payload = [pscustomobject]@{
    createdUtc = (Get-Date).ToUniversalTime().ToString("o")
    status = if ($failed.Count -eq 0) { "passed" } else { "failed" }
    allowUnsigned = [bool]$AllowUnsigned
    artifacts = $artifacts
    checks = @($checks)
}

$jsonPath = Join-Path $reportRootPath "release-validation.json"
$markdownPath = Join-Path $reportRootPath "release-validation.md"
$payload | ConvertTo-Json -Depth 8 | Set-Content -Path $jsonPath -Encoding UTF8
Write-MarkdownReport -PathValue $markdownPath -Payload $payload

Write-Host "Release validation report: $markdownPath"
if ($failed.Count -gt 0) {
    Write-Host "Failed checks:" -ForegroundColor Red
    foreach ($check in $failed) {
        Write-Host " - $($check.name): $($check.message)" -ForegroundColor Red
    }
    exit 1
}

Write-Host "Release validation passed." -ForegroundColor Green
exit 0
