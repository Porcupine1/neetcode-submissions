class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':"(", "}": "{", "]":"["}
        stack = []
        for c in s:
            if c in mp:
                if stack and stack.pop() == mp[c]:
                    continue
                else:
                    return False
            stack.append(c)

        return stack == []