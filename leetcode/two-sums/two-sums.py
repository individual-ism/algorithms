# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in nums:
            for j in nums:
                if (target - i == j) and (nums.index(j) > nums.index(i)):
                    indices.append(nums.index(i))
                    indices.append(nums.index(j))
                    return indices