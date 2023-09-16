# Definir una función para verificar si un número es primo
def es_primo(numero):
    # Verificar si el número es menor o igual a 1, en cuyo caso no es primo
    if numero <= 1:
        return False
    # Verificar si el número es divisible por cualquier número del 2 a la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    # Si no se encontró ningún divisor, el número es primo
    return True

# Solicitar al usuario que ingrese el rango de números
inicio = int(input("Ingresa el número de inicio del rango: "))
fin = int(input("Ingresa el número de fin del rango: "))

# Inicializar una lista para almacenar los números primos
primos = []

# Iterar a través del rango y agregar los números primos a la lista
for numero in range(inicio, fin + 1):
    if es_primo(numero):
        primos.append(numero)

# Mostrar la lista de números primos
print(f"Números primos en el rango de {inicio} a {fin}: {primos}")
