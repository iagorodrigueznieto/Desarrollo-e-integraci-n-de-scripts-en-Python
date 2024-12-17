import requests
import time
import pymongo
from datetime import datetime
import pandas as pd




client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["football"]
collection = db["matches"]
url_api = "https://www.thesportsdb.com/api/v1/json/3/eventslast.php?id=133602"  
minutos = 4320
try:
    while True:
        response = requests.get(url_api)
        datos = response.json()
        
        datos["timestamp"] = datetime.now()

        collection.insert_one(datos)
        print("Datos almacenados correctamente")
        time.sleep(minutos * 60)


except KeyboardInterrupt:
    print("Execución cancelada polo usuario.")
