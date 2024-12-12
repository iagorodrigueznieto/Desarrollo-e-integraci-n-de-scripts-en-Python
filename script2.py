import pandas as pd
from pymongo import MongoClient
import os

# Conectar a MongoDB (ajusta la URI de conexión si es necesario)
client = MongoClient("mongodb://localhost:27017")  # Cambia esto según tu configuración
db = client['city']  # Reemplaza con el nombre de tu base de datos
collection = db['bikes']  # Reemplaza con el nombre de tu colección

# Recuperar todos los documentos de la colección
documents = collection.find()

# Crear una lista de diccionarios para los campos seleccionados
data = []
for doc in documents:
    # Extraer los campos requeridos del documento
    record = {
        'id': doc.get('id'),
        'name': doc.get('name'),
        'timestamp': doc.get('timestamp'),
        'free_bikes': doc.get('free_bikes'),
        'empty_slots': doc.get('empty_slots'),
        'uid': doc.get('extra', {}).get('uid'),
        'last_updated': doc.get('extra', {}).get('last_updated'),
        'slots': doc.get('extra', {}).get('slots'),
        'normal_bikes': doc.get('extra', {}).get('normal_bikes'),
        'ebikes': doc.get('extra', {}).get('ebikes')
    }
    data.append(record)

# Cargar los datos en un DataFrame de pandas
df = pd.DataFrame(data)

# Asegurarse de que los directorios para guardar los archivos existen
output_dir = 'output_files'
os.makedirs(output_dir, exist_ok=True)

csv_file = os.path.join(output_dir, 'bikes_data.csv')
df.to_csv(csv_file, index=False)

parquet_file = os.path.join(output_dir, 'bikes_data.parquet')
df.to_parquet(parquet_file, index=False, engine='pyarrow')

print(f"Datos exportados a {csv_file} y {parquet_file}")
