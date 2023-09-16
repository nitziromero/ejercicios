# Definir una función para multiplicar dos matrices
def multiplicar_matrices(matriz1, matriz2):
    # Obtener el número de filas y columnas de las matrices de entrada
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    # Verificar si las matrices son compatibles para la multiplicación
    if columnas_matriz1 != filas_matriz2:
        raise ValueError("Las matrices no son compatibles para la multiplicación")

    # Inicializar una matriz resultante llena de ceros
    resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]

    # Realizar la multiplicación de matrices
    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(columnas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

# Definir las matrices de ejemplo (puedes modificar estas matrices según tus necesidades)
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8], [9, 10], [11, 12]]

try:
    # Calcular el producto de las dos matrices llamando a la función multiplicar_matrices
    producto = multiplicar_matrices(matriz1, matriz2)

    # Mostrar el resultado al usuario
    for fila in producto:
        print(fila)
except ValueError as e:
    print(e)
