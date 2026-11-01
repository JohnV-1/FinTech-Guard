from pymongo import MongoClient
from cassandra.cluster import Cluster
import pydgraph

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


def connect_dgraph():
    try:
        # Conexión al contenedor local de Dgraph
        stub = pydgraph.DgraphClientStub("localhost:9080")
        client = pydgraph.DgraphClient(stub)

        # Hacemos una consulta sencilla para comprobar la conexión
        txn = client.txn(read_only=True)
        try:
            txn.query("{ test(func: uid(0x1)) { uid } }")
        finally:
            txn.discard()

        print("Conexión exitosa a Dgraph.")
        return client

    except Exception as e:
        print(f"Error conectando a Dgraph: {e}")
        return None


if __name__ == "__main__":
    db_mongo = connect_mongo()
    session_cassandra = connect_cassandra()
    client_dgraph = connect_dgraph()
