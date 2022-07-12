# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        # get the middle node
        mid = self.partition(head)
        
        # get the left portion of the list
        prev = head
        if prev == mid:
            head = None
        else:
            while prev.next and prev.next != mid:
                prev = prev.next
            prev.next = None 

        # pass in the left side of the list to get the left subtree
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        
        # pass in the right side of the list to get the right subtree
        nextHead = mid.next
        mid.next = None
        root.right = self.sortedListToBST(nextHead)
        return root
        
    # helper function for getting the middle node of a linked list
    def partition(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow