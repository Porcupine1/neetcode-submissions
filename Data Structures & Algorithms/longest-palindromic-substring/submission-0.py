class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestl = 0
        bestLen = 0

        for i in range(len(s)):
            print(i)
            l, r = i, i
            sub = s[l:r+1]

            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > bestLen:
                    bestl = l
                    bestLen = r-l+1
                l-= 1
                r+=1

            l, r = i, i+1
            sub = s[l:r+1]

            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > bestLen:
                    bestl = l
                    bestLen = r-l+1
                l-= 1
                r+=1

        return s[bestl:bestl+bestLen]
