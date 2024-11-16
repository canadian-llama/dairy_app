from PyQt5 import QtCore, QtGui, QtWidgets


class SideBar_Ui(object):
    def setupUi(self, parent):
        self.sideMenu = QtWidgets.QFrame(self.centralwidget)
        self.sideMenu.setGeometry(QtCore.QRect(0, 40, 161, 411))
        self.sideMenu.setStyleSheet("background-color: rgb(75, 200, 106);")
        self.sideMenu.setFrameShape(QtWidgets.QFrame.Box)
        self.sideMenu.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sideMenu.setLineWidth(2)
        self.sideMenu.setObjectName("sideMenu")
        self.userNameLabel = QtWidgets.QLabel(self.sideMenu)
        self.userNameLabel.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameLabel.setObjectName("userNameLabel")
        self.userPicture = QtWidgets.QLabel(self.sideMenu)
        self.userPicture.setGeometry(QtCore.QRect(20, 60, 111, 101))
        self.userPicture.setStyleSheet("background-image: \"bio.jpg\"")
        self.userPicture.setFrameShape(QtWidgets.QFrame.Box)
        self.userPicture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userPicture.setLineWidth(2)
        self.userPicture.setText("")
        self.userPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.userPicture.setObjectName("userPicture")
        self.settingsButton = QtWidgets.QPushButton(self.sideMenu)
        self.settingsButton.setGeometry(QtCore.QRect(40, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.settingsButton.setFont(font)
        self.settingsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MY Ai/icons8-settings-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon)
        self.settingsButton.setIconSize(QtCore.QSize(50, 50))
        self.settingsButton.setObjectName("settingsButton")
        self.logoutButton = QtWidgets.QPushButton(self.sideMenu)
        self.logoutButton.setGeometry(QtCore.QRect(10, 330, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.abouButton = QtWidgets.QPushButton(self.sideMenu)
        self.abouButton.setGeometry(QtCore.QRect(110, 340, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.abouButton.setFont(font)
        self.abouButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MY Ai/icons8-about-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abouButton.setIcon(icon1)
        self.abouButton.setObjectName("abouButton")
        