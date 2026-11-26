class Node:
    def __init__(self, key, val, prev, next):
        self.key, self.val = key, val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, None)
        self.right.prev = self.left
        self.left.next = self.right

        self.cache = {}
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
            
    def append(self, node):
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        prev.next =  nxt.prev = node

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        if node != -1:
            self.remove(node)
            self.append(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, -1)

        if node != -1:
            self.remove(node)
        node = Node(key, value, None, None)
        self.append(node)
        self.cache[key] = node
        
        if len(self.cache) > self.cap:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]
        print(self.left.next.val, self.right.prev.val)
        

        
