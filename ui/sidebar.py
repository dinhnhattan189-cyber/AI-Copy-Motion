from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
)


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(240)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        logo = QLabel("AI Copy Motion")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:white;
            padding:15px;
        """)

        layout.addWidget(logo)

        self.dashboard = QPushButton("🏠 Dashboard")
        self.create = QPushButton("🎬 Create Video")
        self.projects = QPushButton("📁 Projects")
        self.history = QPushButton("🕘 History")
        self.settings = QPushButton("⚙ Settings")

        buttons = [
            self.dashboard,
            self.create,
            self.projects,
            self.history,
            self.settings,
        ]

        for b in buttons:
            b.setCursor(Qt.PointingHandCursor)
            b.setMinimumHeight(50)
            b.setStyleSheet("""
                QPushButton{
                    background:#2b2b2b;
                    color:white;
                    border:none;
                    border-radius:10px;
                    text-align:left;
                    padding-left:20px;
                    font-size:15px;
                }

                QPushButton:hover{
                    background:#3b82f6;
                }
            """)
            layout.addWidget(b)

        layout.addStretch()

        self.setStyleSheet("""
            background:#1e1e1e;
        """)