class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        stack = []

        for c in s:
            if not stack and c in closeToOpen:
                return False
            elif c not in closeToOpen:
                stack.append(c)
            elif stack and closeToOpen[c] != stack.pop():
                return False
            
        return stack == []