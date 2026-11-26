class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        h_set = set(nums)
        starts = set()

        
        for num in nums:
            if num -1 not in h_set:
                starts.add(num)


        best = 1
        for num in starts:
            curr = 1
            while num + 1 in h_set:
                curr +=1
                num += 1
            best = max(best, curr)

        return best