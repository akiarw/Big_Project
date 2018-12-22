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
        MainWindow.resize(810, 620)
        MainWindow.setStyleSheet("font: 11pt \"Segoe Print\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 461, 331))
        self.calendarWidget.setStyleSheet("alternate-background-color: rgb(0, 65, 195);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"selection-background-color: rgb(66, 133, 244);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(479, 30, 331, 141))
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
        self.textEdit.setGeometry(QtCore.QRect(0, 330, 461, 221))
        self.textEdit.setStyleSheet("font: 75 italic 11pt \"Arial\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 25, 0, 69), stop:0.375 rgba(70, 2, 0, 69), stop:0.423533 rgba(251, 148, 0, 145), stop:0.45 rgba(247, 155, 0, 208), stop:0.477581 rgba(75, 44, 71, 130), stop:0.518717 rgba(255, 118, 71, 130), stop:0.55 rgba(255, 75, 0, 255), stop:0.57754 rgba(80, 103, 0, 130), stop:0.625 rgba(75, 185, 0, 69), stop:1 rgba(45, 45, 0, 69));")
        self.textEdit.setObjectName("textEdit")
        self.WriteButton = QtWidgets.QPushButton(self.centralwidget)
        self.WriteButton.setGeometry(QtCore.QRect(500, 370, 191, 51))
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
        self.label_2.setGeometry(QtCore.QRect(560, -10, 151, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 170, 151, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 210, 331, 151))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.DelButton = QtWidgets.QPushButton(self.centralwidget)
        self.DelButton.setGeometry(QtCore.QRect(720, 370, 51, 51))
        self.DelButton.setStyleSheet("background-color: rgb(150, 213, 253);")
        self.DelButton.setObjectName("DelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 32))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.DelButton.setText(_translate("MainWindow", "Del"))

