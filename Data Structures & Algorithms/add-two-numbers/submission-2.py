# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2, dummy = l1, l2, None
        count1, count2 = 0, 0

        while curr1 and curr2:
            curr1, curr2 = curr1.next, curr2.next
            count1+=1
            count2+=1
        
        if not curr1 and not curr2:
            dummy = l1
        elif curr1:
            dummy = l1
        else:
            dummy = l2

        curr, curr1, curr2 = dummy, l1, l2
        prev = ListNode(0, dummy)
        carry = 0
        while (curr1 and curr2) or curr:
            if curr1 and curr2:
                val = str(curr1.val + curr2.val + carry)
            else:
                val = str(curr.val + carry)

            if len(val)>1:
                carry = int(val[0])
                curr.val = int(val[1])
            else:
                carry = 0
                curr.val = int(val)

            if curr1 and curr2:
                curr1, curr2 = curr1.next, curr2.next
            prev, curr = curr, curr.next

        if carry:
            prev.next = ListNode(carry, None)
        return dummy
