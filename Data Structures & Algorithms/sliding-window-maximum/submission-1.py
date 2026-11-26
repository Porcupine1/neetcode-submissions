import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]

        h = [(-v, i) for i, v in enumerate(nums[:k])]
        heapq.heapify(h)
        res = []
        res.append(-h[0][0])
        
        for i, v in enumerate(nums[k:], k):
            heapq.heappush(h, (-v, i))
            # while the max element is not in the current window, remove it
            while not (i-k < (h[0])[1] <= i):
                heapq.heappop(h)
            res.append(-h[0][0])

        return res
        