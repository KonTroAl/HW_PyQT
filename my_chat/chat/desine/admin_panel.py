# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.ClientsList = QtWidgets.QListView(self.centralwidget)
        self.ClientsList.setGeometry(QtCore.QRect(30, 30, 350, 300))
        self.ClientsList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ClientsList.setObjectName("ClientsList")
        self.PortTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.PortTextBox.setGeometry(QtCore.QRect(80, 420, 90, 30))
        self.PortTextBox.setObjectName("PortTextBox")
        self.HeddingClientList = QtWidgets.QLabel(self.centralwidget)
        self.HeddingClientList.setGeometry(QtCore.QRect(10, 10, 401, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(True)
        self.HeddingClientList.setFont(font)
        self.HeddingClientList.setStyleSheet("")
        self.HeddingClientList.setAlignment(QtCore.Qt.AlignCenter)
        self.HeddingClientList.setObjectName("HeddingClientList")
        self.HeddingClientStatistic = QtWidgets.QLabel(self.centralwidget)
        self.HeddingClientStatistic.setGeometry(QtCore.QRect(510, 10, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(True)
        self.HeddingClientStatistic.setFont(font)
        self.HeddingClientStatistic.setStyleSheet("")
        self.HeddingClientStatistic.setAlignment(QtCore.Qt.AlignCenter)
        self.HeddingClientStatistic.setObjectName("HeddingClientStatistic")
        self.ClientsStatistic = QtWidgets.QListView(self.centralwidget)
        self.ClientsStatistic.setGeometry(QtCore.QRect(430, 30, 350, 300))
        self.ClientsStatistic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ClientsStatistic.setObjectName("ClientsStatistic")
        self.HeddingServerConnection = QtWidgets.QLabel(self.centralwidget)
        self.HeddingServerConnection.setGeometry(QtCore.QRect(60, 340, 250, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(True)
        self.HeddingServerConnection.setFont(font)
        self.HeddingServerConnection.setStyleSheet("")
        self.HeddingServerConnection.setAlignment(QtCore.Qt.AlignCenter)
        self.HeddingServerConnection.setObjectName("HeddingServerConnection")
        self.PortNumber = QtWidgets.QLabel(self.centralwidget)
        self.PortNumber.setGeometry(QtCore.QRect(85, 390, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PortNumber.setFont(font)
        self.PortNumber.setObjectName("PortNumber")
        self.PortConnectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.PortConnectionButton.setGeometry(QtCore.QRect(200, 420, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PortConnectionButton.setFont(font)
        self.PortConnectionButton.setObjectName("PortConnectionButton")
        self.HeddingDBConnection = QtWidgets.QLabel(self.centralwidget)
        self.HeddingDBConnection.setGeometry(QtCore.QRect(480, 340, 250, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(True)
        self.HeddingDBConnection.setFont(font)
        self.HeddingDBConnection.setStyleSheet("")
        self.HeddingDBConnection.setAlignment(QtCore.Qt.AlignCenter)
        self.HeddingDBConnection.setObjectName("HeddingDBConnection")
        self.DBConnectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.DBConnectionButton.setGeometry(QtCore.QRect(545, 650, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DBConnectionButton.setFont(font)
        self.DBConnectionButton.setObjectName("DBConnectionButton")
        self.ServerTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.ServerTextBox.setGeometry(QtCore.QRect(420, 600, 350, 30))
        self.ServerTextBox.setObjectName("ServerTextBox")
        self.ServerDB = QtWidgets.QLabel(self.centralwidget)
        self.ServerDB.setGeometry(QtCore.QRect(550, 570, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ServerDB.setFont(font)
        self.ServerDB.setObjectName("ServerDB")
        self.DialectDB = QtWidgets.QLabel(self.centralwidget)
        self.DialectDB.setGeometry(QtCore.QRect(420, 370, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DialectDB.setFont(font)
        self.DialectDB.setObjectName("DialectDB")
        self.DialectDBTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.DialectDBTextBox.setGeometry(QtCore.QRect(430, 390, 90, 30))
        self.DialectDBTextBox.setObjectName("DialectDBTextBox")
        self.ServerDB_3 = QtWidgets.QLabel(self.centralwidget)
        self.ServerDB_3.setGeometry(QtCore.QRect(640, 370, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ServerDB_3.setFont(font)
        self.ServerDB_3.setObjectName("ServerDB_3")
        self.DriverDBTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.DriverDBTextBox.setGeometry(QtCore.QRect(650, 390, 90, 30))
        self.DriverDBTextBox.setObjectName("DriverDBTextBox")
        self.UsernameDB = QtWidgets.QLabel(self.centralwidget)
        self.UsernameDB.setGeometry(QtCore.QRect(420, 440, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.UsernameDB.setFont(font)
        self.UsernameDB.setObjectName("UsernameDB")
        self.PasswordDBTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.PasswordDBTextBox.setGeometry(QtCore.QRect(650, 460, 90, 30))
        self.PasswordDBTextBox.setObjectName("PasswordDBTextBox")
        self.PasswordDb = QtWidgets.QLabel(self.centralwidget)
        self.PasswordDb.setGeometry(QtCore.QRect(640, 440, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PasswordDb.setFont(font)
        self.PasswordDb.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordDb.setObjectName("PasswordDb")
        self.UsernameDBTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.UsernameDBTextBox.setGeometry(QtCore.QRect(430, 460, 90, 30))
        self.UsernameDBTextBox.setObjectName("UsernameDBTextBox")
        self.NameDb = QtWidgets.QLabel(self.centralwidget)
        self.NameDb.setGeometry(QtCore.QRect(510, 500, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.NameDb.setFont(font)
        self.NameDb.setAlignment(QtCore.Qt.AlignCenter)
        self.NameDb.setObjectName("NameDb")
        self.NsmeDBTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.NsmeDBTextBox.setGeometry(QtCore.QRect(540, 530, 90, 30))
        self.NsmeDBTextBox.setObjectName("NsmeDBTextBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdminPanel"))
        self.HeddingClientList.setText(_translate("MainWindow", "Список всех клиентов на сервере в данный момент"))
        self.HeddingClientStatistic.setText(_translate("MainWindow", "Статистика клиентов"))
        self.HeddingServerConnection.setText(_translate("MainWindow", "Подключение к серверу"))
        self.PortNumber.setText(_translate("MainWindow", "Номер порта"))
        self.PortConnectionButton.setText(_translate("MainWindow", "Подключиться"))
        self.HeddingDBConnection.setText(_translate("MainWindow", "Подключение к базе данных"))
        self.DBConnectionButton.setText(_translate("MainWindow", "Подключиться"))
        self.ServerDB.setText(_translate("MainWindow", "Сервер базы данных"))
        self.DialectDB.setText(_translate("MainWindow", "Имя базы данных"))
        self.ServerDB_3.setText(_translate("MainWindow", "Драйвер базы данных"))
        self.UsernameDB.setText(_translate("MainWindow", "Имя пользователя"))
        self.PasswordDb.setText(_translate("MainWindow", "Пароль"))
        self.NameDb.setText(_translate("MainWindow", "Название базы данных"))
