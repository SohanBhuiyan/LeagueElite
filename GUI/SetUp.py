from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.Completer import get_autocomplete_list


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LeagueEliteGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
class Ui_MainWindow(object):
    # generated setup code from pyqt5 GUI builder, designer
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 131, 41))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 50, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        completer = QtWidgets.QCompleter(get_autocomplete_list(),self.lineEdit)
        self.lineEdit.setCompleter(completer)

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(340, 50, 93, 28))
        self.searchButton.setObjectName("searchButton")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 260, 881, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.point_value = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.point_value.setFont(font)
        self.point_value.setObjectName("point_value")
        self.horizontalLayout_2.addWidget(self.point_value)
        self.summoner_value = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.summoner_value.setFont(font)
        self.summoner_value.setObjectName("summoner_value")
        self.horizontalLayout_2.addWidget(self.summoner_value)
        self.rank_value = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rank_value.setFont(font)
        self.rank_value.setObjectName("rank_value")
        self.horizontalLayout_2.addWidget(self.rank_value)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 90, 889, 169))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mastery_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mastery_label_2.setFont(font)
        self.mastery_label_2.setObjectName("mastery_label_2")
        self.horizontalLayout_5.addWidget(self.mastery_label_2)
        self.summoner_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        self.summoner_label_2.setFont(font)
        self.summoner_label_2.setObjectName("summoner_label_2")
        self.horizontalLayout_5.addWidget(self.summoner_label_2)
        self.rank_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.rank_label_2.setFont(font)
        self.rank_label_2.setObjectName("rank_label_2")
        self.horizontalLayout_5.addWidget(self.rank_label_2)
        self.label.raise_()
        self.lineEdit.raise_()
        self.searchButton.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 26))
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
        self.label.setText(_translate("MainWindow", "Champion Name"))
        self.searchButton.setText(_translate("MainWindow", "search"))
        self.point_value.setText(_translate("MainWindow", "pVal"))
        self.summoner_value.setText(_translate("MainWindow", "sVal"))
        self.rank_value.setText(_translate("MainWindow", "rVal"))
        self.mastery_label_2.setText(_translate("MainWindow", "points"))
        self.summoner_label_2.setText(_translate("MainWindow", "Summoner"))
        self.rank_label_2.setText(_translate("MainWindow", "Rank"))