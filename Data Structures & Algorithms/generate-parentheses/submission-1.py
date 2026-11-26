class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pars = ""

        def func(pars, o, c):
            if o == c == n:
                res.append(pars)
                return
            if o < n:
                func(pars+"(", o+1, c)

            if c < o:
                func(pars+")", o, c+1)

        func(pars, 0, 0)
        return res