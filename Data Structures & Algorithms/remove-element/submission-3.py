class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        n = len(nums)-1
        while k <= n:
            if nums[k] != val:
                k+=1
            else:
                nums[k] = nums[n]
                nums[n] = val
                n-=1

        return k