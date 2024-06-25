import pandas as pd
import numpy as np

new_dict = {
    "Matemáticas" : 8.0,
    "Programación" : 7.7,
    "Inglés" : 8.2
}
s = pd.Series(new_dict)
print(s)

# generar un numero random desde una serie
s = pd.Series(np.random.randint(2, 10, 8))#ultimo dato es el numero de serie y los numeros aleatorios que se generarian serian del 2 al 10
p = pd.Series(np.random.randint(2, 10, 8))
print(s, p)
print(s * p)

# convertir de minusculas a mayusculas
s = pd.Series(['a', 'b', 'c'])
s.apply(str.upper)#utilizamos el metodo apply para colocar funciones

#imprime la serie mayor que 6 osea me las filtra por el mayor que 
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s[s > 6])
#en diccionarios tambien podemor organizar con el sort_values() por valores y sort_index de menor a mayor


#como colocar datos none o nan en una serie
s = pd.Series(['a', 'b', None, 'c', np.NaN,  'd'])

s.dropna() # La función dropna() se utiliza en la serie 's' para eliminar los valores nulos. Devuelve una nueva serie sin los valores nulos.
print(s)