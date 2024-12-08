"""
Leetcode #33
Search in a rotated sorted array 1

https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

class Solution:

    def search(self, nums, target):
        n = len(nums)
        l, h = 0, n-1

        while l <= h:
            
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            
            elif nums[mid] <= nums[h]:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        
        return -1