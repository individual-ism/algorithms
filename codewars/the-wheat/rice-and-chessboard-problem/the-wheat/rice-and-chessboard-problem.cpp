#include <cmath>
using namespace std;

unsigned int squaresNeeded(long long n) {
  //your code here
  return ceil(log2(n + 1));
}