#include <cmath>
#include <vector>

class Kata
{
public:
    std::vector<int> foldArray(std::vector<int> array, int runs)
    {
      for (int i = 0; i < runs; i++) {
        if (array.size() % 2 == 0) {
          for (int j = 0; j <= array.size() / 2; j++) {
            array[j] += array[array.size() - 1 - j];
          }
          array.erase(array.end() - array.size() / 2, array.end());
        } else {
          for (int k = 0; k < floor(array.size() / 2); k++) {
            array[k] += array[array.size() - 1 - k];
          }
          array.erase(array.end() - floor(array.size() / 2), array.end());
        }
      }
        return array;
    }
};