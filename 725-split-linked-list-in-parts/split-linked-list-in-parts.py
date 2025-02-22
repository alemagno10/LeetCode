# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        for i in range(k):
            res.append(None)

        if not head:
            return res
        
        node = head
        lenght = 0
        while node:
            node = node.next
            lenght += 1
        
        node = head
        for i in range(k):
            nodesPerList = math.ceil((lenght) / (k-i)) if k-i > 1 else lenght
            res[i] = node
            while node and nodesPerList > 0:
                prev = node
                node = node.next
                nodesPerList -= 1
                lenght -= 1
            prev.next = None

        return res
                



        