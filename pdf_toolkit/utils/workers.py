from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, Signal

from pdf_toolkit.models import MissingDependencyError, ToolContext, ToolDefinition, ToolError


LOGGER = logging.getLogger(__name__)


class JobSignals(QObject):
    started = Signal(str)
    progress = Signal(int, str)
    finished = Signal(object)
    failed = Signal(str)


class JobWorker(QRunnable):
    def __init__(self, definition: ToolDefinition, input_files: list[Path], output_path: Path, options: dict[str, Any]) -> None:
        super().__init__()
        self.definition = definition
        self.input_files = input_files
        self.output_path = output_path
        self.options = options
        self.signals = JobSignals()
        self._cancelled = False
        self.setAutoDelete(True)

    def cancel(self) -> None:
        self._cancelled = True

    def run(self) -> None:
        self.signals.started.emit(self.definition.title)
        try:
            context = ToolContext(
                input_files=self.input_files,
                output_path=self.output_path,
                options=self.options,
                progress=lambda value, message: self.signals.progress.emit(value, message),
                is_cancelled=lambda: self._cancelled,
            )
            result = self.definition.executor(context)
            self.signals.finished.emit(result)
        except Exception as exc:  # pragma: no cover
            LOGGER.exception("Job failed")
            if isinstance(exc, (ToolError, MissingDependencyError)):
                message = str(exc)
            else:
                message = f"{exc}"
            self.signals.failed.emit(message)


class JobRunner(QObject):
    job_started = Signal(str)
    job_progress = Signal(int, str)
    job_finished = Signal(object)
    job_failed = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._pool = QThreadPool.globalInstance()
        self._pool.setExpiryTimeout(-1)
        self._active_worker: JobWorker | None = None

    def run_tool(self, definition: ToolDefinition, input_files: list[Path], output_path: Path, options: dict[str, Any]) -> None:
        worker = JobWorker(definition, input_files, output_path, options)
        worker.signals.started.connect(self.job_started, Qt.ConnectionType.QueuedConnection)
        worker.signals.progress.connect(self.job_progress, Qt.ConnectionType.QueuedConnection)
        worker.signals.finished.connect(self.job_finished, Qt.ConnectionType.QueuedConnection)
        worker.signals.failed.connect(self.job_failed, Qt.ConnectionType.QueuedConnection)
        self._active_worker = worker
        self._pool.start(worker)

    def cancel_active(self) -> None:
        if self._active_worker is not None:
            self._active_worker.cancel()
