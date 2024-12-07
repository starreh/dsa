"""
Leetcode #1004
Max Consecutive Ones III

https://leetcode.com/problems/max-consecutive-ones-iii/description/
"""

class Solution:

    def maxConsecutiveOnesIII (self, nums, k):
        
        n = len(nums)
        l, r = 0, 0
        maxLen = 0
        zCount = 0

        for r in range(n):

            if nums[r] == 0:
                zCount += 1

                if zCount > k:
                    while zCount > k:
                        if nums[l] == 0:
                            zCount -= 1
                        l += 1
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
