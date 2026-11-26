# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dist = 0
        def maxD(root):
            if root is None:
                return 0
            
            left = maxD(root.left)
            right = maxD(root.right)
            
            self.dist = max(self.dist, left + right)
            
            return max(left, right)+1
            
        maxD(root)
        return self.dist
        