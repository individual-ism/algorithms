/*
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function(nums) {
    let pos = 0;
    let neg = 0;
    nums.forEach((num) => {
        if (num > 0) {
            pos += 1;
        } else if (num < 0) {
            neg += 1;
        }
    })
    return Math.max(pos, neg);
};

// More efficient in runtime and memory
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function(nums) {
    let pos = 0;
    let neg = 0;
    nums.forEach((num) => {
        if (num > 0) {
            pos += 1;
        } else if (num < 0) {
            neg += 1;
        }
    })
    return (pos > neg) ? pos : neg;
};