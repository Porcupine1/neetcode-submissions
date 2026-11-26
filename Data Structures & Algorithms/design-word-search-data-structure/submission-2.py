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
        def dfs(curr, i):
            if i == len(word):
                return curr.end
            
            if word[i] in curr.children:
                return dfs(curr.children[word[i]], i+1)
            elif word[i] == '.':
                for char in curr.children:
                    res = dfs(curr.children[char], i+1)
                    if res:
                        return True
            return False


        
        return dfs(self, 0)

