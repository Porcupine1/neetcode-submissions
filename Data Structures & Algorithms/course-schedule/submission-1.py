from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        visit = set()
        res = True

        for a, b in prerequisites:
            adj[a].add(b)

        def dfs(curr):
            if curr in visit:
                return False
            
            if adj[curr] == []:
                return True

            visit.add(curr)
            for j in adj[curr]:
                if not dfs(j):
                    return False
            
            visit.remove(curr)
            adj[curr] = []
            return res

        for i in range(numCourses):
           if not dfs(i):
                return False

        return res