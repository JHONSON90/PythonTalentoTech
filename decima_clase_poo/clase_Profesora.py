class Coche:
    def __init__(self, marca, modelo, color, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad  # Atributo adicional

    def arrancar(self):
        self.velocidad = 10  # Cambiar el valor de un atributo
        print(f"El coche {self.marca} {self.modelo} ha arrancado y está a {self.velocidad} km/h.")

    def detener(self):
        self.velocidad = 0  # Cambiar el valor de un atributo
        print(f"El coche {self.marca} {self.modelo} se ha detenido.")

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El coche {self.marca} {self.modelo} ha acelerado y ahora está a {self.velocidad} km/h.")
        
# crear los objetos de esta clase

