# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        
        while any(lists):
            minNode = ListNode(float('inf'))
            j=float('inf')
            for i in range(len(lists)):
                if lists[i] and minNode.val > lists[i].val:
                    minNode = ListNode(lists[i].val)
                    j = i

            curr.next = minNode
            curr = curr.next
            lists[j] = lists[j].next
        return dummy.next