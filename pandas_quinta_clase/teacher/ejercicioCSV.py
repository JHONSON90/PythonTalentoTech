import csv

dias = []
temperaturas = []
condiciones = []

# Nombre del archivo CSV
#_nombre_archivo = 'datos.csv'

# Leer el archivo CSV
with open('weather_data.csv') as data_file:
    # Crear un lector CSV
    lector_csv = csv.reader(data_file)
    # Iterar sobre cada fila del archivo
    for i, fila in enumerate(lector_csv): #nos proporciona tanto el índice como el elemento en cada iteración del bucle for
        # Saltar la primera fila (encabezados)
        if i == 0:
            continue
        # Leer los valores de la fila y almacenarlos en las listas correspondientes
        dia, temperatura, condicion = fila
        dias.append(dia)
        temperaturas.append(int(temperatura))
        condiciones.append(condicion)
        
        print("Dias:", dias)
        print("Temperatura:", temperaturas)
        print("Condicion:", condiciones)
        
        lista_float = [float(numero) for numero in temperaturas]
        print(lista_float)