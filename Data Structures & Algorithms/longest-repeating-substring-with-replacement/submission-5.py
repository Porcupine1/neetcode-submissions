from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        best = 0
        counts = defaultdict(int)

        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxf = max(maxf, counts[s[r]])

            while r-l+1 - maxf > k:
                counts[s[l]] -= 1
                l += 1

            best = max(best, r-l+1)

        return best