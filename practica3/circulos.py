import turtle

circulos = int(input('Introduce el número de círculos: '))

for i in range(circulos):
    if turtle.color() == ('red', 'red'):
        turtle.color('blue')
    else: turtle.color('red')
    turtle.circle(100)
    turtle.right(360/circulos)

turtle.done()
