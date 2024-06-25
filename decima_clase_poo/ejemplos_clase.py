class Alumno:
    def __init__(self, nombres, apellidos, curso):
        self.nombres = nombres
        self.apellidos = apellidos
        self.curso = curso
        
    def __str__(self):
        return f'El nombre del estudiante es {self.nombres} {self.apellidos} y esta en el curso de {self.curso}'


class Animal:
    def __init__(self, clase, numero_de_patas, forma_comunicacion):
        self.clase = clase
        self.numero_de_patas = numero_de_patas
        self.forma_comunicacion = forma_comunicacion
        
class Motocicletas:
    def __init__(self, marca, modelo, cilindraje):
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = cilindraje
        
mi_motocicleta = Motocicletas("Honda", "CB", 1000)

print(mi_motocicleta.cilindraje)