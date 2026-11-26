# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def countDepth(curr, root):
            if root is None:
                return curr
        
            curr += max(countDepth(curr, root.left), countDepth(curr, root.right)) + 1
            return curr


        return countDepth(0, root)
        