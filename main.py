import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QFrame,
    QPushButton,
    QTextEdit,
    QFileDialog,
)
from PyQt5.QtCore import Qt
from capturer import Capture
from PIL import Image
from pytesseract import pytesseract


class ScreenRegionSelector(QMainWindow):

    def __init__(self):
        super().__init__(None)
        self.m_width = 400
        self.m_height = 500

        self.setWindowTitle("Screen Capturer")
        self.setMinimumSize(self.m_width, self.m_height)

        frame = QFrame()
        frame.setContentsMargins(0, 0, 0, 0)
        lay = QVBoxLayout(frame)
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(5, 5, 5, 5)

        self.label = QLabel()
        self.btn_capture = QPushButton("Capture")
        self.btn_capture.clicked.connect(self.capture)

        self.btn_save = QPushButton("Save")
        self.btn_save.clicked.connect(self.save)
        self.btn_save.setVisible(False)

        self.btn_extract = QPushButton("Extract")
        self.btn_extract.clicked.connect(self.extract_text)
        self.btn_extract.setVisible(False)

        self.text_edit = QTextEdit()
        self.text_edit.setMinimumSize(350, 200)
        self.text_edit.setVisible(False)

        lay.addWidget(self.label)
        lay.addWidget(self.btn_capture)
        lay.addWidget(self.btn_save)
        lay.addWidget(self.btn_extract)
        lay.addWidget(self.text_edit)

        self.setCentralWidget(frame)

    def capture(self):
        self.capturer = Capture(self)
        self.capturer.show()
        self.btn_save.setVisible(True)
        self.btn_extract.setVisible(True)

    def save(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "Image files (*.png *.jpg *.bmp)")
        if file_name:
            self.capturer.imgmap.save(file_name)

    def extract_text(self):
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = r"test.png"

        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)

        self.text_edit.setText(text[:-1])
        self.text_edit.setVisible(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QFrame {
        background-color: #ffffff;
    }
                      
    QPushButton {
        border-radius: 5px;
        background-color: rgb(60, 90, 255);
        padding: 10px;
        color: white;
        font-weight: bold;
        font-family: Arial;
        font-size: 12px;
    }
                      
    QPushButton::hover {
        background-color: rgb(60, 20, 255)
    }
    """)
    selector = ScreenRegionSelector()
    selector.show()
    sys.exit(app.exec_())
