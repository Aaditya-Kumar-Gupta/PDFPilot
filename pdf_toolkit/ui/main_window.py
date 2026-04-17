from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QStackedWidget, QWidget

from pdf_toolkit.models import ToolDefinition
from pdf_toolkit.registry import build_registry
from pdf_toolkit.settings import SettingsManager
from pdf_toolkit.ui.dashboard import DashboardPanel
from pdf_toolkit.ui.settings_page import SettingsPage
from pdf_toolkit.ui.sidebar import NavigationItem, SidebarNavigation
from pdf_toolkit.ui.theme import apply_app_theme
from pdf_toolkit.ui.tool_page import ToolPage


class MainWindow(QMainWindow):
    _SIDEBAR_BREAKPOINT = 1120
    _DEFAULT_WIDTH = 1480
    _DEFAULT_HEIGHT = 860
    _MIN_WIDTH = 1200
    _MIN_HEIGHT = 760

    def __init__(self, settings_manager: SettingsManager) -> None:
        super().__init__()
        self.settings_manager = settings_manager
        self.setWindowTitle("PDFPilot")
        self.resize(self._DEFAULT_WIDTH, self._DEFAULT_HEIGHT)
        self.setMinimumSize(self._MIN_WIDTH, self._MIN_HEIGHT)
        self.setAcceptDrops(True)
        self._launch_positioned = False

        self.registry = build_registry()
        self.registry_map = {item.tool_id: item for item in self.registry}
        self.active_tool: ToolDefinition | None = None
        self.active_section = "dashboard"
        self._last_library_section = "dashboard"
        self.search_query = ""

        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(14, 14, 14, 14)
        root.setSpacing(14)

        self.sidebar = SidebarNavigation(self._navigation_items(), initial_collapsed=True)
        self.sidebar.section_changed.connect(self.set_section)
        root.addWidget(self.sidebar)

        self.content_stack = QStackedWidget()
        self.dashboard = DashboardPanel()
        self.dashboard.bind_definitions(self.registry)
        self.dashboard.tool_selected.connect(self.activate_tool)
        self.dashboard.search_changed.connect(self.set_search_query)
        self.settings_page = self._build_settings_page()
        self.tool_page = ToolPage(self.settings_manager, self)
        self.tool_page.back_requested.connect(self.show_library)
        self.content_stack.addWidget(self.dashboard)
        self.content_stack.addWidget(self.settings_page)
        self.content_stack.addWidget(self.tool_page)
        root.addWidget(self.content_stack, 1)

        self._setup_shortcuts()
        self.sidebar.set_active(self.active_section)
        self.refresh_cards()
        QTimer.singleShot(0, self._center_on_screen)

    def _navigation_items(self) -> list[NavigationItem]:
        return [
            NavigationItem("dashboard", "Dashboard", "merge"),
            NavigationItem("Organize PDF", "Organize PDF", "organize"),
            NavigationItem("Optimize PDF", "Optimize PDF", "compress"),
            NavigationItem("Convert to PDF", "Convert to PDF", "office"),
            NavigationItem("Convert from PDF", "Convert from PDF", "export"),
            NavigationItem("Edit PDF", "Edit PDF", "annotate"),
            NavigationItem("PDF Security", "PDF Security", "protect"),
            NavigationItem("settings", "Settings", "repair"),
        ]

    def _build_settings_page(self) -> QWidget:
        page = SettingsPage(self.settings_manager, self)
        page.settings_changed.connect(self._refresh_after_settings_change)
        page.theme_changed.connect(self._apply_theme)
        return page

    def _setup_shortcuts(self) -> None:
        QShortcut(QKeySequence("Ctrl+K"), self, activated=self.dashboard.search_bar.setFocus)
        QShortcut(QKeySequence("Ctrl+B"), self, activated=lambda: self.sidebar.set_collapsed(not self.sidebar.is_collapsed()))

    def set_section(self, section_id: str) -> None:
        self.active_section = section_id
        if section_id != "settings":
            self._last_library_section = section_id
        self.sidebar.set_active(section_id)
        self.content_stack.setCurrentWidget(self.settings_page if section_id == "settings" else self.dashboard)
        if section_id == "settings" and isinstance(self.settings_page, SettingsPage):
            self.settings_page.refresh()
        self.refresh_cards()

    def set_search_query(self, value: str) -> None:
        self.search_query = value.strip().lower()
        self.refresh_cards()

    def refresh_cards(self) -> None:
        if self.active_section == "settings":
            return
        context_label = "Dashboard" if self.active_section == "dashboard" else self.active_section
        definitions = []
        for definition in self.registry:
            if self.active_section not in {"dashboard", definition.category}:
                continue
            haystack = " ".join(
                [definition.title.lower(), definition.description.lower(), " ".join(keyword.lower() for keyword in definition.keywords)]
            )
            if self.search_query and self.search_query not in haystack:
                continue
            definitions.append(definition)
        self.dashboard.set_cards(definitions, context_label)
        self.dashboard.set_active_tool(self.active_tool.tool_id if self.active_tool else None)

    def activate_tool(self, tool_id: str) -> None:
        definition = self.registry_map[tool_id]
        self.active_tool = definition
        self.dashboard.set_active_tool(tool_id)
        if self.active_section != "settings":
            self._last_library_section = self.active_section
        self.tool_page.set_tool(definition)
        self.content_stack.setCurrentWidget(self.tool_page)

    def show_library(self) -> None:
        section_id = self._last_library_section or "dashboard"
        self.active_section = section_id
        self.sidebar.set_active(section_id)
        self.content_stack.setCurrentWidget(self.dashboard)
        self.refresh_cards()
    def resizeEvent(self, event) -> None:  # noqa: N802
        super().resizeEvent(event)

    def showEvent(self, event) -> None:  # noqa: N802
        super().showEvent(event)
        if not self._launch_positioned:
            self._center_on_screen()
            self._launch_positioned = True

    def _center_on_screen(self) -> None:
        screen = self.screen()
        if screen is None:
            return
        available = screen.availableGeometry()
        target_width = min(self._DEFAULT_WIDTH, max(self._MIN_WIDTH, available.width() - 140))
        target_height = min(self._DEFAULT_HEIGHT, max(self._MIN_HEIGHT, available.height() - 140))
        self.resize(target_width, target_height)
        frame = self.frameGeometry()
        frame.moveCenter(available.center())
        self.move(frame.topLeft())

    def _refresh_after_settings_change(self) -> None:
        self.tool_page.refresh_settings()
        self.dashboard.bind_definitions(self.registry)
        self.refresh_cards()

    def _apply_theme(self, theme: str) -> None:
        app = QApplication.instance()
        if app is not None:
            apply_app_theme(app, theme)
