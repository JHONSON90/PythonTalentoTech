from subidadedatos import data
df = data
# simple linear regression 

#vamos a instalar o verificar que este instalado  
"""pip install 'pandas'
pip install'matplotlib'
pip install'scipy'
pip install'scikit-learn'
pip install'skillsnetwork', 'seaborn'"""

#! linear regression

from sklearn.linear_model import LinearRegression
import matplotlib as plt
import numpy as np

# creamos la linea de regresion
lm = LinearRegression()

# vamos a  ver cómo el mpg en carretera puede ayudarnos a predecir el precio del automóvil. Utilizando una regresión lineal simple, crearemos una función lineal con "mpg en carretera" como variable predictiva y el "precio" como variable de respuesta.

X = df[['highway-mpg']]
Y = df['price']

# asignamos la linea de regresion a las columnas
lm.fit(X,Y)

# sacamos la prediccion
Yhat=lm.predict(X)
Yhat[0:5]  # imprime las primeras 5 predicciones

# sacamos la intercepcion
lm.intercept_

# Se imprime el valor de los coeficientes de regresión utilizando el atributo coef_ de la instancia lm
lm.coef_

lm1 = LinearRegression()

lm1.fit(df[["engine-size"]], df[["price"]])

lm1.coef_ # array([[166.86001569]])
lm1.intercept_ # array([-7963.33890628])

# What is the equation of the predicted line? You can use x and yhat or "engine-size" or "price".

Yhat=-7963.34 + 166.86*X #intercep + coef * X

Price=-7963.34 + 166.86*df['engine-size']

#! Multiple Linear Regression
#creamos la linea de regresion
lm = LinearRegression()

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

# podemos asignar de una vez los valores en la linea de regresion 
lm.fit(Z, df['price']) # lm.fit(df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], df['price'])
# sacamos intercepcion
lm.intercept_
# sacamos coheficiente 
lm.coef_


#vamos a graficar todo esto
import seaborn as sns

# vamos a utilizar la grafica de regresion con highwat vs precio
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)

#comparacion peak rpm vs precio
plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)

# calculando la correlacion entre peak higway y precio

df[["peak-rpm","highway-mpg","price"]].corr()

#! RESIDUAL PLOT
"""
Una buena forma de visualizar la varianza de los datos es utilizar un gráfico de residuos.
¿Qué es un residual?
La diferencia entre el valor observado (y) y el valor predicho (Yhat) se llama residual (e). Cuando observamos un gráfico de regresión, el residual es la distancia desde el punto de datos hasta la línea de regresión ajustada.
Entonces, ¿qué es una trama residual?
Una gráfica de residuos es una gráfica que muestra los residuos en el eje y vertical y la variable independiente en el eje x horizontal.
¿A qué prestamos atención cuando miramos una trama residual?
Nos fijamos en la dispersión de los residuos:
- Si los puntos en una gráfica residual están distribuidos aleatoriamente alrededor del eje x, entonces un modelo lineal es apropiado para los datos.
¿Porqué es eso? Los residuos distribuidos aleatoriamente significan que la varianza es constante y, por lo tanto, el modelo lineal se ajusta bien a estos datos.
"""

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(x=df['highway-mpg'],y=df['price'])
plt.show()

""" 
    Podemos ver en este gráfico de residuos que los residuos no están distribuidos aleatoriamente alrededor del eje x, lo que nos lleva a creer que tal vez un modelo no lineal sea más apropiado para estos datos."""

# HACIENDO UNA NUEVA PREDICCION
Y_hat = lm.predict(Z)

plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()
 
""" Podemos ver que los valores ajustados están razonablemente cerca de los valores reales ya que las dos distribuciones se superponen un poco. Sin embargo, definitivamente hay margen de mejora. 
 """

#! Polynomial Regression and Pipelines

""" Vimos anteriormente que un modelo lineal no proporcionaba el mejor ajuste cuando se utilizaba "mpg en carretera" como variable predictiva. Veamos si podemos intentar ajustar un modelo polinomial a los datos.

Usaremos la siguiente función para trazar los datos: """

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()
    
# ASIGNANDO VARIABLES .

x = df['highway-mpg']
y = df['price']

# Ajustemos el polinomio usando la función polyfit, luego usemos la función poly1d para mostrar la función polinomial.
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)

# DAMOS VALORES A LA FUNCION Y LLAMAMOS LA FUNCION

PlotPolly(p, x, y, 'highway-mpg')

np.polyfit(x, y, 3)

#Create 11 order polynomial model with the variables x and y from above.
f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)
print(p1)
PlotPolly(p1,x,y, 'Highway MPG')

#importamos el modulo de sklearn para hacer los polinomios
from sklearn.preprocessing import PolynomialFeatures

#creamos otro polinomio de degree= 2
pr=PolynomialFeatures(degree=2)
Z_pr=pr.fit_transform(Z)
#En los datos originales, hay 201 muestras y 4 características.
Z.shape
#Después de la transformación, hay 201 muestras y 15 funciones.
Z_pr.shape

#! PIPELINE

#Los Pipelines de datos simplifican los pasos de procesamiento de los datos. Usamos el módulo Pipeline para crear una canalización. También utilizamos StandardScaler como un paso en nuestro proceso.

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#Creamos la canalización creando una lista de tuplas que incluye el nombre del modelo o estimador y su correspondiente constructor.

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]

# la lista del input es un argumento para el constructor del pipeline
pipe=Pipeline(Input)

#Primero, convertimos el tipo de datos Z al tipo flotante para evitar advertencias de conversión que puedan aparecer como resultado de que StandardScaler tome entradas flotantes.

#Luego, podemos normalizar los datos, realizar una transformación y ajustar el modelo simultáneamente.

Z = Z.astype(float)
pipe.fit(Z,y)

# normalizamos los datos y producimos la prediccion
ypipe=pipe.predict(Z)

# Cree una canalización que estandarice los datos y luego produzca una predicción utilizando un modelo de regresión lineal utilizando las características Z y el objetivo y.

Input = [("scale", StandardScaler()), ("model", LinearRegression())]
pipe=Pipeline(Input)

pipe.fit(Z,y)
ypipe=pipe.predict(Z)
print(ypipe[0:10])