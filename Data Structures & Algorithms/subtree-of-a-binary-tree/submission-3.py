# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, curr):
            if not root and not curr:
                return True
            
            if root and curr and curr.val == root.val:
                return sameTree(root.left, curr.left) and sameTree(root.right, curr.right)

            return False
        
        if root and not subRoot:
            return True
        
        if subRoot and not root:
            return False

        if root.val == subRoot.val:
            left = sameTree(root.left, subRoot.left)
            right = sameTree(root.right, subRoot.right)

            if left and right:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)