# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None 

        node, end = head, head
        for i in range(n):
            end = end.next
        
        lenght = 0
        while node:
            node = node.next
            lenght += 1
        
        node = head
        while end and end.next:
            node = node.next
            end = end.next
            lenght += 1

        if n == 1:
            node.next = None
        elif n == lenght:
            head = head.next
        else:
            node.next = node.next.next
               
        return head
        