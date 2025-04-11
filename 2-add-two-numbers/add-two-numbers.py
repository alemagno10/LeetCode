# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()

        node = dummy
        while l1 or l2:
            l1Val = l1.val if l1 else 0 
            l2Val = l2.val if l2 else 0 

            s = l1Val + l2Val + carry
            carry = int(s >= 10)
            node.next = ListNode(s%10 if s>=10 else s)

            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            node.next = ListNode(carry)
        
        return dummy.next