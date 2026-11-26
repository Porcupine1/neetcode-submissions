class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if n%2 != 0:
            return False

        def dfs(res, i):
            if res == n//2:
                return True
            elif i >= len(nums) or res > n//2:
                return False
            
            return dfs(res+nums[i], i+1) or dfs(res, i+1)
        
        return dfs(0, 0)
        