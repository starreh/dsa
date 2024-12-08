"""
GFG
Find Kth Rotation

https://www.geeksforgeeks.org/problems/rotation4723/
"""

class Solution:

    def findKthRotation(self, nums):
        n = len(nums)
        l, h = 0, n-1
        ans = -1

        while l <= h:
            mid = (l + h) // 2

            if nums[l] < nums[h]:
                return ans
            
            if nums[l] <= nums[mid]:
               ans = l
               l = mid + 1
            else:
               ans = mid
               h = mid - 1
        
        return ans