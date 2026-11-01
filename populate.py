# ==========================================
# ESTRATEGIA DE POBLACIÓN DE BASES DE DATOS
# ==========================================
#LA CANTIDAD DE PERFILES Y TRANSACCIONES NO REPRESENTA EL NUMERO FINAL A CREAR PROBLABLEMENTE 
#SE CREEN MENOS DATOS 

# PASO 1: Generación de Datos
# - Utilizar la librería Faker de Python para generar 10,000 perfiles de clientes realistas (nombres, correos, RFC, direcciones).
# - Generar catálogos de entidades financieras: Cuentas, Tarjetas (con status de robada/activa) y Comercios.
# - Simular un historial de 50,000 transacciones y transferencias SPEI distribuidas en los últimos 6 meses, incluyendo casos anómalos para pruebas de fraude.
# - Guardar temporalmente estos datos en la carpeta data/ en formato JSON para mantener consistencia entre las tres bases de datos.

# PASO 2: Población en MongoDB (Expedientes y Entidades)
# - Leer el archivo JSON de clientes y cuentas.
# - Insertar en la colección 'customers' los documentos anidados que contengan los datos personales, listas de cuentas, tarjetas asociadas y niveles de riesgo.
# - Insertar en la colección 'merchants' los comercios y sus reportes de riesgo.

# PASO 3: Población en Cassandra (Historiales y Series de Tiempo)
# - Leer el archivo JSON de transacciones, transferencias y accesos (logins).
# - Insertar en la tabla 'transactions_by_card' para optimizar la búsqueda por card_id ordenado por fecha descendente.
# - Insertar en las tablas 'spei_sent_by_account' y 'spei_received_by_account'.
# - Insertar en la tabla 'fraud_alerts_by_date' utilizando la fecha como partition key y la hora como clustering key.

# PASO 4: Población en Dgraph (Grafo de Relaciones)
# - Definir el esquema (Schema) en Dgraph estableciendo los tipos de nodos: Customer, Account, Device, Merchant, IP.
# - Crear las relaciones bidireccionales y dirigidas (ej. <TRANSFERRED_TO>, <LOGGED_IN_FROM>, <USED_AT>).
# - Leer el JSON de relaciones e insertar los RDF triples iterando sobre las transacciones y accesos, conectando cuentas mediante transferencias y clientes mediante IPs/Dispositivos.