class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        
        
        def dfs(i, prev):
            if i == n:
                return 0

            if (i, prev) in dp:
                return dp[(i, prev)]


            dp[(i, prev)]= dfs(i+1, prev)

            if prev<nums[i]:
                dp[(i, prev)] = max(dp[(i, prev)], 1+dfs(i+1, nums[i]))
                
            return dp[(i, prev)]

        return dfs(0, float('-inf'))