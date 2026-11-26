class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def count_pals(i, j):
            count = 0
            while j >= 0 and i < n and s[i] == s[j]:
                j -= 1
                i += 1
                count += 1

            return count

        res = 0
        for i in range(n):
            res += count_pals(i, i) + count_pals(i, i-1)

        return res