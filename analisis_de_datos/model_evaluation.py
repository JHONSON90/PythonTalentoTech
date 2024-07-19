# para esta seccion vamos a utilizar los siguientes modulos

# pip install pandas matplotlib scipy scikit-learn seaborn ipywidgets

#importamos los datos 

from subidadedatos import data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

df = data

#primero vamos a usar solo las columnas de datos numericos
df = df._get_numeric_data()

#las librerias para las graficas serian 

from ipywidgets import interact, interactive, fixed, interact_manual

#Funcion para hacer la grafica
def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    ax1 = sns.kdeplot(RedFunction, color="r", label=RedName)
    ax2 = sns.kdeplot(BlueFunction, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')
    plt.show()
    plt.close()
    
def PollyPlot(xtrain, xtest, y_train, y_test, lr,poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    #training data 
    #testing data 
    # lr:  linear regression object 
    #poly_transform:  polynomial transformation object 
 
    xmax=max([xtrain.values.max(), xtest.values.max()])
    xmin=min([xtrain.values.min(), xtest.values.min()])
    x=np.arange(xmin, xmax, 0.1)

    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()

#! entrenando y testeando
# Un paso importante al probar su modelo es dividir sus datos en datos de entrenamiento y de prueba. Colocaremos el precio de datos objetivo en un marco de datos separado y_data:
y_data = df["price"]

#Colocamos la caida del precio en la variable x_data
x_data=df.drop('price',axis=1)

#Ahora, dividimos aleatoriamente nuestros datos en datos de entrenamiento y prueba usando la función train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)

print("number of test samples :", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

#Utilice la función "train_test_split" para dividir el conjunto de datos de modo que el 40% de las muestras de datos se utilicen para las pruebas. Establezca el parámetro "random_state" en cero. La salida de la función debe ser la siguiente: "x_train1", "x_test1", "y_train1" y "y_test1". 

x_train1,x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.4, random_state=0)
print("number of test samples :", x_test1.shape[0])
print("number of training samples:",x_train1.shape[0])

#? importamos el modulo de regresion lineal

from sklearn.linear_model import LinearRegression

# creamos el objeto de regresion lineal
lre=LinearRegression()

# ajustamos el modelo a la variable horsepower
lre.fit(x_train1[['horsepower']], y_train1)

#calculamos el r^2 en los datos de prueba
lre.score(x_test[['horsepower']], y_test) # 0.3635875575078824 con esto podemos mirar que el resultado es demasiado pequeño en comparacion con  la informacion de entrenamiento por eso lo vamos a calcular con los datos de entrenamiento

lre.score(x_train[['horsepower']], y_train)

#Find the R^2 on the test data using 40% of the dataset for testing.
x_train1, x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.4, random_state=0)
lre.fit(x_train1[['horsepower']],y_train1)
lre.score(x_test1[['horsepower']],y_test1)


#! CROOS VALIDATION SCORE

#Importamos cross_val_score  
from sklearn.model_selection import cross_val_score

#Ingresamos el objeto, la característica ("horsepower") y los datos del objetivo (y_data). El parámetro 'cv' determina el número de pliegues. En este caso son 4.

Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4)

# podemos calcular la media y la desviacion estandar 

print("The mean of the folds are", Rcross.mean(), "and the standard deviation is" , Rcross.std())

# Podemos utilizar el error cuadrado negativo como puntuación estableciendo la métrica de 'puntuación' del parámetro en 'neg_mean_squared_error'.

-1 * cross_val_score(lre,x_data[['horsepower']], y_data,cv=4,scoring='neg_mean_squared_error')

# Calcule el R^2 promedio usando dos pliegues, luego encuentre el R^2 promedio para el segundo pliegue utilizando la función "caballos de fuerza":
Rc=cross_val_score(lre,x_data[['horsepower']], y_data,cv=2)
Rc.mean()

# También puede utilizar la función 'cross_val_predict' para predecir la salida. La función divide los datos en el número especificado de pliegues, uno de ellos para pruebas y el otro para entrenamiento. Primero, importe la función:

from sklearn.model_selection import cross_val_predict

