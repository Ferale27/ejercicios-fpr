import turtle
import math

turtle.clearscreen()    # Borramos la pantalla
turtle.speed(1000)      # Aceleramos la velocidad
ladoEstrella = 10       # lado de cada estrella: 10 pixels
for i in range (3):    # dibujamos tres circulos
    numEstrellas = 10 + 5 * i  # número de estrellas en el circulo
    radioCirculo = 100 * (i + 1) # radio del circulo
    for i in range (numEstrellas):
        turtle.up()
        a = i * ((2*math.pi)/numEstrellas)
        turtle.setpos(radioCirculo * math.cos(a), radioCirculo * math.sin(a))
        turtle.down()
        for i in range (5):
            turtle.forward(ladoEstrella)
            turtle.right(144)
            turtle.forward(ladoEstrella)
            turtle.left(72)
turtle.hideturtle( )    # escondemos el logo de la tortuga
turtle.done()           # desbloquea la ventana, permite responder a eventos
try:
    turtle.bye()        # libera los recursos
except:
    pass