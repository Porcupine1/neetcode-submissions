class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        last_start = max([x[1] for x in intervals])
        mp = [-1]*(last_start+1)
        curr = -1
        res = []

        for s, t in intervals:
            mp[s] = max(mp[s], t)

        for i in range(last_start+1):
            if res and res[-1][1] >= i:
                res[-1][1] = max(res[-1][1], mp[i])
            elif mp[i] != -1:
                res.append([i, mp[i]])

        return res

