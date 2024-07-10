# para esta seccion vamos a utilizar los siguientes modulos

# pip install pandas matplotlib scipy scikit-learn seaborn ipywidgets

#importamos los datos 

from subidadedatos import data

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