# aplicar funcion a series
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
def cuadrado(x):
    return x ** 2

# Aplicar la función a cada elemento de la Serie utilizando apply()
resultado = s.apply(cuadrado)

# Imprimir el resultado
print(resultado)

#filtros a series

import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
# Crear una máscara booleana para filtrar los elementos mayores que 2
mascara = s > 2

# Aplicar la máscara booleana para filtrar la Serie
resultado = s[mascara]

# Imprimir el resultado
print(resultado)


s = pd.Series({'Matemáticas': 6.0,
'Economía': 4.5,
'Programación': 8.5})

mascara1= s > 5
print(s[mascara1])

# ordenar una serie
s = pd.Series({'Matemáticas': 6.0,
'Economía': 4.5,
'Programación': 8.5})
print(s.sort_values(),"oderdenada por valores")
print(s.sort_index(ascending = False))# orden descendente

# eliminar datos nulos
import numpy as np
s = pd.Series(['a','b', None,'c', np.NaN,'d'])
s_n= s.dropna()
print(s_n)
