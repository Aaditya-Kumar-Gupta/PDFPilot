from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from pdf_toolkit.utils.paths import log_file_path


LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging() -> None:
    log_path = log_file_path()
    root = logging.getLogger()
    if root.handlers:
        return

    root.setLevel(logging.INFO)
    formatter = logging.Formatter(LOG_FORMAT)

    file_handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)


def clear_log_file() -> None:
    log_path = log_file_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    root = logging.getLogger()
    for handler in root.handlers:
        base_name = getattr(handler, "baseFilename", "")
        if base_name and base_name == str(log_path):
            handler.flush()
            stream = getattr(handler, "stream", None)
            if stream is not None:
                stream.seek(0)
                stream.truncate()
                stream.flush()
                return
    log_path.write_text("", encoding="utf-8")
