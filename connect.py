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

def connect_cassandra():
    try:
        # Conexión al contenedor local de Cassandra
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        # Crear keyspace si no existe
        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS fintech_guard 
            WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
        """)
        session.set_keyspace('fintech_guard')
        print("Conexión exitosa a Cassandra.")
        return session
    except Exception as e:
        print(f"Error conectando a Cassandra: {e}")


if __name__ == "__main__":
    db_mongo = connect_mongo()
    session_cassandra = connect_cassandra()
