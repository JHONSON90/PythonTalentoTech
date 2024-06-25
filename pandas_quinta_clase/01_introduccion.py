import csv

#crear un archivo csv
weather_data = [
    ["Day", "Temp","Condition"],
    ["Monday",12,"Sunny"],
    ["Tuesday",14,"Rain"],
    ["Wednesday",15,"Rain"],
    ["Thursday",14,"Cloudy"],
    ["Friday",21,"Sunny"],
    ["Saturday",22,"Sunny"],
    ["Sunday",24,"Sunny"],
]
#crea el objeto primero se abre el archivo 
nombre_archivo = 'weather_data.csv'

with open(nombre_archivo, mode="w",newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv) #crear un objeto escritor de csv
    for fila in weather_data:
        escritor_csv.writerow(fila)
        
print("archivo csv creado exitosamente", nombre_archivo, weather_data)