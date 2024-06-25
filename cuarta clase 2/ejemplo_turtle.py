import turtle

ventana = turtle.Screen()
mi_tortuga = turtle.Turtle()

for _ in range(4):
    mi_tortuga.forward(100)
    mi_tortuga.left(90)

ventana.mainloop()

