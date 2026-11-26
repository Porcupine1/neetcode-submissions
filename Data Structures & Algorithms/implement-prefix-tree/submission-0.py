class PrefixTree:

    def __init__(self):
        self.end = False
        self.children = {}

    def insert(self, word: str) -> None:
        def dfs(curr, word):
            if len(word) == 0:
                curr.end = True
                return

            if word[0] in curr.children:
                dfs(curr.children[word[0]], word[1:])
            else:
                node = PrefixTree()
                node.children = {}
                curr.children[word[0]] = node
                dfs(node, word[1:])

        dfs(self, word)

    def search(self, word: str) -> bool:
        curr = self
        i = 0
        while i < len(word) and word[i] in curr.children:
            print(word[i])
            curr = curr.children[word[i]]
            i+=1
        return i == len(word) and curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        i = 0
        while i < len(prefix) and prefix[i] in curr.children:
           curr = curr.children[prefix[i]]
           i+=1

        return i == len(prefix)
        