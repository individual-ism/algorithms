# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        brokenString = s.split()
        for word in range(len(brokenString)):
            brokenString[word] = brokenString[word][::-1]
        return ' '.join(brokenString)
