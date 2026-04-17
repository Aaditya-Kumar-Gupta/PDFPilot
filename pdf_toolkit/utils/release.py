from __future__ import annotations

import os


DEFAULT_RELEASE_FLAVOR = "desktop"
RELEASE_FLAVOR_ENV = "PDFPILOT_RELEASE_FLAVOR"
VALID_RELEASE_FLAVORS = {"desktop", "store"}


def release_flavor() -> str:
    value = os.environ.get(RELEASE_FLAVOR_ENV, DEFAULT_RELEASE_FLAVOR).strip().lower()
    if value in VALID_RELEASE_FLAVORS:
        return value
    return DEFAULT_RELEASE_FLAVOR


def is_store_release() -> bool:
    return release_flavor() == "store"


def bundled_renderer_enabled() -> bool:
    return not is_store_release()


def bundled_tesseract_enabled() -> bool:
    return not is_store_release()
