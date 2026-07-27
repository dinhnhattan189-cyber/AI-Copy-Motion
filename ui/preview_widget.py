from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel


class PreviewWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(700, 450)
        self.setText("Drag & Drop Image Here")

        self.setStyleSheet("""
            QLabel{
                background:#2b2b2b;
                border:2px dashed #555;
                border-radius:15px;
                color:#999;
                font-size:22px;
            }
        """)

    def show_image(self, path):
        pixmap = QPixmap(path)

        if pixmap.isNull():
            self.setText("Cannot load image")
            return

        self.setPixmap(
            pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )