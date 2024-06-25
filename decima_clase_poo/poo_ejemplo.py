""" El siguiente ejemplo es para una cafetería, el programa hace las veces del vendedor, donde dependiendo del dinero que tengamos no indicará qué tamaño de café no podemos comprar y si tenemos cambio. Así por ejemplo, si decimos que tenemos 2, el vendedor nos dirá que podemos comprar uno pequeño y que no hay cambio.
    """
    
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)
        
    def check_budget(self, budget):
        #revisa si el budget es valido
        if not isinstance(budget, (int, float)): #verifica si es una instancia y verifica si es un valor valido
            print('Enter float or int')
            exit()
        if budget < 0: # verifica si tiene presupuesto
            print('Sorry you dont have Money')
            exit()
    def get_change(self, budget): #revisa cuanto seria el cambio que tendria que dar el vendedor
        return budget - self.price
    
    def sell(self, budget): # 
         self.check_budget(budget)
         if budget >= self.price: # verifica que el presupuesto sea mayor a el precio de venta del producto
             print(f'You can buy the {self.name} coffee') 
             if budget == self.price: #entra y revisa que este completo o que no tenga que dar cambio
                 print('Its complete')
             else: 
                 print(f'Here is your change {self.get_change(budget)}$') # evalua el cambio que tiene que dar 
                 exit('Thanks for you transaction')
                 
small = Coffee("Small", 2)
regular = Coffee("Regular", 5)
big = Coffee("Big", 6)


class Tarjeta:
    def __init__(self, numero, cantidad=0):
        self.numero = numero
        self.cantidad = cantidad
        return
    def __str__(self): #Esto imprime una string para dar una descripcion del objeto de la clase y se muestra pa posicion de memoria del objeto
        return f'Tarjeta Numero {self.numero} con saldo {self.cantidad}'

t = Tarjeta('0123456789', 1000)
print(t)

""" Vamos a crear una nueva clase dentro de las tarjetas, que sería la tarjeta
débito, tendrá un número y su saldo, y un método pagar que permite hacer
pagos siempre y cuando el saldo sea suficiente, y verificamos si es instancia
de la clase Tarjeta o Tarjeta_Debito """

class Tarjeta_Debito(Tarjeta):
    def __init__(self, numero, cantidad, cuota):
        super().__init__(numero, cantidad)
        self.cuota = cuota
       
    def pagar(self):
        if self.cuota > self.cantidad:
            print('Dont have money my brother!!!')
        else:
            print(f'Your payment has been a successful for card number {self.numero}, worth {self.cuota}')
    
t_c_c = Tarjeta_Debito('0123456789',2000000,300000000)
print('-----------------------------------------------')
print(t_c_c.pagar())