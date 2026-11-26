# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float("-inf")

        def find(root):
            nonlocal maxPath
            if root is None:
                return 0

            left = max(find(root.left), 0)
            right = max(find(root.right), 0)

            maxPath = max(maxPath, root.val + left + right)

            return root.val + max(right, left)

        find(root)
        return maxPath