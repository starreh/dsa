# Linear Search

class LinearSearch:
    """
    Linear Search Implementation

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def linear_search(self, array, target):
        """
        Checks if an element is present in an array.

        :param array: int[]
        :param target: int
        :return: int
        """

        for idx, ele in enumerate(array):
            if ele == target:
                return idx

        return -1