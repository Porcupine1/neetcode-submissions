class Solution:
    def countPali(self, s:str, l:int, r:int) -> int:
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l-=1
            r+=1
        return res

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPali(s, i, i)
            count += self.countPali(s, i, i+1)

        return count