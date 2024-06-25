#las tuplas se inicializan con parentesis
#las tuplas no se pueden modificar excepto si lo conviertes en lista
estudiantes=("Juan", "Andres", "Maria", "Carmen")

#cambiar de tupla a lista con la funcion list

estudiantes_lista = list(estudiantes)

print(estudiantes, estudiantes_lista)

#tambien se puede convertir una lista a tupla con la funcion tuple

nuevo_estudiantes = tuple(estudiantes_lista)

#desempaquetado de tuplas
Juan, Andres, *mujeres = estudiantes
print(mujeres)

tupla_1 = (3,5,7)
tupla_2 = (2,4,6)

combinada = tupla_1+tupla_2
multivariable0=tupla_1[0]*tupla_2[0]
multivariable1=tupla_1[1]*tupla_2[1]
multivariable2=tupla_1[2]*tupla_2[2]

print(combinada)

print (multivariable0)
print (multivariable1)
print (multivariable2)

resultados = [tupla_1[i]*tupla_2[i] for i in range(len(tupla_1))]
print(resultados)

