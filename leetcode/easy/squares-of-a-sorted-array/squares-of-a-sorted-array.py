# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums = []
        for num in nums:
            sq_nums.append(num ** 2)
        return sorted(sq_nums)
