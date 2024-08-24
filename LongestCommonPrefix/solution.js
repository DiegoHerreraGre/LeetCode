/**
 * Encuentra el prefijo común más largo entre un array de cadenas.
 * @param {string[]} strs - Un array de cadenas.
 * @return {string} - El prefijo común más largo.
 */
var longestCommonPrefix = function (strs) {
    // Si el array está vacío, no hay prefijo común, así que devolvemos una cadena vacía.
    if (strs.length === 0) return "";
    
    // Inicializamos el prefijo con la primera cadena del array.
    let prefix = strs[0];
    
    // Recorremos el array comenzando desde la segunda cadena.
    for (let i = 1; i < strs.length; i++) {
        // Mientras la cadena actual no comience con el prefijo actual...
        while (strs[i].indexOf(prefix) !== 0) {
            // Reducimos el prefijo eliminando el último carácter.
            prefix = prefix.substring(0, prefix.length - 1);
            // Si el prefijo se convierte en una cadena vacía, no hay prefijo común.
            if (prefix === "") return "";
        }
    }
    // Devolvemos el prefijo común más largo encontrado.
    return prefix;
};

// Ejemplo de uso: buscamos el prefijo común más largo entre las cadenas 'flower', 'flow' y 'flight'.
console.log(longestCommonPrefix(['flower', 'flow', 'flight'])); // Output: "fl"