class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = {}
        n = len(strs)
        
        def insert(s, root):
            curr = root
            for c in s:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["end"] = None
            return root
        
        for i in range(n):
            root = insert(strs[i], root)

        curr = []
        while root and len(root) == 1:
            curr.append(*root.keys())
            if curr[-1] == 'end':
                curr = curr[:-1]
                break
            root = root[curr[-1]]

        return "".join(curr)


        