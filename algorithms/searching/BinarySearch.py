# Binary Search

class BinarySearch:
    """
    Binary Search Implementation

    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """

    @staticmethod
    def search(array, data):
        """
        Checks if an element is present in a sorted array.

        :param array: int[]
        :param data: int
        :return: int
        """

        low, high = 0, len(array) - 1

        while low <= high:
            mid = (low + high) // 2

            if array[mid] > data:
                high = mid - 1

            elif array[mid] < data:
                low = mid + 1

            else:
                return mid

        return -1
