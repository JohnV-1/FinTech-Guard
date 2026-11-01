# FinTech Guard: Sistema de Detección de Fraudes Financieros

## Descripción del Proyecto
FinTech Guard es una aplicación diseñada para ayudar a identificar posibles fraudes financieros mediante el análisis de información de clientes, cuentas bancarias, tarjetas y transacciones. Está dirigida a analistas de seguridad de instituciones financieras, permitiéndoles consultar expedientes, revisar operaciones sospechosas e identificar redes de fraude.

Este proyecto integra tres bases de datos NoSQL, cada una con un propósito específico:
*   **MongoDB:** Para consultar la información de clientes, cuentas, tarjetas y reportes de riesgo.
*   **Dgraph:** Para encontrar conexiones y relaciones entre personas, cuentas y dispositivos.
*   **Cassandra:** Para consultar historiales de transacciones, transferencias, accesos y alertas de fraude ordenados por fecha.

## Estructura del Proyecto

El repositorio sigue la siguiente estructura de carpetas y archivos:

```text
FinTech-Guard/
├── Cassandra/
├── Mongo/
├── Dgraph/
├── data/
├── connect.py
├── populate.py
├── main.py
└── README.md
```

## Descripción de Directorios y Archivos

*   **`Cassandra/`, `Mongo/`, `Dgraph/`**: Estos directorios contendrán los esquemas, modelos o definiciones específicas requeridas para interactuar con cada una de las bases de datos respectivas.
*   **`data/`**: Esta carpeta se usará para guardar o generar los datos de prueba. Los datos se manejarán principalmente en formato JSON, pudiendo utilizar herramientas como la librería `Faker` en Python o archivos CSV/JSON preexistentes.
*   **`connect.py`**: Archivo principal para la configuración de la infraestructura. Aquí se establecerán las conexiones a las tres bases de datos. Está diseñado para integrarse preferentemente levantando los contenedores de Docker de MongoDB y Cassandra (y Dgraph).
*   **`populate.py`**: En esta fase del proyecto, este archivo contendrá únicamente comentarios estructurados que describirán paso a paso la estrategia y lógica sobre cómo se planea poblar cada una de las bases de datos con los datos de prueba.
*   **`main.py`**: Archivo de entrada de la aplicación. Por el momento, su función será imprimir en consola el menú interactivo con todas las consultas planeadas para el proyecto (según los requerimientos definidos), aunque aún no contendrá la lógica funcional de ejecución.

## Guía de Instalación

Sigue estos pasos para descargar y configurar el proyecto en tu entorno local:

1. Clonar el repositorio:
```bash
git clone https://github.com/JohnV-1/FinTech-Guard.git
```   
2. Ingresar a la carpeta del proyecto
```bash
cd FinTech-Guard
```  
3. Crear el entorno virtual:
```bash
python3 -m venv venv
```   
4. Activar el entorno virtual
* En Windows
```bash
venv\Scripts\activate
```
* En Mac/Linux
```bash
source venv/bin/activate
```
5. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```
6.Requisitos de Bases de Datos (Docker):<br>
Antes de correr el código (connect.py o main.py), asegúrate de tener Docker instalado y los contenedores de MongoDB, Cassandra y Dgraph corriendo en tu máquina local.<br>
**Puertos de cada base de datos:**
- Cassandra: 9042:9042
- Mongodb: 27017:27017
- Dgraph: 8080:8080
