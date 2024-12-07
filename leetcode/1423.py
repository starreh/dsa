"""
Leetcode #1423
Maximum points you can obtain from cards

https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
"""

class Soulution:

    def maximumPoints(self, nums, k):
        lSum, rSum, mSum = 0, 0, 0
        n = len(nums)

        for i in range(k):
            lSum += nums[i]
        
        mSum = lSum

        l = k - 1
        r = n - 1

        while r > n - 1 - k and l >= 0:
            rSum += nums[r]
            lSum -= nums[l]
            mSum = max(mSum, lSum + rSum)

            r -= 1
            l -= 1

        return mSum
