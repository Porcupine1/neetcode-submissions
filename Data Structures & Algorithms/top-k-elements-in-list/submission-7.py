from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = Counter(nums)
        freqToNum = [[] for _ in range(len(nums)+1)]

        for num in numToFreq:
            freq = numToFreq[num]
            freqToNum[freq].append(num)
        
        res = []
        while len(res) < k and freqToNum:
            if freqToNum[-1] == []:
                freqToNum.pop()
                continue
            res.append(freqToNum[-1].pop())

        return res
