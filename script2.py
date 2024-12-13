import pymongo
import pandas as pd
import os
from datetime import datetime

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "city"
COLLECTION_NAME = "bikes"

client = pymongo.MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

required_fields = ["_id", "name", "timestamp", "free_bikes", "empty_slots", "uid", "last_updated", "slots", "normal_bikes", "ebikes"]

def cargar_datos():
    try:
        documentos = collection.find()

        datos = []
        for doc in documentos:
            doc["_id"] = str(doc["_id"]) if "_id" in doc else None
            filtered_data = {key: doc.get(key, None) for key in required_fields}
            if filtered_data.get("timestamp"):
                try:
                    filtered_data["timestamp"] = pd.to_datetime(filtered_data["timestamp"])
                except ValueError:
                    filtered_data["timestamp"] = None
            datos.append(filtered_data)

        df = pd.DataFrame(datos)

        print(f"Datos cargados correctamente: {len(df)} registros.")
        print(df.head())

        return df

    except pymongo.errors.PyMongoError as e:
        print(f"Error al acceder a MongoDB: {e}")
        return None

def exportar_datos(df):
    if df is not None and not df.empty:
        try:
            df.to_csv('datos_bicis.csv', index=False)
            print("Datos exportados a CSV correctamente.")

            df.to_parquet('datos_bicis.parquet', index=False)
            print("Datos exportados a Parquet correctamente.")

        except Exception as e:
            print(f"Error al exportar los datos: {e}")
    else:
        print("No hay datos para exportar.")

if __name__ == "__main__":
    df_bicis = cargar_datos()
    exportar_datos(df_bicis)