// Paso 1: Definir una función para verificar si un número es primo.
function esPrimo(numero) {
    // Paso 2: Manejar los casos especiales para 0 y 1.
    if (numero <= 1) {
        return false; // 0 y 1 no son primos.
    }

    // Paso 3: Verificar si el número es divisible por cualquier número desde 2 hasta la raíz cuadrada de ese número.
    for (var i = 2; i <= Math.sqrt(numero); i++) {
        if (numero % i === 0) {
            return false; // Si es divisible, no es primo.
        }
    }

    // Paso 4: Si el bucle no encontró ningún divisor, el número es primo.
    return true;
}

// Paso 5: Llamar a la función con un número y mostrar el resultado en la consola.
var numero = 17; // Puedes cambiar este valor por el número que deseas
