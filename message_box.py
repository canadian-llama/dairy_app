from PyQt5.QtWidgets import QMessageBox


class MessageBox:
    @staticmethod
    def show_message(title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        msg.setText(message)
        
        msg.setWindowTitle(title)
        
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        msg.exec()
        
        clicked_btn = msg.clickedButton()
        
        if clicked_btn:
            button_text = clicked_btn.text()
        
            return button_text
        
    @staticmethod
    def show_message1(title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        msg.setText(message)
        
        msg.setWindowTitle(title)
        
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        
        msg.exec()
        
        clicked_btn = msg.clickedButton()
        
        if clicked_btn:
            button_text = clicked_btn.text()
        
            return button_text
        