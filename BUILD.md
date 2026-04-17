# PDFPilot Build Guide

## 1. Create the environment

Preferred target: Python `3.12`.

Validated in this workspace: Python `3.14` with the pinned package versions in `requirements.txt`.

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. Optional offline dependencies

- Install `Tesseract OCR` locally to enable OCR. PDFPilot will auto-detect common Windows install locations, or you can point it at `tesseract.exe` in Settings.
- Optional: set `PDFPILOT_TESSERACT_PATH` to a custom executable or install folder if you want to override discovery without using the Settings UI.
- `pdf2image` may require Poppler if you expand the app to use that workflow directly.

## 3. Bundle a portable LibreOffice renderer for high-fidelity Office-to-PDF

To keep the app independent while preserving Office formatting, unpack a portable LibreOffice build into:

```text
vendor/libreoffice/
```

The app looks for:

```text
vendor/libreoffice/program/soffice.exe
```

You can also override the bundled renderer location at runtime with:

```powershell
$env:PDFPILOT_RENDERER_DIR="C:\path\to\libreoffice"
```

If no bundled or system LibreOffice is found, the app falls back to the built-in converter with reduced formatting fidelity.

## 4. Run the app

```powershell
.venv\Scripts\pythonw.exe main.pyw
```

## 5. Build the Windows executable

```powershell
python -m PyInstaller --clean PDFPilot.spec
```

The packaged app will be created in `dist\PDFPilot\`.

If `vendor/libreoffice/` exists at build time, it will be bundled automatically into the packaged app.

## 6. Release flavors

The build now supports two release flavors:

- `desktop`: bundles LibreOffice when `vendor/libreoffice/` exists and is intended for the direct Windows installer.
- `store`: excludes bundled LibreOffice/Tesseract payloads and is intended for Microsoft Store MSIX packaging.

Set the flavor with:

```powershell
$env:PDFPILOT_RELEASE_FLAVOR="desktop"
```

or:

```powershell
$env:PDFPILOT_RELEASE_FLAVOR="store"
```

## 7. Build the release outputs

Desktop installer:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_release.ps1 -Flavor desktop -Version 1.0.0
```

Microsoft Store MSIX:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_release.ps1 -Flavor store -Version 1.0.0.0 -PackageName PDFPilot -DisplayName PDFPilot -Publisher "CN=REPLACE_WITH_PARTNER_CENTER_PUBLISHER"
```

Notes:

- `scripts/build_msix.ps1` requires `makeappx.exe`, and signing requires `signtool.exe`.
- `scripts/build_installer.ps1` requires Inno Setup (`iscc.exe`) on PATH.
- `scripts/generate_store_assets.ps1` generates placeholder Store PNG assets from `assets/app.ico`.
- The MSIX packaging step strips `python-docx`'s exploded `default-docx-template/` folder because MSIX rejects bracketed filenames like `[Content_Types].xml`; `default.docx` remains available for runtime use.

## 8. Distribution notes

- The app performs all processing locally and does not require internet access.
- If you want high-fidelity Office conversion on clean machines, ship a portable LibreOffice runtime inside `vendor/libreoffice/` before building.
- For the desktop installer, optionally provide a Tesseract installer path or place it at `vendor/installers/tesseract-ocr.exe`.
- The app now stores mutable data under the user's local app data directory. Use `PDFPILOT_DATA_DIR` to override that location during testing or portable runs.
- Test the built executable on a machine without Python installed before release.

## 9. Validate release artifacts

Run the release gate after building both artifacts:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate_release.ps1
```

The strict gate requires valid production signatures for both `releases\PDFPilot-Store.msix` and `releases\PDFPilot-Setup.exe`. For a local unsigned dry run only, use:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate_release.ps1 -AllowUnsigned
```

See `docs\RELEASE_TESTING.md` for the clean Windows 10 and Windows 11 VM checklist.
