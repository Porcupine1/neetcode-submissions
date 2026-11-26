class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = []
        suffixProduct = []

        prefixProduct.append(0)
        prefixProduct.append(nums[0])

        nums_rev = nums[::-1]

        suffixProduct.append(0)
        suffixProduct.append(nums_rev[0])

        l = len(nums)
        for i in range(2, l):
            prefixProduct.append(prefixProduct[i-1]*nums[i-1])
            suffixProduct.append(suffixProduct[i-1]*nums_rev[i-1])

        suffixProduct.reverse()
        res = []
        res.append(suffixProduct[0])
        for i in range(1,l-1):
            res.append(prefixProduct[i] * suffixProduct[i])
        res.append(prefixProduct[-1])

        return res