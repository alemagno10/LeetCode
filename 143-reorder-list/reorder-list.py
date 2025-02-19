# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        queue = []
        lenght = 0
        node = head
        while node:
            nxt = node.next
            node.next = None
            queue.append(node)
            node = nxt
            lenght += 1
        
        queue.pop(0)
        start = False
        node = head
        while len(queue) > 0:
            node.next = queue.pop(0 if start else -1)
            node = node.next
            start = not start

        return head