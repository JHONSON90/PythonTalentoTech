import tkinter as tk
from tkinter import messagebox

class GestionEstudiantesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Estudiantes")

        # Etiquetas
        self.lbl_nombre = tk.Label(root, text="Nombre")
        self.lbl_nombre.grid(row=0, column=0)

        self.lbl_apellido = tk.Label(root, text="Apellido")
        self.lbl_apellido.grid(row=0, column=2)

        self.lbl_edad = tk.Label(root, text="Edad")
        self.lbl_edad.grid(row=1, column=0)

        self.lbl_carrera = tk.Label(root, text="Carrera")
        self.lbl_carrera.grid(row=1, column=2)

        # Entradas
        self.nombre_texto = tk.StringVar()
        self.entrada_nombre = tk.Entry(root, textvariable=self.nombre_texto)
        self.entrada_nombre.grid(row=0, column=1)

        self.apellido_texto = tk.StringVar()
        self.entrada_apellido = tk.Entry(root, textvariable=self.apellido_texto)
        self.entrada_apellido.grid(row=0, column=3)

        self.edad_texto = tk.StringVar()
        self.entrada_edad = tk.Entry(root, textvariable=self.edad_texto)
        self.entrada_edad.grid(row=1, column=1)

        self.carrera_texto = tk.StringVar()
        self.entrada_carrera = tk.Entry(root, textvariable=self.carrera_texto)
        self.entrada_carrera.grid(row=1, column=3)

        # Listbox y Scrollbar
        self.lista = tk.Listbox(root, height=6, width=35)
        self.lista.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.barra_desplazamiento = tk.Scrollbar(root)
        self.barra_desplazamiento.grid(row=2, column=2, rowspan=6)

        self.lista.configure(yscrollcommand=self.barra_desplazamiento.set)
        self.barra_desplazamiento.configure(command=self.lista.yview)

        # Botones
        self.btn_ver_todos = tk.Button(root, text="Ver Todos", width=12)
        self.btn_ver_todos.grid(row=2, column=3)

        self.btn_buscar_entrada = tk.Button(root, text="Buscar Entrada", width=12)
        self.btn_buscar_entrada.grid(row=3, column=3)

        self.btn_agregar_entrada = tk.Button(root, text="Agregar Entrada", width=12)
        self.btn_agregar_entrada.grid(row=4, column=3)

        self.btn_actualizar_seleccionado = tk.Button(root, text="Actualizar Seleccionado", width=12)
        self.btn_actualizar_seleccionado.grid(row=5, column=3)

        self.btn_eliminar_seleccionado = tk.Button(root, text="Eliminar Seleccionado", width=12)
        self.btn_eliminar_seleccionado.grid(row=6, column=3)

        self.btn_cerrar = tk.Button(root, text="Cerrar", width=12, command=root.destroy)
        self.btn_cerrar.grid(row=7, column=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionEstudiantesApp(root)
    root.mainloop()
