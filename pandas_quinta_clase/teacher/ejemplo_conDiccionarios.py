import pandas as pd

new_dict = {
    "Matemáticas" : 8.0,
    "Programación" : 7.7,
    "Inglés" : 8.2
}

#Índices automáticos tomados de las llaves del diccionario
m = pd.Series(new_dict)
print(m)

#Ejercitación generando Series random y operaciones con series
import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(2, 10, 8))# de NumPy para generar una matriz de números enteros aleatorios entre 2 (inclusive) y 10 (exclusive) con una longitud de 8 
p = pd.Series(np.random.randint(2, 10, 8))
print("--"*100)
print(s, p)
print(s * p)

import pandas as pd
s = pd.Series(range(10))
print("--"*100)
print(s)
# 

import pandas as pd# imprime el 10 con el index indicado
s = pd.Series(10, index=[0, 1, 2, 3, 4, 5])
print("--"*100)
print(s)

import pandas as pd
import numpy as np
s = pd.Series(np.linspace(1, 100, 10)) #generar un array de números que comienza en 1, termina en 100 y contiene 10 elementos igualmente espaciados entre sí.
print("--"*100)
print(s)

import pandas as pd
s = pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])# genera numeros del 1 al 20 en pasos de tres y asigna como index letras 
print("--"*100)
print(s)
