# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {v:i for i,v in enumerate(inorder)}
        preIdx = 0
        
        def dfs(l, r):
            nonlocal preIdx
            if l>r or preIdx >= len(inorder):
                return
            
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            indx = mp[root.val]
            root.left = dfs(l, indx-1)
            root.right = dfs(indx+1, r)
            return root

        return dfs(0, len(inorder)-1)