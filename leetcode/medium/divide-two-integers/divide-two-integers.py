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