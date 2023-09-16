// Paso 1: Definir una función para encontrar el elemento más grande en un arreglo.
function encontrarMaximo(arreglo) {
    // Paso 2: Manejar el caso en el que el arreglo esté vacío.
    if (arreglo.length === 0) {
        return undefined; // Si el arreglo está vacío, no hay elemento más grande.
    }

    // Paso 3: Inicializar una variable para almacenar el elemento más grande.
    var maximo = arreglo[0]; // Suponemos que el primer elemento es el más grande.

    // Paso 4: Utilizar un bucle for para comparar cada elemento del arreglo.
    for (var i = 1; i < arreglo.length; i++) {
        if (arreglo[i] > maximo) {
            maximo = arreglo[i]; // Si encontramos un elemento mayor, lo asignamos como el nuevo máximo.
        }
    }

    // Paso 5: Devolver el elemento más grande.
    return maximo;
}

// Paso 6: Llamar a la función con un arreglo y mostrar el resultado en la consola.
var numeros = [12, 45, 6, 78, 23, 56, 89]; // Puedes cambiar este arreglo por uno con los números que desees.
var maximoEncontrado = encontrarMaximo(numeros);
console.log("El elemento más grande en el arreglo es: " + maximoEncontrado);
