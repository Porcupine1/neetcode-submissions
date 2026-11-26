class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        times = {i:0 for i in nums}
        print(times)
        for i, e in enumerate(nums):
            if times[e] == 1:
                return True
            times[e] += 1
        return False
         