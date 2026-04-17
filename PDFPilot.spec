# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path

block_cipher = None

project_root = Path.cwd()
release_flavor = os.environ.get("PDFPILOT_RELEASE_FLAVOR", "desktop").strip().lower() or "desktop"
assets = [(str(project_root / "assets"), "assets")]
style_datas = [(str(project_root / "pdf_toolkit" / "ui" / "styles"), "pdf_toolkit/ui/styles")]
bundled_renderer_root = project_root / "vendor" / "libreoffice"
include_bundled_renderer = release_flavor != "store"
vendor_datas = [(str(bundled_renderer_root), "vendor/libreoffice")] if include_bundled_renderer and bundled_renderer_root.exists() else []

a = Analysis(
    ["main.pyw"],
    pathex=[str(project_root)],
    binaries=[],
    datas=assets + style_datas + vendor_datas,
    hiddenimports=["PySide6.QtPrintSupport", "fitz", "pytesseract", "pdf2image", "docx", "pptx", "openpyxl", "pdf2docx"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="PDFPilot",
    icon=str(project_root / "assets" / "app.ico"),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="PDFPilot",
)
