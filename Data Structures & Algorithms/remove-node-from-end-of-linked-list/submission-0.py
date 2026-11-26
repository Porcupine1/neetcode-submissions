# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            curr = curr.next
            count += 1

        if count == n:
            return head.next
        print(count)
        count -= n
        print(count)
        prev, curr = ListNode(), head
        for i in range(count):
            prev, curr = curr, curr.next
        print(curr.val)
        prev.next = curr.next
        curr.next = None
        return head