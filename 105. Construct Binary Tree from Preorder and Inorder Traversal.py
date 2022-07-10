# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. for preorder traversal, the first element is always the root
        # 2. in the inorder traversal, all the element to the left of the root are in the left subtree, and everything to the right of the root are in the right subtree
        # base case:
        if not preorder or not inorder:
            return None
        
        # recurrsive step
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+mid], inorder[:mid])
        root.right = self.buildTree(preorder[1+mid:], inorder[mid+1:])
        return root