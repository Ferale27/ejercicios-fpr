import random

eleccionOrdenador = random.randint(1, 3)

if eleccionOrdenador == 1:
    eleccionOrdenador = "piedra"
elif eleccionOrdenador == 2:
    eleccionOrdenador = "papel"
else:
    eleccionOrdenador = "tijeras"

eleccionUsuario = input('Elige piedra papel o tijeras: ').lower()

if eleccionUsuario == "piedra" or eleccionUsuario == "papel" or eleccionUsuario == "tijeras":
    if eleccionUsuario == eleccionOrdenador:
        resultado = "Hay un empate!!!"
    elif (eleccionUsuario == "piedra" and eleccionOrdenador == "tijeras") or (eleccionUsuario == "papel" and eleccionOrdenador == "piedra") or (eleccionUsuario == "tijeras" and eleccionOrdenador == "papel"):
        resultado = "El usuario gana!!!"
    else:
        resultado = "El ordenador gana!!!"
        
    print(f"El ordenador ha elegido {eleccionOrdenador} y el usuario {eleccionUsuario}. {resultado}")
else:

    print("La palabra indicada no es válida. El programa se ha terminado")
