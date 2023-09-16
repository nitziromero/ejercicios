// Paso 1: Definir una función para revertir una cadena.
function revertirCadena(cadena) {
    // Paso 2: Utilizar el método split para convertir la cadena en un array de caracteres.
    var caracteres = cadena.split('');

    // Paso 3: Utilizar el método reverse para invertir el orden de los caracteres en el array.
    var caracteresRevertidos = caracteres.reverse();

    // Paso 4: Utilizar el método join para convertir el array invertido de caracteres nuevamente en una cadena.
    var cadenaRevertida = caracteresRevertidos.join('');

    // Paso 5: Devolver la cadena revertida.
    return cadenaRevertida;
}

// Paso 6: Llamar a la función con una cadena y mostrar el resultado en la consola.
var cadenaOriginal = "Hola, mundo!"; // Puedes cambiar este valor por la cadena que deseas revertir.
var cadenaRevertida = revertirCadena(cadenaOriginal);
console.log("Cadena original: " + cadenaOriginal);
console.log("Cadena revertida: " + cadenaRevertida);
