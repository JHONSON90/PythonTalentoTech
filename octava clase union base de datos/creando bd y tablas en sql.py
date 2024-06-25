#creando bd y tablas en sql
#!primero vamos a instalar la conexion a mysql con el siguiente comando pip install mysql-connector-python 
 # vamos a unir nuestra base de datos de sql con python
import mysql.connector
import time
 
def connect_to_mysql(config, attempts=3, delay=2):
    attempt = 1
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if attempt == attempts:
                # Attempts to reconnect failed; returning None
                print("Failed to connect, exiting without a connection:", err)
                return None
            print("Connection failed:", err, ". Retrying (", attempt, "/", attempts - 1, ")...")
            # progressive reconnect delay
            time.sleep(delay ** attempt)
            attempt += 1
    return None

config2 = {
"host" : "localhost",
"user" : "root",
"password" : "1085917679JHon"
}
# llamamos la funcion y le pasamos los datos
mydb = connect_to_mysql(config2)
 
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE usuarios")