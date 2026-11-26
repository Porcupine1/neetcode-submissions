class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1]-x[0])
        output = [-1 for i in range(len(queries))]

        for idx, query in enumerate(queries):
            for start, end in intervals:
                if start <= query <= end:
                    output[idx] = end - start + 1
                    break

        return output