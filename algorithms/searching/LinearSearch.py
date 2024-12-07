# Linear Search

class LinearSearch:
    """
    Linear Search Implementation

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    @staticmethod
    def search(array, data):
        """
        Checks if an element is present in an array.

        :param array: int[]
        :param data: int
        :return: int
        """

        for idx, ele in enumerate(array):
            if ele == data:
                return idx

        return -1