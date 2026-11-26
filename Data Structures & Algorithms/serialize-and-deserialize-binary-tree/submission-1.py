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
            nonlocal serial
            if root is None:
                serial.append("N")
                return

            serial.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        print(serial)
        print(",".join(serial))
        return ",".join(serial)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        idx = 0

        def build():
            nonlocal idx
            if vals[idx] == "N" or idx >= len(vals):
                idx += 1
                return
            
            val = int(vals[idx])
            print(val)
            idx += 1
            root = TreeNode(val)

            root.left = build()
            root.right = build()

            return root
        return build()