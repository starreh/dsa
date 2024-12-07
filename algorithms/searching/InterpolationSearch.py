# Interpolation Seach

class InterpolationSearch:
    """
    Interpolation Search Implementation
    
    Time Complexity : O(log log n)
    Space Complexity : O(1)
    """

    def interpolation_search(self, array, target):
        """
        Interpolation search in a sorted & uniformly idstributed array
        
        :param array: int[]
        :param target: int
        :return: int
        """
        left, right = 0, len(array) - 1

        while left <= right and target >= array[left] and target <= array[right]:
            if left == right:
                if array[left] == target:
                    return left
                return -1

            pos = left + ((right - left) * (target - array[left])) // (array[right] - array[left])

            if array[pos] == target:
                return pos

            if array[pos] < target:
                left = pos + 1
                
            else:
                right = pos - 1

        return -1
