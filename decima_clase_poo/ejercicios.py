""" Escribir una clase en python llamada círculo que contenga un radio, con
un método que devuelva el área y otro que devuelva el perímetro del
círculo
"""
from math import pi
import roman

class Circulo:
    def __init__(self, diametro):
        self.diametro = diametro
        
    def area(self):
        return pi * (self.diametro/2) ** 2
    
    def perimetro(self):
        return 2* pi * (self.diametro/2)
    
    
""" 
Escribir una clase en python llamada rectángulo que contenga una base
y una altura, y que contenga un método que devuelva el área del
rectángulo.
"""

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base * self.altura) / 2 

""" 
Escribir una clase en python con 2 métodos: get_string y print_string.
get_string acepta una cadena ingresada por el usuario y print_string
imprime la cadena en mayúsculas."""

class Printeando:
    def __init__(self, cadena):
        self.cadena = cadena
    def get_string(self):
        print(self.cadena)
    def print_string(self):
        mayusc= self.cadena.upper()
        print(mayusc)

"""
Escribir una clase en python que convierta un número entero a número
romano
"""

class Romanos:
    def __init__(self, numero):
        self.numero = numero
        print(roman.toRoman(self.numero))

"""
Escribir una clase en python que convierta un número romano en un
número entero
"""

class ConversorNumerosRomanos:
    def __init__(self):
        self.romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def convertir_a_entero(self, numero_romano):
        resultado = 0
        for i in range(len(numero_romano)):
            if i > 0 and self.romanos[numero_romano[i]] > self.romanos[numero_romano[i-1]]:
                resultado += self.romanos[numero_romano[i]] - 2 * self.romanos[numero_romano[i-1]]
            else:
                resultado += self.romanos[numero_romano[i]]
        return resultado

conversor = ConversorNumerosRomanos()
numero_entero = conversor.convertir_a_entero("XXIV")
print(numero_entero) 

