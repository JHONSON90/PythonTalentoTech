"""# definimos el padre
class guayos:
    #vamos a crear atributos comunes
    def __init__(self, suela, cuerpo, modelo):
        self.suela = suela
        self.cuerpo = cuerpo
        self.modelo = modelo
    # creamos atributos particulares osea que la funcion va a cambiar dependiendo de cada elemento
        def tipo_de_suela(self):
            pass
        
#definimos un hijo

class nike(guayos):
    def tipo_de_suela(self):
        print("FG")


nike_tiempo = nike("Goma", "sintetico", "Tiempo")


print(nike_tiempo.suela)
print(nike_tiempo.cuerpo)
print(nike_tiempo.modelo)

nike_tiempo.tipo_de_suela()

#nueva variable que modifica al padre
class nike(guayos):
    def __init__(self, cordones, duracion):
        super().__init__(cordones, duracion)
        self.cordones = cordones
        self.duracion = duracion

nike_mercurial = nike("azules", "30 dias")
print(nike_mercurial.cordones, nike_mercurial.duracion)"""


class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        pass
    
    def moverse(self):
        pass
    def describeme(self):
        print("Soy un animal de tipo ", type(self).__name__)
        
class Perro(Animal):
    pass

mi_perro = Perro('mamifero', 15)
mi_perro.describeme()

class Perro(Animal):
    def hablar(self):
        print("Guauu!!")
    def moverse(self):
        print("En 4 Patas")
    def comer(self):
        print("cada 3 horas")
        
mi_perro = Perro("mamifero", 16)
mi_perro.hablar()
mi_perro.moverse()
mi_perro.comer()

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño
        
mi_perro = Perro("mamifero", 7, "Carlitos")
mi_perro.especie
mi_perro.edad
mi_perro.dueño

print(mi_perro.dueño)