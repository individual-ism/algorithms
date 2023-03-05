'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        median = int((n - 1) / 2)
        i = median
        while isBadVersion(i):
            i -= 1
        while not isBadVersion(i):
            i += 1
            if isBadVersion(i):
                return i
            

# Works when n != bad
        median = int((n - 1) / 2)
        i = median
        while isBadVersion(i):
            if isBadVersion(i - 1):
                i -= 2
            if not isBadVersion(i - 1):
                return i
        while not isBadVersion(i):
            if not isBadVersion(i + 1):
                i += 2
            if isBadVersion(i + 1):
                return i
            



        median = int((n - 1) / 2)
        i = median
        if not isBadVersion(i) and isBadVersion(i + 1):
            return i + 1
        if isBadVersion(i) and not isBadVersion(i - 1):
            return i - 1
        if isBadVersion(i) and isBadVersion(i - 1):
            i -= 2
        if not isBadVersion(i) and not isBadVersion(i + 1):
            i += 2
        while isBadVersion(i):
            if isBadVersion(i - 1):
                i -= 2
            if not isBadVersion(i - 1):
                return i
        while not isBadVersion(i):
            if not isBadVersion(i + 1):
                i += 2
            if isBadVersion(i + 1):
                return i
