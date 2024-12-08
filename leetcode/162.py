"""
Leetcode #162
Find peak element

https://leetcode.com/problems/find-peak-element/description/
"""

class Solution:

    def findPeakElement(self, nums):
        n = len(nums)
        l, h = 0, n-2

        # edge cases
        if n == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[n-1] > nums[n-2]:
            return n-1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                l = mid + 1
            
            if nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]:
                h = mid - 1

        return -1