class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                node = WordDictionary()
                curr.children[char] = node
                curr = node
        curr.end = True
        

    def search(self, word: str) -> bool:
        res = False
        def dfs(curr, i):
            nonlocal res
            
            if i == len(word):
                res = curr.end
                return
            
            if res:
                return

           
            if word[i] in curr.children:
                dfs(curr.children[word[i]], i+1)
            elif word[i] == '.':
                for char in curr.children:
                    dfs(curr.children[char], i+1)


        dfs(self, 0)
        return res

