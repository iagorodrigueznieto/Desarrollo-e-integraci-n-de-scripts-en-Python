from pymongo import MongoClient
import pandas as pd


client = MongoClient("mongodb://localhost:27017/")  
db = client["city"] 
collection = db["bikes"]  

# Obtener todos los documentos de la colección
documents = list(collection.find())

# Filtrar y normalizar los datos
filtered_data = []
for doc in documents:
    filtered_doc = {
        "id": doc.get("id"),
        "name": doc.get("name"),
        "timestamp": doc.get("timestamp"),
        "free_bikes": doc.get("free_bikes"),
        "empty_slots": doc.get("empty_slots"),
    }
    extra_data = doc.get("extra", {})
    filtered_doc.update({
        "uid": extra_data.get("uid"),
        "last_updated": extra_data.get("last_updated"),
        "slots": extra_data.get("slots"),
        "normal_bikes": extra_data.get("normal_bikes"),
        "ebikes": extra_data.get("ebikes"),
    })
    filtered_data.append(filtered_doc)

# Crear el DataFrame
df = pd.DataFrame(filtered_data)

# Exportar a CSV
output_csv_path = "filtered_output.csv"
df.to_csv(output_csv_path, index=False)

print(f"Archivo CSV generado: {output_csv_path}")