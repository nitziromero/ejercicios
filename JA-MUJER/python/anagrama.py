# Definir una función para verificar si dos palabras son anagramas
def es_anagrama(palabra1, palabra2):
    # Eliminar espacios en blanco y convertir las palabras a minúsculas
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # Verificar si las palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False

    # Crear diccionarios para contar la frecuencia de cada letra en ambas palabras
    frecuencia1 = {}
    frecuencia2 = {}

    # Contar la frecuencia de letras en la primera palabra
    for letra in palabra1:
        if letra in frecuencia1:
            frecuencia1[letra] += 1
        else:
            frecuencia1[letra] = 1

    # Contar la frecuencia de letras en la segunda palabra
    for letra in palabra2:
        if letra in frecuencia2:
            frecuencia2[letra] += 1
        else:
            frecuencia2[letra] = 1

    # Comparar los diccionarios de frecuencia
    return frecuencia1 == frecuencia2

# Solicitar al usuario que ingrese las dos palabras a verificar
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

# Verificar si las palabras son anagramas llamando a la función es_anagrama
if es_anagrama(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} son anagramas.")
else:
    print(f"{palabra1} y {palabra2} no son anagramas.")
