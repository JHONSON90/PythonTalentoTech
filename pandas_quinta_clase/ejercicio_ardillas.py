import pandas as pd

#importa el archivo de csv mediante la funcion read
data = pd.read_csv("ardillas.csv")

#print(data);
print(data.columns); # imprime las columnas

cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"] #filtra las filas tienen el color cinnamon
black_squirrels = data[data["Primary Fur Color"] == "Black"]
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]

print(len(cinnamon_squirrels)) #cuenta las filas que tienen color cinnamon
print(len(black_squirrels))
print(len(gray_squirrels))

result_data = {
    "Color" : ["Negro", "Rojo", "Gris"],
    "Total" : [len(cinnamon_squirrels), len(black_squirrels), len(gray_squirrels)]
} #crea un diccionario con los colores negro, rojo y gris y en el total cuenta segun los colores

print(result_data)

squirrel_total = pd.DataFrame(result_data); #crea un nuevo dataframe con el resultado que teniamos anteriormente

print(squirrel_total)

squirrel_total.to_csv("squirrel_results.csv") #guarda el dataframe con el nombre squirrel_total