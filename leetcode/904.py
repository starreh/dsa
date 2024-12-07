"""
Leetcode #904
Fruits into basket

https://leetcode.com/problems/fruit-into-baskets/description/
"""

class Solution:

    def fruitsIntoBasket(self, fruits):
        maxFruits = 0
        freq = dict()
        l, r = 0, 0
        n = len(fruits)

        while r < n:

            if fruits[r] in freq:
                freq[fruits[r]] += 1
            else:
                freq[fruits[r]] = 1
            
            while len(freq) > 2:
                freq[fruits[l]] -= 1

                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                
                l += 1

            if len(freq) <= 2:
                maxFruits = max(maxFruits, r - l + 1)
                r += 1

        return maxFruits
