"""
Leetcode #81
Search in a rotated sorted array 2

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
"""

class Solution:

    def search(self, nums, target):
        n = len(nums)
        l, h = 0, n-1

        while l <= h:
            
            mid = (l + h) // 2

            if nums[mid] == target:
                return True
            
            if nums[l] == nums[mid] and nums[mid] == nums[h]:
                l += 1
                h -= 1
                continue
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        
        return False