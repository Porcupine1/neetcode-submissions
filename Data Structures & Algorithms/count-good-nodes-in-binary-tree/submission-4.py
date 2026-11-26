# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0
        def dfs(maxV, root):
            if not root:
                return

            if root.val >= maxV:
                self.goodCount += 1
            dfs(max(root.val, maxV), root.left)
            dfs(max(root.val, maxV), root.right)

        dfs(float("-inf"), root)
        return self.goodCount