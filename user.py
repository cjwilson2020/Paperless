from pymongo import MongoClient
# pprint library is used to make the output look more pretty
import pprint
import json 

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://cwilson:Cps41906243@cluster0-lftpp.gcp.mongodb.net/test")

db = client['paperless']



class User(object):

    def __init__(self):
        self.conn = client['paperless']['user_data']
        self.user = User

    def populate_user_data(self):
        db = self.conn['paperless']['user_data']
        userData = json.load(self.user)

        db.insert_one(userData)


    

