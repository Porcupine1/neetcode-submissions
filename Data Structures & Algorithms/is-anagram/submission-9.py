class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_sig = {}
        t_sig = {}

        for i in range(len(s)):
            s_sig[s[i]] = 1 + s_sig.get(s[i], 0)
            t_sig[t[i]] = 1 + t_sig.get(t[i], 0)

        return s_sig == t_sig