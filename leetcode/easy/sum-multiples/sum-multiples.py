'''
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
'''

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        totalSum = 0
        iteration = n
        while iteration > 0:
            if iteration % 3 == 0 or iteration % 5 == 0 or iteration % 7 == 0:
                totalSum += iteration
            iteration -= 1
        return totalSum