from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *

from GUI.Completer import get_autocomplete_list


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #background imamge
        """oImage = QImage("backgroundImg.jpg")
        sImage = oImage.scaled(QSize(871, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)"""


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 561, 41))
        self.lineEdit.setStyleSheet(  """QLineEdit { background-color: rgb(255,255,255); color: black; border: 0 }""")
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        completer = QtWidgets.QCompleter(get_autocomplete_list(), self.lineEdit)
        self.lineEdit.setCompleter(completer)

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setStyleSheet("QPushButton {background: rgb(8,166,255); border: 0;}")
        icon = QIcon("searchIcon.png")
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QSize(30,30))
        self.searchButton.setGeometry(QtCore.QRect(640, 50, 121, 41))
        self.searchButton.setObjectName("searchButton")


        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 190, 661, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.summoner_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.summoner_value.setFont(font)
        self.summoner_value.setText("")
        self.summoner_value.setObjectName("summoner_value")
        self.verticalLayout.addWidget(self.summoner_value)

        self.point_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.point_value.setFont(font)
        self.point_value.setText("")
        self.point_value.setObjectName("point_value")
        self.verticalLayout.addWidget(self.point_value)

        self.rank_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.rank_value.setFont(font)
        self.rank_value.setText("")
        self.rank_value.setObjectName("rank_value")
        self.verticalLayout.addWidget(self.rank_value)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
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
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "champ name here"))
