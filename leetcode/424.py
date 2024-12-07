"""
Leetcode #424
Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""

class Solution:

    def longestRepeatingCharacterReplacement(s, k):
        n = len(s)
        l, r = 0, 0
        maxLen = 0
        maxFreq = 0
        freq = {}

        for r in range(n):
            char = s[r]

            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            
            maxFreq = max(freq.values())
            currLen = r - l + 1

            if (currLen - maxFreq) <= k:
                maxLen = max(maxLen, currLen)
            else:
                freq[s[l]] -= 1

                if not freq[s[l]]:
                    del freq[s[l]]
                
                l += 1
        
        return maxLen
