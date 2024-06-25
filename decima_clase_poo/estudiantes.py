"""
Funcionalidades a Implementar:
Gestión de Estudiantes:
    Permite agregar nuevos estudiantes al sistema con su nombre,
apellido y edad.
    Permite eliminar estudiantes del sistema.
    Permite modificar la información de estudiantes existentes,
incluyendo su nombre, apellido y edad.
Gestión de Asignaturas:
    Permite crear nuevas asignaturas en el sistema con su nombre.
    Permite eliminar asignaturas del sistema.
    Permite modificar el nombre de las asignaturas existentes.
Gestión de Notas:
    Permite agregar notas para un estudiante en una asignatura
específica.
    Permite consultar las notas de un estudiante en todas sus
asignaturas.
    Permite consultar el promedio de notas de un estudiante en todas
sus asignaturas.
    Permite consultar el promedio de notas de una asignatura específica.
    Permite consultar las notas individuales de todos los estudiantes en
una asignatura específica. """

class Estudiante:
    def __init__ (self, nombres, apellidos, edad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.notas = {}
        
    def agregar_nota(self, asignatura, nota):
        self.notas[asignatura] = nota
    
    def promedio_general(self):
        if not self.notas:
            return 0
        return sum(self.notas.values())/ len(self.notas)
    
    def __str__(self):
        return f'{self.nombres} {self.apellidos} (Edad: {self.edad})'
    
class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = {}
        
    def agregar_estudiante(self, estudiante, nota):
        self.estudiantes[estudiante] = nota
        
    def promedio_asignatura(self):
        if not self.estudiantes:
            return 0
        return sum(self.estudiantes.values())/len(self.estudiantes)
    def __str__(self):
        return self.nombre
    
class SistemaGestionEstudiantes:
    def __init__(self):
        self.estudiantes = {}
        self.asignaturas = {}
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes[estudiante] = True
    
    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            del self.estudiantes[estudiante]
    
    def agregar_asignatura(self, asignatura):
        self.asignaturas[asignatura] = True
        
    def eliminar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            del self.asignaturas[asignatura]
    
    def asignar_nota(self, estudiante, asignatura, nota):
     if estudiante in self.estudiantes and asignatura in self.asignaturas:
         asignatura.agregar_estudiante(estudiante, nota)
         estudiante.agregar_nota(asignatura, nota)
         
    def mostrar_notas_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            print(f"Notas de {estudiante}:")
        for asignatura, nota in estudiante.notas.items():
            print(f"{asignatura}: {nota}")
            
    def promedio_general_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            print(f"Promedio de {estudiante}: {estudiante.promedio_general()}")
            
    def promedio_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            print(f"Promedio de {asignatura}: {asignatura.promedio_asignatura()}")
            
    
sistema = SistemaGestionEstudiantes()
 # Crear estudiantes
estudiante1 = Estudiante("Juan", "Pérez", 20)
estudiante2 = Estudiante("María", "Gómez", 22)
 # Crear asignaturas
asignatura1 = Asignatura("Matemáticas")
asignatura2 = Asignatura("Ciencias")
 # Agregar estudiantes y asignaturas al sistema
sistema.agregar_estudiante(estudiante1)
sistema.agregar_estudiante(estudiante2)
sistema.agregar_asignatura(asignatura1)
sistema.agregar_asignatura(asignatura2)
 # Asignar notas
sistema.asignar_nota(estudiante1, asignatura1, 90)
sistema.asignar_nota(estudiante1, asignatura2, 85)
sistema.asignar_nota(estudiante2, asignatura1, 88)
sistema.asignar_nota(estudiante2, asignatura2, 92)

# Mostrar notas y promedios
sistema.mostrar_notas_estudiante(estudiante1)
sistema.mostrar_notas_estudiante(estudiante2)
sistema.promedio_general_estudiante(estudiante1)
sistema.promedio_general_estudiante(estudiante2)
sistema.promedio_asignatura(asignatura1)
sistema.promedio_asignatura(asignatura2)