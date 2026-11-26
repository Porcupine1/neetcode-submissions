class Solution:

    def encode(self, strs: List[str]) -> str:
        print("".join([f"{len(word)}#{word}" for word in strs]))
        return "".join([f"{len(word)}#{word}" for word in strs])
    def decode(self, s: str) -> List[str]:
        start=end=0
        res = []

        while start < len(s):
            if s[end] != "#":
                end += 1
                continue
            
            word_len = int(s[start:end])
            start = end+1
            end = start + word_len
            res.append(s[start:end])

            start = end
            end += 1

        return res