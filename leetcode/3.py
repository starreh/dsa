""" 
Leetcode #3
Longest Sub-string without repeating characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution:

    def longestSubstringWithoutRepeatingCharacters(self, s):
 
        n = len(s)
        maxLen = 0
        l, r = 0, 0
        visited = set()

        if n == 0:
            return 0

        for r in range(n):
            if s[r] in visited:
                while l < r and s[r] in visited:
                    visited.remove(s[l])
                    l += 1

            visited.add(s[r])  
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

if __name__ == "__main__":

    sol = Solution()
    res = sol.longestSubstringWithoutRepeatingCharacters("abcabcbb")
    print(res)
