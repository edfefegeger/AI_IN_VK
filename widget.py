# widget.py
from PySide6.QtWidgets import QApplication, QWidget, QDialog
from ui_form import Ui_Widget
from ui_about import Ui_Form  # Импортируем UI для нового окна
import sys
import subprocess

# Класс для нового окна "О программе"
class AboutForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Подключаем кнопки к их функциям
        self.ui.pushButton.clicked.connect(self.show_about_form)  # Открыть новое окно
        self.ui.pushButton_2.clicked.connect(self.on_start_button_clicked)  # Запустить main.py

    def show_about_form(self):
        self.about_form = AboutForm(self)
        self.about_form.exec()  # Открываем новое окно

    def on_start_button_clicked(self):
        subprocess.Popen(["python", "main.py"])  # Запускаем main.py

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
