from graphfile import Ui_MainWindow
from password import Ui_MainWindow1
from really import Ui_Dialog
from TrashWiew import Ui_MainWindow3
from ban import Ui_Ban
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import sys


class Calendar(QMainWindow, Ui_MainWindow):

    def __init__(self):
        try:
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
            self.action.triggered.connect(self.connector_for_trash_wiew)
            self.oImage = QImage("UFiles/Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
            self.background()
        except BaseException:
            sys.exit('Ошибка! Проверьте целостность файлов')

    def background(self):
        self.oImage = QImage("UFiles/Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
        sImage = self.oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def add_to_trash(self):
        with open('UFiles/trash.txt', 'a') as file:
            file.write(self.date + ' - ' + self.text + '\n')

    def save(self, is_all=False):
        with open('UFiles/save.txt', 'a') as file:
            if self.text:
                if is_all:
                    file.write(self.data)
                else:
                    file.write(self.date + ' - ' + self.text + '\n')

    def repair_data(self):
        self.note = {}
        try:
            with open('UFiles/save.txt', 'r') as file1:
                file1 = file1.read()
                for i in file1.split('\n'):
                    if i:
                        i1 = i.split(' - ')
                        self.note[i1[0]] = i1[1]
        except IndexError:
            self.cal = Question(None, True)
            self.cal.show()
            sys.exit(app.exec_())

    def delete_note(self):  # Удаление одной заметки
        with open('UFiles/save.txt', 'r') as file:
            str1 = ''
            for line in file.read().split('\n'):
                if self.date in line:
                    line = ''
                str1 += line + '\n' if line else ''
        with open('UFiles/save.txt', 'w') as file:
            file.write(str1)

    def full_delete(self):  # Удаление всех заметок
        with open('UFiles/save.txt', 'w') as file:
            file.write('')
        self.note = {}

    def make_note(self):  # Создает заметки
        self.text = self.textEdit.toPlainText().replace('\n', ' ')
        if self.text.strip():
            if self.date in self.note.keys():
                self.note[self.date] += ' ' + self.text
            else:
                self.note[self.date] = self.text
            self.text = self.note[self.date]
            self.save()

    def connector_for_trash_wiew(self):
        self.sec = TrashWiew()
        self.sec.show()

    def connector_for_rep_all_notes(self):
        with open('UFiles/Trash.txt', 'r') as file:
            self.data = file.read()
        with open('UFiles/Trash.txt', 'w') as file:
            file.write('')
        self.save(True)
        self.repair_data()
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()

    def connector_for_rep_one_note(self):
        str1 = ''
        with open('UFiles/Trash.txt', 'r') as file:
            self.text = ''
            for line in file.read().split('\n'):
                if self.date == line.split(' - ')[0]:
                    self.text = line.split(' - ')[1]
                    line = ''
                str1 += line + '\n' if line else ''
        with open('UFiles/Trash.txt', 'w') as file:
            file.write(str1)
        self.save()
        self.repair_data()
        self.text = self.note.get(self.date, 'Заметок на этот день нет')
        self.write_text()

    def connector_for_exit(self):
        self.que = Question(sys.exit)
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
        self.oImage = QImage("UFiles/Backgrounds/" + self.date.split(',')[1].strip() + ".jpg")
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
        with open('UFiles/Holydays.txt', 'r') as txtfile:
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
            self.ban = Ban()
            self.ban.show()
            self.close()


class Question(QMainWindow, Ui_Dialog):

    def __init__(self, action, is_error=False):
        super().__init__()
        self.setupUi(self)
        if is_error:
            self.label.setText(
                'Возникла критическая ошибка!\nТребуется сброс сохранений\n(Удаленные заметки затронуты не будут,\n но их стоит удалить вручную).\nСовершить?')
            self.action = self.restart
        else:
            self.action = action

    def restart(self):
        with open('UFiles/save.txt', 'r') as file:
            s1 = file.read()
        with open('UFiles/Trash.txt', 'a') as file:
            file.write('\n' + s1)
        with open('UFiles/save.txt', 'w') as file:
            file.write('')
        sys.exit(0)

    def accept(self):
        self.close()
        self.action()

    def reject(self):
        self.close()


class TrashWiew(QMainWindow, Ui_MainWindow3):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action.triggered.connect(self.close)
        self.action_2.triggered.connect(self.pre_clear)
        with open('UFiles/trash.txt', 'r') as file:
            self.text = file.read()
        self.text_word_wrap()
        self.label.setText(self.result if self.result else '\t' * 5 + 'Корзина пуста')

    def pre_clear(self):
        self.sec = Question(self.clear)
        self.sec.show()

    def clear(self):
        with open('UFiles/trash.txt', 'w') as file:
            file.write('')
        self.label.setText('\t' * 5 + 'Корзина пуста')

    def text_word_wrap(self):  # Преобразует текст для перевода на новую строку
        result = ''
        length = 0
        self.text.replace('\n', '')
        if len(self.text) > 90:  # 90 - максимальная длина строки при этом шрифте и этом размере лейбела
            text = self.text.split()
            for i in text:
                if length + len(i) < 90:
                    result += i + ' '
                    length += len(i)
                else:
                    result += '\n' + i + ' '
                    length = 0
        self.result = result if result else self.text


class Ban(QMainWindow, Ui_Ban):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
cal = Calendar()
cal.show()
sys.exit(app.exec_())
