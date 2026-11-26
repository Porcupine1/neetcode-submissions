from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        times = defaultdict(int)
        for i in nums:
            if times[i] == 1:
                return True
            times[i] += 1
        return False
         