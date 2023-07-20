lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Y aquí tienes una función que recibe como parámetro una lista y devuelve un nuevo arreglo con los números pares que existen:

#python
def obtener_numeros_pares(lista):
    numeros_pares = []
    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares


#Para utilizar la función con la lista anterior, puedes hacer lo siguiente:

#python
lista_resultado = obtener_numeros_pares(lista_numeros)
print(lista_resultado)
