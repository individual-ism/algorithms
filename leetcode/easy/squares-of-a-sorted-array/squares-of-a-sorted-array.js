// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let sq_nums = []
    nums.map((num) => {
        sq_nums.push(num ** 2)
    })
    return sq_nums.sort(function(a, b) {return a - b})
};