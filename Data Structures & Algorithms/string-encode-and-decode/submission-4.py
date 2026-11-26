class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + "$" + st

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        j = 0
        res = []

        while j < len(s):
            i = j
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
        return res