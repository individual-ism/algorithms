# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        bString = ''
        for i in b:
            bString += str(i)
        return pow(a, int(bString), 1337)