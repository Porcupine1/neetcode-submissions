# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr):
            print(curr == p, curr.val)
            if ((curr.val - p.val) * (curr.val - q.val) < 0) or (curr.val == p.val) or (curr.val == q.val):
                return curr

            if curr.val > p.val:
                return dfs(curr.left)
            else:
                return dfs(curr.right)

        return dfs(root)

            