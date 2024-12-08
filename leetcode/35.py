"""
Leetcode #35
Search Insert Position

https://leetcode.com/problems/search-insert-position/description/
"""

class Solution:

    def searchInsertPosition(self, nums, target):
        n = len(nums)
        l, h = 0, n-1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] > target:
                h = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                return mid
        
        return l
