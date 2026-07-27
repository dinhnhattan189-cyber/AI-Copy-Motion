from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
)

from ui.preview_widget import PreviewWidget


class Workspace(QWidget):
    def __init__(self):
        super().__init__()

        self.current_image = None

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

        self.preview_widget = PreviewWidget()
        layout.addWidget(self.preview_widget)

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

        # ===== Signals =====

        self.btnImage.clicked.connect(self.import_image)

    # ======================================================

    def import_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.webp)"
        )

        if not file_name:
            return

        self.current_image = file_name

        self.preview_widget.show_image(file_name)

    # ======================================================

    def remove_background(self):
        if self.current_image is None:
            print("Chưa chọn ảnh.")
            return

        print("Remove background:", self.current_image)