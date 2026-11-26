from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        counts = defaultdict(int)
        best = 0

        while r < len(s):
            while counts[s[r]] > 0:
                counts[s[l]] -=1
                l += 1
            
            counts[s[r]] += 1
            best = max(best, r-l+1)
            r+= 1

        return best
