"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        hp = {node.val: Node(node.val, [])}
        dq = deque([node])

        while dq:
            curr = dq.pop()

            for v in curr.neighbors:
                if v and v.val in hp:
                    newNode = hp[v.val]
                else:
                    newNode = Node(v.val, [])
                hp[curr.val].neighbors.append(newNode)
                
                if not (v and v.val in hp):
                    hp[v.val] = newNode
                    dq.append(v)
        return hp[node.val]

