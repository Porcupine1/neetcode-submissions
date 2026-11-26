class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        n = len(intervals)
        min_len = []
        sorted_qs = sorted([val, i] for i, val in enumerate(queries))
        i = 0
        output = [-1]*len(queries)

        for query, idx in sorted_qs:
            while i < n and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_len, (end-start+1, end))
                i+=1
            
            while min_len and min_len[0][1] < query:
                heapq.heappop(min_len)
            
            if min_len:
                output[idx] = min_len[0][0]
        return output