import pandas as pd
import numpy as np

# crea una serie de pandas a partir de la lista  [10,20,30,40,50] luego imprime la serie

numeros = pd.Series([10,20,30,40,50])
print(numeros)


#crea una serie con etiquetas personalizadas {"a":100,"b":200, "c": 300}

personalizadas = pd.Series({"a":100,"b":200, "c": 300})
print(personalizadas)

#acceder al valor correspondiente a la serie "b"

print(personalizadas["b"])

#dadas las series s1= pd.Series([1,2,3,4,5]) y s2= pd.Series([10,20,30,40,50]) suma estas series y guarda una nueva en s3 e imprime s3

s1= pd.Series([1,2,3,4,5])
s2= pd.Series([10,20,30,40,50])

s3 = s1+s2
print(s3)


# dada la serie s=pd.Series([10,20,30,40,50]) imprimir los valores mayores que 25

s=pd.Series([10,20,30,40,50])
mayores = s > 25

resultado = s[mayores]
print(resultado)

# dada la serie s=pd.Series([1,2,3,4,5]) eleva al cuadrado cada serie y guarda esta nueva serie llama a s_cuadrado

s=pd.Series([1,2,3,4,5])
def cuadrado(x):
    return x**2

s_cuadrado = s.apply(cuadrado)
print(s_cuadrado)

# dada la serie s=pd.Series(["a","b","c","a","a","b","c","d"]) cuenta cuantas veces aparece el valor en la serie 

s=pd.Series(["a","b","c","a","a","b","c","d"])

s_contar = s.value_counts()
print(s_contar)


# dada la serie s=pd.Series([4,2,6,1,5]) ordena los valores de mayor a menor y almacena el resultado en una nueva serie
s=pd.Series([4,2,6,1,5])
print(s.sort_values())

