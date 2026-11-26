from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        best = 0
        res = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            best = max(best, counts[s[r]])

            if r-l+1 - best > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res

            