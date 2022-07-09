# sulotion 1: recurrsive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(curr):
            # base case:
            if not curr:
                return
            
            # recurrsive steps:
            if curr.left:
                traverse(curr.left)
            result.append(curr.val)
            if curr.right:
                traverse(curr.right)
        
        traverse(root)
        return result

# solution 2: iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
            else:
                break
        return result