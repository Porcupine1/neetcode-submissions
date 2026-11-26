"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        mp = {}

        curr = head
        curr2 = dummy
        while curr:
            curr2.next = Node(curr.val, None)
            curr2 = curr2.next
            mp[curr] = curr2
            curr = curr.next
        print(mp)
        curr = head
        curr2 = dummy.next
        while curr:
            if curr.random:
                curr2.random = mp[curr.random]
            else:
                curr2.random = None
            curr = curr.next
            curr2 = curr2.next

        return dummy.next

        
        