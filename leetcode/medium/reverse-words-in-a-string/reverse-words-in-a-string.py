'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        finalString = ''
        wordList = s.split(' ')[::-1]
        while '' in wordList:
            wordList.remove('')
        for i in range(len(wordList)):
            finalString += wordList[i] + ' '
        return finalString.strip()
    
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1]).strip()