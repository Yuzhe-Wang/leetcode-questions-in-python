# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(curr):
            if not curr.left:
                return curr
            
            newRoot = dfs(curr.left)
            curr.left.left = curr.right
            curr.left.right = curr
            curr.left = None
            curr.right = None
            return newRoot
        
        if not root:
            return None
        return dfs(root)