# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyLess, dummyGrater = ListNode(), ListNode()
        less, grater = dummyLess, dummyGrater

        if not head:
            return None

        node = head
        while node:
            if node.val < x:
                less.next = node
                less = node
            else:
                grater.next = node
                grater = node

            nxt = node.next
            node.next = None
            node = nxt
        
        less.next = dummyGrater.next
        return dummyLess.next
            