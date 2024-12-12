import pandas as pd
from pymongo import MongoClient
import os

client = MongoClient("mongodb://localhost:27017")  
db = client['city']  
collection = db['bikes']  

documents = collection.find()
print(client.list_database_names())
print(db.list_collection_names())


for x in collection.find(): 
    print(x)
