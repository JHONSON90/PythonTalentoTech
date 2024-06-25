
# EJEMPLO PANDAS SERIES , CREACION DE SERIES DESDE ARRAYS

# creando series de listas
import pandas as pd
s = pd.Series(['Mark', 'Justin', 'John', 'Vicky'])
print(s)

print("series de listas con numero")
import pandas as pd
s = pd.Series(['Mark', 'Justin', 'John', 'Vicky'], dtype="string")
print(s)

s = pd.Series(['Mark', 'Justin', 'John', 'Vicky'], index=[222,333,444,555], dtype='string')
print(s)

notas = [5.7,8.5,9.1,5.5,8.2,9.0,10,7.0,7.7,9.9]
estudiantes = ["Juan","Jenifer","David","Pablo","Armando","Magdalena","Francesca","Rosmery","Vicente","Martin"]

s=pd.Series(notas, index=estudiantes)
print(s)
### CREACION DE SERIES DEDE ARRAYS CON NUMPY
import numpy as np

a = np.array([1,2,3,4,5])

print(pd.Series(a));


print("Tipo de datos del array de NumPy:", a.dtype)

# Convertir el array de NumPy en una Serie de Pandas y mostrarla
serie = pd.Series(a)
print(serie)