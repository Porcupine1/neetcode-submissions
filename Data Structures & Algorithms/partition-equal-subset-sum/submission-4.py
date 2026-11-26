class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        target = arr_sum//2
        if arr_sum%2==1:
            return False

        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        dp[0][nums[0]] = True

        for i in range(n):
            dp[i][0] = True
        
        for i in range(n):
            for t in range(1, target+1):
                dp[i][t] = dp[i-1][t] or dp[i-1][t-nums[i]]

        return dp[n-1][target]