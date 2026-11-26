# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def in_order(root, result):
            if not root:
                return result
            
            result = in_order(root.left, result)
            result.append(root.val)
            result = in_order(root.right, result)
            return result

        return in_order(root, [])