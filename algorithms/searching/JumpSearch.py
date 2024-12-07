# Jump Search

class JumpSearch:
    """
    Jump Search Implementation
    
    Time Complexity: O(sqrt(n))
    Space Complexity : O(1)
    """

    def jump_search(self, array, target):
        """
        Jump search in a sorted arrayay.

        :param arrayay: int[]
        :param target: int
        :return: int
        """
        import math

        n = len(array)
        step = int(math.sqrt(n))
        prev = 0

        while prev < n and array[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        
        for i in range(prev, min(step, n)):
            if array[i] == target:
                return i

        return -1
