<div align="center">

<br />

<img src="assets/icon.png" alt="PDFPilot Logo" width="80" />

<br />
<br />

# Privacy Policy

**PDFPilot — by Aditya Kumar Gupta**

*Last updated: April 18, 2026*

</div>

---

## Overview

PDFPilot is a local desktop application for Windows. It is built on a single principle: **your files are yours**. No document, page, or byte of content you process with PDFPilot is ever transmitted to an external server, cloud service, or third party — because PDFPilot never makes those connections in the first place.

This policy explains exactly what PDFPilot does and does not do with your data.

---

## 1. Data We Do Not Collect

PDFPilot collects **nothing**. The following activities do not occur at any point during installation, use, or uninstallation:

| What We Do Not Collect | Details |
|---|---|
| **File content** | Your PDFs, images, Office files, and exported outputs are never read by anyone other than you |
| **Usage analytics** | No events, clicks, tool usage, or session data are recorded |
| **Crash reports** | No automatic error reporting is sent anywhere |
| **Device identifiers** | No hardware IDs, OS details, or machine fingerprints are collected |
| **Personal information** | No name, email, account, or profile is required or stored |
| **Network activity** | PDFPilot does not make outbound network requests during normal operation |

---

## 2. How Your Files Are Processed

All file processing happens **entirely on your machine**, using bundled and locally installed libraries.

- Files you open or import are read from your local disk.
- Processed output files are written back to your local disk at the path you choose.
- No temporary copies are sent to or cached by any remote system.
- Temporary files created during processing (if any) are stored in your system's local temp directory and are not accessible to any external party.

PDFPilot uses the following libraries for local processing — all open-source, all running on your machine:

| Library | Purpose |
|---|---|
| PyMuPDF · pypdf · pdfplumber | PDF reading and manipulation |
| pdf2docx | PDF to Word conversion |
| Pillow | Image processing |
| python-docx · python-pptx · openpyxl | Office file export |
| pytesseract + Tesseract OCR | Optical character recognition (local) |
| LibreOffice | Office-to-PDF conversion (local, when installed) |

---

## 3. Internet Access

PDFPilot does **not** require an internet connection and does **not** initiate any outbound network requests during normal operation.

The only scenarios in which your system may make a network request related to PDFPilot are:

- **Manual update checks** — if you choose to visit the GitHub Releases page to download an update yourself. This is a browser action you initiate, not an automatic background call from the app.
- **Optional dependency installation** — if you manually install Tesseract OCR or LibreOffice from their respective websites. PDFPilot itself does not trigger these downloads.

There are no automatic update checks, no telemetry pings, and no background services.

---

## 4. Third-Party Services

PDFPilot does not integrate with, send data to, or depend on any third-party cloud service, API, or analytics platform during operation.

Distribution channels (GitHub Releases, Microsoft Store) have their own privacy policies that apply when you visit those platforms to download PDFPilot. Those policies are independent of this one.

---

## 5. Children's Privacy

PDFPilot does not collect any data from anyone, including children. Because no personal information is gathered, there is no special handling required for users under the age of 13 (COPPA) or any other age-based data protection framework.

---

## 6. Open Source Transparency

PDFPilot is open-source software licensed under the MIT License. You can inspect every line of code that runs on your machine:

- **Source code:** [github.com/Aaditya-Kumar-Gupta/PDFPilot](https://github.com/Aaditya-Kumar-Gupta/PDFPilot)
- **Dependencies:** Listed in `requirements.txt` in the repository root
- **Build scripts:** Available in the `scripts/` directory

If you have concerns about what the application does, you are welcome and encouraged to review the source.

---

## 7. Changes to This Policy

If this policy is updated, the new version will be committed to the repository with an updated *Last updated* date at the top of this file. Because PDFPilot collects no data, changes to this policy will not affect any data previously gathered — there is none.

---

## 8. Contact

If you have questions about this privacy policy or PDFPilot's data practices, please open an issue on GitHub:

**[github.com/Aaditya-Kumar-Gupta/PDFPilot/issues](https://github.com/Aaditya-Kumar-Gupta/PDFPilot/issues)**

---

<div align="center">

*PDFPilot processes your files locally. Always has. Always will.*

<br />

**Built by [Aditya Kumar Gupta](https://github.com/Aaditya-Kumar-Gupta) · MIT License**

</div>