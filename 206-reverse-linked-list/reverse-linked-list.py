# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        prev, curr, nxt = None, head, head.next
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
            
        curr.next = prev
        return curr



#   | | |
#   1 2 3 4 5

#  5 4 3 2 1 -