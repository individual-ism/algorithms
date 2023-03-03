// Given an integer x, return true if x is a palindrome, and false otherwise

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let useX = x.toString().split('')
    let forward = useX.join()
    let backward = useX.reverse().join()
    if (forward === backward) {
        return true
    } else {
        return false
    }
};