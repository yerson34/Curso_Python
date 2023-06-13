while True:
    edad = input("Ingresa tu edad: ")
    if not edad.isdigit():
        print("Por favor, ingresa un número entero.")
        continue
    edad = int(edad)
    if edad >= 20:
        print("Eres mayor de edad.")
        break
    elif edad < 10:
        print("Eres menor de edad.")
        break
    else:
        print("Aún eres menor de edad. Sigue esperando.")
