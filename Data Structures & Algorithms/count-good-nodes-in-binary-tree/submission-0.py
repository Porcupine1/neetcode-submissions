# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(currMax, root, count):
            if root is None:
                return count

            add = 0
            if root.val >= currMax:
                add = 1
                currMax = root.val
            
            return dfs(currMax, root.left, count) + dfs(currMax, root.right, count) + add

        return dfs(float("-inf"), root, 0)
