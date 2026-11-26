from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        used = 0
        seen = defaultdict(int)
        best = 0

        l=0

        for r in range(len(s)):
            seen[s[r]] += 1

            while r-l+1 - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1

            best = max(r-l+1, best)

        return best