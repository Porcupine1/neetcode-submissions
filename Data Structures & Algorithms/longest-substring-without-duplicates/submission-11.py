class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        best = 0

        for r in range(len(s)):
            while s[r] in seen and seen[s[r]] > 0:
                seen[s[l]] -= 1
                l += 1
            seen[s[r]] = 1 + seen.get(s[r], 0)
            best = max(best, r-l+1)

        return best