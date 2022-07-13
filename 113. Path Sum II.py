# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return None
        result = []
        self.dfs(root, targetSum, [], result)
        return result
    
    def dfs(self, node, targetSum, curr, result):
        # base case:
        if not node:
            return
        if node.val == targetSum and not node.left and not node.right:
            curr.append(node.val)
            result.append(curr.copy())
            curr.pop()
            return
        if node.val != targetSum and not node.left and not node.right:
            return
        
        # recurrsive steps
        curr.append(node.val)
        if node.left:
            self.dfs(node.left, targetSum - node.val, curr, result)
        if node.right:
            self.dfs(node.right, targetSum - node.val, curr, result)
        curr.pop()