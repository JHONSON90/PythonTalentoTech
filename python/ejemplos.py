"""
una forma de cambiar los datos seria asi
n1 = int(input("Escribe numero 1: "))
n2 = int(input("Escribe numero 2: "))
otra forma de hacerlo es de la siguiente manera
"""
n1 = input("Escribe numero 1: ")
n2 = input("Escribe numero 2: ")
n1=int(n1)
n2=int(n2)
n3=n1+n2

n1+=10
n2-=5
n3=n1+n2
#print("el valor ingresado en N1 fue: "+n1,"el valor ingresado en N2 fue: "+ n2,"El resultado de tu operacion es: "+  n3)

operacion = input("escribe operacion a realizar")
valor1 = input("escribe valor 1 ")
valor2 = input("escribe valor 2 ")

if operacion == "suma":
    print(int(valor1) + int(valor2))
elif operacion == "resta":
    print(int(valor1) - int(valor2))
else:
    print(int(valor1) * int(valor2))





