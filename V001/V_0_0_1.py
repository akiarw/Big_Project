from graphfile import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class MyWidget(QMainWindow, Ui_MainWindow):

    def notes(self):
        self.date = str(self.calendarWidget.selectedDate())[18:]
        if self.date not in self.note.keys():
            self.note[self.date] = input()
        self.text = self.note[self.date]
        self.write_text()

    def __init__(self):
        self.note = {}
        super().__init__()
        self.setupUi(self)
        self.date = str(self.calendarWidget.selectedDate())[18:]
        self.calendarWidget.clicked.connect(self.notes)

    def write_text(self):
        #   self.text_func()
        self.label.setText(self.text)

    def text_func(self):  # Преобразует текст для перевода на новую строку
        self.text.replace('\n', '')
        if len(self.text) > 48:  # 48 - максимальная длина строки при этом шрифте и этом размере лейбела
            self.text = [x for x in self.text]
            for i in range(42, len(self.text), 43):  # Не спрашивай, откуда взялись числа 42 и 43
                self.text.insert(i, '\n')            # (просто точная подгонка)
            self.text = ''.join(self.text)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
