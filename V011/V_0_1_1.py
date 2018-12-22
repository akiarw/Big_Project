from graphfile import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Calendar(QMainWindow, Ui_MainWindow):

    def make_note(self):
        if self.textEdit.toPlainText():
            self.note[self.date] = self.textEdit.toPlainText()
        self.write_text()

    def notes(self):
        self.date = str(self.calendarWidget.selectedDate())[18:]
        self.WriteButton.clicked.connect(self.make_note)
        self.calendarWidget.clicked.connect(self.write_text)

    def __init__(self):
        super().__init__()
        self.note = {}
        self.setupUi(self)
        self.date = str(self.calendarWidget.selectedDate())[18:]
        self.calendarWidget.clicked.connect(self.notes)

    def write_text(self):
        if self.date in self.note.keys():
            self.text = self.note[self.date]
        else:
            self.text = ''
        self.text_word_wrap()
        self.label.setText(self.text)

    def text_word_wrap(self):  # Преобразует текст для перевода на новую строку
        self.text.replace('\n', '')
        if len(self.text) > 48:  # 48 - максимальная длина строки при этом шрифте и этом размере лейбела
            self.text = [x for x in self.text]
            for i in range(42, len(self.text), 43):  # Не спрашивай, откуда взялись числа 42 и 43
                self.text.insert(i, '\n')  # (просто точная подгонка)
            self.text = ''.join(self.text)

    def holidays(self):
        pass


app = QApplication(sys.argv)
cal = Calendar()
cal.show()
sys.exit(app.exec_())
