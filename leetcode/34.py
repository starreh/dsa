"""
Leetcode #34
Find the first and last occurance of an element in a sorted array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""

class Solution:

    def searchRange(self, nums, target):

        def binary_search(nums, target, search):
            n = len(nums)
            l, h = 0, n-1
            idx = -1

            while l <= h:
                mid = (l + h) // 2

                if nums[mid] > target:
                    h = mid - 1

                elif nums[mid] < target:
                    l = mid + 1
                
                else:
                    idx = mid

                    if search:
                        h = mid - 1
                    else:
                        l = mid + 1

            return idx
        
        l = binary_search(nums, target, True)
        h = binary_search(nums, target, False)
        
        return [l, h]