'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        # constValues = [
        #     ('M', 1000),
        #     ('D', 500),
        #     ('C', 100),
        #     ('L', 50),
        #     ('X', 10),
        #     ('V', 5),
        #     ('I', 1)
        # ]
        constValues = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        number = 0
        index = 0

        independent = s.split('')
        while index < len(independent):
            presentValue = constValues[independent[index]]
            adjacentValue = constValues[independent[index + 1]]
            if adjacentValue:
                if presentValue >= adjacentValue:
                    number += presentValue
                else:
                    number += (adjacentValue - presentValue)
                    index + 1
            return number


        # for z in s:
        #     presentValue = constValues[s[z]]
        #     adjacentValue = constValues[s[s.index(z) + 1]]
        #     if adjacentValue:
        #         if presentValue >= adjacentValue:
        #             number += presentValue
        #         else:
        #             number += (adjacentValue - presentValue)
        #             s.index(z) + 1
        #     else:
        #         number += presentValue
        #     return number
        
Solution.romanToInt('MMXXIII')