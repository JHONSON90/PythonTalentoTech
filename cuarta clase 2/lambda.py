# calcular el area de un triangulo escribe una funcion lambda que tome la altura y base de un triangulo como argumentos y devuelva su area

area_triangulo = lambda base, altura: (base * altura) / 2


base_del_triangulo = 10
altura_del_triangulo = 5
resultado = area_triangulo(base_del_triangulo, altura_del_triangulo)
print(resultado)


# ordenar una lista de cadenas por longitud dada una lista de cadenas utiliza una funcion lambda para ordenar la lista por longitud de las cadenas

lista_cadenas = ["manzana", "pera", "uva", "kiwi", "fresa"]

lista_ordenada = sorted(lista_cadenas, key=lambda x: len(x))
print(lista_ordenada)
for cadena in lista_ordenada:
    print(cadena)

    # filtrar una lista de numeros negativos dada una lista de numeros utiliza una funcion lambda para fltrar solo los numeros negativos
numeros_negativos = [0, -1, -2, -3, 5, 6, 7, 8, 910]

negativos = list(filter(lambda x: x < 0, numeros_negativos))
print(negativos)
