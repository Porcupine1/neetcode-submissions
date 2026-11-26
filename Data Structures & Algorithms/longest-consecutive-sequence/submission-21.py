class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0


        for num in unique:
            if num-1 not in unique:
                curr = num
                count = 0
                
                while curr in unique:
                    count += 1
                    curr+=1
                res = max(res, count)
            
        return res