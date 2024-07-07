class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convierte un número romano dado en su equivalente entero.

        Args:
        s (str): Una cadena que representa el número romano.

        Returns:
        int: El valor entero correspondiente al número romano.

        La función utiliza un diccionario para mapear cada símbolo romano a su valor entero.
        Recorre la cadena de entrada y suma o resta los valores basándose en la posición relativa
        de los símbolos para manejar las substracciones específicas de la numeración romana.
        """
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            # Verifica si el símbolo actual es menor que el siguiente en la cadena.
            # Esto es necesario para manejar casos como 'IV' o 'IX'.
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                # Si el símbolo actual es menor que el siguiente, se resta su valor.
                # Por ejemplo, en 'IV', I es menor que V, por lo que se resta 1.
                ans -= m[s[i]]
            else:
                # Si no hay un símbolo mayor después, simplemente se suma el valor del símbolo actual.
                # Por ejemplo, en 'III', cada I se suma, dando un total de 3.
                ans += m[s[i]]
        
        return ans

print(Solution().romanToInt("III"))
# Pruebas adicionales
print(Solution().romanToInt("IV"))  # Debería devolver 4
print(Solution().romanToInt("IX"))  # Debería devolver 9
print(Solution().romanToInt("LVIII"))  # Debería devolver 58
print(Solution().romanToInt("MCMXCIV"))  # Debería devolver 1994
print(Solution().romanToInt("MMXXI"))  # Debería devolver 2021
