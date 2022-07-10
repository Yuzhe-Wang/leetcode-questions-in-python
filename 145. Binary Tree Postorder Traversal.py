# solution 1: recurrsion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
            
        dfs(root)
        return result

# solution 2: iterative
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        result = []
        stackA = []
        stackB = []
        stackA.append(root)
        while stackA:
            curr = stackA.pop()
            stackB.append(curr)
            if curr.left:
                stackA.append(curr.left)
            if curr.right:
                stackA.append(curr.right)
        
        while stackB:
            top = stackB.pop()
            result.append(top.val)
        
        return result