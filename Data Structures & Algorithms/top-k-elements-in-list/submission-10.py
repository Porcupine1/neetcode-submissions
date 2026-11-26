from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsToCounts = Counter(nums)
        countsToNums = [[] for _ in range(len(nums)+1)]
        res = []

        for num, count in numsToCounts.items():
            countsToNums[count].append(num)


        while countsToNums and len(res) < k:
            if countsToNums[-1]:
                res.append(countsToNums[-1].pop())
            else:
                countsToNums.pop()

        return res