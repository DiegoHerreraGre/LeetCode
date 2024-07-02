#include <vector>

class Solution {
public:
    bool threeConsecutiveOdds(std::vector<int>& arr) {
       for (int i = 0; i < arr.size() - 2; i++) { // Cambiado de arr.size() - 1 a arr.size() - 2
          if (arr[i] % 2 == 1 && arr[i+1] % 2 == 1 && arr[i+2] % 2 == 1) {
            return true;
          }
       }
       return false;
    }
};