const std = @import("std");

/// Una estructura que contiene la función `threeConsecutiveOdds` para determinar si un arreglo contiene tres números impares consecutivos.
const Solution = struct {
    /// Verifica si hay tres números consecutivos impares en el arreglo proporcionado.
    /// @param arr  Un arreglo de enteros para verificar.
    /// @return     Retorna `true` si hay tres números impares consecutivos, de lo contrario retorna `false`.
    pub fn threeConsecutiveOdds(arr: []i32) bool {
        if (arr.len < 3) {
            return false;
        }
        var i: usize = 0;
        while (i < arr.len - 2) {
            if (arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0) {
                return true;
            }
            i += 1;
        }
        return false;
    }
};

/// Pruebas para la función `threeConsecutiveOdds`.


test "threeConsecutiveOdds" {
    const arr1 = []i32{ 1, 3, 5, 7, 9 };
    const arr2 = []i32{ 2, 4, 6, 8, 10 };
    const arr3 = []i32{ 1, 2, 3, 5, 7 };
    std.testing.expect(Solution.threeConsecutiveOdds(arr1) == true);
    std.testing.expect(Solution.threeConsecutiveOdds(arr2) == false);
    std.testing.expect(Solution.threeConsecutiveOdds(arr3) == false);
}
