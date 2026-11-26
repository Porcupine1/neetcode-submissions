# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        l = [root]

        while l:
            newl = []
            for v in l:
                for u in [v.left, v.right]:
                    if u:
                        newl.append(u)
            if newl:
                res.append(list(map(lambda x: x.val, newl)))
            l = newl
            

        return res

            

