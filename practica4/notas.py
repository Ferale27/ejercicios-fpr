def comprobarFormato(minimo,maximo,pregunta,tipo_dato):
    while (True):
        try:
            n = tipo_dato(input(pregunta))
            if minimo <= n <= maximo:
                break
            else:
                print(f'Debes introducir un número entre el {minimo} y el {maximo}.\n')
        except ValueError:
            print('Formato incorrecto \n')
    return n

notaMin = 10
notaMax = 0
totalNota = 0
suspensos = 0
aprobados = 0
notables = 0
sobresa = 0
matHonor = 0

numNotas = comprobarFormato(1, 100, '¿Cuántas notas quieres introducir? ', int)
       
for i in range (numNotas):
    tempNota = comprobarFormato(0, 10, f'Introduce la nota ({i+1}/{numNotas}): ', float)
    
    if tempNota < notaMin:
        notaMin = tempNota
    if tempNota > notaMax:
        notaMax = tempNota
    
    '''
    El bloque de código de arriba se puede simplificar usando las funciones max() y min()
    
    notaMin = min(notaMin, tempNota)
    notaMax = max(notaMax, tempNota)
    
    Aún así he usado el método que hemos dado en clase para entenderlo mejor.
    '''
    
    if tempNota < 5:
        suspensos += 1
    elif tempNota < 7:
        aprobados += 1
    elif tempNota < 9:
        notables += 1
    elif tempNota < 10:
        sobresa += 1
    else:
        matHonor += 1
    
    totalNota += tempNota

media = totalNota / numNotas

print(f'\nMedia = {media:.2f}, Mínima = {notaMin}, Máxima = {notaMax}')
print('Tabla resumen de las calificaciones')
print('-' * 35)
print(f'{'Calificación':<12} {'Cantidad':^8} {'Porcentaje':^10}')
print(f'{'Suspensos':<12} {suspensos:^8} {suspensos/numNotas:^10.2%}')
print(f'{'Aprobados':<12} {aprobados:^8} {aprobados/numNotas:^10.2%}')
print(f'{'Notables':<12} {notables:^8} {notables/numNotas:^10.2%}')
print(f'{'Sobresa.':<12} {sobresa:^8} {sobresa/numNotas:^10.2%}')
print(f'{'Mat.Honor':<12} {matHonor:^8} {matHonor/numNotas:^10.2%}')