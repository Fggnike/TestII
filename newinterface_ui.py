
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newinterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 700)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #b0abab;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 570, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #20bf6b;\n"
"    border-radius: 6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d9d4d4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8a8888;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 570, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #eb3b5a;\n"
"    border-radius: 6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d9d4d4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8a8888;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 500, 471))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    background-color: #c7c3c3;\n"
"    color: black;    \n"
"    border-radius: 7;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(225, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setStyleSheet("QLabel {\n" 
"color: #f7b731; \n" 
"font-size: 20px; \n" 
"}")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Слушать"))
        self.pushButton_2.setText(_translate("MainWindow", "Стоп"))
        self.label.setText(_translate("MainWindow", "Rhombus"))
