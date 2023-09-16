# Definir una función recursiva para calcular el factorial de un número
def factorial(n):
    # Caso base: si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: calcular el factorial de n multiplicándolo por el factorial de n-1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número entero no negativo
try:
    numero = int(input("Ingresa un número entero no negativo: "))
    
    if numero < 0:
        print("El número debe ser no negativo.")
    else:
        # Llamar a la función factorial para calcular el factorial del número ingresado
        resultado = factorial(numero)
        
        # Mostrar el resultado al usuario
        print(f"El factorial de {numero} es {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero no negativo.")

