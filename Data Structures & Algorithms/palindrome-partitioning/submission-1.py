class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def findPal(curr, i):
            if i == len(s):
                res.append(curr[:])
                return 

            for j in range(i, len(s)):
                pal = s[i:j+1]
                if pal == pal[::-1]:
                    curr.append(pal)
                    findPal(curr, j+1)
                    curr.pop()

        findPal([], 0)
        return res
        