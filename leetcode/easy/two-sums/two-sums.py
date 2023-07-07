# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) and (i < j):
                    indices.append(i)
                    indices.append(j)
                    return indices
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) and (i < j):
                    return [i, j]