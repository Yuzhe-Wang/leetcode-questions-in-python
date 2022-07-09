'''
pseudo-code template for building BSTs
left = dfs()
right = dfs()
for l in left:
    for r in right:
        root.left = l
        root.right = r
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = list(range(1, n+1))
        
        def dfs(nums):
            # base case:
            if not nums:
                return [None]
            
            # recurrsive step:
            result = []
            for i in range(len(nums)):
                left = dfs(nums[:i])
                right = dfs(nums[i+1:])
                for l in left:
                    for r in right:
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        result.append(root)
            return result
    
        return dfs(nums)