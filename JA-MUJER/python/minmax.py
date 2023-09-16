# Solicitar al usuario que ingrese una lista de números separados por comas
numeros_str = input("Ingresa una lista de números separados por comas: ")

# Convertir la cadena de entrada en una lista de números
numeros = [float(numero) for numero in numeros_str.split(",")]

# Verificar si la lista está vacía
if len(numeros) == 0:
    print("La lista está vacía, no se puede encontrar el mínimo y máximo.")
else:
    # Encontrar el mínimo y el máximo de la lista
    minimo = min(numeros)
    maximo = max(numeros)

    # Mostrar el resultado al usuario
    print(f"El mínimo de la lista es: {minimo}")
    print(f"El máximo de la lista es: {maximo}")
