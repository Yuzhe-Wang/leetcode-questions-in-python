# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # idea: dfs
        if not root:
            return True
        
        def isSymmetric(left, right):
            if not left or not right:
                if not left and not right:
                    return True
                else:
                    return False
            else:
                if left.val != right.val:
                    return False
                else:
                    return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)
        
        return isSymmetric(root.left, root.right)