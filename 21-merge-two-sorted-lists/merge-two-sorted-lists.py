# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head, list1 = list1, list1.next
            else:
                head, list2 = list2, list2.next

            node.next = head
            node = node.next
        
        node.next = list1 if list1 else list2
        
        return dummy.next
