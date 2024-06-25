"""
Hasta el momento se han utilizado diferentes funciones propias de Python como print() e input(), 
estas se conocen como funciones propias del lenguaje y en caso de necesitar saber como funcionan, 
puede utilizar el comando
help(print) #ayuda sobre la función print()

Pero también es posible definir funciones propias del usuario.

Una definición de función especifica el nombre de una nueva función y la secuencia de declaraciones 
que se ejecutan cuando se llama la función. Una vez que definimos una función, podemos reutilizar la 
función una y otra vez a lo largo de nuestro programa.
"""

def suma(a,b,c):
    if(a<b):
        return (a+c)
    if(a==c):
        return(b)
    if(c<b):
        return(a+b+c)
    
respuesta = suma(5,6,2)
print(respuesta)

#funcion Ramdom
"""Este módulo implementa generadores de números pseudoaleatorios para varias distribuciones, lo que quiere decir es que los números generados no son realmente aleatorios.

Cuenta con un listado de métodos
Method	Description
seed()	Initialize the random number generator
getstate()	Returns the current internal state of the random number generator
setstate()	Restores the internal state of the random number generator
getrandbits()	Returns a number representing the random bits
randrange()	Returns a random number between the given range
randint()	Returns a random number between the given range
choice()	Returns a random element from the given sequence
choices()	Returns a list with a random selection from the given sequence
shuffle()	Takes a sequence and returns the sequence in a random order
sample()	Returns a given sample of a sequence
random()	Returns a random float number between 0 and 1
uniform()	Returns a random float number between two given parameters
triangular()	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate()	Returns a random float number based on the Gamma distribution (used in statistics)
gauss()	Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate()	Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)

Para trabajar con el módulo Python es necesario importarlo previamente

El módulo random cuenta con un método seed que permite obtener siempre el mismo número o grupo de números aleatorios a diferencia de no establecerla, lo que provoca que en cada ejecución se generen nuevos números
"""

import random

#Seleccionar un elemento aleatorio de una lista
listado_estudiantes = ["Alice", "Joha", "Damien", "Javi"]
print(random.choice(listado_estudiantes))


print(random.random())
print(random.random())

#random.seed(4)
#print(random.random())
#print(random.random())
