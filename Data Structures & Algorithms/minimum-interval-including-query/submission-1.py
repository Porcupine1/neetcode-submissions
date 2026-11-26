from collections import defaultdict
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        output = [-1 for _ in range(len(queries))]
        min_len_heap = []

        idx = 0
        n = len(intervals)
        for q_val, q_idx in sorted_queries:
            while idx < n and intervals[idx][0] <= q_val:
                start, end = intervals[idx][0], intervals[idx][1]
                heapq.heappush(min_len_heap, (end-start+1,  end))
                idx += 1
            
            while min_len_heap and min_len_heap[0][1] < q_val:
                heapq.heappop(min_len_heap)
            
            if min_len_heap:
                output[q_idx] = min_len_heap[0][0]

        return output