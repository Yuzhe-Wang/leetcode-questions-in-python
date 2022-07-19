"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # idea: dfs with a set of already created nodes
        visited = {}
        newHead = self.dfs(head, visited)
        return newHead
        
    def dfs(self, node, visited):
        # base case:
        if not node:
            return None
        
        # recurrsive steps:
        if node in visited:
            return visited[node]
        else:
            currCopy = Node(node.val)
            visited[node] = currCopy
            currCopy.next = self.dfs(node.next, visited)
            currCopy.random = self.dfs(node.random, visited)
            return currCopy