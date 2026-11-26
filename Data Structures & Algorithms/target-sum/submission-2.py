class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, curr):
            if i == n:
                if curr == target:
                    return 1
                else:
                    return 0

            if dp and (i, curr) in dp:
                return dp[(i, curr)]

            dp[(i, curr)] = dfs(i+1, curr-nums[i]) + dfs(i+1, curr+nums[i])

            return dp[(i, curr)]

        return dfs(0, 0)