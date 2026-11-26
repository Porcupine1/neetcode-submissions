# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []
        def preorder(root):
            if root is None:
                serial.append("N")
                return

            serial.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        print(",".join(serial))
        return ",".join(serial)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        idx = 0
        def dfs():
            nonlocal idx
            if idx >= len(vals) or vals[idx] == "N":
                idx += 1
                return

            root = TreeNode(int(vals[idx]))
            idx += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()