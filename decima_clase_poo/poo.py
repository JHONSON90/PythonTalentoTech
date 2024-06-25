# PROGRAMACION ORIENTADA A OBJETOS - POO

#? HERENCIA
#La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre

# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass
#De hecho podemos ver como efectivamente la clase Perro es la hija de Animal usando __bases__
print(Perro.__bases__)
# (<class '__main__.Animal'>,)

#De manera similar podemos ver que clases descienden de una en concreto con __subclasses__.
print(Animal.__subclasses__())

"""¿Y para que queremos la herencia? Dado que una clase hija hereda los atributos y métodos de la padre, nos puede ser muy útil cuando tengamos clases que se parecen entre sí pero tienen ciertas particularidades. En este caso en vez de definir un montón de clases para cada animal, podemos tomar los elementos comunes y crear una clase Animal de la que hereden el resto, respetando por tanto la filosofía DRY. Realizar estas abstracciones y buscar el denominador común para definir una clase de la que hereden las demás, es una tarea de lo más compleja en el mundo de la programación."""

#Definimos la clase padre, con una serie de atributos comunes para todos los animales como hemos indicado.

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
        
"""Tenemos ya por lo tanto una clase genérica Animal, que generaliza las características y funcionalidades que todo animal puede tener. Ahora creamos una clase Perro que hereda del Animal. Como primer ejemplo vamos a crear una clase vacía, para ver como los métodos y atributos son heredados por defecto."""

# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro

""" Con tan solo un par de líneas de código, hemos creado una clase nueva que tiene todo el contenido que la clase padre tiene, pero aquí viene lo que es de verdad interesante. Vamos a crear varios animales concretos y sobreescrbir algunos de los métodos que habían sido definidos en la clase Animal, como el hablar o el moverse, ya que cada animal se comporta de una manera distinta.

Podemos incluso crear nuevos métodos que se añadirán a los ya heredados, como en el caso de la Abeja con picar()."""

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")
        
mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()
mi_vaca.hablar()
mi_vaca.describeme()
mi_abeja.describeme()
mi_abeja.picar()

"""Tal vez queramos que nuestro Perro tenga un parámetro extra en el constructor, como podría ser el dueño. Para realizar esto tenemos dos alternativas:

Podemos crear un nuevo __init__ y guardar todas las variables una a una.
O podemos usar super() para llamar al __init__ de la clase padre que ya aceptaba la especie y edad, y sólo asignar la variable nueva manualmente."""

class Perro(Animal): 
    def __init__(self, especie, edad, dueño):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño
        
mi_perro = Perro('mamífero', 7, 'Luis')
mi_perro.especie
mi_perro.edad
mi_perro.dueño



""" 
Una tarjeta de crédito puede representarse como un objeto: Atributos: Número de la tarjeta, titular, balance, fecha de caducidad, pin, entidad emisora, estado (activa o no), etc. Métodos: Activar, pagar, renovar, anular.

Para ver si un objeto tiene un determinado atributo o método se utiliza la siguiente función: hasattr(objeto, elemento): Devuelve True si elemento es un atributo o un método del objeto objeto y False en caso contrario. Para acceder a los atributos y métodos de un objeto se pone el nombre del objeto seguido del operador punto y el nombre del atributo o el método. objeto.atributo: Accede al atributo atributo del objeto objeto. objeto.método(parámetros): Ejecuta el método método del objeto objeto con los parámetros que se le pasen.

vamos a definir la clase mascota con atributos como raza y nombre y metodos como asigar los valores
"""

class Mascota:
    def __init__(self, nombre, raza):  #Inicializador y los atributos son de instancia si se crean por aparte serian atributos de clase y esto no se deberian crear
        # Creacion de los atributos
        self.nombre = nombre 
        self.raza = raza
        
        #Creacion de metodos o funciones
        def get_nombre(self): #obtener el nombre
            return self.nombre
        def set_nombre(self, nombre): #editamos el nombre
            self.nombre = nombre
        def get_raza(self):
            return self.raza
        def set_raza(self, raza):
            self.raza = raza
            
        def __str__(self):
            return f'Nombre: {self.nombre}, Raza: {self.raza}'

# vamos a crear una instancia de la clase mascota

#from Mascota import Mascota

#creamos un objeto de mascota

mascota = Mascota("Firulais", "Pastor Aleman")

print(mascota)


class Tarjeta:
    def __init__(self, numero, cantidad=0):
        self.numero = numero
        self.cantidad = cantidad
        return
    def __str__(self): #Esto imprime una string para dar una descripcion del objeto de la clase y se muestra pa posicion de memoria del objeto
        return f'Tarjeta Numero {self.numero} con saldo {self.cantidad}'

t = Tarjeta('0123456789', 1000)
print(t)

#! Herencia 

""" Una de las características más potentes de la programación orientada a
objetos es la herencia, que permite definir una especialización de una clase
añadiendo nuevos atributos o métodos. La nueva clase se conoce como
clase hija y hereda los atributos y métodos de la clase original que se conoce
como clase madre.
Para crear un clase a partir de otra existente se utiliza la misma sintaxis que
para definir una clase, pero poniendo detrás del nombre de la clase entre
paréntesis los nombres de las clases madre de las que hereda.
Ejemplo. A partir de la clase Tarjeta definida antes podemos crear mediante
herencia otra clase Tarjeta_Descuento para representar las tarjetas de
crédito que aplican un descuento sobre las compras."""


class Tarjeta_Descuento(Tarjeta):
    def __init__(self, numero, descuento):
        self.numero = numero
        self.descuento = descuento
        return
    def mostrar_descuentos(self):
        #metodo exclusivo de la clase de descuento
        print('Descuento de ', self.descuento, '% en los pagos.')
        return
    def __str__(self):
        return 'Tarjeta numero {} con descuento del {}%'.format(self.numero, str(self.descuento))

# Creamos el objeto 

t_d = Tarjeta_Descuento('01234567890',2)
print(t_d)

#! ENCAPSULAMIENTO

"""Hace referencia al ocultamiento de los estados internos de una clase al
exterior. Dicho de otra manera, encapsular consiste en hacer que los
atributos o métodos internos a una clase no se puedan acceder ni modificar
desde fuera, sino que tan solo el propio objeto pueda acceder a ellos."""


class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        

#! abstraccion

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        
    def mostrar_informacion(self):
        print(f'{self.titulo}, autor: {self.autor}')
        
#clase miembro

class Miembro:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.libros_prestados = []
        
    def tomar_prestado(self, Libro):
        self.libros_prestados.append(Libro)
        print(f'{self.nombre} ha tomado prestado el libro {libro.titulo}')
        
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print(f'{self.nombre} ha devuelto el libro {libro.titulo}')
            
    def mostrar_prestamos(self):
        print(f'{self.nombre} tiene prestados los siguientes libros: ')
        for libro in self.libros_prestados:
            print(f'{libro.titulo}')
            
    class Prestamo:
        def __init__(self, libro, miembro, fecha_prestamo, fecha_devolucion):
            self.libro = libro
            self.miembro = miembro
            self.fecha_prestamo = fecha_prestamo
            self.fecha_devolucion = fecha_devolucion
        
        def mostrar_detalles(self):
            print(f'El libro {self.libro} fue devuelto por el miembro {self.miembro} el cual fue prestado {self.fecha_prestamo} y devuelto en {self.fecha_devolucion}')
            
