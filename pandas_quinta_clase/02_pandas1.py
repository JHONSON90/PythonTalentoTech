#ya instalado pandas mediante pip install pandas
#para utilizarlo podemos hacer la importacion

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["Day"], data["Temp"], data["Condition"]);#de esta manera accedemos a las columnas de la tabla

#asi podemos crear series o columnas 
#? desde listas
s = pd.Series(["Nombres", "Mark", "Justin", "Jhon", "Vicky"]) #si lo creamos asi nos va crear un objeto
print(s) 

xs = pd.Series(["Nombres", "Mark", "Justin", "Jhon", "Vicky"], dtype = "string")
print(xs) #asi creamos unos estrings

s = pd.Series(['Mark', 'Justin', 'John', 'Vicky'], index=[222,333,444,555], dtype='string') #asi colocamos el indice donde queremos los nuevos datos
print(s) 

#crearemos un cuadro de notas en flotante y en index los nombres de cada estudiante
print(pd.Series([5.7,8.5,9.1,5.5,8.2,9.0,10,7.0,7.7,9.9],index=["Juan","Jenifer","David","Pablo","Armando","Magdalena","Francesca","Rosmery","Vicente","Martin"]))


#? Numpy
import numpy as np

a = np.array([1,2,3,4,5])

print(pd.Series(a));