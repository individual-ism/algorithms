'''
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.
'''

class Solution:
    def bulbSwitch(self, n: int) -> int:
        roundNumber = 2
        bulbs = n
        while roundNumber < n:
            for i in range(n):
                if n % (i + 1) == 0:
                    bulbs -= 1
            roundNumber += 1
        return bulbs