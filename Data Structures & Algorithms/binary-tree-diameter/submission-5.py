# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findDepth(root, best_diameter):
            if root is None:
                return 0, best_diameter

            left_d, best_diameter = findDepth(root.left, best_diameter)
            right_d, best_diameter = findDepth(root.right, best_diameter)
            
            return max(left_d, right_d)+1, max(best_diameter, left_d+right_d)

        _, res = findDepth(root, 0)
        return res