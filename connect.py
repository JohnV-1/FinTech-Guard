from pymongo import MongoClient
from cassandra.cluster import Cluster

def connect_mongo():
    try:
        # Conexión al contenedor local de MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["fintech_guard"]
        print("Conexión exitosa a MongoDB.")
        return db
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")




if __name__ == "__main__":
    db_mongo = connect_mongo()
