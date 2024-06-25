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
            database="gestion_empleados"
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

    def actualizar(self, id):
        conn = self.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''UPDATE empleados SET nombre = %s, cargo = %s, salario = %s WHERE id = %s''',
                       (self.nombre, self.cargo, self.salario, id))
        conn.commit()
        conn.close()

    @staticmethod
    def borrar(id):
        conn = Empleado.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM empleados WHERE id = %s''', (id,))
        conn.commit()
        conn.close()
# empezamos a desarrollar la interfaz

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados")
        
        self.nombre_var = tk.StringVar()
        self.cargo_var = tk.StringVar()
        self.salario_var = tk.StringVar()
        
        self.crear_widgets()
        self.mostrar_empleados()
    
    def crear_widgets(self):
        # Campos de entrada
        tk.Label(self.root, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Cargo").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.cargo_var).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Salario").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.salario_var).grid(row=2, column=1, padx=10, pady=10)
        
        # Botones
        tk.Button(self.root, text="Agregar", command=self.agregar_empleado).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Actualizar", command=self.actualizar_empleado).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Borrar", command=self.borrar_empleado).grid(row=3, column=2, padx=10, pady=10)
        
        # Lista de empleados
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Cargo", "Salario"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cargo", text="Cargo")
        self.tree.heading("Salario", text="Salario")
        self.tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.seleccionar_empleado)
    #metodos
    
    def mostrar_empleados(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        empleados = Empleado.obtener_empleados()
        for empleado in empleados:
            self.tree.insert("", "end", values=empleado)
    
    def agregar_empleado(self):
        nombre = self.nombre_var.get()
        cargo = self.cargo_var.get()
        salario = self.salario_var.get()
        if nombre and cargo and salario:
            empleado = Empleado(nombre, cargo, float(salario))
            empleado.guardar()
            self.mostrar_empleados()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
    
    def actualizar_empleado(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            id_empleado = self.tree.item(seleccionado)["values"][0]
            nombre = self.nombre_var.get()
            cargo = self.cargo_var.get()
            salario = self.salario_var.get()
            if nombre and cargo and salario:
                empleado = Empleado(nombre, cargo, float(salario))
                empleado.actualizar(id_empleado)
                self.mostrar_empleados()
                self.limpiar_campos()
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para actualizar")
    
    def borrar_empleado(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            id_empleado = self.tree.item(seleccionado)["values"][0]
            Empleado.borrar(id_empleado)
            self.mostrar_empleados()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para borrar")
    
    def seleccionar_empleado(self, event):
        seleccionado = self.tree.selection()
        if seleccionado:
            empleado = self.tree.item(seleccionado)["values"]
            self.nombre_var.set(empleado[1])
            self.cargo_var.set(empleado[2])
            self.salario_var.set(empleado[3])
    
    def limpiar_campos(self):
        self.nombre_var.set("")
        self.cargo_var.set("")
        self.salario_var.set("")

if __name__ == "__main__":
    Empleado.crear_tabla()
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
