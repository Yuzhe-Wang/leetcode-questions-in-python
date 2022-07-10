# solution #1: O(n) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # idea: to an inorder traversal and sort 
        temp = []
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            temp.append(node)
            inorder(node.right)
            
        inorder(root)
        
        sort = sorted(node.val for node in temp)

        for i in range(len(temp)):
            temp[i].val = sort[i]

# solution2: using constant space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # idea: do an inorder traversal and sort
        # to use constant memory, use a variable to store the last seen node
        
        lastSeen = None
        first = None
        second = None
        
        def dfs(node):
            if not node: return
            dfs(node.left)
            nonlocal lastSeen, first, second
            if (not lastSeen) or (node.val > lastSeen.val):
                lastSeen = node
            else:
                if not first:
                    first = lastSeen
                    second = node
                    lastSeen = node
                else:
                    second = node
                    return
            dfs(node.right)
        
        dfs(root)
        first.val, second.val = second.val, first.val
        return