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
        slow, fast = head, head.next

        # get LL mid 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev, slow.next = None, None

        # reverse second part
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        second = prev

        # merge first and second part
        while second:
            T1, T2 = first.next, second.next

            first.next = second
            second.next = T1

            first, second = T1, T2