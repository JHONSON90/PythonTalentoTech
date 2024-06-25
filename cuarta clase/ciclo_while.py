##Ciclo while

"""La sentencia while se usa para la ejecución repetida siempre que una expresión sea verdadera. Cuenta con la senntencia `break` que permite finalizar la iteración en el momento que se determine, por ejemplo en un ciclo de contar hasta 100 parar cuando llegue a un número determinado.
También cuenta con `continue` para solo saltar la iteración actual y pasar a la siguiente.
Finalmente cuenta con la sentencia `else` que es opcional y se ejecuta cuando la expresión que evalúa el `while` no es más verdadera """
""""""

want_greet = "S"
valid_options = 0
while want_greet == "S":
    print("Hola qué tal!")
    want_greet = input("¿Quiere otro saludo? [S/N] ")
    if want_greet not in "SN":
        print("No le he entendido pero le saludo")
        want_greet = "S"
        continue
    valid_options += 1

print(f"{valid_options} respuestas válidas")
print("Que tenga un buen día")

# Implementar un código que imprima los números factoriales, utilizando while, hasta un número determinado.
# Imprimir la sucesión de Fibonacci hasta el número 20

numero_determinado = 10
condicion = 1
factorial = int(input("Numero de Factorial: "))
n = factorial
num_res = 1

while condicion <= n:
    resultado = numero_determinado * num_res
    print("Factorial", numero_determinado, resultado)
    condicion += 1
    num_res = resultado
    numero_determinado += 1

# otro ejemplo mas sencillo que nos permitira entender mejor el while
    x = 5
    while x >= 0:
        x -= 1
        print(x)
