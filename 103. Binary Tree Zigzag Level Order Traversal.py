# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        result = []
        deque = collections.deque()
        deque.append(root)
        odd = True
        
        while deque:
            curr = []
            breadth = len(deque)
            for i in range(breadth):
                if odd:
                    front = deque.popleft()
                    curr.append(front.val)
                    if front.left:
                        deque.append(front.left)
                    if front.right:
                        deque.append(front.right)
                else:
                    front = deque.pop()
                    curr.append(front.val)
                    if front.right:
                        deque.appendleft(front.right)
                    if front.left:
                        deque.appendleft(front.left)
            odd = not odd
            result.append(curr.copy())
            
        return result