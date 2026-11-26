# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(left, right, root):
            if not root:
                return True

            if left < root.val < right:
                return check(left, min(root.val, right), root.left) and check(max(root.val, left), right, root.right)
            return False

        return check(float("-inf"), float("inf"), root)