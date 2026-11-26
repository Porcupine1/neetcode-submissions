from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1,n+1):
            for curr, count in dp[i-1].items():
                dp[i][curr-nums[i-1]] += count
                dp[i][curr+nums[i-1]] += count

        return dp[n][target]