# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
    
# More efficient in memory usage
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** float(n)