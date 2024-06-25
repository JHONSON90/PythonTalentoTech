#? creacion de dataframes

import pandas as pd
import numpy as np

datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
'edad':[18, 22, 20, 21],
'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
 }

df = pd.DataFrame(datos)

print (df)

#crear un dataframes con un indice personalizado

datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
'edad':[18, 22, 20, 21],
'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
 }

df = pd.DataFrame(datos, index=[2,4,6,8])

print (df)

#crear data frames de listas de listas

df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df)


#crear dataframes desde lista de diccionarios y con idex personalizado
df = pd.DataFrame([
    {
        'Nombre':'María',
        'Edad':18
    },
    {
        'Nombre':'Luis',
        'Edad':22
    },
    {
        'Nombre':'Carmen'
    }
  ],
  index = ['primero', 'segundo','tercero'])
print(df)

# si queremos que lo cree con indice por defecto seria asi
df = pd.DataFrame([{'Nombre':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])
print(df)

#creando dataframes desde arrays de numpys

arr = np.array([1,2,3,4,5], dtype='int')
df = pd.DataFrame((arr), )
print(df)

#? uniendo dataframes desde arrays y listas
arr = np.array([1,2,3,4,5], dtype='int')
df = pd.DataFrame((arr, [5,4,3,2,1]), )
print(df)


#dataframes desde archivos de excel o csv

df = pd.read_csv("weather_data.csv")
print(df.head());

"""
un pequeño listado de los atributos de los dataframes
https://pandas.pydata.org/docs/reference/frame.html

.info()
.shape
.size
.columns
.index
.head(n)
.tail(n)
.values
.axes
.at[m, n]
"""

print(df);

#print(df.info())
print(df.shape) #imprime una tupla con el numero defilas y columnas que tiene el frem
print(df.columns)
print(df.index)
print(df.head(3))
print(df.tail(3))
print(df.values)
print(df.axes)
print(df.at[1,"Condition"])



print(df.Temp.mean()) #saca el promedio del segundo dato proporcionado por ejemplo en el primer caso es el de la columna temperatura
print(df["Temp"].mean()) #saca el promedio pero la forma de acceder a los datos es diferente esta esta mediante corchete
print(df.Temp.max()) #trae el maximo de la columna Temp tambien se puede acceder mediante los corchetes
print(df.Temp.min()) #trae el minimo de la columna
print(df[df.Temp == df.Temp.max()]) # compara cada dato con el maximo y trae el dato
print(df[df.Temp == df.Temp.min()]) # compara cada dato con el minimo y trae el dato


#para exportar un data frame se lo puede hacer mediante esta linea de codigo data.to_csv("new_data.csv")