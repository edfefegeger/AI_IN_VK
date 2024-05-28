# widget.py
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
from ui_form import Ui_Widget
import sys
import subprocess

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.on_start_button_clicked)

    def on_start_button_clicked(self):
        subprocess.Popen(["python", "main.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
