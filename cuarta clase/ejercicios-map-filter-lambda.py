#convertir de fahrenheit a celsius
from functools import reduce

temperaturas_fahre = [25,35,45,50]

celsius = list(map(lambda x: (x*9/5)+32, temperaturas_fahre))
print(celsius)

# Filtrar numeros primos de una lista
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def primos(x):
    if x < 2:
        return False       
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


numeros_primos = list(filter(primos, numeros))
print(numeros_primos)

#multiplicar los elementos de una lista usando reduce

multiplicacion = reduce((lambda x,y: x*y),numeros)
print(multiplicacion)

#convertir una lista de palbras a mayusculas usando map
nombres = ["juan", "maría", "pedro", "ana", "luisa"]
mayusculas = list(map(lambda nombre: nombre.upper(), nombres))

print(mayusculas)