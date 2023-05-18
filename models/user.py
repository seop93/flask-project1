from .mongo import conn_mongodb
from datetime import datetime
from bson import ObjectId



class User():
    @staticmethod
    def insert_one(form_data):
        db = conn_mongodb()
        db.users.insert_one({
            'email': form_data['email'],
            'password': form_data['password'],
            'create_at': int(datetime.now().timestamp()),
            'update_at': int(datetime.now().timestamp())
        })


