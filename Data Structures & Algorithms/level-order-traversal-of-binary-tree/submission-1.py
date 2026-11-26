# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                curr = q.popleft()
                
                if curr:
                    print(curr.val)
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)

            if level:
                res.append(level)
        return res