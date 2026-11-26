from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = defaultdict(int)
        dp[0]=0
        
        def dfs(i, amount):
            if amount <0 or i==n:
                return 0
            
            if amount==0:
                return 1
            
            if dp and (i,amount) in dp:
                return dp[(i,amount)]

            for j in range(i, n):
                dp[(i,amount)] += dfs(j, amount-coins[j])
            
            return dp[(i,amount)]

        return dfs(0,amount)