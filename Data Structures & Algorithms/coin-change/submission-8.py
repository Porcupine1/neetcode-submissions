class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amt):
            if 0 >= amt:
                return 0 if amt == 0 else float('inf')
            
            if dp and amt in dp:
                return dp[amt]
            
            dp[amt] = min([1+dfs(amt-c) for c in coins])
            return dp[amt]
        res = dfs(amount)
        return res if res!=float('inf') else -1
