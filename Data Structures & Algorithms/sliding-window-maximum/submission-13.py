import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        l = 0
        for r, val in enumerate(nums):  
            if r < k-1:
                heapq.heappush(heap, (-val, r))
                continue

            heapq.heappush(heap, (-val, r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            l+=1
            print(heap, " ->", -heap[0][0])
           

        return res

