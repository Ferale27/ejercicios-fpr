import math

x = float(input('Introduce la coordenada x del punto: '))
y = float(input('Introduce la coordenada y del punto: '))
m = float(input('Introduce la pendiente m de la recta: '))
b = float(input('Introduce el término independiente b de la recta: '))

numerador = abs(m*x - y + b)
denominador = math.sqrt(m**2 + 1)

print('La distancia entre el punto y la recta es ', numerador/denominador,'.', sep='')