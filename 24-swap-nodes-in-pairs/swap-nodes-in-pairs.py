# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummyNode = ListNode(0, head)
        
        prev, curr = dummyNode, head
        while curr and curr.next:
            toSwap = curr.next
            nextPair = curr.next.next

            prev.next = toSwap
            toSwap.next = curr
            curr.next = nextPair

            prev = curr
            curr = curr.next
        
        return dummyNode.next