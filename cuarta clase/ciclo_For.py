"""El ciclo For es otra de las formas con las que cuenta Python para realizar iteraciones sobre secuencias o iterables como lo son listas, tuplas, diccionarios, sets e incluso cadenas.
Funciona menos como ciclos for en otros lenguajes de programación y más como un método iterador en lenguajes orientados a objetos.
Dentro del bloque for es posible realizar diferentes operaciones aplicadas a cada uno de los elementos del iterable y combinar todos los elementos vistos hasta el momento.
El ciclo for cuenta con una sentencia break que detiene la iteración al detectar su llamado.
Tambien con continueque finaliza la iteración actual pero no rompe el ciclo."""

# Iterando la lista de estudiantes

listado_estudiantes = ["Alice", "Joha", "Damien", "Javi"]

for estudiante in listado_estudiantes:
    print(estudiante)

nombre_asignatura = "Matemáticas"

for x in nombre_asignatura:
    if x.lower() == "c":
        break #para la ejecucion cuando encuentra la c
    print("\n", x)
print("\n")
for x in nombre_asignatura:
    if x.lower() == "t": # no imprime la t pero el continue permite seguir imprimiendo el siguiente
        continue
    print(x)

##Ahora, el ciclo for cuenta con la sentencia range() donde es posible definir el inicio y el final de la iteración, sin necesidad de estar recorriendo un iterable.

"""for x in range(2, 9, 2):
  print(x)
else:
  print('Solo pares')
"""

listado_estudiantes2 = ["Alice", "Joha", "Damien", "Javi"]
notas_estudiantes = [4, 4.5, 5, 3.8]

for estudiante in listado_estudiantes2:
  for nota in notas_estudiantes:
    print(estudiante, nota)
  else:
    print("algo no quedó bien")
else:
  print('Hay que repetir todo')