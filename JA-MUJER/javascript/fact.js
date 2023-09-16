// Paso 1: Definir la función factorial que toma un número como argumento.
function calcularFactorial(numero) {
    // Paso 2: Verificar si el número es 0 o 1 (caso base).
    if (numero === 0 || numero === 1) {
        return 1; // El factorial de 0 y 1 es 1.
    } else {
        // Paso 3: Inicializar una variable para almacenar el resultado del factorial.
        var factorial = 1;

        // Paso 4: Usar un bucle for para calcular el factorial.
        for (var i = 2; i <= numero; i++) {
            factorial *= i; // Multiplicar factorial por el valor actual de i.
        }

        // Paso 5: Devolver el resultado del factorial.
        return factorial;
    }
}

// Paso 6: Llamar a la función con un número y mostrar el resultado en la consola.
var numero = 5; // Puedes cambiar este valor por el número del que deseas calcular el factorial.
var resultado = calcularFactorial(numero);
console.log("El factorial de " + numero + " es " + resultado);
