# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(root):
            if root is None:
                return 0, True

            left_height, left_balanced = is_balanced(root.left)
            right_height, right_balanced = is_balanced(root.right) 

            return max(left_height, right_height)+1, \
                    (abs(right_height-left_height)<=1 and left_balanced and right_balanced)

        _, res = is_balanced(root)
        return res