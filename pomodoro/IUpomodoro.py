import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Temporizador Pomodoro")


# Configurar los frames
main_frame = tk.Frame(root)
main_frame.pack(padx=30, pady=30)

#cronometro
timer_frame = tk.Frame(main_frame)
timer_frame.pack(side=tk.TOP)

#dividir frame
bottom_frame = tk.Frame(main_frame)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

#frame de la izquierda
left_frame = tk.LabelFrame(bottom_frame, text="Botones")

left_frame.pack(side=tk.LEFT, padx=20,pady=20)

#frame de la derecha
rigth_frame = tk.LabelFrame(bottom_frame, text="Historial")
rigth_frame.pack(side=tk.RIGHT, padx=20,pady=20)

conteo_frame = tk.Frame(main_frame)
conteo_frame.pack(side=tk.BOTTOM)


# Añadir etiquetas para el cronómetro
timer_label = tk.Label(timer_frame, text="25:00", font=("Courier", 60))
timer_label.pack()

# Añadir botones
start_button = tk.Button(left_frame, text="Iniciar")
start_button.pack(padx=10, pady=10)
start_button.config(width=15)


pause_button = tk.Button(left_frame, text="Pausar")
pause_button.pack(padx=10, pady=10)
pause_button.config(width=15)

cancel_button = tk.Button(left_frame, text="Cancelar")
cancel_button.pack(padx=10, pady=10)
cancel_button.config(width=15)

# Añadir caja de texto para mostrar el historial
history_text = tk.Text(rigth_frame, width=40, height=10)
history_text.pack()

history_button = tk.Button(rigth_frame, text="Mostrar Historial")
history_button.pack(side=tk.RIGHT,padx=10, pady=10)
history_button.config(width=15)

graph_button = tk.Button(rigth_frame, text="Mostrar Gráfica")
graph_button.pack(side=tk.RIGHT,padx=10, pady=10)
graph_button.config(width=15)

label_pomodoro = tk.Label(conteo_frame, text="Conteo de Pomodoros 0", font=("Courier", 25))
label_pomodoro.pack()


# Iniciar el bucle principal de la aplicación
root.mainloop()

