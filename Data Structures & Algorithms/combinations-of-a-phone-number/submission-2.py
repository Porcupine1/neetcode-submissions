class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mp = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        res = []

        def findCombo(curr, i):
            if i == len(digits):
                res.append("".join(curr))
                return

            ops = mp[int(digits[i])]
            for j in ops:
                findCombo(curr+[j], i+1)

        findCombo([], 0)
        return res