# Ingresamos el objeto, la característica "caballos de fuerza" y los datos de destino y_data. El parámetro 'cv' determina el número de pliegues. En este caso, es 4. Podemos generar un resultado:
yhat = cross_val_predict(lre,x_data[['horsepower']], y_data,cv=4)
yhat[0:5]

#! Overfitting, Underfitting and Model Selection
"""Resulta que los datos de prueba, a veces denominados "datos fuera de muestra", son una medida mucho mejor de qué tan bien se desempeña su modelo en el mundo real. Una razón para esto es el sobreajuste.

Repasemos algunos ejemplos. Resulta que estas diferencias son más evidentes en la regresión lineal múltiple y la regresión polinómica, por lo que exploraremos el sobreajuste en ese contexto."""

# vamos a crear una regresion lineal multiple  usando 'horsepower', 'curb-weight', 'engine-size' and 'highway-mpg'

lr = LinearRegression()
lr.fit(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_train)

# predicciones usando datos de entrenamiento
yhat_train = lr.predict(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
yhat_train[0:5]

# Predicciones usando datos de test
yhat_test = lr.predict(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
yhat_test[0:5]

# vamos a modelar la evaluacion usando los datos de entrenamiento y los test separadamente pero primero importemos las graficas

import matplotlib.pyplot as plt
import seaborn as sns

# examinemos la distribucion y la prediccion de los valores entrenados

Title = 'Distribution  Plot of  Predicted Value Using Training Data vs Training Data Distribution'
DistributionPlot(y_train, yhat_train, "Actual Values (Train)", "Predicted Values (Train)", Title)

# Hasta ahora, el modelo parece estar funcionando bien en el aprendizaje del conjunto de datos de entrenamiento. Pero, ¿qué sucede cuando el modelo encuentra nuevos datos del conjunto de datos de prueba? Cuando el modelo genera nuevos valores a partir de los datos de prueba, vemos que la distribución de los valores predichos es muy diferente de los valores objetivo reales.

Title='Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution of Test Data'
DistributionPlot(y_test,yhat_test,"Actual Values (Test)","Predicted Values (Test)",Title)

# Al comparar la Figura 1 y la Figura 2, es evidente que la distribución de los datos de prueba en la Figura 1 ajusta mucho mejor los datos. Esta diferencia en la Figura 2 es evidente en el rango de 5.000 a 15.000. Aquí es donde la forma de la distribución es extremadamente diferente. Veamos si la regresión polinómica también muestra una caída en la precisión de la predicción al analizar el conjunto de datos de prueba.

#! Overfitting

# El sobreajuste ocurre cuando el modelo se ajusta al ruido, pero no al proceso subyacente. Por lo tanto, al probar su modelo utilizando el conjunto de prueba, su modelo no funciona tan bien ya que está modelando ruido, no el proceso subyacente que generó la relación. Creemos un modelo polinómico de grado 5.

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.45, random_state=0)

# Realizaremos una transformación polinómica de grado 5 en la característica 'caballos de fuerza'.
pr = PolynomialFeatures(degree=5)
x_train_pr = pr.fit_transform(x_train[['horsepower']])
x_test_pr = pr.fit_transform(x_test[['horsepower']])

# Ahora crearemos un modelo de regresion lineal de poly y entrenarla
poly = LinearRegression()
poly.fit(x_train_pr, y_train)
 
#miremos la prediccion
yhat = poly.predict(x_test_pr)

# Tomemos los primeros cinco valores predichos y compárelos con los objetivos reales..
print("Predicted values:", yhat[0:4])
print("True values:", y_test[0:4].values)

#Usaremos la función "PollyPlot" que definimos al comienzo para mostrar los datos de entrenamiento, los datos de prueba y la función predicha.
PollyPlot(x_train['horsepower'], x_test['horsepower'], y_train, y_test, poly,pr)

# Figura 3: Un modelo de regresión polinómica donde los puntos rojos representan datos de entrenamiento, los puntos verdes representan datos de prueba y la línea azul representa la predicción del modelo.

# Vemos que la función estimada parece rastrear los datos, pero alrededor de 200 caballos de fuerza, la función comienza a divergir de los puntos de datos.

#R^2 de los datos de entrenamiento:
poly.score(x_train_pr, y_train) # 0.5567716897754004
#R^2 de los datos de test:
poly.score(x_test_pr, y_test) # -29.8709962338727

#Vemos que el R^2 de los datos de entrenamiento es 0,5567, mientras que el R^2 de los datos de prueba fue -29,87. Cuanto menor sea el R^2, peor será el modelo. Un R^2 negativo es un signo de sobreajuste

#Veamos cómo cambia R ^ 2 en los datos de prueba para polinomios de diferentes órdenes y luego tracemos los resultados.

Rsqu_test = []

order = [1, 2, 3, 4]
for n in order:
    pr = PolynomialFeatures(degree=n)
    
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    
    x_test_pr = pr.fit_transform(x_test[['horsepower']])    
    
    lr.fit(x_train_pr, y_train)
    
    Rsqu_test.append(lr.score(x_test_pr, y_test))

plt.plot(order, Rsqu_test)
plt.xlabel('order')
plt.ylabel('R^2')
plt.title('R^2 Using Test Data')
plt.text(3, 0.75, 'Maximum R^2 ')

# Vemos que R^2 aumenta gradualmente hasta que se utiliza un polinomio de orden tres. Luego, R ^ 2 disminuye drásticamente en un polinomio de orden cuatro.
def f(order, test_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=test_data, random_state=0)
    pr = PolynomialFeatures(degree=order)
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])
    poly = LinearRegression()
    poly.fit(x_train_pr,y_train)
    PollyPlot(x_train['horsepower'], x_test['horsepower'], y_train,y_test, poly, pr)
    
