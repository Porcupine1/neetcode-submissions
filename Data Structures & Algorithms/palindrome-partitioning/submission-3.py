class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []
        def findParts(i):
            if i >= len(s):
                res.append(parts[:])
                return
            print(res)
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    parts.append(sub)
                    findParts(j+1)
                    parts.pop()

        findParts(0)
        return res
            

