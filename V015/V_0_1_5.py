from graphfile import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import sys
#from secret import Hided


class Calendar(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.holidays()
        self.repair_data()
        self.today = str(self.calendarWidget.selectedDate())[18:]
        self.date = self.today
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()
        self.text = self.text = self.hldy['(' + self.date[7:]]
        self.write_holiday()
        self.calendarWidget.clicked.connect(self.connector_for_calendarWidget)
        self.WriteButton.clicked.connect(self.connector_for_WriteButton)
        self.DelButton.clicked.connect(self.delete_note)
        self.oImage = QImage("Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
        self.background()

    def background(self):
        self.oImage = QImage("Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
        sImage = self.oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def save(self):
        with open('save.txt', 'a') as file:
            file.write(self.date + ' - ' + self.text + '\n')

    def repair_data(self):
        self.note={}
        with open('save.txt', 'r') as file1:
            file1 = file1.read()
            for i in file1.split('\n'):
                if i:
                    i1 = i.split(' - ')
                    self.note[i1[0]] = i1[1]

    def delete_note(self):
        with open('save.txt', 'r') as file:
            str1 = ''
            for line in file.read().split('\n'):
                if self.date in line:
                   line = ''
                str1 += line+'\n' if line else ''
        with open('save.txt', 'w') as file:
            file.write(str1)
        self.repair_data()
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()

    def full_delete(self):  # перспективная ветка
        with open('save.txt', 'w') as file:
            file.write('')

    def make_note(self):  # Создает заметки
        self.text = self.textEdit.toPlainText()
        if self.text:
            self.note[self.date] = self.text
        self.save()
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()

    def connector_for_WriteButton(self):
        self.make_note()
        if self.date=='(1989, 9, 13)':
            self.secret()

    def connector_for_calendarWidget(self):
        self.date = str(self.calendarWidget.selectedDate())[18:]
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()
        self.text = self.hldy['(' + self.date[7:]]
        self.write_holiday()
        self.oImage = QImage("Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
        self.background()

    def write_text(self):  # Выводит в лейбел заметки на этот день
        self.text_word_wrap()
        self.label.setText(self.result)

    def text_word_wrap(self):  # Преобразует текст для перевода на новую строку
        result = ''
        length = 0
        self.text.replace('\n', '')
        if len(self.text) > 30:  # 30 - максимальная длина строки при этом шрифте и этом размере лейбела
            text = self.text.split()
            for i in text:
                if length + len(i) < 30:
                    result += i + ' '
                    length += len(i)
                else:
                    result += '\n' + i + ' '
                    length = 0
        self.result = result if result else self.text

    def holidays(self):
        self.hldy = {}
        with open('Holydays.txt', 'r') as txtfile:
            for i in txtfile.read().split('\n'):
                i1 = i.split(' - ')
                self.hldy[i1[0]] = i1[1]

    def write_holiday(self):
        self.text_word_wrap()
        self.label_4.setText(self.result)

    def secret(self):
        if 'валакас' in self.note.get('(1989, 9, 13)', '').lower():
            app = QApplication(sys.argv)
            sec = Start()
            sec.show()
            sys.exit(app.exec_())


class Start(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ask = False
        self.pushButton.clicked.connect(self.enter)

    def enter(self):
        if self.lineEdit.text() == '1511282683110':
            self.ask = True
            self.label.setText('\tТы точно хочешь этого? (Y/N)')
        elif self.ask:
            self.final()

    def final(self):
        if self.lineEdit.text() == 'Y':
            pass  # someone action
            sys.exit()


app = QApplication(sys.argv)
cal = Calendar()
cal.show()
sys.exit(app.exec_())
