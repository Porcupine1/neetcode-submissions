class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        dp.append(True)
        r = len(s)
        minl = min(len(word) for word in wordDict)

        for l in range(len(s)-minl, -1, -1):
            for word in wordDict:
                r = l + len(word)
                if s[l:r] == word and dp[r]:
                    dp[l] = True

        return dp[0]