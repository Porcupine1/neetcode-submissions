class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        def dfs(i):
            if i <= 1:
                return max(nums[:i+1])
            if dp[i]:
                return dp[i]
            
            dp[i] =  max(dfs(i-2) + nums[i], dfs(i-1))
            return dp[i]

        return dfs(len(nums)-1)