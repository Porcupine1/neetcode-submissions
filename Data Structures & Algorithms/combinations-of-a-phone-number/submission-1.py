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

        def findCombo(curr):
            if len(curr) >= len(digits):

                res.append("".join(curr[:]))
                return

            ops = mp[int(digits[len(curr)])]
            for j in range(len(ops)):
                findCombo(curr+[ops[j]])

        findCombo([])
        return res