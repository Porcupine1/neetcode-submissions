class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pars = ""

        def func(pars, o, c):
            if o == c == n:
                res.append(pars)
                return
            if o < n:
                pars += "("
                func(pars, o+1, c)
                pars = pars[:-1]

            if c < o:
                pars += ")"
                func(pars, o, c+1)
                pars = pars[:-1]

        func(pars, 0, 0)
        return res