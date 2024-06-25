#listas
# se crean a partir de los []

carreras=["contaduria","ingenieria de sistemas", "ingenieria industrial", "artes visuales"]

# Metodos en las listas

#agregar datos a la lista
carreras.append("Psicologia")
print(carreras)
#Quitar datos de la lista
carreras.pop(0)
print(carreras)
#traer el indice indicado
print(carreras.index("artes visuales"))


accesorios=["Reloj", "gafas", "chaquetas"]
newlist = [variable for variable in accesorios if variable != "Reloj"]
print(newlist)

#metodos de las listas

""" 
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""


productos=["arroz", "papa", "platano", "leche", "lentejas"]
precios=[5000, 4000, 2000, 5000, 9000]

position= int(len(productos)/2)
print(position)
#colocar en una posicion especifica un articulo
productos.insert(position,"lechuga")
precios.insert(position,"1000")
print(productos, precios)
#quitar un elemento en una posicion especifica
productos.pop(5)
precios.pop(5)



