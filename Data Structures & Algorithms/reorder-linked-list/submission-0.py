# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0

        curr = head
        while curr:
            curr = curr.next
            count += 1
        mid = count // 2 if count%2==0 else (count // 2)+1
        prev, curr = None, head
        while mid != 0:
            prev, curr = curr, curr.next
            mid -= 1
        prev.next = None
        
        # reverse second half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        
        dummy = curr = head
        count = 0
        while curr:
            print(curr.val)
            temp = curr.next
            curr.next = prev
            prev = temp
            curr = curr.next
            
