# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        
        # move curr to the position of left
        count = 1
        while count < left:
            curr = curr.next
            prev = prev.next
            count += 1
            
        # store the node of left and the node before left
        l = curr
        prevLeft = prev
        
        # reverse
        while count <= right:
            temp = prev
            prev = curr
            curr = curr.next
            prev.next = temp
            count += 1
            
        # now prev points to right
        r = prev
        postRight = curr
        
        # connect the reversed part with the rest of the list
        l.next = postRight
        prevLeft.next = r
        return dummy.next