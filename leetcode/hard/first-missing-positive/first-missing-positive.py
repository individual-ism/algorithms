'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''

# Does not work for list [3, 4, -1, 1]
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] <= 0:
                nums.remove(nums[i])
            elif nums[0] > 1:
                return 1
            else:
                return nums[1] + 1
            
# Does not work for list [1]
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == 0 or (len(nums) == 1 and nums[0] == 0):
            return 1
        for i in range(len(nums)):
            if nums[0] > 1:
                return 1
            elif nums[i] <= 0:
                nums.remove(nums[i])
            elif nums[0] == 1 and (nums[1] != 2 or len(nums) == 1):
                return 2
            else:
                return nums[1] + 1