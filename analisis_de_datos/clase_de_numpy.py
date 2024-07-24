import numpy as np

# crear arrays con numpy

a = [ 1,2,3,4,5]
#cambiando a un array
x = np.array(a)

#imprimiendo la version de numpy
print(np.__version__)

#tipo
print(type(x))

#shape o largo La forma del shape es una tupla de números enteros que indica el tamaño de la matriz en cada dimensión:
print(x.shape)
print(x.size)

#buscando las dimensiones
print(x.ndim)

# mirando el tipo de datos que hay dentro del array
print(x.dtype)

#! funciones basicas
# buscando la media del array
print(x.mean())

# buscando el producto de dos arrays 
np.dot(np.array([1,-1]),np.array([1,1]))

# buscando la desviacion estándar del array
print(x.std())

# sacando el mayor valor
print(x.max()) 

#sacando el menor 
print(x.min())

# adicion de arrays osea suma las arrays teniendo en cuenta su indice osea suma u[0]+v[0] = 1+0 = 1
u = np.array([1, 0])
v = np.array([0, 1])

z = np.add(u, v)
print(z)

#sustraccion osea resta y lo hace de la misma manera que la suma
z = np.subtract(u, v)
print(z)

#multiplicacion
z = np.multiply(u, v)

#division 
z = np.divide(u, v)

#accediendo al primer elemento y cambiandolo
a[0] = 100
print(a)

# creando una nueva array mediante slicing o rango

d = a[0:3]
print(d)

#asignando nuevos valores a partir del cuarto elemento
d[3:5] = 400,500
print(d)

#se pueden definir rangos como estos [start:end:step], si no colocamos el comienzo [:3] python asimila que comienza desde 0 tambien pasa al contrario osea [1:] asimila que va hasta el final otro ejemplo de esto es [1::2] e imprime todos los segundos resultados
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

#se puede hacer que python cree la lista usando linspace
#linspace es un metodo que crea una lista de numeros entre un rango
arr1 = np.linspace(5, 4, num=6)
print(arr1)

#iteerando listas
for i in arr1:
    print(i)



import time 
import sys
import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    
Plotvec1(u, z, v)

# asignando constantes a una array osea sumando o restando a cada elemento es como hacer una funcion con un for pero esto lo hace automaticamente
x * 100
print(x, "-------")

# arrays con mas de una dimension
A=np.array([[11,12],[21,22],[31,32]])
# estos metodos funcionan igual que los de arriba
print(type(A))
print(A.shape) # aqui nos da primero el numero de dimensiones y despues el numero de datos por dimension
print(A.dtype)

#accediendo a las dimensiones
print(A[1]) #accede a la segunda dimension
print(A[0,1]) # accede a la primera fila y la segunda columna

#multiplicacion que es diferentes a las demas operaciones xq las demas si lo hacen por indice como se lo hace con una dimension
A=np.array([[11,12],[21,22]])
B=np.array([[1, 0],[0,1]])

C= A * B
print(C)

Z =  np.dot(A, B)
print(Z)

# para mirar las dimensiones 
print(A.ndim)
#para mirar el numero de datos hay en el array
print(A.size)

#accediendo a el primer elemento y primera y segunda columna
print(A[0,0:2])

#accediendo a los dos primeras filas de la tercera columna
print(A[0:2,2])