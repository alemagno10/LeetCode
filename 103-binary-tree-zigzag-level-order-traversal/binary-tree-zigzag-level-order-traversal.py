# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([(root,0)])
        depth = 0
        res = [[]]

        while len(queue) > 0:
            curr = queue.popleft()

            if curr[1] > depth:
                res.append([])
                depth += 1
            
            res[-1].append(curr[0].val)
            if curr[0].left:
                queue.append((curr[0].left, depth+1))
            if curr[0].right:
                queue.append((curr[0].right, depth+1))

        for i,level in enumerate(res):
            if i%2==1:
                level.reverse()

        return res