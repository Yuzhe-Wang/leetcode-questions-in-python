"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        newGraph = self.dfs(node, visited)
        return newGraph
    
    def dfs(self, node, visited):
        # base case:
        if not node:
            return None
        
        # recurrsive step:
        copy = Node(node.val)
        visited[node] = copy
        for neighbor in node.neighbors:
            if not neighbor in visited:
                copy.neighbors.append(self.dfs(neighbor, visited))
            else:
                copy.neighbors.append(visited[neighbor])
        return copy