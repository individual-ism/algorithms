# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        reversed(s)
        return ''.join(s)
    
    
        newS = list(s.rsplit(' '))
        for word in newS:
            newWord = list(word)
            rNewWord = newWord.reverse()
            rNewWord
        return rNewWord
