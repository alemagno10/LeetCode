# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}
        
        def backtracking(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in memo:
                return memo[n]
            
            res = []
            for a in range(0,n):
                b = n-a-1 
                for left in backtracking(a):
                    for right in backtracking(b):
                        root = TreeNode(0, left, right)   
                        res.append(root)

            memo[n] = res
            return res
 
        return backtracking(n)
         
