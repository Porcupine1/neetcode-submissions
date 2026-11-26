class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)

        def dfs(n):
            if n < 0:
                return 0

            if dp[n]:
                return dp[n]

            dp[n] = max(nums[n]+dfs(n-2), dfs(n-1))
            return dp[n]
        return dfs(len(nums)-1)

            