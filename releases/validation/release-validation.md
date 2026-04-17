# PDFPilot Release Validation Report

- Created UTC: 2026-04-17T20:08:37.1834753Z
- Overall status: failed
- Unsigned artifacts allowed: False

## Artifacts

### msix

- Path: `C:\Users\adity\pdf-tool\releases\PDFPilot-Store.msix`
- Bytes: 157421950
- SHA256: `D813BDBAAD5F5D1CD907C32E80B2904AE927DBEE600AB3B2D441D70D7262DB41`
- Signature: NotSigned
- Signer: 

### installer

- Path: `C:\Users\adity\pdf-tool\releases\PDFPilot-Setup.exe`
- Bytes: 539212716
- SHA256: `7CBBB1378F32311D570664A706CF6A01C4EB87CAB1B81AEE9F83A0F2A776519E`
- Signature: NotSigned
- Signer: 

## Checks

| Check | Status | Message |
| --- | --- | --- |
| production_signatures | failed | Both release artifacts must have valid production signatures unless -AllowUnsigned is supplied. |
| unit_tests | passed | C:\Users\adity\pdf-tool\.venv\Scripts\python.exe -m unittest discover -s tests |
| functional_smoke | passed | C:\Users\adity\pdf-tool\.venv\Scripts\python.exe scripts\release_functional_smoke.py --output-root C:\Users\adity\pdf-tool\releases\validation\functional --json-report C:\Users\adity\pdf-tool\releases\validation\functional-smoke.json --markdown-report C:\Users\adity\pdf-tool\releases\validation\functional-smoke.md |
| msix_manifest_identity | passed | MSIX package identity name is PDFPilot. |
| msix_manifest_version | passed | MSIX version uses four-part package version format. |
| msix_manifest_architecture | passed | MSIX architecture is x64. |
| msix_manifest_executable | passed | MSIX executable points at app\PDFPilot.exe. |
| msix_manifest_full_trust | passed | MSIX declares full-trust desktop app capability. |
| msix_store_assets | passed | MSIX contains required Store visual assets. |
| msix_excludes_bundled_libraries | passed | Store package excludes bundled LibreOffice and Tesseract payloads. |
| msix_excludes_incompatible_docx_template | passed | MSIX excludes python-docx exploded template files that makeappx rejects. |
| installer_desktop_build_root_exists | passed | Desktop build root exists for installer payload validation. |
| installer_contains_app_exe | passed | Desktop installer payload contains PDFPilot.exe. |
| installer_contains_bundled_libreoffice | passed | Desktop installer payload includes bundled LibreOffice renderer. |
| installer_admin_privileges | passed | Installer requires admin privileges as expected. |
| installer_shortcuts_configured | passed | Installer defines Start menu and optional desktop shortcuts. |
| installer_uninstall_cleanup_configured | passed | Installer has uninstall cleanup for app directory. |

## VM Validation

Complete the clean-machine checklist in `docs\RELEASE_TESTING.md` before release. This local report is not a substitute for Windows 10 and Windows 11 VM validation.