# Podemos realizar transformaciones polinomiales con más de una característica. Creamos un objeto "PolynomialFeatures" "pr1" de grado dos.

pr1 = PolynomialFeatures(degree=2)

# Transformamos las muestras de entrenamiento y prueba para las características "caballos de fuerza", "peso en vacío", "tamaño del motor" y "mpg en carretera". utilizando el método "fit_transform".

x_train_pr1 = pr1.fit_transform(x_train[["horsepower",  'curb-weight', 'engine-size' , 'highway-mpg']])
x_test_pr1 = pr1.fit_transform(x_test[["horsepower",  'curb-weight', 'engine-size' , 'highway-mpg']])

# utilizando shape mirar cuantas dimensiones tiene la caracteristica

x_train_pr1.shape #imprime(110,15) la respuesta es 15 dimensiones

# Cree un modelo de regresión lineal "poly1". Entrene el objeto usando el método "ajustar" usando las características polinomiales

poly1 = LinearRegression().fit(x_train_pr1, y_train)

# Utilice el método "predict" para predecir una salida en las características polinomiales, luego use la función "DistributionPlot" para mostrar la distribución de la salida de prueba prevista frente a los datos de prueba reales.

yhat_test1=poly1.predict(x_test_pr1) # hacemos la prediccion
Title='Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution of Test Data' #le da un titulo a la grafica
DistributionPlot(y_test, yhat_test1, "Actual Values (Test)", "Predicted Values (Test)", Title) #graficamos

# Utilizando el gráfico de distribución anterior, describa (en palabras) las dos regiones donde los precios previstos son menos precisos que el precio real.

#El valor previsto es mayor que el valor real para los automóviles cuyo precio oscila entre $ 10 000; por el contrario, el precio previsto es menor que el precio de costo en el rango de $ 30 000 a $ 40 000. Como tal, el modelo no es tan preciso en estos rangos.

#! RIDE REGRESSION - Regresión de cresta

# En esta sección, revisaremos la regresión de crestas y veremos cómo el parámetro alfa cambia el modelo. Solo una nota, aquí nuestros datos de prueba se utilizarán como datos de validación.

# Realicemos una transformación polinómica de grado dos en nuestros datos.

pr=PolynomialFeatures(degree=2)
x_train_pr=pr.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_pr=pr.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])

from sklearn.linear_model import Ridge
# creamos una regresion de cresta  estableciendo el parametro de regularizacion  (alpha) en 1
RigeModel=Ridge(alpha=1)

