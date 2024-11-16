from message_box import MessageBox
import hmac
from pymongo import MongoClient, errors
import hashlib, os

class AuthDB:
    def __init__(self):
        self.msg_box = MessageBox()
        try:
            connection_string = "mongodb://localhost:27017/"
            self.client = MongoClient(connection_string)
            self.db = self.client.users_db
            self.collection = self.db.users
        except errors:
            print(errors)
            self.msg_box("Error", "Can't contact server at the moment contact your admin")
        self.salt = os.urandom(16)
        self.var = ""
        self.tag = 0   

    def create_user(self, username, password):
        pwd = password
        encrypted_pwd = self.encrypt_password(pwd)
        self.collection.insert_one({"username" : username, "salt" : self.salt, "password": encrypted_pwd, "entry" : [], "remember_me": False})
        
    def encrypt_password(self, password): 
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), self.salt, 100000)
        return hashed_password       

    def decrypt_password(self, password, hashed_password, salt):
        return hmac.compare_digest(hashed_password, hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000))

    # sign up function checks if the password & retyped match then inserts into the db     
    def sign_up(self, username, password, retyped):
        if username != "" and password != "" and retyped != "":
            users = self.collection.find_one({"username": username})
            if users:
                self.var = "None"
                # print(users)
            else:
                if password == retyped:
                    self.create_user(username, password)
                    self.var = 'True'
                elif password != retyped: 
                    self.var = "False"
        else:
            self.var = "Unfilled"
        # print(self.var)
    
    def login(self, username, password, remember_me):                        
        if username != "" and password != " ":
            user = self.collection.find_one({"username": username})
            if user:
                salt = user["salt"]
                hashed_password = user["password"]
                pwd = self.decrypt_password(password, hashed_password, salt)
                if pwd:
                    self.var = "True"
                    self.add_remember_to_db(remember_me, username)
                elif not pwd:
                    self.var = "False"
            else:
                self.var = "None"
        else:
            self.var = "Unfilled"

