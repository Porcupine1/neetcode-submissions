# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dist = 0
        def maxD(root):
            nonlocal dist
            if root is None:
                return 0
            
            left = maxD(root.left)
            right = maxD(root.right)
            
            dist = max(dist, left + right )
            
            return max(left, right)+1
            
        maxD(root)
        return dist
        