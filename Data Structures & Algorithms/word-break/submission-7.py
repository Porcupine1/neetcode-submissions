class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp ={len(s): True}
        start = min([len(word) for word in s])

        for i in range(len(s)-start, -1, -1):
            print(dp)
            for word in wordDict:
                wordLen = len(word)
                print(s[i:i+wordLen])
                if word  == s[i:i+wordLen] and dp.get(i+wordLen, False):
                    dp[i] = True
                    break

        return dp[0] if 0 in dp else False
        