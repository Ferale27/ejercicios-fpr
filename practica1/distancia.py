import math

x1 = float(input('Escribe la cordenada X del primer punto: '))
y1 = float(input('Escribe la cordenada Y del primer punto: '))
x2 = float(input('Escribe la cordenada X del segundo punto: '))
y2 = float(input('Escribe la cordenada Y del segundo punto: '))
dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('La distancia entre ambos puntos es:', dist)