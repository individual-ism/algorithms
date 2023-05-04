'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalString = ''
        index = 0
        for i in range(min(len(word1), len(word2))):
            finalString += word1[i] + word2[i]
            index += 1
        if len(word1) > len(word2):
            for i in range(index, len(word1)):
                finalString += word1[i]
        elif len(word2) > len(word1):
            for i in range(index, len(word2)):
                finalString += word2[i]
        return finalString
    
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalString = ''.join(map(''.join, zip(word1, word2)))
        if len(word1) > len(word2):
            for i in range(len(word2), len(word1)):
                finalString += word1[i]
        elif len(word2) > len(word1):
            for i in range(len(word1), len(word2)):
                finalString += word2[i]
        return finalString