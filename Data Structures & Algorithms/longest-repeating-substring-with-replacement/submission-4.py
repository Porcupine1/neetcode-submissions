from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        seen = defaultdict(int)
        best = 0

        l=0

        for r in range(len(s)):
            seen[s[r]] += 1
            maxf = max(maxf, seen[s[r]])

            while r-l+1 - maxf > k:
                seen[s[l]] -= 1
                l += 1

            best = max(r-l+1, best)

        return best