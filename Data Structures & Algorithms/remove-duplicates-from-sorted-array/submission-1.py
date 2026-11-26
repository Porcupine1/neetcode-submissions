class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)

        i=j=0
        while i<n:
            if nums[i] in seen and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                continue
            seen.add(nums[i])
            if i == j:
                j+=1
            i+=1
        
        return len(seen)
