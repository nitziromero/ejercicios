// Paso 1: Definir una función para verificar si una palabra es un palíndromo.
function esPalindromo(palabra) {
    // Paso 2: Convertir la palabra a minúsculas y eliminar espacios en blanco.
    palabra = palabra.toLowerCase().replace(/\s/g, '');

    // Paso 3: Invertir la palabra.
    var palabraInvertida = palabra.split('').reverse().join('');

    // Paso 4: Comparar la palabra original con la palabra invertida.
    return palabra === palabraInvertida;
}

// Paso 5: Llamar a la función con una palabra y mostrar el resultado en la consola.
var palabra = "reconocer"; // Puedes cambiar esta palabra por la que desees verificar.
var resultado = esPalindromo(palabra);

if (resultado) {
    console.log("'" + palabra + "' es un palíndromo.");
} else {
    console.log("'" + palabra + "' no es un palíndromo.");
}
