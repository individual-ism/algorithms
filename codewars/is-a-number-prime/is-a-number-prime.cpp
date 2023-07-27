bool isPrime(int num) {
  // your code here..
  if (num <= 1) {
    return false;
  }
  for (int i = 2; i <= pow(num, 0.5); i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

// Fails a test
#include <cmath>

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }

    for (int i = 2; i < sqrt(num); i++) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}