# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def dfs(root):
            if root is None:
                return

            dfs(root.left)
            nodes.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return nodes[k-1]



        # def dfs(root, k):
        #     if root is None:
        #         return 0
            
        #     left = abs(dfs(root.left,k))
        #     k -= 1
        #     print(k)
        #     if k == 0:
        #         res = root.val
        #         print("val "+str(root.val))
        #     right = abs(dfs(root.right,k))
        #     return k-right
        
        # dfs(root, k)
        # return res



        
        
