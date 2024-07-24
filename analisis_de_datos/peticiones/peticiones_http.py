import requests
import os

from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'

#hacemos una peticion a la url
r=requests.get(url)
#imprimimos el estado osea un 200 diciendo que la peticion se realizo correctamente
print(r.status_code)

#imprimimos los encabezados de lo que me trajo
print(r.request.headers)

#imprimimos 
print("request body:", r.request.body)

#Puede ver el encabezado de respuesta HTTP utilizando los encabezados de atributos. Esto devuelve un diccionario Python de encabezados de respuesta HTTP.
header=r.headers
print(r.headers)

#podemos imprimir la fecha que se hizo la peticion
header['date']

#imprimimos tambien el tipo de contenido que tiene la peticion
header['content-type']

#podemos tambien imprimir la codificacion
r.encoding

# Como el tipo de contenido es texto/html, podemos usar el atributo texto para mostrar el HTML en el cuerpo. Podemos repasar los primeros 100 caracteres:
print(r.text[0:100])

#podemos tambien hacer la peticion de imagenes asi como el siguiente
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r = requests.get(url)

print(r.headers)
print(r.headers["Content-Type"]) #imprimira que es una imagen/png

#Una imagen es un objeto de respuesta que contiene la imagen como un objeto similar a bytes. Como resultado, debemos guardarlo usando un objeto de archivo. Primero, especificamos la ruta y el nombre del archivo
path=os.path.join(os.getcwd(),'image.png')

#Guardamos el archivo, para acceder al cuerpo de la respuesta usamos el atributo content y luego lo guardamos usando la función open y el método write
with open(path,'wb') as f:
    f.write(r.content)
#mostramos la imagen
print(Image.open(path))


# hacemos lo mismo pero con un archivo txt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"

path= os.path.join(os.getcwd(), "Example1.txt")
r = requests.get(url)
with open(path, "wb") as f:
    f.write(r.content)

# podemos hacer el requerimiento con la url con parametros
url_get= "http://httpbin.org/get"

# Para crear una cadena de consulta, agregue un diccionario. Las claves son los nombres de los parámetros y los valores son el valor de la cadena de consulta.
payload={"name":"Joseph","ID":"123"}

#Luego, pasa la carga útil del diccionario al parámetro params de la función get():
r = requests.get(url_get, params=payload)

#imprimimos la url
print(r.url)
# Imprimimos el body pero no hay cuerpo de solicitud
print("request body:", r.request.body)

#Imprimimos la respuesta como texto

print(r.text)

#Podemos imprimir el content type
print(r.headers["Content-Type"])

#cambiamos el json que nos responde por un dict que puede ser interpretado en python
print(r.json())

# podemos imprimir los args
print(r.json()["args"])

#! vamos hacer envio de informacion con un post o creamos informacion

url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)

#comparamos como son las respuestas de un post con u get
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

# Ahora comparamos el cuerpo de una peticion get con una post
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

# podemos mirar el formulario
r_post.json()['form']

import json
import pandas as pd
#usando requests.get() funcion cargar la informacion de la url

data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")

#con la funcion json.loads() trae los resultados
jokes = json.loads(data2.text)

#convertir el json en un dataframe

df = pd.DataFrame(jokes)
#quitamos el typo e id del data frame
df.drop(columns=['type','id'],inplace=True)

print('1,2,3,4'.split(','))