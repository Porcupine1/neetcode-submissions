class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefProd = [1]*n

        for i in range(n):
            if i > 0 and nums[i-1] == 0:
                prefProd[i] = nums[i]
            else: prefProd[i] = (nums[i] if i == 0 else prefProd[i-1]*nums[i])
       
        print(prefProd)
        best = float('-inf')
        for i in range(n):
            for j in range(i, -1, -1):
                if i!=j and prefProd[j]!=0:
                    best = max(best, prefProd[i]//(1 if (j-1 < 0 or prefProd[j-1] == 0) else prefProd[j-1]))
                else: best = max(best, nums[j])
                print(j, i, best)

        return best
