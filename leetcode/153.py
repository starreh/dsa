"""
Leetcode #153
Find minimum in a rotated sorted array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""

import sys

class Solution:

    def findMin(self, nums):
        n = len(nums)
        l, h = 0, n-1
        ans = sys.maxsize

        while l <= h:

            mid = (l + h) // 2

            if nums[l] <= nums[h]:
                ans = l
                break
            
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                ans = min(ans, nums[mid])
                h = mid - 1
        
        return ans