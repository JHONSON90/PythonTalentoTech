import mysql.connector

#! creamos la clase de empleado

class Empleado: 
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargp = cargo
        self.salario = salario
        
    @staticmethod
    def conectar_bd():
        host='localhost',
        user='root',
        password='1085917679JHon',
        database='gestion_empleados'