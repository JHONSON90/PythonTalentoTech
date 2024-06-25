
#antes de utilizarlo lo tenemos que descargar con el comando pip install requests
import requests
import json


#vamos hacer un pedido a la pagina de wikipedia

URL = 'https://es.wikipedia.org/'

respuesta = requests.get(URL)

# el response de requests tiene los siguientes elementos principales:
#    .text, .content, .json(), .status_code

print(f'Data: {respuesta.text} \n')

#! HEADERS

URL = 'https://scrapepark.org/courses/spanish/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}
respuesta = requests.get(URL, headers=headers)
print(respuesta)