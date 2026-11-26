class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l=0
        res = 0

        for r, char in enumerate(s):
            if seen and char in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(char)
            res = max(res, r-l+1)

        return res

        