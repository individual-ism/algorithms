'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2**31, 2**31 − 1]. For this problem, if the quotient is strictly greater than 2**31 - 1, then return 2**31 - 1, and if the quotient is strictly less than -2**31, then return -2**31.
'''

# Fails on minimum and maximum quotients
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        if dividend >= 2147483647 and divisor == 1:
            quotient = 2147483647
        elif dividend >= 2147483648 and divisor == -1:
            quotient = -2147483648
        elif dividend <= -2147483648 and divisor == 1:
            quotient = -2147483648
        elif dividend <= -2147483648 and divisor == -1:
            quotient = 2147483647
        else:
            while dividend >= divisor and dividend > 0:
                if divisor >= 0:
                    dividend -= divisor
                    quotient += 1
                else:
                    dividend += divisor
                    quotient -= 1
            while dividend >= divisor and dividend < 0:
                dividend -= divisor
                quotient += 1
            while dividend <= divisor and dividend > 0:
                dividend -= divisor
                quotient += 1
            while dividend <= divisor and dividend < 0:
                if divisor < 0:
                    dividend -= divisor
                    quotient += 1
                else:
                    dividend += divisor
                    quotient -= 1
        return quotient

# Time limit exceeded
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        absDividend = abs(dividend)
        absDivisor = abs(divisor)
        quotient = 0

        while absDividend >= absDivisor:
            absDividend -= absDivisor
            quotient += 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return -1 * quotient
        else:
            return quotient
        

# Base
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        while dividend >= divisor:
            if divisor >= 0:
                dividend -= divisor
                quotient += 1
            else:
                dividend += divisor
                quotient -= 1
        return quotient


# 2023.04.02
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        abs_quotient = abs(dividend) / abs(divisor)
        if abs_quotient > 2**31 - 1 and (dividend / divisor > 0):
            return 2**31 - 1
        elif abs_quotient > 2**31 and (dividend / divisor < 0):
                return -2**31
        else:
            while abs(dividend) >= abs(divisor):
                if divisor >= 0:
                    dividend -= divisor
                    quotient += 1
                else:
                    dividend += divisor
                    quotient -= 1

        return quotient
    
# 20 April 2023
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        abs_quotient = abs(dividend / divisor)
        if abs_quotient > (2 ** 31 - 1) and ((divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)):
            return 2 ** 31 - 1
        if abs_quotient > (2 ** 31) and ((divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0)):
            return -2 ** 31
        if dividend == divisor:
            return 1
        while abs(dividend) > abs(divisor):
            if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
                dividend -= divisor
                quotient += 1
            elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
                dividend += divisor
                quotient -= 1
        return quotient
    
# 22 April 2023
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mid_div = math.floor(abs(dividend) ** 0.5)
        upperLimit = 2147483647
        lowerLimit = -2147483648
        quotient = 0
        # workingDividend = dividend
        # workingDivisor = divisor
        abs_quotient = abs(dividend) // abs(divisor)
        if abs_quotient >= upperLimit and ((divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)):
            return upperLimit
        elif abs_quotient >= -lowerLimit and ((divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0)):
            return lowerLimit
        elif dividend == divisor:
            return 1
        elif (dividend == -divisor) or (-dividend == divisor):
            return -1
        else:
            while mid_div >= abs(divisor):
                if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
                    mid_div -= divisor
                    quotient += 1
                elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
                    mid_div += divisor
                    quotient -= 1
            return quotient + quotient
        
# Unknown Date
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         quotient = 0
#         upperLimit = 2147483647
#         lowerLimit = 2147483648
#         workingDividend = dividend
#         workingDivisor = divisor
#         abs_quotient = abs(dividend) // abs(divisor)
#         if abs_quotient >= upperLimit and ((divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)):
#             return 2147483647
#         if abs_quotient >= lowerLimit and ((divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0)):
#             return 2147483648
#         if dividend == divisor:
#             return 1
#         if (dividend == -divisor) or (-dividend == divisor):
#             return -1
#         while abs(workingDividend) >= abs(workingDivisor):
#             if (workingDividend > 0 and workingDivisor > 0) or (workingDividend < 0 and workingDivisor < 0):
#                 workingDividend -= workingDivisor
#                 quotient += 1
#             elif (workingDividend > 0 and workingDivisor < 0) or (workingDividend < 0 and workingDivisor > 0):
#                 workingDividend += workingDivisor
#                 quotient -= 1
#         return quotient

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mid_div = abs(dividend) ** 0.5
        upperLimit = 2147483647
        lowerLimit = -2147483648
        quotient = 0
        abs_quotient = abs(dividend) // abs(divisor)
        if abs_quotient >= upperLimit and ((divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)):
            return upperLimit
        elif abs_quotient >= -lowerLimit and ((divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0)):
            return lowerLimit
        elif dividend == divisor:
            return 1
        elif (dividend == -divisor) or (-dividend == divisor):
            return -1
        elif math.floor(mid_div) == abs(divisor):
            return math.floor(mid_div)
        else:
            while mid_div > divisor:
                if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
                    mid_div -= divisor
                    quotient += 1
                elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
                    mid_div += divisor
                    quotient -= 1
            return quotient
        
# 2023 July 02
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_sqrt = math.sqrt(dividend)
        whil