from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
)

from ui.sidebar import Sidebar
from ui.workspace import Workspace


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Copy Motion v8.0")
        self.resize(1400, 800)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar()
        self.workspace = Workspace()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.workspace)

        # ==========================
        # Kết nối các nút Sidebar
        # ==========================

        self.sidebar.create.clicked.connect(
            self.workspace.import_image
        )

        self.sidebar.remove_bg_btn.clicked.connect(
            self.workspace.remove_background
        )