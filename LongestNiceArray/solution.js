/**
 * @param {number[]} nums
 * @return {number}
 * */

function longestNiceSubarray(nums) {
  let maxLen = 1; // Subarreglos de longitud 1 siempre son bonitos
  let currentAND = 0;
  let start = 0; // Inicio de la ventana deslizante

  for (let end = 0; end < nums.length; end++) {
    // Mientras haya una intersección de bits, contrae la ventana
    while ((currentAND & nums[end]) !== 0) {
      // Quita el número de inicio de la ventana del AND actual
      currentAND &= ~nums[start];
      // Incrementa el inicio de la ventana
      start++;
    }
    // Añade el número actual al AND
    currentAND |= nums[end];
    // Actualiza el tamaño máximo del subarreglo bonito
    maxLen = Math.max(maxLen, end - start + 1);
  }

  return maxLen;
}