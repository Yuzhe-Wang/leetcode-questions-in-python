# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """ 
        self.helper(root)
    
    # helper function, returns a pointer to the last node in the flattened linked list
    def helper(self, node):
        if not node:
            return None
        
        leftTail = self.helper(node.left)
        rightTail = self.helper(node.right)
        
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        
        last = rightTail or leftTail or node
        return last