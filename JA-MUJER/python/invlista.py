# Definir una función para invertir una lista
def invertir_lista(lista):
    # Utilizar la rebanada [::-1] para invertir la lista y devolverla
    return lista[::-1]

# Solicitar al usuario que ingrese una lista de elementos separados por comas
elementos_str = input("Ingresa una lista de elementos separados por comas: ")

# Convertir la cadena de entrada en una lista utilizando split(",")
elementos_lista = elementos_str.split(",")

# Llamar a la función invertir_lista para invertir la lista
resultado = invertir_lista(elementos_lista)

# Mostrar el resultado al usuario
print(f"Lista invertida: {resultado}")
