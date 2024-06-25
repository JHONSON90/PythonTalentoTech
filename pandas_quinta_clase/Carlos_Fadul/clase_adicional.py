import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'velocidad': [80,120,100]
}



myvar = pd.DataFrame(mydataset) #dataframe es un metodo para mirar los datos de forma mucho mas organizada

print(myvar)

print(pd.__version__)

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x","y","z"]) #aqui podemos cambiar el nombre del indice

print(myvar["y"])


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)



