def contar_vocales(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in texto:
        if letra.lower() in vocales:
            contador += 1
    return contador

texto = input("Ingresa un texto: ")
cantidad_vocales = contar_vocales(texto)
print("El texto tiene", cantidad_vocales, "vocales.")