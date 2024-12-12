import requests
import time
import pymongo
from datetime import datetime
import pandas as pd




client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["city"]
collection = db["bikes"]
url_api = "http://api.citybik.es/v2/networks/bicicorunha"  
minutos = 3 
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
