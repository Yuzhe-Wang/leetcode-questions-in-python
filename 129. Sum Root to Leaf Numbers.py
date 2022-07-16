# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def dfs(node, curr):
            nonlocal result
            # base case:
            if not node.left and not node.right:
                curr = curr*10 + node.val
                result += curr
                return
            
            # recurrsive steps:
            if node.left:
                dfs(node.left, curr*10 + node.val)
            if node.right:
                dfs(node.right, curr*10 + node.val)
                
        dfs(root, 0)
        return result