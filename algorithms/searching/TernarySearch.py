# Ternary Search

class TernarySeach:
    """
    Ternary Search Implementation
    
    Time Complexity : O(log3n)
    Space Complexity : O(1)
    """

    def ternary_search(self, array, target):
        """
        Ternary search in a sorted array.

        :param array: int[]
        :param target: int
        :return: int
        """
        left, right = 0, len(array) - 1

        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            if array[mid1] == target:
                return mid1
            if array[mid2] == target:
                return mid2

            if target < array[mid1]:
                right = mid1 - 1
            elif target > array[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1

        return -1
