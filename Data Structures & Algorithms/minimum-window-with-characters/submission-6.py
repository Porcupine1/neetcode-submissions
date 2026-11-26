from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_num = len(set(t))
        chars_hp = defaultdict(int)
        best = float('inf')
        b_l, b_r = 0, 0

        for c in t:
            chars_hp[c] += 1

        l=0
        for r in range(len(s)):
            if s[r] in t:
                chars_hp[s[r]] -= 1
                
                if chars_hp[s[r]] == 0:
                    chars_num-=1
                
            while chars_num == 0:
                if best > r-l+1:
                    best = r-l+1
                    b_l, b_r = l, r
                
                if s[l] in t:
                    chars_hp[s[l]] += 1
                    if chars_hp[s[l]] == 1:
                        chars_num += 1

                l += 1
        print(b_l, b_r)
        return "" if best==float('inf') else s[b_l: b_r+1]