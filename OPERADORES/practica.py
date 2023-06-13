dni = input("Introduce tu DNI: ")
if len(dni) == 8:
    primer_numero = int(dni[0])
    ultimo_numero = int(dni[-1])
    suma = primer_numero + ultimo_numero
    print("La suma del primer y último número del DNI es:", suma)
else:
    print("El DNI debe tener 8 dígitos.")
