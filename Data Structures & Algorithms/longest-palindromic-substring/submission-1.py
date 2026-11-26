class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=r=0
        n = len(s)

        def find_pal(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if s[i+1] != s[j-1]:
                return 0,0
            return i+1, j-1

        for i in range(n):
            l1, r1 = find_pal(i, i)
            l2, r2 = find_pal(i-1, i)
            
            if r1-l1 < r2-l2:
                l1, r1 = l2,r2
            if r1-l1 > r-l:
                l, r = l1, r1
                
            
        print(l, r)
        return s[l:r+1]