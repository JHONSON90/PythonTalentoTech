import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "1085917679JHon"
)

my_cursor = conexion.cursor()
my_cursor.execute("SHOW DATABASES")
for dataBase in my_cursor:
    print(dataBase)

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "1085917679JHon",
    database="sakila"
)

my_cursor = mydb.cursor()
my_cursor.execute("select * from actor")
my_result = my_cursor.fetchall()

for x in my_result:
    print(x)
    
my_cursor = mydb.cursor();

print("----------------------------------------------------------------")
sql =  '''
        SELECT *
        FROM actor
        WHERE upper(first_name) = "SCARLETT";
        '''

my_cursor.execute(sql);
my_result = my_cursor.fetchall();
for x in my_result:
    print(x)
    
#! insertando datos en las tablas

my_cursor = mydb.cursor();

sql = '''
insert into actor(first_name, last_name)
values("Scarlett", "Johansson")
        '''
my_cursor.execute(sql)

#? para confirmar que se hizo la modificacion vamos a meter un metodo llamado commit()

mydb.commit()
print(my_cursor.rowcount, "record inserted")

print("----------------------------------------------------------------")
sql =  '''
        SELECT *
        FROM actor
        WHERE upper(first_name) = "SCARLETT";
        '''

my_cursor.execute(sql);
my_result = my_cursor.fetchall();
for x in my_result:
    print(x)
    
#! para cerrar la conexion solo es necesario utilizar el metodo close()

my_cursor.close()

#! haciendo varios intentos de conexion al servidor con lapso de tiempo

import time

config = {
"host" : "localhost",
"user" : "root",
"password" : "None", # provocamos el error por que la contraseña no es la correcta para hacer el ejemplo
"database" : "sakila"
}
#? vamos a colocar que lo realice en tres intentos y con un lapso de tiempo de 2 segundos de lo contrario nos mostrara el error
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

mydb = connect_to_mysql(config)

# vamos a utilizar la funcion pero con los datos bien para que pueda hacer la conexion 

config2 = {
"host" : "localhost",
"user" : "root",
"password" : "1085917679JHon", # provocamos el error por que la contraseña no es la correcta para hacer el ejemplo
"database" : "sakila"
}
# llamamos la funcion y le pasamos los datos correctos
mydb = connect_to_mysql(config2)

#! haciendo consultas utilizando parametros

my_cursor2 = mydb.cursor();
sql_query = '''
SELECT * 
FROM actor 
WHERE upper(first_name) = %s
OR upper(first_name) = %s;
'''

sql_data = ("SCARLETT", "CUBA");
my_cursor2.execute(sql_query, sql_data);
my_result = my_cursor2.fetchall();

for x in my_result:
    print(x)
    

#! haciendo consultas utilizando parametros cambiando la impresion

my_cursor2.execute(sql_query, sql_data);
my_result = my_cursor2.fetchall();pip install mysql-connector-python

for x in my_result:
    print(f"Su nombre es {first_name}, y su apellido es {last_name}".format(first_name, last_name))
