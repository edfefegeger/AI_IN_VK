import sys
import subprocess
import psutil
from PySide6.QtWidgets import QApplication, QWidget, QDialog
from ui_form import Ui_Widget
from ui_about import Ui_Form  
from logger import log_and_print

class AboutForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Информация о программе")

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Главное меню")  

        self.process = None


        self.ui.pushButton.clicked.connect(self.show_about_form)  
        self.ui.pushButton_2.clicked.connect(self.on_start_button_clicked)  # Запустить main.py
        self.ui.pushButton_3.clicked.connect(self.on_pause_button_clicked)  
        self.ui.pushButton_4.clicked.connect(self.on_resume_button_clicked) 

    def show_about_form(self):
        self.about_form = AboutForm(self)
        self.about_form.exec()  

    def on_start_button_clicked(self):
        if self.process is None:
            self.process = subprocess.Popen(["python", "main.py"])
            log_and_print("Процесс main.py запущен")

    def on_pause_button_clicked(self):
        if self.process is not None:
            p = psutil.Process(self.process.pid)
            p.suspend()
            log_and_print("Процесс main.py приостановлен")

    def on_resume_button_clicked(self):
        if self.process is not None:
            p = psutil.Process(self.process.pid)
            p.resume()
            log_and_print("Процесс main.py возобновлен")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
