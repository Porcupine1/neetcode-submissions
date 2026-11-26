class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [None for _ in range(n)]

        def dfs(l):
            if l >= n:
                return 0

            if memo[l]:
                return memo[l]
            
            maxres = 0
            for r in range(l+1, n):
                prof = prices[r]-prices[l]
                print(maxres, prof+dfs(r+2), dfs(r+1))
                maxres = max(maxres, prof+dfs(r+2), dfs(r+1))

            memo[l] = maxres
            return maxres

        return max(dfs(i) for i in range(n))