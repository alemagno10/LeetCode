# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numbers = defaultdict(int)

        if not head:
            return None

        # insert values into dict
        node = head
        while node:
            numbers[node.val] += 1
            node = node.next

        # update head if needed
        while head and numbers[head.val] > 1:
            head = head.next

        # run through the rest of the list
        prev, node = head, head
        while node:
            if numbers[node.val] > 1:
                prev.next = node.next if node else None
            else:
                prev = node
            node = node.next
        
        return head
