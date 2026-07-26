from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)


class Workspace(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        title = QLabel("Create AI Motion Video")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:white;
        """)

        layout.addWidget(title)

        # ===== Preview =====
        preview = QFrame()
        preview.setMinimumHeight(400)
        preview.setStyleSheet("""
            QFrame{
                background:#2b2b2b;
                border:2px dashed #555;
                border-radius:15px;
            }
        """)

        preview_layout = QVBoxLayout(preview)

        text = QLabel("Drag & Drop Image Here")
        text.setAlignment(Qt.AlignCenter)
        text.setStyleSheet("""
            color:#999;
            font-size:22px;
        """)

        preview_layout.addWidget(text)

        layout.addWidget(preview)

        # ===== Buttons =====

        row = QHBoxLayout()

        self.btnImage = QPushButton("📷 Character")
        self.btnVideo = QPushButton("🎥 Motion")
        self.btnBg = QPushButton("🖼 Background")

        for b in [self.btnImage, self.btnVideo, self.btnBg]:

            b.setMinimumHeight(50)

            b.setStyleSheet("""
                QPushButton{
                    background:#3b82f6;
                    color:white;
                    border:none;
                    border-radius:10px;
                    font-size:15px;
                }

                QPushButton:hover{
                    background:#2563eb;
                }
            """)

            row.addWidget(b)

        layout.addLayout(row)

        self.btnGenerate = QPushButton("Generate Video")

        self.btnGenerate.setMinimumHeight(60)

        self.btnGenerate.setStyleSheet("""
            QPushButton{
                background:#10b981;
                color:white;
                border:none;
                border-radius:12px;
                font-size:18px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#059669;
            }
        """)

        layout.addWidget(self.btnGenerate)

        self.setStyleSheet("""
            background:#181818;
        """)