# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {v:i for i,v in enumerate(inorder)}
        preIdx = inIdx = 0
        
        def dfs(bound):
            nonlocal preIdx, inIdx
            if preIdx >= len(inorder):
                return
            
            if inorder[inIdx] == bound:
                inIdx += 1
                return

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(bound)

            return root

        return dfs(float("inf"))