# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead = ListNode()
        greatHead = ListNode()
        lessTail = lessHead
        greatTail = greatHead
        curr = head
        
        while curr:
            if curr.val < x:
                lessTail.next = curr
                curr = curr.next
                lessTail = lessTail.next
                lessTail.next = None
            else:
                greatTail.next = curr
                curr = curr.next
                greatTail = greatTail.next
                greatTail.next = None
        
        lessTail.next = greatHead.next
        return lessHead.next