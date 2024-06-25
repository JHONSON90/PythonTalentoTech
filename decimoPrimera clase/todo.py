# calculadora

# vamos a utilizar el button.grid para definir la ubicacion exacta donde va a ir nuestro boton pero inicialmente tenemos que 

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Widgets with TKINTER")
window.geometry("800x700")
#para el tamaño de la ventana tambien puedo cambiarlo con 
#window.config(width=400, height=400)
#window.minsize(width=400, height=400)

#! LABELS 
my_label = ttk.Label(window, text=
"Hello World!"
, font=("Arial"
, 24))
my_label2 = ttk.Label(window, text=
"Hello World!"
, font=("Arial"
, 24))
# En una posición específica
# my_label.place(x=20, y=20)

#? En el centro de la ventana
my_label.pack(pady=10)
my_label2.pack(pady=20)#my_label.pack(pady=20, side="bottom")
my_label.config(foreground="red", background="black") # Coloca fondo y cambia el color de la letra del label
my_label.config(anchor="center")
my_label["text"] = "New Text"
my_label.config(text= "New Text 2")


#! botones

def button_clicked():
    print("Button was clicked!")
my_label.config(text= "Button was clicked!")
#my_label2.config(text=input.get())

# button = ttk.Button(window, text= "Click Me!")
button = ttk.Button(window, text= "Click Me!", command=button_clicked)
button.pack(pady=10)

window.mainloop()