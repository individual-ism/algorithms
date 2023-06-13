'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            rev_nums = list(reversed(nums))  
            return [nums.index(target), len(nums) - rev_nums.index(target) - 1]
        except:
            return [-1, -1]

# Significantly more efficient solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            rev_nums = nums[::-1]  
            return [nums.index(target), len(nums) - rev_nums.index(target) - 1]
        except:
            return [-1, -1]