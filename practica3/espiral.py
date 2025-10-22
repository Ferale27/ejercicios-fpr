import turtle

for i in range(38):
    if turtle.color() == ('red', 'red'):
        turtle.color('blue')
    elif turtle.color() == ('blue', 'blue'):
        turtle.color('green')
    else: turtle.color('red')
    turtle.forward(i*10)
    turtle.left(90)

turtle.done()
