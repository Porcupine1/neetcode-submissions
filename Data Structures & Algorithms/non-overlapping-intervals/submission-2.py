class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = []

        for s, t in intervals:
            if res and res[-1][1] > s:
                res[-1][1] = min(res[-1][1], t)
            else:
                res.append([s, t])

        return len(intervals) - len(res)