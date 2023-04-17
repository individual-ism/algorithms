'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        merged = sorted(nums1)
        lowIndex = 0
        highIndex = len(nums1) - 1
        if len(merged) == 1:
            return merged[0]
        while lowIndex <= highIndex:
            lowIndex += 1
            highIndex -= 1
            if lowIndex == highIndex:
                return merged[lowIndex]
        return (merged[lowIndex] + merged[highIndex]) / 2
    