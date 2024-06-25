import turtle

interfaz= turtle.Screen()
interfaz.title("Matriz puntos")

filas= 8
columnas= 8
espacio_p= 80

def dibujar_punto(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(20, color)

for fila in range(filas):
    for columna in range(columnas):
        x = columna * espacio_p - (columnas * espacio_p) /2
        y = fila * espacio_p - (filas * espacio_p) /2
        color = ("Black")
        dibujar_punto(x, y, color)

# Ocultar la tortuga y mantener la ventana abierta

interfaz.mainloop()


