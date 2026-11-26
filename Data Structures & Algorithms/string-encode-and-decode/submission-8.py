class Solution:

    def encode(self, strs: List[str]) -> str:
        curr = []
        for word in strs:
            curr.append(f"{len(word)}#{word}")
            
        return "".join(curr)

    def decode(self, s: str) -> List[str]:
        idx = 0
        end = len(s)-1
        res = []

        while idx < end:
            l = idx
            while s[idx] != "#":
                idx += 1
            size = int(s[l: idx])
            l = idx + 1
            idx = l + size
            word = s[l: idx]
            res.append(word)

        return res

