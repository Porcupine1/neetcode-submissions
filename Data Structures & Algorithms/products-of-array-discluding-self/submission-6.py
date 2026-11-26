class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*len(nums)
        arr_rev = [0]*len(nums)
        res = [0]*len(nums)
    
        arr[0] = nums[0]
        arr_rev[-1] = nums[-1]

        for idx in range(1, n):
            arr[idx] = arr[idx-1] * nums[idx]
            arr_rev[n-idx-1] = arr_rev[n-idx] * nums[n-idx-1]
        print(arr, arr_rev)

        for idx in range(n):
            if idx == 0:
                res[idx] = arr_rev[1]
            elif idx == n-1:
                res[idx] = arr[-2]
            else:
                res[idx] = arr[idx-1] * arr_rev[idx+1]
        
        return res