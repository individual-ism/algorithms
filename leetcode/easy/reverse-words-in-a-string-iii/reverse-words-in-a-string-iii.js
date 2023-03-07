// Given a string s, reverse the order of charactersin each word within a sentence while still preserving whitespace and initial word order.

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.split('').reverse().join('').split(' ').reverse().join(' ')
};