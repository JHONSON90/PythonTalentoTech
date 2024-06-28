import pandas as pd
import numpy as np

data = pd.read_csv('analisis_de_datos/ardillas.csv')

print(data.head())
print(data.tail())
print(data.describe())
print(data.describe(include="all"))
print(data.info())

# para editar las filas de los dataframes podemos usar este comando 

data["Hectare Squirrel Number"]= data["Hectare Squirrel Number"]+1

#usamos dropna() para eliminar los datos que no son validos o que tienen na 
#para el ejemplo vamos a quitar las ardillas que no tengan edad age

#! data.dropna(subset=["Age"], axis=0, inplace=True)
#! print(data.head())

#para remplazar los valores no validos se utilizaria la funcion replace
"""
mean = data["Hectare Squirrel Number"].mean()
data["Hectare Squirrel Number"].replace(np.nan, mean)
print(data.head())
"""

#? correccion de datos

#! cambiar tipo de datos de una columna
"""
df["Ciudad-mpg"] = 235/df["Ciudad-mpg"] divide el valor original a (235/ el valor que estaba en la celda)
df.rename(columns={"city_mpg": "City-L/100km"}, inplace=true cambia el nombre de la columna algo importante es el inplace hace los cambios al dataframe original 

dt["Price"]= df["Price"].astype("int")
"""