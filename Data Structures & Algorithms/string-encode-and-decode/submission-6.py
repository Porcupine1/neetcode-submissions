class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f"{len(word)}")
            res.append("#")
            res.append(word)
            
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        l = r= 0
        res = []
        while r < len(s):
            while s[r] != "#":
                r += 1
            
            num = int(s[l:r])
            res.append(s[r+1:r+1+num])
            l = r = r+num + 1
        return res
