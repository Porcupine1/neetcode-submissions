# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, limit):
        prev, curr = None, head
       
        while limit:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            limit -= 1
        return prev, head, curr
 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevTail = None
        dummy = ListNode()

        curr = head
        count = 0
        while curr:
            while curr:
                curr = curr.next
                count += 1
                if count % k == 0:
                    break
            if count < k:
               
                return head
            
            if count % k != 0 and not curr:
                break
            
            if count == k:
               
                dummy.next = head
            
                
            fstHead, tail, head = self.reverse(head, k)
            
            if count == k:
                dummy.next = fstHead

            if prevTail:
                prevTail.next = fstHead
            tail.next = head
                
            prevTail = tail

        return dummy.next



        