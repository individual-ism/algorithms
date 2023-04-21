'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ind_words = s.split(' ')
        print(ind_words)
        while ind_words[-1] == '':
            ind_words.pop()
        return len(ind_words[-1])