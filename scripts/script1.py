import requests
import time
import pymongo
from datetime import datetime
import pandas as pd


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["citybik"]
collection = db["stations"]
while True: 
    url_api = "http://api.citybik.es/v2/networks/bicicorunha"  
    response=requests.get(url_api)
    json=response.json()
    estaciones=json['network']['stations']
    try:
        result = collection.insert_many(estaciones)
        print('Informacion insertada con exito')
    except Exception as e:
        print("Error inserting"+ str(e))
    time.sleep(300) 