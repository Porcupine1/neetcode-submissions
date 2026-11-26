class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix_prod = [1]*size
        suffix_prod = [1]*size
    

        for idx in range(1, size):
            prefix_prod[idx] = nums[idx-1] * (prefix_prod[idx-1] if idx-1 >= 0 else 1)
            
        for idx in range(size-2,-1,-1):
            suffix_prod[idx] = nums[idx+1] * (suffix_prod[idx+1] if idx+1 < size else 1)
        
        res = [1]*size
        for idx in range(size):
            if idx ==0:
                res[idx] = suffix_prod[0]
                continue
            if idx==size-1:
                res[idx] = prefix_prod[-1]
                continue
            res[idx] = prefix_prod[idx] * suffix_prod[idx]
        return res