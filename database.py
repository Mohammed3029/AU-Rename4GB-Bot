from pymongo import MongoClient
from config import Config

class Database:
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(Config.MONGO_URL)
        self.db = self.client["rename4gb"]

    def get_user(self, user_id):
        return self.db.users.find_one({"_id": user_id}) or {}

    def set_user(self, user_id, data):
        self.db.users.update_one({"_id": user_id}, {"$set": data}, upsert=True)

db = Database()
