import sys
from turtle import color
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from auth_db_functions import AuthDB
from dairy_db_functions import DiaryDB
from diary_ui import Dairy_Ui_Window
# from signup_login import Auth_MainWindow
from message_box import MessageBox
from circular_progress import CircularProgressBar
from sidebar import SideBar_Ui
class MainApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.progress_status = ""  
        db = DiaryDB()
        self.user = db.retrieve_user()
        self.saved = False
        self.content = ""
        self.selected_index = 0
        self.msg = MessageBox()
        self.ui = Dairy_Ui_Window()
        self.ui.setupUi(self)
        self.tag = 0
        self.current_tag = 0
        self.remember_val = None
        self.ui.diaryEntry.setReadOnly(False)
        # self.gui_remember_me()
        
        self.ui.linkLogin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage))
        
        self.ui.linkSignup.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signupPage))
        
        self.ui.loginButton.clicked.connect(self.login)    

        self.ui.signupButton.clicked.connect(self.signup)

        self.ui.addDiaryButton.clicked.connect(self.create_diary)
        
        self.ui.backButton.clicked.connect(self.back)
        
        self.ui.saveButton.clicked.connect(self.save)
        
        self.ui.diaryList.itemClicked.connect(self.select_item)

        self.ui.backButton_2.clicked.connect(self.modify_back)
        
        self.ui.saveButton_2.clicked.connect(self.modify_save)

        self.ui.clearDiaryButton.clicked.connect(self.clear_all_notes)
        
        self.ui.deleteButton.clicked.connect(self.delete)
   
        self.ui.sidebarButton.clicked.connect(self.show_side_bar)
   
        self.gui_remember_me()
   
    def signup(self):
        username = self.ui.usernameInput_2.text()
        pwd = self.ui.pwdInput_2.text()
        retyped = self.ui.pwdconfirmInput.text()
        self.ui.pwdInput_2.clear()
        self.ui.pwdconfirmInput.clear()
        db = AuthDB()
        db.sign_up(username, pwd, retyped)
        self.start_signup_progress()
        if db.var == "True":
            self.progress_status = "True"
        elif db.var == "False":
            self.progress_status = "False"
        elif db.var == "None":
            self.progress_status = "None"
        elif db.var == "Unfilled":
            self.progress_status = "Unfilled"
     
    def login(self):
        username = self.ui.usernameInput.text()
        pwd = self.ui.pwdInput.text()
        self.ui.pwdInput.clear()
        remember_me = self.check_remember_me()
        db = AuthDB()
        db.login(username, pwd, remember_me)
        self.start_login_progress()
        self.ui.diaryList.clear()
        self.ui.greetingLabel.setText(f"Welcome {self.user.title()} To Your Dairy")
        self.show_all_diary()
        if db.var == "True":
            self.progress_status = "True"
        elif db.var == "False":
            self.progress_status = "False"
        elif db.var == "None":
            self.progress_status = "None"
        elif db.var == "Unfilled":
            self.progress_status = "Unfilled"
    
    def start_signup_progress(self):
        progress = CircularProgressBar(10, 179, 240, self.ui.signupFrame)
        progress.progress_finished.connect(self.show_messagebox_signup_after)
        progress.start_progress()
    
    def start_login_progress(self):
        progress = CircularProgressBar(1, 179, 270, self.ui.loginFrame)
        progress.progress_finished.connect(self.show_messagebox_login_after)
        progress.start_progress()
    
    def show_messagebox_login_after(self):
        if self.progress_status == "True":
            self.msg.show_message("Success", "Login Successful")
            self.ui.stackedWidget.setCurrentWidget(self.ui.dairyHomePage)
        elif self.progress_status == "False":
            self.msg.show_message("Error", "Login failed! Incorrect Password")
        elif self.progress_status == "None":
            self.msg.show_message("Error", "User not found! Try SignUp First")
        elif self.progress_status == "Unfilled":
            self.msg.show_message("Error", "All Input Fields required")
   
    def show_messagebox_signup_after(self):
        if self.progress_status == "True":
            self.msg.show_message("Success", "User signup Successful! Proceed to login")
            self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
        elif self.progress_status == "False":
            self.msg.show_message("Error", "Sign Up failed! Password does not match")
        elif self.progress_status == "None":
            self.msg.show_message("Error", "User Already Exist Try Logging in")
        elif self.progress_status == "Unfilled":
            self.msg.show_message("Error", "All Input Fields required")

    def create_diary(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.addPage)
        self.ui.diaryEntry.setReadOnly(False)

    def back(self):
        message = self.ui.diaryEntry.toPlainText()
        db = DiaryDB()        
        tag = db.check_tags(self.user)
        if message != "" and not self.saved:
            db.add_diary(self.user, message, tag)
            self.ui.stackedWidget.setCurrentWidget(self.ui.dairyHomePage)
            self.ui.diaryEntry.setText("")
            self.ui.diaryList.clear()
            self.show_all_diary()
        else:
            self.ui.diaryEntry.setReadOnly(False)
            self.ui.diaryEntry.setText("")
            self.ui.stackedWidget.setCurrentWidget(self.ui.dairyHomePage)
   
    def increment(self):
        self.tag +=1
        return self.tag
   
    def save(self):
        db = DiaryDB()
        message = self.ui.diaryEntry.toPlainText()
        tag = db.check_tags(self.user)
        if message != "": 
            db.add_diary(self.user, message, tag)
            self.msg.show_message("Note Saved", "Note saved successfully")
            self.saved = True
            self.ui.diaryEntry.setReadOnly(True)
            self.ui.diaryList.clear()
            self.show_all_diary()
        else:
            self.msg.show_message("Empty Note", "Can't save an empty note try typing something in")

    def show_all_diary(self):
        db = DiaryDB()
        user = db.collection.find_one({"username" : self.user})
        if user and "entry" in user:
            for entry in user["entry"]:
                time_stamp, content = entry["timestamp"], entry["content"]
                if len(content) > 20:
                    content = content[:20] + "..." 
                item_text = f"** {time_stamp}   =>    {content}"
                self.ui.diaryList.addItem(item_text)
        else:
            pass
        
    def select_item(self):
        db = DiaryDB()
        user = db.collection.find_one({"username" : self.user})
        self.selected_index = self.ui.diaryList.currentRow()
        if user and "entry" in user and self.selected_index != -1:
            entry = user["entry"]
            selected = entry[self.selected_index]
            content = selected["content"]
            self.ui.stackedWidget.setCurrentWidget(self.ui.modifyPage)
            self.ui.modifyingEntry.setText(content)
            self.content = self.get_content()
            self.current_tag = selected["tag"]
       
    def get_tag(self):
        db = DiaryDB()
        user = db.collection.find_one({"username" : self.user})
        self.selected_index = self.ui.diaryList.currentRow()
        if user and "entry" in user and self.selected_index != -1:
            entry = user["entry"]
            selected = entry[self.selected_index]
            tag = selected["tag"]
            return tag 

    def get_content(self):
        content = self.ui.modifyingEntry.toPlainText()
        return content

    def modify_save(self):
        message = self.ui.modifyingEntry.toPlainText()
        tag = self.get_tag()
    
        if message != "" and tag != None: 
            db = DiaryDB()
            new_tag = db.check_tags(self.user)
            db.update_diary_entry(self.user, message, tag, new_tag)
            self.saved = True
            self.msg.show_message("Note Modified", "Note Modified successfully")
            self.ui.modifyingEntry.setReadOnly(True)
            self.ui.diaryList.clear()
            self.show_all_diary()
        else:
            pass

    def modify_back(self):
        content  = self.ui.modifyingEntry.toPlainText()
        if content != self.content and self.saved != True:
            confirm_msg_box = self.msg.show_message1("Confirm Exit", f"Are you sure you want to go back without saving?")
            if confirm_msg_box == "&Yes":
                self.ui_format()
            else:
                pass

        else:
            self.ui.modifyingEntry.setReadOnly(False)
            self.ui_format()
            
    def ui_format(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dairyHomePage)
        self.ui.diaryList.clear()
        self.show_all_diary()

    def clear_all_notes(self):
        db = DiaryDB()
        user = db.collection.find_one({"username": self.user})
        if user:
            entry = user["entry"]
            if entry != []:
                confirm_msg = self.msg.show_message1("Confirm Delete", "Are you sure you want to delete all your diaries")
                if confirm_msg == "&Yes":
                    db.delete_all(self.user)
                    self.ui.diaryList.clear()
                    self.show_all_diary()
                else:
                    pass
            else:
                self.msg.show_message("No Notes", "No Notes to Clear")
        else:
            print("user not found")
    
    def delete(self):
        db = DiaryDB()
        tag = self.get_tag()
        confirm_msg = self.msg.show_message1("Confirm Delete", "Are you sure you want to delete this diary?")
        if confirm_msg == "&Yes":
            db.delete_entry(self.user, tag)
            self.ui_format()
        else:
            return

    def check_remember_me(self):
        remember_me_state = self.ui.remeberMe.checkState()
        if remember_me_state == 0:
            remember_me = False
        else:
            remember_me = True
        return remember_me    

    def gui_remember_me(self):
        db = DiaryDB()
        username = db.retrieve_user()
        remember_val = db.retrieve_remember_from_db(username)
        if remember_val:
            self.ui.stackedWidget.setCurrentWidget(self.ui.dairyHomePage)
            # self.ui.diaryList.clear()
            self.ui.greetingLabel.setText(f"Welcome {username.title()} To Your Dairy")
            self.show_all_diary()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
            
    def show_side_bar(self):
        print(True)
        sidebar = SideBar_Ui()
        sidebar.setupUi(self.ui.dairyHomePage)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainApp()
    myapp.show()
    sys.exit(app.exec_())