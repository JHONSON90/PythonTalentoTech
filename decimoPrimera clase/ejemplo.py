import tkinter as tk
from tkinter import ttk

class Distancia(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.etiqueta_dist_km = ttk.Label(parent, text='Distancia en Km:')
        self.etiqueta_dist_km.place(x=20, y=20)
        
        self.caja_dist_km = ttk.Entry(parent)
        self.caja_dist_km.place(x=140, y=20, width=60)
        
        self.boton_convertir = ttk.Button(parent, text='Convertir', command = self.convertir_dist)
        self.boton_convertir.place(x=20, y=60)
        
        self.etiqueta_millas = ttk.Label(parent, text='Distancia en Millas: ')
        self.etiqueta_millas.place(x=40, y=120)
        
        self.etiqueta_metros = ttk.Label(parent, text='Distancia en Metros: ')
        self.etiqueta_metros.place(x=40, y=160)
        
        self.etiqueta_pies = ttk.Label(parent, text='Distancia en Pies: ')
        self.etiqueta_pies.place(x=40, y=180)
        
    def convertir_dist(self):
        dist_km = float(self.caja_dist_km.get())
        
        dist_millas = dist_km / 1.609
        dist_metros = dist_km * 1000
        dist_pies = dist_km * 3280.84
        
        self.etiqueta_millas.config(text=f'Distancia en Millas: {dist_millas}')
        self.etiqueta_metros.config(text=f'Distancia en Metros: {dist_metros}')
        self.etiqueta_pies.config(text=f'Distancia en Pies: {dist_pies}')
        
ventana = tk.Tk()
ventana.title("Convertidos distancias")
ventana.config(width=400, height=300)

app = Distancia(ventana)

ventana.mainloop()

#https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm  -> widgets disponibles con sus propiedades

