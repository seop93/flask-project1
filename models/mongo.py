import os
from pymongo import MongoClient

mongo_username = os.environ.get('MONGO_USERNAME')
mongo_password = os.environ.get('MONGO_PASSWORD')

client = MongoClient('ec2-15-165-48-208.ap-northeast-2.compute.amazonaws.com', 27017, username=mongo_username, password=mongo_password)

def conn_mongodb():
    db = client.online_store
    return db



