class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}")
        
# clase miembro 
class Miembro:
    def __init__(self,nombre,id_miembro) :
        self.nombre= nombre
        self.id_miembro= id_miembro
        self.libros_prestados=[]
        
    def tomar_prestado(self,libro) :
        self.libros_prestados.append(libro)   
        print(f"{self.nombre} ha tomado prestado { libro.titulo}.")
        
    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro {libro.titulo}")
    
    def mostrar_prestamos(self):
        print(f"{self.nombre} tiene los siguientes libros ")  
        for libro in self.libros_prestados:
            print(f"{libro.titulo}")    
            
class Prestamo:
    def __init__(self, libro, miembro, fecha_prestamo, fecha_devolucion) :
        self.libro= libro
        self.miembro=miembro
        self.fecha_prestamo=fecha_prestamo
        self.fecha_devolucion=fecha_devolucion
    def mostrar_detalles (self):
        print(f" libro {self.libro.titulo}, miembro {self.miembro.nombre}, fecha prestamo {self.fecha_prestamo}")    
                    
            
mi_libro = Libro("El simbolo perdido", "Dan Brown", 12154145 )

miembro1 = Miembro("Jhon Edison Portilla", 1085917679)

mi_libro.mostrar_informacion()

miembro1.tomar_prestado(mi_libro)
miembro1.libros_prestados()

nuevo_prestamo = Prestamo(mi_libro, miembro1, "10/01/2024", "20/01/2024")
nuevo_prestamo.mostrar_detalles()