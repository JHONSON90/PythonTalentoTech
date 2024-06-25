"""
La función map() aplica la función pasada por su primer
argumento a todos los elementos de su segundo argumento
y devuelve un iterador que entrega todos los resultados de
funciones subsequentes.
"""

def cuadrados(x):
    return x**2

def es_par(x):
    return x%2==0

#lista de numeros
numeros = [1,2,3,4,5]

resultado = list(map(cuadrados, numeros))
print(resultado)

#filter

numeros_pares = list(filter(es_par, numeros ))
print(numeros_pares)

#lambda
from functools import reduce
producto = reduce((lambda x,y:x*y),[1,2,3,4])
print(producto)