# como en la regresion regular podemos ajustar el modelo utilizando el metodo fit
RigeModel.fit(x_train_pr, y_train)

# igualmente podemos obtener la prediccion
yhat = RigeModel.predict(x_test_pr)

# comparemos las primeras cuatro muestras predichas con nuestro conjunto de prueba
print('predicted:', yhat[0:4])
print('test set :', y_test[0:4].values)

#Seleccionamos el valor de alfa que minimice el error de prueba. Para hacerlo, podemos usar un bucle for. También hemos creado una barra de progreso para ver cuántas iteraciones hemos completado hasta ahora.

from tqdm import tqdm

Rsqu_test = []
Rsqu_train = []
dummy1 = []
Alpha = 10 * np.array(range(0,1000))
pbar = tqdm(Alpha)

for alpha in pbar:
    RigeModel = Ridge(alpha=alpha) 
    RigeModel.fit(x_train_pr, y_train)
    test_score, train_score = RigeModel.score(x_test_pr, y_test), RigeModel.score(x_train_pr, y_train)
    
    pbar.set_postfix({"Test Score": test_score, "Train Score": train_score})

    Rsqu_test.append(test_score)
    Rsqu_train.append(train_score)

# 100%|██████████| 1000/1000 [00:05<00:00, 188.83it/s, Test Score=0.564, Train Score=0.859]

# podemos graficar el valor de r^2 para diferentes alphas

width = 12
height = 10
plt.figure(figsize=(width, height))

plt.plot(Alpha,Rsqu_test, label='validation data  ')
plt.plot(Alpha,Rsqu_train, 'r', label='training Data ')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()

#La línea azul representa el R^2 de los datos de validación y la línea roja representa el R^2 de los datos de entrenamiento. El eje x representa los diferentes valores de Alpha.
#Aquí el modelo se construye y prueba con los mismos datos, por lo que los datos de entrenamiento y prueba son los mismos.
#La línea roja en la Figura 4 representa el R^2 de los datos de entrenamiento. A medida que alfa aumenta, R ^ 2 disminuye. Por lo tanto, a medida que aumenta alfa, el modelo se desempeña peor en los datos de entrenamiento.
#La línea azul representa el R^2 en los datos de validación. A medida que aumenta el valor de alfa, R^2 aumenta y converge en un punto. 

# Realizar regresión de Ridge. Calcule R^2 usando las características polinómicas, use los datos de entrenamiento para entrenar el modelo y use los datos de prueba para probar el modelo. El parámetro alfa debe establecerse en 10.

RigeModel=Ridge(alpha=10)
RigeModel.fit(x_train_pr, y_train)
RigeModel.score(x_test_pr, y_test)

# El término alfa es un hiperparámetro. Sklearn tiene la clase GridSearchCV para simplificar el proceso de encontrar el mejor hiperparámetro.
# Importemos GridSearchCV desde el módulo model_selection.
from sklearn.model_selection import GridSearchCV

#creamos un diccionario de parametros 
parameters1 = [{'alpha': [0.001,0.1,1, 10, 100, 1000, 10000, 100000, 100000]}]

#creamos una regresion ridge
RR=Ridge()
# Cree un objeto de búsqueda de cuadrícula de crestas: 
Grid1 = GridSearchCV(RR, parameters1,cv=4)

#Para evitar una advertencia de obsolescencia debido al parámetro iid, configuramos el valor de iid en "Ninguno".
#Ajustar el modelo:

Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)

#El objeto encuentra los mejores valores de parámetros en los datos de validación. Podemos obtener el estimador con mejores parámetros y asignarlo a la variable BestRR de la siguiente manera:

BestRR=Grid1.best_estimator_

# Ahora probamos nuestro modelo con los datos de prueba.
BestRR.score(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_test)

# Realice una búsqueda en cuadrícula para el parámetro alfa y el parámetro de normalización, luego encuentre los mejores valores de los parámetros:

parameters2 = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000, 100000, 100000]}]

Grid2 = GridSearchCV(Ridge(), parameters2, cv=4)
Grid2.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)
best_alpha = Grid2.best_params_['alpha']
best_ridge_model = Ridge(alpha=best_alpha)
best_ridge_model.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)