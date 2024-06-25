import mysql.connector

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    @staticmethod
    def conectar_bd():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="ejemplobd"
        )

    @staticmethod
    def crear_tabla():
        conn = Empleado.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                          (id INT AUTO_INCREMENT PRIMARY KEY,
                           nombre VARCHAR(255) NOT NULL,
                           cargo VARCHAR(255) NOT NULL,
                           salario DECIMAL(10, 2) NOT NULL)''')
        conn.commit()
        conn.close()

    def guardar(self):
        conn = self.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO empleados (nombre, cargo, salario)
                          VALUES (%s, %s, %s)''', (self.nombre, self.cargo, self.salario))
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_empleados():
        conn = Empleado.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM empleados''')
        empleados = cursor.fetchall()
        conn.close()
        return empleados

    @staticmethod
    def obtener_empleado_por_nombre(nombre):
        conn = Empleado.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM empleados WHERE nombre = %s''', (nombre,))
        empleado = cursor.fetchone()
        conn.close()
        return empleado

    def actualizar(self):
        conn = self.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''UPDATE empleados SET cargo = %s, salario = %s WHERE nombre = %s''',
                       (self.cargo, self.salario, self.nombre))
        conn.commit()
        conn.close()

    @staticmethod
    def borrar(nombre):
        conn = Empleado.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM empleados WHERE nombre = %s''', (nombre,))
        conn.commit()
        conn.close()

# Crear la tabla de empleados si no existe
Empleado.crear_tabla()

# Ejemplo de uso
# Crear un nuevo empleado
empleado1 = Empleado('Juan', 'Gerente', 5000)
empleado1.guardar()

# Obtener todos los empleados
print("Empleados:")
print(Empleado.obtener_empleados())

# Obtener un empleado por nombre
print("\nEmpleado por nombre:")
print(Empleado.obtener_empleado_por_nombre('Juan'))

# Actualizar el cargo y salario de un empleado
empleado1.cargo = 'Director'
empleado1.salario = 6000
empleado1.actualizar()

print("\nEmpleado actualizado:")
print(Empleado.obtener_empleado_por_nombre('Juan'))

# Borrar un empleado
Empleado.borrar('Juan')

print("\nEmpleados después de borrar:")
print(Empleado.obtener_empleados())

