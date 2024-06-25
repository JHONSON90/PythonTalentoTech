#las condicionales son el control de flujo que se realizan en una aplicacion


a = 4
b = 2

if(a == b):
    print('a es igual a b');
elif(a < b):
    print('a es mejor que b')
else:
  print('a es mayor que b')

#También existen el atajo para el if y el atajo para el if ... else
print("A") if a > b else print("B")
if a > b: print("a es mayor que b")

"""Cree un código que permita identificar si un número es par, impar 
o si es 0, si el número es impar, determine si es divisible entre 3."""

numero = int(input("ingrese un valor :" ))
print(type(numero))

if(int(numero) == 0):
    print("EL numero ingresado es 0, intenta de nuevo!!!");
elif(int(numero) % 2 == 0):
    print("El numero ingresado es Par");
else: "El numero ingresado es Inpar"