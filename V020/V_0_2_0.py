from graphfile import Ui_MainWindow
from password import Ui_MainWindow1
from really import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import sys


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
        self.DelButton.clicked.connect(self.connector_for_DelButton)
        self.action_exit.triggered.connect(self.connector_for_exit)
        self.action_full_del.triggered.connect(self.connector_for_question_before_full_del)
        self.action_4.triggered.connect(self.connector_for_rep_one_note)
        self.action_5.triggered.connect(self.connector_for_rep_all_notes)
        self.oImage = QImage("Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
        self.background()

    def background(self):
        self.oImage = QImage("Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
        sImage = self.oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def add_to_trash(self):
        with open('trash.txt', 'a') as file:
            file.write(self.date + ' - ' + self.text + '\n')

    def save(self, is_all=False):
        with open('save.txt', 'a') as file:
            if self.text:
                if is_all:
                    file.write(self.data)
                else:
                    file.write(self.date + ' - ' + self.text + '\n')

    def repair_data(self):
        self.note = {}
        with open('save.txt', 'r') as file1:
            file1 = file1.read()
            for i in file1.split('\n'):
                if i:
                    i1 = i.split(' - ')
                    self.note[i1[0]] = i1[1]

    def delete_note(self, filename='save.txt'):  # Удаление одной заметки
        with open(filename, 'r') as file:
            str1 = ''
            for line in file.read().split('\n'):
                if self.date in line:
                    line = ''
                str1 += line + '\n' if line else ''
        with open(filename, 'w') as file:
            file.write(str1)

    def full_delete(self):  # Удаление всех заметок
        with open('save.txt', 'w') as file:
            file.write('')
        self.note = {}

    def make_note(self):  # Создает заметки
        self.text = self.textEdit.toPlainText()
        if self.text.strip():
            self.note[self.date] = self.text
            self.save()

    def connector_for_rep_all_notes(self):
        with open('Trash.txt', 'r') as file:
            self.data = file.read()
        with open('Trash.txt', 'w') as file:
            file.write('')
        self.save(True)
        self.repair_data()
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()

    def connector_for_rep_one_note(self):
        str1 = ''
        with open('Trash.txt', 'r') as file:
            self.text=''
            for line in file.read().split('\n'):
                if self.date == line.split(' - ')[0]:
                    self.text = line.split(' - ')[1]
                    line = ''
                str1 += line + '\n' if line else ''
        with open('Trash.txt', 'w') as file:
            file.write(str1)
        self.save()
        self.repair_data()
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()

    def connector_for_exit(self):
        self.que = Question(exit)
        self.que.show()

    def connector_for_question_before_full_del(self):  # Выводит "Вы уверены?" перед удалением всех заметок
        self.que = Question(self.connector_for_action_full_del)
        self.que.show()

    def connector_for_action_full_del(self):  # Все процедуры для удаления всех заметок
        for self.date, self.text in self.note.items():
            self.add_to_trash()
        self.full_delete()
        self.text = 'Заметок на этот день нет'
        self.write_text()

    def connector_for_DelButton(self):  # Все функции, срабатывающие при нажатии на "Удалить заметку"
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        if self.text != 'Заметок на этот день нет':
            self.add_to_trash()
        self.delete_note()
        self.repair_data()
        self.text = 'Заметок на этот день нет'
        self.write_text()

    def connector_for_WriteButton(self):  # Все функции, срабатывающие при нажатии на "Добавить заметку"
        self.make_note()
        self.textEdit.clear()
        if self.text.strip():
            self.text_word_wrap()
            self.write_text()
        if self.date == '(1989, 9, 13)':
            self.secret()

    def connector_for_calendarWidget(self):  # Все функции, срабатывающии при нажатии на календарь
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
            self.delete_note()
            self.sec = Start()
            self.sec.show()


class Start(QMainWindow, Ui_MainWindow1):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.enter)

    def enter(self):
        if self.lineEdit.text() == '1511282683110':
            self.final()

    def final(self):
        self.close()  # someone action


class Question(QMainWindow, Ui_Dialog):

    def __init__(self, action):
        super().__init__()
        self.setupUi(self)
        self.action = action

    def accept(self):
        self.close()
        self.action()

    def reject(self):
        self.close()


app = QApplication(sys.argv)
cal = Calendar()
cal.show()
sys.exit(app.exec_())
