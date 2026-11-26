from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        visit = set()

        def dfs(curr):
            if curr in visit:
                return False

            if adj[curr] == []:
                return True

            visit.add(curr)
            for j in adj[curr]:
                adj[j].remove(curr)
                if not dfs(j):
                    return False

            adj[curr] = []
            return True

        res = dfs(0)
        print(res, len(visit))
        if res and len(visit) == n:
            return True
        
        return False