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