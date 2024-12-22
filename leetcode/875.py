"""
Leetcode #875
Koko eating bananas

https://leetcode.com/problems/koko-eating-bananas/description/
"""

import math

class Solution:

    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)

        def timeTaken(k):
            total = 0

            for i in piles:
                total += math.ceil(i/k)
            
            return total

        while low <= high:
            mid = (low + high) // 2

            time = timeTaken(mid)

            if time <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low
    