import pymongo
import os
from os import path
if path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get('MONGO_URI') 
#MONGODB_URI = os.getenv(MONGO_URI)
#MONGODB_URI = "mongodb+srv://root:Sock8sold@myfirstcluster-pxgx9.mongodb.net/myTestDB?retryWrites=true&w=majority"

DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#new_doc = {'first': 'douglas', 'last': 'adams', 'dob':'11/03/1952', 'gender': 'm', hair_color': 'grey', 'occupation': 'writer', 'nationality': 'english'}
#coll.insert(new_doc)
#documents = coll.find()

#new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob':'28/04/1948', 'gender': 'm','hair_color': 'no much', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'dob':'20/09/1948', 'hair_color': 'white', 'occupation': 'writer', 'nationality': 'american'}]
#coll.insert_many(new_docs)
#documents = coll.find()

#documents = coll.find({'first': 'douglas'})

#documents = coll.remove({'first': 'douglas'})

#documents = coll.update_one({'nationality': 'american'}, {'$set': {'hair_color': 'maroon'}})
documents = coll.update_many({'nationality': 'american'}, {'$set': {'hair_color': 'maroon'}})

documents = coll.find({'nationality': 'american'})

#documents = coll.find()


for doc in documents:
    print(doc)
