from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_to_freq = defaultdict(int)
        freqs_to_nums = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            nums_to_freq[num] += 1

        for num in nums_to_freq:
            idx = nums_to_freq[num]
            freqs_to_nums[idx].append(num)

        
        while len(res) < k:
            if freqs_to_nums:
                if freqs_to_nums[-1]:
                    res.append(freqs_to_nums[-1].pop())
                else:
                    freqs_to_nums.pop()

        return res
