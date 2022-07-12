# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque()
        odd = True
        
        if not root:
            return []
        
        queue.append(root)
        
        while queue:
            level = len(queue)
            curr = []
            for i in range(level):
                front = queue.pop()
                curr.append(front.val)
                if front.left:
                    queue.appendleft(front.left)
                if front.right:
                    queue.appendleft(front.right)
            result.insert(0, curr.copy())
            
        return result