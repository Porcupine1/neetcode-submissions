from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        grey = set()
        black = set()
        res = True

        for a, b in prerequisites:
            adj[a].add(b)

        def dfs(curr):
            nonlocal res
            
            if not res:
                return False

            grey.add(curr)
            for j in adj[curr]:
                if j in grey:
                    return False
                if not dfs(j):
                    return False
            
            grey.remove(curr)
            black.add(curr)
            return res

        for i in range(numCourses):
            if i not in black:
                res = dfs(i)
                if not res:
                    return False

        return res