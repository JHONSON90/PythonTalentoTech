# 1. Uso de *args y **kwargs
# La mayoría de los programadores nuevos en Python tienen dificultades para entender el uso de *args y **kwargs. ¿Para qué se usan? Lo primero de todo es que en realidad no tienes porque usar los nombres args o kwargs, ya que se trata de una mera convención entre programadores. Sin embargo lo que si que tienes que usar es el asterisco simple * o doble **. Es decir, podrías escribir *variable y **variables. Empecemos viendo el uso de *args.

""" 1.1. Uso de *args
El principal uso de *args y **kwargs es en la definición de funciones. Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera el uso de *args o **kwargs como una opción. De hecho, el nombre de args viene de argumentos, que es como se denominan en programación a los parámetros de entrada de una función.

A continuación te mostramos un ejemplo para que veas el uso de *args: """


def test_var_args(
    *argv,
):  ## en pocas palabras el * toma todos los argumentos que se pasen y no tener que poner a, b, c por que limita el numero de datos que se puedan pasar a la funcion
    # print("primer argumento normal:", f_arg)
    for arg in argv:
        print("argumentos de *argv:", arg)


test_var_args("python", "foo", "bar", "react", "astro")


# Otro ejemplo de *args


def sumar(*args):
    resultado = 0
    for numeros in args:
        resultado += numeros
        return resultado


datos1 = (2, 3, 4, 5, 6, 7)

print(sumar(*datos1))

# 1.2. Uso de **kwargs
# **kwargs permite pasar argumentos de longitud variable asociados con un nombre o key a una función. Deberías usar **kwargs si quieres manejar argumentos con nombre como entrada a una función. Aquí tienes un ejemplo de su uso.

""" def saludame(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

#saludame(nombre="Covadonga")
nombre = Covadonga """


# escribe una funcion llamada conteo_elementos que tome una lista como argumento y devuelva un diccionario
# donde las claves sean elementos unicos presentes en la lista y los valores sean la cantidad de veces que
# aparece cada elemento


def conteo_elementos(elementos):
    conteo = {}
    for element in elementos:
        print("estamos en el elemento" ,element)
        if element in conteo:
            conteo[element] += 1
        else:
            conteo[element] = 1
    return conteo


listaNumeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = conteo_elementos(listaNumeros)
print(resultado)
