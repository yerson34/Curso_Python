import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    jugador = input("Elige piedra, papel o tijera: ")
    computadora = random.choice(opciones)
    print("La computadora eligió:", computadora)
    
    if jugador == computadora:
        print("Empate!")
    elif jugador == "piedra":
        if computadora == "tijera":
            print("Ganaste!")
        else:
            print("Perdiste!")
    elif jugador == "papel":
        if computadora == "piedra":
            print("Ganaste!")
        else:
            print("Perdiste!")
    elif jugador == "tijera":
        if computadora == "papel":
            print("Ganaste!")
        else:
            print("Perdiste!")
    else:
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        
    volver_a_jugar()

def volver_a_jugar():
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() == "s":
        jugar()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

jugar()