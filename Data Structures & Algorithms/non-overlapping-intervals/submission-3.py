class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        curr = None
        count = 0
        print(intervals)

        for s, t in intervals:
            if curr and curr > s:
                curr = min(curr, t)
                count += 1
            else:
                curr = t

        return  count