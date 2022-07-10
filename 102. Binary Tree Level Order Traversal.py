# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        result = []
        queue = []
        queue.append(root)
        
        while queue:
            breadth = len(queue)
            curr = []
            for i in range(breadth):
                front = queue.pop(0)
                curr.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            result.append(curr.copy())
        
        return result