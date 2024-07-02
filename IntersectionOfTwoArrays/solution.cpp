#include <vector>
using namespace std;

class Solution
{
public:
  /**
   * @brief Encuentra la intersección de dos arreglos.
   * 
   * Esta función toma dos vectores de enteros, los ordena y luego encuentra los elementos comunes en ambos vectores.
   * 
   * @param nums1 Primer vector de enteros.
   * @param nums2 Segundo vector de enteros.
   * @return vector<int> Un vector que contiene los elementos comunes en ambos vectores.
   */
  vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
  {
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());

    int i = 0, j = 0;

    vector<int> result;

    while (i < nums1.size() && j < nums2.size())
    {
      if (nums1[i] < nums2[j])
      {
        i++;
      }
      else if (nums1[i] > nums2[j])
      {
        j++;
      }
      else
      {
        result.push_back(nums1[i]);
        i++;
        j++;
      }
    }
    return result;
  }
};