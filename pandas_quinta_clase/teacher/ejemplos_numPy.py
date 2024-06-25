import pandas as pd


#Listado de notas
new_dict = {
"Matemáticas" : 8.0,
"Programación" : 7.7,
"Inglés" : 8.2
}
#Índices automáticos tomados de las llaves del diccionario
s = pd.Series(new_dict)
print(s)

# utilizando range
s = pd.Series(range(10))
print(s)

s = pd.Series(10, index=[0, 1, 2, 3, 4, 5])
print(s)

#Utilizando linspace de NumPy

import numpy as np
s = pd.Series(np.linspace(1, 100, 10))
print(s)
