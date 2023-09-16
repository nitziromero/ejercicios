# Solicitar al usuario que ingrese una lista de números separados por comas
elementos_str = input("Ingresa una lista de números separados por comas: ")

# Convertir la cadena de entrada en una lista de números
elementos_lista = [float(numero) for numero in elementos_str.split(",")]

# Implementar el algoritmo de ordenamiento de burbuja para ordenar la lista
n = len(elementos_lista)
for i in range(n):
    for j in range(0, n - i - 1):
        if elementos_lista[j] > elementos_lista[j + 1]:
            # Intercambiar los elementos si están en el orden incorrecto
            elementos_lista[j], elementos_lista[j + 1] = elementos_lista[j + 1], elementos_lista[j]

# Mostrar la lista ordenada de forma ascendente
print(f"Lista ordenada de forma ascendente: {elementos_lista}")
