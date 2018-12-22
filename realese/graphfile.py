# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphfile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 589)
        MainWindow.setStyleSheet("font: 11pt \"Segoe Print\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 551, 331))
        self.calendarWidget.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 30, 371, 141))
        self.label.setStyleSheet("\n"
"font: 75 italic 11pt \"Arial\";")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 380, 621, 121))
        self.textEdit.setStyleSheet("font: 75 italic 11pt \"Arial\";\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(0, 0, 0, 0), stop:0.65 rgba(0, 0, 0, 0), stop:0.721925 rgba(0, 0, 0, 0), stop:0.77 rgba(0, 0, 0, 0), stop:0.89 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.WriteButton = QtWidgets.QPushButton(self.centralwidget)
        self.WriteButton.setGeometry(QtCore.QRect(670, 380, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.WriteButton.setFont(font)
        self.WriteButton.setStyleSheet("background-color: rgb(150, 213, 13);")
        self.WriteButton.setObjectName("WriteButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(680, -10, 151, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 170, 151, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 210, 371, 151))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.DelButton = QtWidgets.QPushButton(self.centralwidget)
        self.DelButton.setGeometry(QtCore.QRect(670, 440, 101, 61))
        self.DelButton.setStyleSheet("background-color: rgb(150, 213, 253);")
        self.DelButton.setObjectName("DelButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 350, 191, 31))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 32))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setCheckable(False)
        self.action_3.setEnabled(True)
        self.action_3.setObjectName("action_3")
        self.action_full_del = QtWidgets.QAction(MainWindow)
        self.action_full_del.setObjectName("action_full_del")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_full_del)
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:72; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.WriteButton.setText(_translate("MainWindow", "Добавить заметку"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Заметки</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">В этот день...</span></p></body></html>"))
        self.DelButton.setText(_translate("MainWindow", "Удалить\n"
"заметку"))
        self.label_5.setText(_translate("MainWindow", "Напишите заметку"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Восстановить"))
        self.action_3.setText(_translate("MainWindow", "Выйти"))
        self.action_full_del.setText(_translate("MainWindow", "Удалить все заметки"))
        self.action_exit.setText(_translate("MainWindow", "Выйти"))
        self.action_4.setText(_translate("MainWindow", "Заметку на этот день"))
        self.action_5.setText(_translate("MainWindow", "Все заметки"))
        self.action.setText(_translate("MainWindow", "Показать корзину"))

