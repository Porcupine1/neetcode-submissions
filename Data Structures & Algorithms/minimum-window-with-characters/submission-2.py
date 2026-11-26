from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = defaultdict(int)
        need = defaultdict(int)
        count = 0
        left, right, l = 0,0,0
        min_len = float("inf")

        for e in t:
            need[e] += 1

        for r in range(len(s)):
            curr = s[r]
            if curr in need:
                have[curr] += 1
                if have[curr] == need[curr]:
                    count += 1
            
            while count == len(need):
                if r-l+1 < min_len:
                    left = l
                    right = r
                    min_len = r-l+1

                curr = s[l]
                print(l, r)
                if curr in need:
                    have[curr] -= 1
                    if have[curr] < need[curr]:
                        count -= 1

                l += 1

        return s[left:right+1] if min_len != float("inf") else ""