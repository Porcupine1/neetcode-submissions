class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        
        def findCombo(curr, i):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for j in range(i,len(digits)):
                for char in mapping[digits[i]]:
                    findCombo(curr+char, j+1)

        findCombo("", 0)
        return res