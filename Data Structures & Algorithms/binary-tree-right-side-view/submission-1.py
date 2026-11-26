# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depth = -1
        res = []
        def dfs(curr, root):
            nonlocal depth
            
            if not root:
                return
            if curr > depth:
                res.append(root.val)
                depth = curr
            dfs(curr+1, root.right)
            dfs(curr+1, root.left)

        dfs(0, root)
        return res