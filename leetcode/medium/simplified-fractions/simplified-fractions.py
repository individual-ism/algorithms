'''
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. You can return the answer in any order.
'''

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        sim_frac = []
        for denom in range(2, n + 1, 1):
            for numer in range(1, n, 1):
                if numer < denom and (numer == 1 if denom % numer == 0 else numer):
                    sim_frac.append(f"{numer}/{denom}")
        return sim_frac