# PDFPilot Functional Smoke Report

- Created UTC: 2026-04-17T20:08:36.779134+00:00
- Fixture root: `C:\Users\adity\pdf-tool\runtime_tests`
- Output root: `C:\Users\adity\pdf-tool\releases\validation\functional`
- Office renderer: bundled-libreoffice (C:\Users\adity\pdf-tool\vendor\libreoffice\program\soffice.exe)
- Tesseract: Tesseract OCR auto-detected (C:\Program Files\Tesseract-OCR\tesseract.exe)
- Status: passed

## Cases

| Case | Status | Notes |
| --- | --- | --- |
| merge_pdf | passed | pdf |
| split_pdf | passed | pdf |
| remove_pages | passed | pdf |
| organize_pdf | passed | pdf |
| rotate_pdf | passed | pdf |
| compress_pdf | passed | pdf |
| repair_pdf | passed | pdf |
| image_to_pdf | passed | pdf |
| scan_to_pdf | passed | pdf |
| pdf_to_jpg | passed |  |
| pdf_to_word | passed | docx |
| pdf_to_powerpoint | passed | pptx |
| pdf_to_excel | passed | xlsx |
| pdf_to_pdfa | passed | pdf |
| page_numbers | passed | pdf |
| watermark | passed | pdf |
| annotate_pdf | passed | pdf |
| crop_pdf | passed | pdf |
| protect_pdf | passed | pdf |
| unlock_pdf | passed | pdf |
| sign_pdf | passed | pdf |
| compare_pdf | passed | txt |
| redact_pdf | passed | pdf |
| office_to_pdf_word | passed | pdf |
| office_to_pdf_powerpoint | passed | pdf |
| office_to_pdf_excel | passed | pdf |
| office_to_pdf_csv | passed | pdf |
| invalid_empty_selection | passed | Please choose at least one input file. |
| invalid_page_range | passed | No valid page selection was provided. |
| invalid_wrong_password | passed | Incorrect PDF password. |
| cancelled_operation | passed | Operation cancelled. |
| encrypted_pdfa_rejected | passed | PDF to PDF/A cannot process encrypted PDFs. Unlock the PDF first. |
