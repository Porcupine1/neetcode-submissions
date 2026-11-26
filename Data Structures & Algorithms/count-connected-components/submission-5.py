from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(x):
            par = parent[x]
            
            if par == x:
                return x
            
            parent[x] = find(par)
            return parent[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            

            if rx == ry:
                return

            if rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[rx] = ry
                if rank[rx] == rank[ry]:
                    rank[ry] += 1

        for a, b in edges:
            print(parent, rank)
            union(a, b)
        print(parent)
        

        return sum([1 for i in range(n) if i == parent[i]])

