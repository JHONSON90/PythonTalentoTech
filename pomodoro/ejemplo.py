import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Crear un frame
frame = tk.Frame(ventana)

# Agregar un título al frame
titulo = tk.Label(frame, text="Título del Frame")
titulo.pack()

# Agregar más widgets al frame
# ...

# Mostrar el frame en la ventana
frame.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()