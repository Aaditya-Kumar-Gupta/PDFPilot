from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from pdf_toolkit.settings import AppSettings, MAX_RECENT_FILES, SettingsManager
from pdf_toolkit.ui.components.file_picker_row import FilePickerRow
from pdf_toolkit.utils.dependencies import office_renderer_status, tesseract_status
from pdf_toolkit.utils.logging_config import clear_log_file
from pdf_toolkit.utils.paths import log_file_path, settings_file_path, temp_dir
from pdf_toolkit.utils.release import release_flavor


class SettingsPage(QWidget):
    settings_changed = Signal()
    theme_changed = Signal(str)

    def __init__(self, settings_manager: SettingsManager, parent=None) -> None:
        super().__init__(parent)
        self.settings_manager = settings_manager

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        outer.addWidget(scroll)

        host = QWidget()
        self.root_layout = QVBoxLayout(host)
        self.root_layout.setContentsMargins(28, 28, 28, 28)
        self.root_layout.setSpacing(16)
        scroll.setWidget(host)

        eyebrow = QLabel("Preferences")
        eyebrow.setProperty("role", "eyebrow")
        self.root_layout.addWidget(eyebrow)

        title = QLabel("Settings")
        title.setProperty("role", "title")
        self.root_layout.addWidget(title)

        subtitle = QLabel(
            "Personalize the offline workspace, choose default paths, and control the local-only history stored on this device."
        )
        subtitle.setWordWrap(True)
        subtitle.setProperty("role", "subtitle")
        self.root_layout.addWidget(subtitle)

        self.theme_combo = QComboBox()
        self.theme_combo.addItem("Auto", "auto")
        self.theme_combo.addItem("Light", "light")
        self.theme_combo.addItem("Dark", "dark")
        self.theme_combo.currentIndexChanged.connect(self._on_theme_changed)
        self.root_layout.addWidget(self._form_section("Appearance", "Choose how the app should render on startup and while it is running.", [
            ("Theme", self.theme_combo),
        ]))

        self.default_output_picker = FilePickerRow("Leave empty to use the input file folder", directory=True)
        self.default_output_picker.browse_title = "Choose default output folder"
        self.default_output_picker.changed.connect(self._on_default_output_changed)
        self.remember_paths_checkbox = QCheckBox("Remember last-used input and output folders")
        self.remember_paths_checkbox.toggled.connect(self._on_remember_paths_changed)
        self.last_input_label = QLabel()
        self.last_input_label.setProperty("role", "subtitle")
        self.last_output_label = QLabel()
        self.last_output_label.setProperty("role", "subtitle")
        self.root_layout.addWidget(
            self._form_section(
                "Defaults",
                "Set a fallback output folder and control whether the app remembers your last-used locations.",
                [
                    ("Default output folder", self.default_output_picker),
                    ("Remember paths", self.remember_paths_checkbox),
                    ("Last input folder", self.last_input_label),
                    ("Last output folder", self.last_output_label),
                ],
            )
        )

        self.libreoffice_picker = FilePickerRow("Folder containing soffice.exe", directory=True)
        self.libreoffice_picker.browse_title = "Choose LibreOffice folder"
        self.libreoffice_picker.changed.connect(self._on_libreoffice_changed)
        self.tesseract_picker = FilePickerRow("Path to tesseract.exe or Tesseract-OCR folder", directory=False)
        self.tesseract_picker.browse_title = "Choose tesseract executable"
        self.tesseract_picker.changed.connect(self._on_tesseract_changed)
        self.libreoffice_status_label = QLabel()
        self.libreoffice_status_label.setWordWrap(True)
        self.libreoffice_status_label.setProperty("role", "subtitle")
        self.tesseract_status_label = QLabel()
        self.tesseract_status_label.setWordWrap(True)
        self.tesseract_status_label.setProperty("role", "subtitle")
        libreoffice_reset = QPushButton("Reset LibreOffice override")
        libreoffice_reset.clicked.connect(self._reset_libreoffice_override)
        tesseract_reset = QPushButton("Reset Tesseract override")
        tesseract_reset.clicked.connect(self._reset_tesseract_override)
        deps_section = self._section_frame("Dependencies", "Auto-detect local tools and override paths only when you need to.")
        deps_layout = deps_section.layout()
        deps_layout.addWidget(self._field_row("LibreOffice folder", self.libreoffice_picker))
        deps_layout.addWidget(self.libreoffice_status_label)
        deps_layout.addWidget(libreoffice_reset, 0)
        deps_layout.addSpacing(8)
        deps_layout.addWidget(self._field_row("Tesseract path", self.tesseract_picker))
        deps_layout.addWidget(self.tesseract_status_label)
        deps_layout.addWidget(tesseract_reset, 0)
        self.root_layout.addWidget(deps_section)

        self.remember_recent_checkbox = QCheckBox(f"Remember up to {MAX_RECENT_FILES} recent files on this device")
        self.remember_recent_checkbox.toggled.connect(self._on_remember_recent_changed)
        self.recent_count_label = QLabel()
        self.recent_count_label.setProperty("role", "subtitle")
        self.recent_list = QListWidget()
        self.recent_list.setMaximumHeight(200)
        clear_recent_button = QPushButton("Clear recent files")
        clear_recent_button.clicked.connect(self._clear_recent_files)
        clear_logs_button = QPushButton("Clear logs")
        clear_logs_button.clicked.connect(self._clear_logs)
        privacy_section = self._section_frame("Privacy", "Everything stays local. You can decide whether the app remembers file history and path history.")
        privacy_layout = privacy_section.layout()
        privacy_layout.addWidget(self.remember_recent_checkbox)
        privacy_layout.addWidget(self.recent_count_label)
        privacy_layout.addWidget(self.recent_list)
        self.storage_summary_label = QLabel()
        self.storage_summary_label.setWordWrap(True)
        self.storage_summary_label.setProperty("role", "subtitle")
        privacy_layout.addWidget(self.storage_summary_label)
        actions = QHBoxLayout()
        actions.addWidget(clear_recent_button)
        actions.addWidget(clear_logs_button)
        actions.addStretch(1)
        privacy_layout.addLayout(actions)
        self.root_layout.addWidget(privacy_section)
        self.root_layout.addStretch(1)

        self.refresh()

    def refresh(self) -> None:
        settings = self.settings_manager.load()
        self._set_theme_value(settings.theme)
        for widget in (
            self.default_output_picker.line_edit,
            self.remember_paths_checkbox,
            self.libreoffice_picker.line_edit,
            self.tesseract_picker.line_edit,
            self.remember_recent_checkbox,
        ):
            widget.blockSignals(True)
        self.default_output_picker.line_edit.setText(settings.default_output_dir)
        self.remember_paths_checkbox.setChecked(settings.remember_last_used_paths)
        self.libreoffice_picker.line_edit.setText(settings.libreoffice_override)
        self.tesseract_picker.line_edit.setText(settings.tesseract_override)
        self.remember_recent_checkbox.setChecked(settings.remember_recent_files)
        for widget in (
            self.default_output_picker.line_edit,
            self.remember_paths_checkbox,
            self.libreoffice_picker.line_edit,
            self.tesseract_picker.line_edit,
            self.remember_recent_checkbox,
        ):
            widget.blockSignals(False)
        self._update_path_labels(settings)
        self._update_recent_files(settings)
        self._update_storage_summary()
        self._refresh_dependency_status()

    def _section_frame(self, title: str, description: str) -> QFrame:
        frame = QFrame()
        frame.setObjectName("surface")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        heading = QLabel(title)
        heading.setProperty("role", "sectionTitle")
        layout.addWidget(heading)
        subtitle = QLabel(description)
        subtitle.setWordWrap(True)
        subtitle.setProperty("role", "subtitle")
        layout.addWidget(subtitle)
        return frame

    def _form_section(self, title: str, description: str, rows: list[tuple[str, QWidget]]) -> QFrame:
        frame = self._section_frame(title, description)
        layout = frame.layout()
        for label, widget in rows:
            layout.addWidget(self._field_row(label, widget))
        return frame

    def _field_row(self, label: str, widget: QWidget) -> QWidget:
        host = QWidget()
        layout = QVBoxLayout(host)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        title = QLabel(label)
        title.setProperty("role", "eyebrow")
        layout.addWidget(title)
        layout.addWidget(widget)
        return host

    def _set_theme_value(self, theme: str) -> None:
        index = self.theme_combo.findData(theme)
        self.theme_combo.blockSignals(True)
        self.theme_combo.setCurrentIndex(index if index >= 0 else 0)
        self.theme_combo.blockSignals(False)

    def _on_theme_changed(self) -> None:
        theme = str(self.theme_combo.currentData())
        self.settings_manager.update(theme=theme)
        self.theme_changed.emit(theme)
        self.settings_changed.emit()

    def _on_default_output_changed(self, value: str) -> None:
        self.settings_manager.update(default_output_dir=value.strip())
        self.settings_changed.emit()

    def _on_remember_paths_changed(self, checked: bool) -> None:
        settings = self.settings_manager.update(remember_last_used_paths=checked)
        if not checked:
            settings = self.settings_manager.clear_last_used_paths()
        self._update_path_labels(settings)
        self.settings_changed.emit()

    def _on_libreoffice_changed(self, value: str) -> None:
        self.settings_manager.update(libreoffice_override=value.strip())
        self._refresh_dependency_status()
        self.settings_changed.emit()

    def _on_tesseract_changed(self, value: str) -> None:
        self.settings_manager.update(tesseract_override=value.strip())
        self._refresh_dependency_status()
        self.settings_changed.emit()

    def _on_remember_recent_changed(self, checked: bool) -> None:
        settings = self.settings_manager.update(remember_recent_files=checked)
        if not checked:
            settings = self.settings_manager.clear_recent_files()
        self._update_recent_files(settings)
        self.settings_changed.emit()

    def _reset_libreoffice_override(self) -> None:
        self.libreoffice_picker.line_edit.setText("")
        self.settings_manager.update(libreoffice_override="")
        self._refresh_dependency_status()
        self.settings_changed.emit()

    def _reset_tesseract_override(self) -> None:
        self.tesseract_picker.line_edit.setText("")
        self.settings_manager.update(tesseract_override="")
        self._refresh_dependency_status()
        self.settings_changed.emit()

    def _clear_recent_files(self) -> None:
        settings = self.settings_manager.clear_recent_files()
        self._update_recent_files(settings)
        self.settings_changed.emit()

    def _clear_logs(self) -> None:
        clear_log_file()
        QMessageBox.information(self, "PDFPilot", "App logs were cleared.")

    def _refresh_dependency_status(self) -> None:
        libreoffice = office_renderer_status()
        tesseract = tesseract_status()
        self.libreoffice_status_label.setText(f"{libreoffice.summary}\n{libreoffice.details}")
        self.tesseract_status_label.setText(f"{tesseract.summary}\n{tesseract.details}")

    def _update_recent_files(self, settings: AppSettings) -> None:
        self.recent_count_label.setText(f"{len(settings.recent_files)} recent file(s) stored locally")
        self.recent_list.clear()
        self.recent_list.addItems(settings.recent_files)
        self.recent_list.setEnabled(settings.remember_recent_files)

    def _update_path_labels(self, settings: AppSettings) -> None:
        self.last_input_label.setText(settings.last_input_dir or "Not stored")
        self.last_output_label.setText(settings.last_output_dir or "Not stored")

    def _update_storage_summary(self) -> None:
        self.storage_summary_label.setText(
            "Release flavor: "
            f"{release_flavor()}\n"
            f"Settings: {settings_file_path()}\n"
            f"Logs: {log_file_path()}\n"
            f"Temporary files: {temp_dir()}"
        )
