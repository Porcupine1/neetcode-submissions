# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getNext(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverse(self, curr, nextGroup):
        prev = nextGroup
        while curr != nextGroup:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)

        while True:
            kth = self.getNext(prev, k)
            if not kth:
                break
            
            self.reverse(prev.next, kth.next)

            temp = prev.next
            prev.next = kth
            prev = temp

        return dummy.next

            