import tkinter as tk

from tkinter import ttk
"""
ventana = tk.Tk()

#Vamos a colocarle un titulo a la ventana y ajustar el ancho y alto los valores de estos estan en pixeles
ventana.title("Conversor de Temperatura")
ventana.config(width=400, height=300)

#! Funcion que convierte el input en kevin y farenheit

def convertir_temp():
    temp_celsius = float(caja_temp_celsius.get())
    temp_kelvin = temp_celsius + 273.15
    temp_fahrenheigt = temp_celsius*1.8 + 32
    etiqueta_temp_kevin.config(text=f'Temperatura en K: {temp_kelvin}')
    etiqueta_temp_Farenheit.config(text=f'Temperatura en F: {temp_fahrenheigt}')



#vamos a colocar un label en nuestra ventana
etiqueta_temp_celsius = ttk.Label(text='Temperatura en °C:')
etiqueta_temp_celsius.place(x=20, y=20)
#colocamos un input
caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=20, width=60)
#creamos el boton y le colocamos la funcion de convertir
boton_convertir = ttk.Button(text='Convertir', command=convertir_temp)
boton_convertir.place(x=20, y=60)
#creamos la etiqueta de transformar los datos en kevin y farenheit
etiqueta_temp_kevin = ttk.Label(text='Temperatura en K: n/a')
etiqueta_temp_kevin.place(x=20, y=120)

etiqueta_temp_Farenheit = ttk.Label(text='Temperatura en F: n/a')
etiqueta_temp_Farenheit.place(x=20, y=160)

ventana.mainloop()

"""


#? LA MISMA APLICACION CON CLASEs

class Aplicacion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.etiqueta_temp_celsius = ttk.Label(parent, text='Temperatura en °C:')
        self.etiqueta_temp_celsius.place(x=20, y=20)
        
        self.caja_temp_celsius = ttk.Entry(parent)
        self.caja_temp_celsius.place(x=140, y=20, width=60)
        
        self.boton_convertir = ttk.Button(parent, text='Convertir', command = self.convertir_temp)
        self.boton_convertir.place(x=20, y=60)
        
        self.etiqueta_temp_kevin = ttk.Label(parent, text='Temperatura en K: n/a')
        self.etiqueta_temp_kevin.place(x=20, y=120)

        self.etiqueta_temp_Farenheit = ttk.Label(parent, text='Temperatura en F: n/a')
        self.etiqueta_temp_Farenheit.place(x=20, y=160)
        
    def convertir_temp(self):
        temp_celsius = float(self.caja_temp_celsius.get())
            
        temp_kelvin = temp_celsius + 273.15
        temp_fahrenheigt = temp_celsius*1.8 + 32
            
        self.etiqueta_temp_kevin.config(text=f'Temperatura en K: {temp_kelvin}')
        self.etiqueta_temp_Farenheit.config(text=f'Temperatura en F: {temp_fahrenheigt}')
            
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)

app = Aplicacion(ventana)

ventana.mainloop()