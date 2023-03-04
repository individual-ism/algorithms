/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    if (nums.indexOf(target)) {
        return nums.indexOf(target)
    } else {
        nums.push(target)
        nums.sort()
        nums.sort(nums[0] - nums[nums.findLastIndex()])
        return nums.find(target)
    }
};