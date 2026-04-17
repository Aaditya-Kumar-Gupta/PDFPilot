# Microsoft Store Submission Checklist

## Identity and Signing

- Create or reserve the app in Partner Center before your production submission.
- Replace the placeholder publisher in `scripts/build_release.ps1` / `scripts/build_msix.ps1` with the exact Partner Center publisher subject.
- Keep the MSIX identity `Name`, `Publisher`, and version aligned with the Partner Center record.
- For local sideload testing, sign the MSIX with a trusted `.pfx` certificate using `-CertificatePath` and `-CertificatePassword`.

## Packaging Inputs

- Build the `store` flavor so the package stays lean and avoids bundled heavy dependencies.
- Confirm the Store visual assets under `packaging/msix/assets/` look acceptable; the generator produces placeholders, not final marketing art.
- Verify `packaging/msix/AppxManifest.template.xml` values before submission.

## Validation

- Install the generated `.msix` on a clean Windows VM.
- Launch the app from Start menu.
- Confirm settings, logs, and temp files are written under the user's app data path.
- Confirm Office conversion falls back cleanly when LibreOffice is not installed.
- Confirm OCR clearly reports its prerequisite state when Tesseract is not installed.

## Store Listing Readiness

- Prepare screenshots for the Store listing.
- Prepare privacy/support/store description text.
- Verify version increments on every submission.
- Keep the app icon and Store logos consistent with the listing branding.
