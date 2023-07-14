'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(1, len(intervals)):
            if newInterval[0] < intervals[i - 1][1]:
                intervals[i - 1][1] = newInterval[1]
            elif intervals[i][0] < intervals[i - 1][1] or intervals[i][0] == intervals[i - 1][1]:
                intervals[i - 1][1] = intervals[i][1]
                intervals.remove(intervals[i])
            else:
                continue
        return intervals