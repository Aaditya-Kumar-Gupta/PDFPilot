# PDFPilot Release Testing

Use this checklist before publishing `PDFPilot-Store.msix` or `PDFPilot-Setup.exe`.

## Build-Machine Gate

Run the strict release gate from the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate_release.ps1
```

This command:

- runs the unit test suite;
- runs the functional tool smoke matrix against `runtime_tests`;
- records SHA256, size, version metadata, and Authenticode signature status for both artifacts;
- validates the MSIX manifest, Store assets, `runFullTrust`, executable path, and Store-flavor exclusions;
- validates that the desktop installer payload includes the app executable and bundled LibreOffice;
- writes evidence to `releases\validation\release-validation.md` and `releases\validation\release-validation.json`.

For a local dry run before production signing, use:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate_release.ps1 -AllowUnsigned
```

Do not ship from an `-AllowUnsigned` report. Production release requires `Get-AuthenticodeSignature` to report `Valid` for both artifacts.

## Clean Windows 11 VM

Start from a clean snapshot with no Python, Microsoft Office, LibreOffice, or Tesseract installed unless the specific test step says otherwise.

1. Copy `PDFPilot-Setup.exe`, `PDFPilot-Store.msix`, and `runtime_tests` into the VM.
2. Install `PDFPilot-Setup.exe` as admin.
3. Launch from the installer finish page, Start menu, desktop shortcut, and installed `PDFPilot.exe`.
4. Run these tools with `runtime_tests` fixtures and confirm each successful tool creates a readable output:
   - Merge PDF
   - Split PDF
   - Remove PDF Pages
   - Organize PDF
   - Scan to PDF
   - Compress PDF
   - Repair PDF
   - Image to PDF
   - PDF to JPG
   - PDF to Word
   - PDF to PowerPoint
   - PDF to Excel
   - PDF to PDF/A
   - Rotate PDF
   - Page Numbers
   - Watermark
   - Edit PDF
   - Crop PDF
   - Protect PDF
   - Unlock PDF
   - Sign PDF
   - Compare PDF
   - Redact PDF
5. Convert `.docx`, `.pptx`, `.xlsx`, and `.csv` to PDF. Desktop installer builds must report or demonstrate bundled LibreOffice rendering.
6. Check OCR behavior. It must either detect Tesseract if installed by the installer, or clearly explain that OCR needs setup.
7. Cancel one long-running operation and confirm no crash, hang, or final corrupt output.
8. Try invalid inputs: wrong password, encrypted PDF for PDF/A, missing output folder, empty selection, and invalid page range.
9. Close and reopen the app. Confirm settings and logs are under the user local app data directory, not the install directory.
10. Uninstall from Windows Settings. Confirm app files, shortcuts, and uninstall entry are removed.
11. Reinstall the same installer and repeat launch plus one representative conversion.

## Clean Windows 10 VM

Use a clean Windows 10 machine at or above the manifest minimum version `10.0.17763.0`.

1. Repeat installer install, launch, Office-to-PDF, OCR messaging, uninstall, and reinstall checks.
2. Run one representative tool from each category:
   - Organize PDF: Merge PDF
   - Optimize PDF: Compress PDF
   - Convert to PDF: Image to PDF
   - Convert from PDF: PDF to JPG
   - Edit PDF: Watermark
   - PDF Security: Protect PDF and Unlock PDF
3. If Windows 11 found any defect, rerun the affected tool or workflow on Windows 10 after the fix.

## MSIX Store Package

Only run final MSIX validation after production signing or a Store-valid identity is available.

1. Install `PDFPilot-Store.msix`.
2. Verify PDFPilot appears in Start and launches from Start.
3. Confirm the running app uses the packaged executable path.
4. Repeat the smoke tools that exercise file picker and output-folder permissions:
   - Merge PDF
   - Split PDF
   - Image to PDF
   - PDF to JPG
   - PDF to Word
   - Office-to-PDF for `.docx` and `.csv`
   - Watermark
   - Protect PDF and Unlock PDF
5. Confirm the Store build does not include bundled LibreOffice or Tesseract, and that missing dependencies are explained cleanly.
6. Uninstall from Windows Settings and confirm package removal.
7. Install an older package, upgrade to the current package, and confirm settings survive if the package identity is unchanged.

## Release Criteria

Release only when:

- `scripts\validate_release.ps1` passes without `-AllowUnsigned`;
- both artifacts have final SHA256 hashes recorded;
- Windows 11 full VM validation passes;
- Windows 10 smoke VM validation passes;
- MSIX Store validation passes;
- every defect found during validation is fixed, rebuilt, and retested from a clean snapshot.
