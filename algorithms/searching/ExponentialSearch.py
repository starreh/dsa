# Exponential Search

class ExponentialSearch:
    """
    Exponential Search Implementation
    
    Time Complexity : O(log n)
    Space Complexity : O(1)
    """

    def exponential_search(self, array, target):
        """
        Exponential search in a sorted array.

        :param array: int[]
        :param target: int
        :return: int
        """
        n = len(array)

        if n == 0:
            return -1
        if array[0] == target:
            return 0

        bound = 1
        while bound < n and array[bound] < target:
            bound *= 2

        return self.binary_search(array, bound // 2, min(bound, n - 1), target)

    def binary_search(self, array, left, right, target):
        """
        Binary Search helper function
        """
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
