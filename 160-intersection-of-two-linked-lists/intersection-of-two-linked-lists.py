# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length
        
        A,B = length(headA), length(headB)
        nodeA, nodeB = headA, headB

        for i in range(A-B):
            nodeA = nodeA.next
        
        for i in range(-A+B):
            nodeB = nodeB.next

        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None
            


