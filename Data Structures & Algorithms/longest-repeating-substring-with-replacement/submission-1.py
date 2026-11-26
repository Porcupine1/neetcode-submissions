from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hFreq = 0
        res = 0
        l = 0
        n=len(s)
        counts = defaultdict(int)

        for r in range(n):
            counts[s[r]] += 1
            hFreq = max(hFreq, counts[s[r]])

            while r-l+1 - hFreq > k:
                counts[s[l]] -= 1
                l += 1

            
            res = max(res, r-l+1)

        return res