# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_string = str(x)[::-1]
        string = str(x)
        if string == reversed_string:
            return True
        return False