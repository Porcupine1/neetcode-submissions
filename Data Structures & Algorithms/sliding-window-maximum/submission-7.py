import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        heapq.heapify(h)
        res = []
        l = 0

        for r, v in enumerate(nums):
            heapq.heappush(h, (-v, r))

            if r >= k-1:
                while not (l <= h[0][1] <= r):
                    heapq.heappop(h)
                res.append(-h[0][0])
                l += 1

        return res
