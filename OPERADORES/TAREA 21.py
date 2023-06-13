jugador1 = input("Jugador 1, ¿piedra, papel o tijera? ").lower()
jugador2 = input("Jugador 2, ¿piedra, papel o tijera? ").lower()

puntaje_jugador1 = 0
puntaje_jugador2 = 0

for ronda in range(3):
    print("Ronda", ronda+1)
    jugador1 = input("Jugador 1, ¿piedra, papel o tijera? ").lower()
    jugador2 = input("Jugador 2, ¿piedra, papel o tijera? ").lower()

    if jugador1 == jugador2:
        print("Empate")
    elif jugador1 == "piedra":
        if jugador2 == "papel":
            print("¡Jugador 2 gana!")
            puntaje_jugador2 += 1
        else:
            print("¡Jugador 1 gana!")
            puntaje_jugador1 += 1
    elif jugador1 == "papel":
        if jugador2 == "tijera":
            print("¡Jugador 2 gana!")
            puntaje_jugador2 += 1
        else:
            print("¡Jugador 1 gana!")
            puntaje_jugador1 += 1
    elif jugador1 == "tijera":
        if jugador2 == "piedra":
            print("¡Jugador 2 gana!")
            puntaje_jugador2 += 1
        else:
            print("¡Jugador 1 gana!")
            puntaje_jugador1 += 1
    else:
        print("Entrada inválida. Debe ser piedra, papel o tijera.")

print("Puntaje final:")
print("Jugador 1:", puntaje_jugador1)
print("Jugador 2:", puntaje_jugador2)

if puntaje_jugador1 > puntaje_jugador2:
    print("¡JUGADOR 1 GANA!")
elif puntaje_jugador2 > puntaje_jugador1:
    print("¡JUGADOR 2 GANA!")
else:
    print("¡EMPATE!")
