import datetime
from message_box import MessageBox
from pymongo import MongoClient, errors

class DiaryDB:
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
        self.var = ""
        self.tag = 0 
        
    def add_diary(self, username, content, tag):
        current_timestamp = datetime.datetime.now().strftime("Date: %d/%m/%Y, Time: %H:%M:%S")
        
        update_dictionary = {"timestamp" : current_timestamp, "content" : content, "tag": tag}
        
        user = self.collection.find_one({"username" : username})

        if user:
            db_filter = {"username" : username} 
            update_query = {"$push" : {"entry" : update_dictionary}}      
            
            self.collection.update_one(db_filter, update_query)
            self.var = "Added"

    def update_diary_entry(self, username, new_content, current_tag, new_tag,):

    # Find the user by username
        user = self.collection.find_one({"username": username})
        timestamp = datetime.datetime.now().strftime("Date: %d/%m/%Y, Time: %H:%M:%S")
        if user:
            entry_to_update = next((entry for entry in user["entry"] if entry["tag"] == current_tag), None)

            if entry_to_update:
                # Update the entry with the new content and timestamp
                entry_to_update["content"] = new_content
                entry_to_update["timestamp"] = timestamp
                entry_to_update["tag"] = new_tag

                # Update the document in the collection
                db_filter = {"username": username, "entry.tag": current_tag}
                update_query = {"$set": {"entry.$": entry_to_update}}

                self.collection.update_one(db_filter, update_query)
                print("Diary entry updated successfully.")
                self.var = "Updated"
            else:
                print("Entry with the provided tag not found.")
        else:
            print("User does not exist.")        
    
    def delete_entry(self, username, current_tag):
        user = self.collection.find_one({"username" : username})       
        if user:
            entry_to_delete = next((entry for entry in user["entry"] if entry["tag"] == current_tag), None)
            print(entry_to_delete)
            if entry_to_delete:
                db_filter = {"username": username, "entry.tag": current_tag}
                update_query = {"$pull": {"entry": {"tag": current_tag}}}
                self.collection.update_one(db_filter, update_query)
            else:
                pass
        else:
            print("error")

    def delete_all(self, username):
        user = self.collection.find_one({"username" : username})
        if user:
            db_filter = {"username": username}
            update = {"$set": {"entry": []}}
            self.collection.update_one(db_filter, update)       

    def check_tags(self, username):
        user = self.collection.find_one({"username": username})
        
        if user:
            existing_tags = {tag["tag"] for tag in user.get("entry", [])}
            
            new_tag = self.get_unique_tag(existing_tags)
            
            return new_tag
            
            # Now you can use 'new_tag' for further processing or assignment

    def get_unique_tag(self, existing_tags):
        all_tags = set(range(10000))  # Assuming you have 1000 possible tags
        
        available_tags = all_tags - existing_tags
        
        if available_tags:
            return available_tags.pop()
        else:
            print("No more unique tags available.")
            return None

    def add_remember_to_db(self, remember_me, username):
        user = self.collection.find_one({"username": username})
        if user:
            db_filter = {"username": username}
            update = {"$set": {"remember_me": remember_me}}
            self.collection.update_one(db_filter, update)

    def retrieve_remember_from_db(self, username):
        user = self.collection.find_one({"username": username})
        if user:
            remember_value = user["remember_me"]
            print(remember_value)
            return remember_value
        
    def retrieve_user(self):
        user = self.collection.find_one()
        if user:
            username = user["username"]
            return username        
