"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            level = len(queue)
            for i in range(level):
                front = queue.popleft()
                if i < level - 1:
                    front.next = queue[0]
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        return root