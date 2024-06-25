import pandas as pd

data = pd.read_csv("data.csv")
print(data.head(5))

#? para limpiar datos en pandas podemos llenar celdas vacias, cambiar formatos de celdas, datos erroneos y duplicados

#! llenar celdas vacias
 
new_df = data.dropna() #este metodo no nos cambia el original pero si queremos que lo haga tenemos que colocarle dentro del parentesis (inplace=True) y lo que hace es eliminar las filas que contengan un valor null
print(new_df.to_string())

#! reemplazar valores vacios o null

new_df = data.fillna(130, inplace=True) # nos buscara todos los null en el dataframe y lo reemplazara por 130 y este cambio lo realizaria en todos los valores null
print(new_df)

#! reemplazar valores vacios en columnas especificas

new_df = data["Calories"].fillna(130, inplace=True)
print(data)
print(new_df)

#! reemplazar valores vacios con mean - promedio, median - valor medio o con mode - moda

mean = data["Calories"].mean() # promedio
median = data["Calories"].median() # medio
modal = data["Calories"].mode()[0] # moda el valor mas frecuente

new_df = data["Calories"].fillna(median, inplace=True) #aqui inyectamos la media en los valores nullen la columna calorias

#? cambiando formatos 

#! cambiar a fechas

#si nuestro csv tuviera fechas para cambiar toda una columna a fechas se realizaria de la siguiente manera

#df['date'] = pd.to_datetime(df['date']) colocamos primero la columna y la igualamos a el formato que le queremos dar que en este caso es date de fecha

#! eliminando filas con errores
#df.dropna(subset=['date'], inplace = True)

#? reemplazando valores

#! reemplazando valores especificos
# vamos a cambiar el de la duracion de 210 que esta en la fila 60
data.loc[60, "Duration"] = 60
print(data.head(62))

#! eliminando filas que la duracion este mayor a 120
"""
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)"""

#? eliminando duplicados
#el duplicated nos arroja como resultado un booleano que nos dice si esta o no repetido
print(data.duplicated()) 

#para eliminar lo realizariamos de la siguiente manera
data.drop_duplicates(inplace=True)
print(data)

#! sacar correlaciones

print(data.corr())

#! graficando con pandas



