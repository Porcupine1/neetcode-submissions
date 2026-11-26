from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r, maxSeen = 0, 0, 0
        
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            maxSeen = max(r-l+1, maxSeen)

        return maxSeen