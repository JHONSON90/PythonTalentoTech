# los diccionarios son almacenados en llaves como los objetos de javascript
# de igual manera tiene sus metodos
"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
juan = {
    "nombre": "Juan",
    "apellido": "Doe",
    "edad": 10,
    "curso": 5,
    "materias": ["inglés", "matemáticas"],
}

# Para acceder a un valor, debemos hacerlo a través de las llaves
# Utilizando notación de corchetes
print(juan["nombre"])

# o utilizando método get

juan.get("edad")

# En caso de no conocer el diccionario, es posible obtener todas las llaves, sin imprimir el diccionario completo
print(juan.keys())

# también puede imprimir solo los valores
print(juan.values())

# y modificar valores

juan["materias"] = [
    {"asignatura": "ingles", "nota": 4},
    {"asignatura": "matemáticas", "nota": 4.5},
]
print(juan)

# También obtener los pares llave valor en tuplas con el metodo items
juan.items()

"""
Utilizando las estructuras de datos conocidas hasta el momento, 
su tarea es presentar la información de 5 asignaturas de un colegio, 
cada asignatura tiene información como el profesor, el nombre de la asignatura, 
el salón donde se da la clase, los horarios de las clases, 
cada salón tiene un número máximo de estudiantes, cada clase tiene un estudiante monitor, 
cada profesor tiene un correo y un horario de asesorías.
"""
cursos = (
    {
        "programacion": {
            "Profesor": {
                "nombre": "Roberto Pelaez",
                "email": "RobertoPelaez@gmail.com",
                "hras_asesorias": 3,
            },
            "Salon": "5A",
            "Horarios": "8:00 am a 2:00 pm",
            "n_max_estudiantes": 45,
            "est_monitor": "Francisco Navarro",
        },
        "ciencia_datos": {
            "Profesor": {
                "nombre": "Carlos Apraez",
                "email": "Carlosapraez@gmail.com",
                "hras_asesorias": 20,
            },
            "Salon": "15D",
            "Horarios": "10:00 am a 2:00 pm",
            "n_max_estudiantes": 20,
            "est_monitor": "Ricardo Cabrera",
        },
        "block_Chain": {
            "Profesor": {
                "nombre": "William Portilla",
                "email": "WilliamPortilla@gmail.com",
                "hras_asesorias": 60,
            },
            "Salon": "1A",
            "Horarios": "2:00 pm a 6:00 pm",
            "n_max_estudiantes": 30,
            "est_monitor": "Nicolas Rosero",
        },
        "react_native": {
            "Profesor": {
                "nombre": "Nancy Arteaga",
                "email": "NancyArteaga@gmail.com",
                "hras_asesorias": 40,
            },
            "Salon": "2A",
            "Horarios": "8:00 am a 2:00 pm",
            "n_max_estudiantes": 18,
            "est_monitor": "Carlos Estrada",
        },
        "astro": {
            "Profesor": {
                "nombre": "Juan Erazo",
                "email": "JuanErazo@gmail.com",
                "hras_asesorias": 15,
            },
            "Salon": "6",
            "Horarios": "8:00 am a 11:00 am",
            "n_max_estudiantes": 45,
            "est_monitor": "Rosa Valencia",
        },
    }
)
