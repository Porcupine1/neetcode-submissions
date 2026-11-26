class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                return [*res, newInterval, *intervals[i:]]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                continue
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res