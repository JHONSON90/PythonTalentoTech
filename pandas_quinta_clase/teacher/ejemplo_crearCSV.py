#creado csv 
import csv

weather_data = [
    ['dia', 'temperatura', 'condicion'],
    ['lunes', 25, 'soleado'],
    ['Martes', 30, 'lluvioso'],
    ['miercoles', 35, 'nublado'],
    ['jueves', 40, 'Soleado'],
    ['viernes',12,'nublado']
    
    
]

nombre_archivo = 'weather_data.csv'

with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv) # Crear un objeto escritor de CSV
    for fila in weather_data:
        escritor_csv.writerow(fila)

print("Archivo CSV creado exitosamente:", nombre_archivo)

# ejemplo aplicaion recorriido
with open('weather_data.csv') as data_file:
    #Se recorre el archivo y se crea un iterable en data
    data = csv.reader(data_file)
    for row in data:
        print(row)