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
            
# Does not work for list [1, 2, 0]
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
            elif nums[0] == 1:
                return 2
            else:
                return nums[1] + 1
            
# Does not work for [-1, -2]
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[0] > 1 or len(nums) == 0 or (len(nums) == 1 and nums[0] == 0):
                return 1
            elif nums[i] <= 0:
                if len(nums) == 1:
                    return 1
                else:
                    nums.remove(nums[i])
            elif nums[0] == 1 and len(nums) == 1 or nums[1] != 2:
                return 2
            else:
                return nums[i] + 1
            

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if nums[i] <= 0:
                nums.remove(nums[i])
        if len(nums) == 0 or len(nums) == 1 and nums[0] != 1 or nums[0] != 1:
            return 1
        while nums[i + 1] == nums[i] + 1:
            i += 1
        return nums[i] + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] <= 0:
                nums.remove(nums[i])
            elif len(nums) == 0 or nums[0] != 1:
                return 1
            else:
                return nums[i] + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] <= 0:
                nums.remove(nums[i])
            elif nums[0] == 1 and nums[i + 1] != nums[i] + 1:
                return nums[i] + 1
            else:
                return 1