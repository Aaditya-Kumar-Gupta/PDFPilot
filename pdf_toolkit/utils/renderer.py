from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from pdf_toolkit.settings import get_settings_manager
from pdf_toolkit.utils.paths import bundled_renderer_dir
from pdf_toolkit.utils.release import bundled_renderer_enabled


@dataclass(slots=True)
class RendererResolution:
    available: bool
    mode: str
    soffice_path: Path | None = None
    details: str = ""


def _candidate_paths(root: Path) -> list[Path]:
    return [
        root / "program" / "soffice.exe",
        root / "soffice.exe",
        root / "program" / "soffice.com",
        root / "soffice.com",
    ]


def _prefer_gui_soffice(candidate: Path) -> Path:
    if candidate.suffix.lower() != ".com":
        return candidate
    gui_candidate = candidate.with_suffix(".exe")
    return gui_candidate if gui_candidate.exists() else candidate


def _configured_override() -> Path | None:
    configured = get_settings_manager().load().libreoffice_override.strip()
    if not configured:
        return None
    return Path(configured).expanduser()


def resolve_office_renderer() -> RendererResolution:
    override = _configured_override()
    if override is not None:
        for candidate in _candidate_paths(override):
            if candidate.exists():
                return RendererResolution(
                    available=True,
                    mode="manual-libreoffice",
                    soffice_path=candidate,
                    details=str(candidate),
                )
        return RendererResolution(
            available=False,
            mode="manual-libreoffice",
                soffice_path=None,
                details=f"Configured LibreOffice path is invalid: {override}",
        )

    if bundled_renderer_enabled():
        bundled_root = bundled_renderer_dir()
        for candidate in _candidate_paths(bundled_root):
            if candidate.exists():
                return RendererResolution(
                    available=True,
                    mode="bundled-libreoffice",
                    soffice_path=candidate,
                    details=str(candidate),
                )

    system_path = shutil.which("soffice")
    if system_path:
        preferred = _prefer_gui_soffice(Path(system_path))
        return RendererResolution(
            available=True,
            mode="system-libreoffice",
            soffice_path=preferred,
            details=str(preferred),
        )

    return RendererResolution(
        available=False,
        mode="builtin-fallback",
        soffice_path=None,
        details="No bundled or system LibreOffice renderer found.",
    )
