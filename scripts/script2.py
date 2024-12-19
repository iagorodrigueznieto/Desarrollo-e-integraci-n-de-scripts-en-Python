from pymongo import MongoClient
import pandas as pd


client = MongoClient("mongodb://localhost:27017/")  
db = client['citybik']
collection =db['stations']

pipeline = [
    {
        "$project": {
            "_id": 0,
            "id": 1, 
            "name": 1,
            "timestamp": 1,
            "free_bikes": 1,
            "empty_slots": 1,
            "uid": 1,
            "last_updated": 1,
            "slots": 1,
            "normal_bikes": 1,
            "ebikes": 1
        }
    }
]

estaciones = collection.aggregate(pipeline)
df=pd.DataFrame(list(estaciones))
client.close()

df.to_parquet('output/bicis.parquet')
df.to_csv('output/bicis.csv')
print('Se han creado los datasets')