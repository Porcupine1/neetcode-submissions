class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for c in strs:
            s += str(len(c))+'#'+c

        print(s)
        return(s)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            word = s[i: j]
            i=j
            res.append(word)
        return(res)