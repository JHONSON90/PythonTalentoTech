
#crear dataframes
"""
Nombre,edad,peso,enfermedad,dirección,teléfono
Lina Trejo,25,85,obesidad,diagonal-12,3105823695
Jose Luna,45, ,hipertencionArterial,prados del sur, 325456875
Carlos Mangual, 35,65,diabetes,laureles,3156458796
Mauricio Linares,18,70,asma,,3216549856
Javier Coral, 35,73,depresión,rosales,3186542175
Gisela Gonzales, 29,73,asma,santodomingo,3254875698
Natalia Narvaez, 36,65,hipertencionArterial,lapradera,3154789565
Caren Solarte, , 56,diabetes,Sanlucas,

"""

import pandas as pd

# datos = {
#     'nombre': ["Lina Trejo", "Jose Luna", "Carlos Mangual", "Mauricio Linares", "Javier Coral","Gisela Gonzales", "Natalia Narvaez", "Caren Solarte"],
#     'edad': [25,45,35,18,35,29,36,None],
#     'peso': [85,None,65,70,73,73,65,56],
#     'enfermedad': ['obesidad','hipertencionArterial','diabetes','asma','depresión','asma','hipertencionArterial','diabetes'],
#     'dirección':['diagonal-12','prados del sur','laureles','','rosales','santodomingo','lapradera','Sanlucas'],
#     'telefono':[3105823695,325456875,3156458796,3216549856,3186542175,3254875698,3154789565,None]
# }


df = pd.read_csv('datos.csv')

# explorando el dataframe
print(df.head())
print(df.info())
print(df.describe())

#imprime una columna
print(df['Nombre'])

#pacientes con obesidad
pacientes_obesidad = df.loc[df['enfermedad'] == "obesidad"]
print(pacientes_obesidad)

# agregando alergias en el df
df["alergias"] = pd.Series([True,True,False,False,True,False,True,False])

print(df)

#cambiando el nombre en la columna
df.rename(columns={'Nombre': "Paciente"})
print(df.head())

#borrando direccion
df.pop("dirección")
print(df.head())

#ordenando valores
print(df.sort_values(by="edad", ascending=True))
print(df.sort_values(by="edad", ascending=False))

#rellenando Nan
print(df.fillna(0))

#agrupando el df
print(df.groupby('edad').agg({'edad': "mean", 'enfermedad': 'count'}))

# estadisticas descriptivas
estadisticas_descriptivas = df[["edad","enfermedad"]].describe()
print(estadisticas_descriptivas)

#encontrar correlaciones
#correlaciones = df.corr()
#print(correlaciones)

#aplicando aply

print(df['edad'].apply(lambda x: x * 2))

# combinando columnas

import matplotlib.pyplot as plt
import numpy as np

import matplotlib  as mpl
#agrupando el df

agrupado = df.groupby('edad').agg({'enfermedad': 'count'})
print(agrupado)

fig,ax = plt.subplots()
ax.plot(agrupado)

plt.show()


