class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]

        def dfs(i):
            if i==n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            
            dp[i] = 1+ max([0]+[dfs(j) for j in range(i-1, -1, -1) if nums[j]<nums[i]])
            return dp[i]


        return max(dfs(i) for i in range(n))