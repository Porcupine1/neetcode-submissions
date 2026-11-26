from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        visit = set()

        def dfs(curr, prev=None):
            if curr in visit:
                return

            visit.add(curr)
            for j in adj[curr]:
                
                if j in visit:
                    continue
                dfs(j, curr)


        def build_adj():
            for a, b in edges:
                adj[a].add(b)
                adj[b].add(a)


        build_adj()
        count = 0
        for curr in range(n):
            if curr not in visit:
                dfs(curr)
                count += 1

        return count

        

        