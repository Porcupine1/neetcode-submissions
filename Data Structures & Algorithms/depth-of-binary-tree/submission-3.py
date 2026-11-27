# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        stack = [(1, root)]
        res = 0

        while stack:
            d, node = stack.pop()
            res = max(res, d)
            if node.left:
                stack.append((d+1, node.left))
            if node.right:
                stack.append((d+1, node.right))

        return res