class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        n = len(coins)

        def dfs(i, curr):
            if i == n or curr > amount:
                return 0
            if curr == amount:
                return 1
            
            if dp and (i, curr) in dp:
                return dp[(i, curr)]

            # go to next coint (i+1) or use coin but don't move to next coin yet as might reuse
            dp[(i, curr)] = dfs(i+1, curr) + dfs(i, curr+coins[i])
            
            return dp[(i, curr)]

        res = dfs(0, 0)
        return res