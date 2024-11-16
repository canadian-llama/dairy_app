from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QListWidget, QListWidgetItem


class Dairy_Ui_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(850, 650))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 700))
        self.stackedWidget.setObjectName("stackedWidget")
        
        # login page ui
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.loginFrame = QtWidgets.QFrame(self.loginPage)
        self.loginFrame.setEnabled(True)
        self.loginFrame.setGeometry(QtCore.QRect(210, 80, 451, 441))
        self.loginFrame.setAcceptDrops(False)
        self.loginFrame.setAutoFillBackground(True)
        self.loginFrame.setStyleSheet("color:rgb(74, 74, 74)")
        self.loginFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginFrame.setLineWidth(2)
        self.loginFrame.setObjectName("loginFrame")
        self.usernamelabel = QtWidgets.QLabel(self.loginFrame)
        self.usernamelabel.setGeometry(QtCore.QRect(20, 30, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.usernamelabel.setFont(font)
        self.usernamelabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.usernamelabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usernamelabel.setObjectName("usernamelabel")
        self.pwdlabel = QtWidgets.QLabel(self.loginFrame)
        self.pwdlabel.setGeometry(QtCore.QRect(20, 80, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pwdlabel.setFont(font)
        self.pwdlabel.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.pwdlabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pwdlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pwdlabel.setObjectName("pwdlabel")
        self.loginButton = QtWidgets.QPushButton(self.loginFrame)
        self.loginButton.setGeometry(QtCore.QRect(160, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.linkSignup = QtWidgets.QCommandLinkButton(self.loginFrame)
        self.linkSignup.setGeometry(QtCore.QRect(270, 380, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.linkSignup.setFont(font)
        self.linkSignup.setObjectName("linkSignup")
        self.label_2 = QtWidgets.QLabel(self.loginFrame)
        self.label_2.setGeometry(QtCore.QRect(50, 390, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.remeberMe = QtWidgets.QCheckBox(self.loginFrame)
        self.remeberMe.setGeometry(QtCore.QRect(330, 149, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remeberMe.setFont(font)
        self.remeberMe.setObjectName("remeberMe")
        self.usernameInput = QtWidgets.QLineEdit(self.loginFrame)
        self.usernameInput.setGeometry(QtCore.QRect(130, 30, 311, 31))
        self.usernameInput.setObjectName("usernameInput")
        self.pwdInput = QtWidgets.QLineEdit(self.loginFrame)
        self.pwdInput.setGeometry(QtCore.QRect(130, 80, 311, 31))
        self.pwdInput.setObjectName("pwdInput")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(False)
        self.pwdInput.setFont(font)
        self.usernameInput.setFont(font)
        self.pwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_4 = QtWidgets.QLabel(self.loginPage)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.loginPage)
        self.username = self.usernameInput.text()
        # --------------------------------------------------------------------------------
        
        # sign up ui page
        self.signupPage = QtWidgets.QWidget()
        self.signupPage.setObjectName("signupPage")
        self.signupFrame = QtWidgets.QFrame(self.signupPage)
        self.signupFrame.setEnabled(True)
        self.signupFrame.setGeometry(QtCore.QRect(210, 80, 451, 441))
        self.signupFrame.setAcceptDrops(False)
        self.signupFrame.setAutoFillBackground(True)
        self.signupFrame.setStyleSheet("color:rgb(74, 74, 74)")
        self.signupFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.signupFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signupFrame.setLineWidth(2)
        self.signupFrame.setObjectName("signupFrame")
        self.usernamelabel_2 = QtWidgets.QLabel(self.signupFrame)
        self.usernamelabel_2.setGeometry(QtCore.QRect(20, 30, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.usernamelabel_2.setFont(font)
        self.usernamelabel_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.usernamelabel_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usernamelabel_2.setObjectName("usernamelabel_2")
        self.pwdlabel_2 = QtWidgets.QLabel(self.signupFrame)
        self.pwdlabel_2.setGeometry(QtCore.QRect(20, 80, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pwdlabel_2.setFont(font)
        self.pwdlabel_2.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.pwdlabel_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pwdlabel_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pwdlabel_2.setObjectName("pwdlabel_2")
        self.signupButton = QtWidgets.QPushButton(self.signupFrame)
        self.signupButton.setGeometry(QtCore.QRect(160, 280, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.signupButton.setFont(font)
        self.signupButton.setObjectName("signupButton")
        self.pwdconfirmlabel = QtWidgets.QLabel(self.signupFrame)
        self.pwdconfirmlabel.setEnabled(True)
        self.pwdconfirmlabel.setGeometry(QtCore.QRect(20, 120, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pwdconfirmlabel.setFont(font)
        self.pwdconfirmlabel.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.pwdconfirmlabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pwdconfirmlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pwdconfirmlabel.setWordWrap(True)
        self.pwdconfirmlabel.setObjectName("pwdconfirmlabel")
        self.linkLogin = QtWidgets.QCommandLinkButton(self.signupFrame)
        self.linkLogin.setGeometry(QtCore.QRect(270, 380, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.linkLogin.setFont(font)
        self.linkLogin.setObjectName("linkLogin")
        self.label_3 = QtWidgets.QLabel(self.signupFrame)
        self.label_3.setGeometry(QtCore.QRect(50, 390, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.usernameInput_2 = QtWidgets.QLineEdit(self.signupFrame)
        self.usernameInput_2.setGeometry(QtCore.QRect(120, 30, 311, 31))
        self.usernameInput_2.setObjectName("usernameInput_2")
        self.pwdInput_2 = QtWidgets.QLineEdit(self.signupFrame)
        self.pwdInput_2.setGeometry(QtCore.QRect(120, 80, 311, 31))
        self.pwdInput_2.setObjectName("pwdInput_2")
        self.pwdconfirmInput = QtWidgets.QLineEdit(self.signupFrame)
        self.pwdconfirmInput.setGeometry(QtCore.QRect(120, 150, 311, 31))
        self.pwdconfirmInput.setObjectName("pwdconfirmInput")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(False)
        self.pwdInput_2.setFont(font)
        self.usernameInput_2.setFont(font)
        self.pwdconfirmInput.setFont(font)
        self.pwdInput_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdconfirmInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_5 = QtWidgets.QLabel(self.signupPage)
        self.label_5.setGeometry(QtCore.QRect(80, 10, 710, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        # ----------------------------------------------------------------------------------
        
        # diary homepage ui
        self.stackedWidget.addWidget(self.signupPage)
        self.dairyHomePage = QtWidgets.QWidget()
        self.dairyHomePage.setObjectName("dairyHomePage")
        self.dairyHomeFrame = QtWidgets.QFrame(self.dairyHomePage)
        self.dairyHomeFrame.setGeometry(QtCore.QRect(-10, 0, 900, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dairyHomeFrame.sizePolicy().hasHeightForWidth())
        self.dairyHomeFrame.setSizePolicy(sizePolicy)
        self.dairyHomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dairyHomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dairyHomeFrame.setObjectName("dairyHomeFrame")
        self.diaryList = QListWidget(self.dairyHomeFrame)
        self.diaryList.setGeometry(QtCore.QRect(10, 90, 851, 501))
        self.diaryList.setStyleSheet("font: 700 16pt \"Consolas\";\n"
        "background-color: rgb(193, 186, 200);\n"
        "color: rgb(0, 0, 0);" "padding-top: 20px;" "padding-left: 10px;")
        self.diaryList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.diaryList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diaryList.setUniformItemSizes(True)
        self.diaryList.setSelectionRectVisible(True)
        self.diaryList.setObjectName("diaryList")
        self.greetingLabel = QtWidgets.QLabel(self.dairyHomeFrame)
        self.greetingLabel.setGeometry(QtCore.QRect(10, 0, 851, 91))
        self.greetingLabel.setMaximumSize(QtCore.QSize(851, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.greetingLabel.setFont(font)
        self.greetingLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.greetingLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.greetingLabel.setLineWidth(2)
        self.greetingLabel.setTextFormat(QtCore.Qt.RichText)
        self.greetingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.greetingLabel.setObjectName("greetingLabel")
        self.addDiaryButton = QtWidgets.QPushButton(self.dairyHomeFrame)
        self.addDiaryButton.setGeometry(QtCore.QRect(780, 590, 80, 41))
        self.addDiaryButton.setToolTipDuration(2)
        self.addDiaryButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-email-send-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDiaryButton.setIcon(icon)
        self.addDiaryButton.setIconSize(QtCore.QSize(25, 25))
        self.addDiaryButton.setAutoDefault(False)
        self.addDiaryButton.setDefault(True)
        self.addDiaryButton.setFlat(False)
        self.addDiaryButton.setObjectName("clearDiaryButton")
        self.clearDiaryButton = QtWidgets.QPushButton(self.dairyHomeFrame)
        self.clearDiaryButton.setGeometry(QtCore.QRect(15, 590, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.clearDiaryButton.setFont(font)
        self.clearDiaryButton.setAutoDefault(False)
        self.clearDiaryButton.setDefault(True)
        self.addDiaryButton.setFlat(False)
        self.clearDiaryButton.setText("Clear All")
        self.clearDiaryButton.setObjectName("clearDiaryButton")
        self.sidebarButton = QtWidgets.QPushButton(self.dairyHomeFrame)
        self.sidebarButton.setGeometry(QtCore.QRect(20, 10, 51, 31))
        self.sidebarButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MY Ai/icons8-menu-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebarButton.setIcon(icon1)
        self.sidebarButton.setIconSize(QtCore.QSize(25, 25))
        self.sidebarButton.setObjectName("sidebarButton")
        self.stackedWidget.addWidget(self.dairyHomePage)
        # --------------------------------------------------------------------------------
        
        # add diary ui 
        self.addPage = QtWidgets.QWidget()
        self.addPage.setObjectName("addPage")
        self.addFrame = QtWidgets.QFrame(self.addPage)
        self.addFrame.setGeometry(QtCore.QRect(-10, 0, 900, 700))
        self.addFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addFrame.setObjectName("addFrame")
        self.diaryEntry = QtWidgets.QTextEdit(self.addFrame)
        self.diaryEntry.setGeometry(QtCore.QRect(10, 30, 851, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diaryEntry.sizePolicy().hasHeightForWidth())
        self.diaryEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.diaryEntry.setFont(font)
        self.diaryEntry.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.diaryEntry.setStyleSheet("background-color:rgb(147, 147, 147); color: rgb(0, 0, 0);")
        self.diaryEntry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.diaryEntry.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.diaryEntry.setUndoRedoEnabled(False)
        self.diaryEntry.setObjectName("diaryEntry")
        self.saveButton = QtWidgets.QPushButton(self.addFrame)
        self.saveButton.setGeometry(QtCore.QRect(790, 0, 71, 31))
        self.saveButton.setObjectName("saveButton")
        self.backButton = QtWidgets.QPushButton(self.addFrame)
        self.backButton.setGeometry(QtCore.QRect(10, 0, 71, 31))
        self.backButton.setObjectName("backButton")
        self.stackedWidget.addWidget(self.addPage)
        # -----------------------------------------------------------------------------------
        
        # modifying diary ui
        self.modifyPage = QtWidgets.QWidget()
        self.modifyPage.setObjectName("modifyPage")
        self.modifyFrame = QtWidgets.QFrame(self.modifyPage)
        self.modifyFrame.setGeometry(QtCore.QRect(-10, 0, 900, 700))
        self.modifyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modifyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modifyFrame.setObjectName("modifyFrame")
        self.modifyingEntry = QtWidgets.QTextEdit(self.modifyFrame)
        self.modifyingEntry.setGeometry(QtCore.QRect(10, 30, 851, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyingEntry.sizePolicy().hasHeightForWidth())
        self.modifyingEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.modifyingEntry.setFont(font)
        self.modifyingEntry.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.modifyingEntry.setStyleSheet("color: rgb(0, 0, 0)")
        self.modifyingEntry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.modifyingEntry.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.modifyingEntry.setUndoRedoEnabled(False)
        self.modifyingEntry.setPlaceholderText("")
        self.modifyingEntry.setObjectName("modifyingEntry")
        self.saveButton_2 = QtWidgets.QPushButton(self.modifyFrame)
        self.saveButton_2.setGeometry(QtCore.QRect(790, 0, 71, 31))
        self.saveButton_2.setObjectName("saveButton_2")
        self.backButton_2 = QtWidgets.QPushButton(self.modifyFrame)
        self.backButton_2.setGeometry(QtCore.QRect(10, 0, 71, 31))
        self.backButton_2.setObjectName("backButton_2")
        self.deleteButton = QtWidgets.QPushButton(self.modifyFrame)
        self.deleteButton.setGeometry(QtCore.QRect(425, 0, 71, 31))
        self.deleteButton.setObjectName("deleteButton")
        self.stackedWidget.addWidget(self.modifyPage)
        # --------------------------------------------------------------------------------------
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyDairy"))
        self.usernamelabel.setText(_translate("MainWindow", "UserName:"))
        self.pwdlabel.setText(_translate("MainWindow", "Password:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.linkSignup.setText(_translate("MainWindow", "Sign Up!"))
        self.label_2.setText(_translate("MainWindow", "Don\'t have an account!"))
        self.remeberMe.setText(_translate("MainWindow", "Remember Me"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Welcome Back! You have been Missed💖</p></body></html>"))
        self.usernamelabel_2.setText(_translate("MainWindow", "UserName:"))
        self.pwdlabel_2.setText(_translate("MainWindow", "Password:"))
        self.signupButton.setText(_translate("MainWindow", "Sign Up"))
        self.pwdconfirmlabel.setText(_translate("MainWindow", "Retype Password:"))
        self.linkLogin.setText(_translate("MainWindow", "Login!"))
        self.label_3.setText(_translate("MainWindow", "Already have an account!"))
        self.label_5.setText(_translate("MainWindow", "Welcome New User! We are pleased  to have You💖"))
        self.addDiaryButton.setToolTip(_translate("MainWindow", "add diary"))
        self.diaryEntry.setPlaceholderText(_translate("MainWindow", "Type something here......."))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.backButton.setText(_translate("MainWindow", "<----"))
        self.saveButton_2.setText(_translate("MainWindow", "Save"))
        self.backButton_2.setText(_translate("MainWindow", "<----"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Dairy_Ui_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())