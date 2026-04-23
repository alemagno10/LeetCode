# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        def dfs(node):
            if not node.next:
                return node.val, 1
            
            new, isTail = dfs(node.next)
            node.val, new = new, node.val

            if isTail:
                node.next = None
            return new, 0

        dfs(node)