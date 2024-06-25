import pandas as pd

df = pd.read_csv(
'https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')

print(df.rename(columns={'nombre':'nombre y apellidos', 'altura':'estatura'}, index={0:1000, 1:1001, 2:1002}).head()) # con este metodo cambiamos los nombres de los indices osea los nombres de las filas

print(df.set_index("nombre").head()) # definimos que se quite el indice y que el metodo nombre queda como indice y cambiamos de nombres y apellidos y queda como nombre nada mas

#? accediendo a un elemento

print(df.loc[1], end= '\n\n') # con este metodo accedemos a un elemento en especifico y lo imprimimos con un salto de linea al final 
print(df.loc[1]) # imprime el dato del segundo elemento del df


print(df.iloc[0, 0]) # con este metodo accedemos a un elemento en especifico accediendo a la ubicacion fila 0 columna 0 

#vamos acceder a la posicion 2 de la columna edad
print(df.loc[2, 'edad'])

#vamos acceder a las posiciones 2 y 5 y las imprimimos

print(df.loc[[2, 5]])

# agregar columnas en el dataframe

df['diabetes'] = pd.Series([False, False, True, False, True])
print(df)

# quitar columnas 

df.pop('diabetes')
print(df)

print("----------------datos desconocidos---------------------------")
# eliminar filas con datos desconocidos

print(df.dropna(subset="colesterol"))
