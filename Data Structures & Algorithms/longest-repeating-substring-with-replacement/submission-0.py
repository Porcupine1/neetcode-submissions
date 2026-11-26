from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        l, maxFreq, res = 0, 0, 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(count[s[r]], maxFreq)
            subLen = r-l+1
            
            if subLen - maxFreq > k:
                count[s[l]] -= 1
                l += 1
                subLen -= 1
            res = max(res, subLen)

        return res