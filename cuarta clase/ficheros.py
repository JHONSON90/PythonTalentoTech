""" Manejo de Ficheros
El manejo de archivos es una parte muy importante de cualquier aplicación, ya sea para la escritura de logs como vbitácora de acciones o errores, o para el almacenamiento de datos.

En python existen un par de maneras de hacer, la primera y que tiene integrada entre sus funciones propias es el método open()

El método cuenta con las opciones que se presentan a continuación, aunque no todas son obligatorias

open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file es la ruta hacía el fichero que se quiere abrir, puede ser relativa o absoluta.
mode define la forma en la cual se abrirá el archivo, por defecto se abre en modo 'r' que es solo lectura pero cuenta con más opciones
Opción	Significado
'r'	abierto para lectura (por defecto)
'w'	abierto para escritura
'x'	abierto para creación en exclusiva, falla si el fichero ya existe
'a'	abierto para escritura, añadiendo al final del fichero si este existe
'b'	modo binario
't'	modo texto (por defecto)
'+'	abierto para actualizar (lectura y escritura)

buffering es opcional y. permite configurar la política del buffer
encoding es el nombre de la codificación empleada con el fichero. Esto solo debe ser usado en el modo texto, por ejemplo UTF-8
errors es una cadena opcional que especifica como deben manejarse los errores de codificación y descodificación – esto no puede ser usado en modo binario. Están disponibles varios gestores de error. Cuenta con opciones como:
'strict' para lanzar una excepción ValueError si hay un error de codificación. El valor por defecto, None, produce el mismo efecto.
'ignore' ignora los errores. Nótese que ignorar errores de codificación puede conllevar la pérdida de datos.
'replace' provoca que se inserte un marcador de reemplazo (como '?') en aquellos sitios donde hay datos malformados.
'surrogateescape' representará cualquier bytes incorrectos como unidades de código sustituto bajo que van desde U+DC80 a U+DCFF. Estas unidades de código sustituto volverán a convertirse en los mismos bytes cuando el gestor de errores surrogateescape sea usado al escribir datos. Esto es útil para el procesado de ficheros con una codificación desconocida.
'xmlcharrefreplace' está soportado solamente cuando se escribe a un fichero. Los caracteres que no estén soportados por la codificación son reemplazados por la referencia al carácter XML apropiado &#nnn;.
'backslashreplace' reemplaza datos malformados con las secuencias de escapes de barra invertida de Python.
'namereplace' reemplaza caracteres no soportados con secuencias de escape \N{...} (y también está sólo soportado en escritura).
newline determina cómo analizar los caracteres de nueva línea de la secuencia. Puede ser None, '', '\n', '\r', y '\r\n'.
Los archivos, como buena practica
"""
#es importante cerrarlos después de operar, para ello se utiliza el comando close()
f = open('/content/sample_data/anscombe.json', 'rt')

print(f.read(40)) #Puede leer todo el archivo con solo read() o indicar un número de carácteres

#o readline para leer una línea completa
print(f.readline())
print(f.readline())
print(f.readline())

# O ciclar por todo el archivo
for line in f:
  print(line)