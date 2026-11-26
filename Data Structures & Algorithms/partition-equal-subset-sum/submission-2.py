class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = {0, nums[0]}
        n = sum(nums)

        if n%2!=0:
            return False

        for i in range(1, len(nums)):
            sub = set()
            for num in res:
                ans = num + nums[i]
                if ans == n//2:
                    return True
                if ans not in res:
                    sub.add(ans)
                
            print(res, sub)
            res.update(sub)
            print(res,'\n')
        
        return False