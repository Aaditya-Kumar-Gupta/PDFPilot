from __future__ import annotations

import os
import shutil
from pathlib import Path

from pdf_toolkit.models import DependencyStatus
from pdf_toolkit.settings import get_settings_manager
from pdf_toolkit.utils.paths import runtime_root
from pdf_toolkit.utils.release import is_store_release, bundled_tesseract_enabled
from pdf_toolkit.utils.renderer import resolve_office_renderer


def detect_binary(binary_name: str, label: str) -> DependencyStatus:
    path = shutil.which(binary_name)
    if path:
        return DependencyStatus(True, f"{label} available", path)
    return DependencyStatus(False, f"{label} not found", f"Install {label} locally and add it to PATH.")


def _normalize_tesseract_candidate(raw_path: str | Path | None) -> Path | None:
    if not raw_path:
        return None
    candidate = Path(raw_path).expanduser()
    if candidate.is_dir():
        candidate = candidate / "tesseract.exe"
    return candidate if candidate.exists() else None


def _common_tesseract_locations() -> list[Path]:
    candidates: list[Path] = []
    for env_name in ("PDFPILOT_TESSERACT_PATH", "TESSERACT_PATH"):
        raw_value = os.environ.get(env_name, "").strip()
        if raw_value:
            candidates.append(Path(raw_value).expanduser())
    if bundled_tesseract_enabled():
        candidates.append(runtime_root() / "vendor" / "tesseract" / "tesseract.exe")
    candidates.extend(
        [
            Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Tesseract-OCR" / "tesseract.exe",
            Path(os.environ.get("ProgramFiles", "")) / "Tesseract-OCR" / "tesseract.exe",
            Path(os.environ.get("ProgramFiles(x86)", "")) / "Tesseract-OCR" / "tesseract.exe",
            Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
            Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
        ]
    )
    resolved: list[Path] = []
    for candidate in candidates:
        normalized = _normalize_tesseract_candidate(candidate)
        if normalized is not None and normalized not in resolved:
            resolved.append(normalized)
    return resolved


def _resolve_tesseract_installation() -> tuple[Path | None, str | None]:
    configured = get_settings_manager().load().tesseract_override.strip()
    if configured:
        candidate = _normalize_tesseract_candidate(configured)
        return candidate, "override"

    system_path = shutil.which("tesseract")
    if system_path:
        return Path(system_path), "path"

    for candidate in _common_tesseract_locations():
        return candidate, "common-path"
    return None, None


def resolve_tesseract_path() -> Path | None:
    path, _ = _resolve_tesseract_installation()
    return path


def tesseract_status() -> DependencyStatus:
    configured = get_settings_manager().load().tesseract_override.strip()
    if configured:
        candidate = _normalize_tesseract_candidate(configured)
        if candidate is not None:
            return DependencyStatus(True, "Tesseract OCR available", str(candidate))
        return DependencyStatus(False, "Tesseract OCR override is invalid", str(Path(configured).expanduser()))

    candidate, source = _resolve_tesseract_installation()
    if candidate is not None:
        summary = "Tesseract OCR available"
        if source == "common-path":
            summary = "Tesseract OCR auto-detected"
        return DependencyStatus(True, summary, str(candidate))
    if is_store_release():
        return DependencyStatus(
            False,
            "Tesseract OCR not bundled in Store build",
            "Install Tesseract locally, then add it to PATH or choose tesseract.exe in Settings to enable OCR.",
        )
    return DependencyStatus(
        False,
        "Tesseract OCR not found",
        "Install Tesseract locally, then add it to PATH or open Settings > Dependencies and choose "
        "tesseract.exe or the Tesseract-OCR install folder.",
    )


def libreoffice_status() -> DependencyStatus:
    resolution = resolve_office_renderer()
    if resolution.available:
        return DependencyStatus(True, "LibreOffice available", resolution.details)
    if resolution.mode == "manual-libreoffice":
        return DependencyStatus(False, "LibreOffice override is invalid", resolution.details)
    return detect_binary("soffice", "LibreOffice")


def office_renderer_status() -> DependencyStatus:
    resolution = resolve_office_renderer()
    if resolution.available:
        if resolution.mode == "manual-libreoffice":
            label = "Custom LibreOffice renderer"
        elif resolution.mode == "bundled-libreoffice":
            label = "Bundled LibreOffice renderer"
        else:
            label = "System LibreOffice renderer"
        return DependencyStatus(True, f"{label} available", resolution.details)
    if resolution.mode == "manual-libreoffice":
        return DependencyStatus(False, "Custom LibreOffice path is invalid", resolution.details)
    if is_store_release():
        return DependencyStatus(
            True,
            "Built-in fallback available",
            "Store build does not bundle LibreOffice. Install LibreOffice locally or choose a custom folder in Settings for higher-fidelity Office conversion.",
        )
    return DependencyStatus(True, "Built-in fallback available", "Formatting may differ without a bundled/system renderer.")


def always_available() -> DependencyStatus:
    return DependencyStatus(True, "Available")
