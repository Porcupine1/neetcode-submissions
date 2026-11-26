class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def findParts(i):
            if i >= len(s):
                res.append(part[:])
                return
                
            for j in range(i, len(s)):
                    
                sub = s[i:j+1]
                print(sub)
                if sub == sub[::-1]:
                    part.append(sub)
                    findParts(j+1)
                    part.pop()

        findParts(0)
        return res