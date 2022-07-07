# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        # don't connect dummy to head yet, because the head might be duplicate
        prev = dummy
        curr = head
        tail = dummy
        
        while curr:
            if (prev == dummy or prev.val != curr.val) and (curr.next == None or curr.val != curr.next.val):
                tail.next = curr
                tail = curr
            prev = curr
            curr = curr.next
            # disconnect prev and curr to avoid edge cases like 1->2->2
            prev.next = None
        
        return dummy.next