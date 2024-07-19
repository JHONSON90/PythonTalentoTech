import pandas as pd
import numpy as np


data = pd.read_csv('analisis_de_datos/vehiculos.csv')

print(data.head())
print(data.tail())
print(data.describe())
print(data.describe(include="all"))
print(data.info())

# para editar las filas de los dataframes podemos usar este comando 

#data["Hectare Squirrel Number"]= data["Hectare Squirrel Number"]+1

#usamos dropna() para eliminar los datos que no son validos o que tienen na 
#para el ejemplo vamos a quitar las ardillas que no tengan edad age

#! data.dropna(subset=["Age"], axis=0, inplace=True)
#! print(data.head())

#para remplazar los valores no validos se utilizaria la funcion replace
"""
mean = data["Hectare Squirrel Number"].mean()
data["Hectare Squirrel Number"].replace(np.nan, mean)
print(data.head())
"""

#? correccion de datos

#! cambiar tipo de datos de una columna
"""
df["Ciudad-mpg"] = 235/df["Ciudad-mpg"] divide el valor original a (235/ el valor que estaba en la celda)
df.rename(columns={"city_mpg": "City-L/100km"}, inplace=true cambia el nombre de la columna algo importante es el inplace hace los cambios al dataframe original 

dt["Price"]= df["Price"].astype("int")
"""

#?normalizacion de datos
"""
formulas 

1)xnew= xold/xmax  simple feture scaling
2)xnew = xold-xmin/xmax - xmin  min max
3)xnew = xold-u/0 z-score

df["nombrecolumna"] = (df["nombrecolumna"] - df["nombrecolumna"].mean())/df["nombrecolumna"].std()
"""

#? agrupaciones en python
"""
primero vamos hacer unos bins que nos clasifique el rango de valores que hay en la tabla

bins = np.linspace(min(df["price"]), max(df["price"]),4)
group_names = ["low", "Medium", "High"]
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)
"""

#? cambiando variables cualitativas a cuantitativas osea cuando tengo un texto y quiero convertirlo en un 1

# pd.get_dummies(df["nombre de la columna que tiene las variables en texto"])

#! LABORATORIO



print("---------------------------------------------------------------------------------------------------------------------")


# Cambiar los encabezados
# df = df.rename(columns={'viejo_encabezado1': 'nuevo_encabezado1', 'viejo_encabezado2': 'nuevo_encabezado2',...})


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

data.columns = headers
print(data.head())

# reemplazar los "?" en nan

data.replace("?", np.nan, inplace=True)
print(data.head())

#! evaluando informacion perdida

missing_data = data.isnull() # indica que valores son nulos y coloca como verdadero, tambien podemos hacer lo contrario con notnull()
print(missing_data.head())

#! contar valores nulos por columna

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
    
#! cambiando el valor de los Nan 
#calculamos el promedio para cambiar el nan por el promedio

avg_norm_loss = data["normalized-losses"].astype("float").mean(axis=0)
print("el Promedio para esta columna es: ", avg_norm_loss)

# cambiamos los nan por el promedio
data["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)
print(data.head())


# contar por numero de puertas cuantos registros hay
print(data["num-of-doors"].value_counts())

# sacar valores unicos de una columna
print(data["num-of-doors"].unique())

# si queremos saber cual es el registro que mas se utiliza en el numero de puertas utilizamos el idxmax

data['num-of-doors'].value_counts().idxmax()

#eliminar los valores nan de price
data.dropna(subset=["price"], axis=0, inplace=True)

# colocar un nuevo indice xq se quitaron dos filas entonces la numeracion ya no es consecutiva

data.reset_index(drop=True, inplace=True)

# miramos que tipo de datos estan en cada columna
print(data.dtypes)

# vamos a cambiar los tipos de datos de cada una de las columnas
data[["bore", "stroke"]] = data[["bore", "stroke"]].astype("float")
data[["normalized-losses"]] = data[["normalized-losses"]].astype("int")
data[["price"]] = data[["price"]].astype("float")
data[["peak-rpm"]] = data[["peak-rpm"]].astype("float")


# transformando datos vamos a cambiar la columna highway-mpg 
data["highway-mpg"] = 235/data["highway-mpg"] # utilizamos la misma columna para cambiar los datos osea estamos dividiendo 235/ el valor que esta actualmente en la columna

#reemplazamos el nombre de la columna
data.rename(columns={"highway-mpg":'highway-L/100km'}, inplace=True) #dentro de las llaves va el nombre actual y despues de los dos puntos el nuevo nombre

#cambiando valores y reemplazando los valores originales por el valor original / con el maximo de la columna
data["height"] = data["height"]/data["height"].max()

#imprimiendo en consola columnas en especifico
data[["length","width","height"]].head()

data["horsepower"]= data["horsepower"].astype(float, copy = True)

#vamos a graficar los caballos de fuerza 

# import matplotlib as plt
# from matplotlib import pyplot

# plt.pyplot.hist(data["horsepower"])

# #establecer el eje x y y labels and plot tittle

# plt.pyplot.xlabel("horsepower")
# plt.pyplot.ylabel("count")
# plt.pyplot.title("horsepower bins")

#vamos a crear tres grupos bajo medio y alto con los caballos de fuerza

bins = np.linspace(min(data["horsepower"]), max(data["horsepower"]), 4)
print(bins)

group_names = ["Low", "Medium", "High"]

#Crea una nueva columna llamada 'horsepower-binned' que contiene los valores binneados de la columna 'horsepower'. Los valores binneados se obtienen dividiendo los valores de 'horsepower' en intervalos específicos llamados 'bins'. Los intervalos se definen mediante la variable 'bins' y los nombres de las etiquetas de los intervalos se especifican en la variable 'group_names'. El parámetro 'include_lowest=True' indica que el intervalo más bajo debe incluir el valor más bajo de 'horsepower'.

data['horsepower-binned'] = pd.cut(data['horsepower'], bins, labels=group_names, include_lowest=True )
print(data[['horsepower','horsepower-binned']].head(20))

print(data["horsepower-binned"].value_counts())

"""
# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

"""
print(data.columns) #imprime los nombres de las columnas

# hacer un dummy variable con el tipo de combustible 

dummy_variable_1 = pd.get_dummies(data['fuel-type'])
print(dummy_variable_1.head(20))

#cambiamos el nombre de las columnas

dummy_variable_1.rename(columns={"gas": "fuel-type-gas", "diesel": "fuel-type-diesel"}, inplace=True)

#adicionamos los dummis a la tabla original

data = pd.concat([data, dummy_variable_1], axis=1)
#eliminamos la columna de fuel type
data.drop("fuel-type", axis=1, inplace=True)
