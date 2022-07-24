# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # idea: preppend A to B and B to A so that they are of the same length, and use two pointers to step through and find the intersection
        first, second = headA, headB
        while first != second:
            first = first.next if first else headB
            second = second.next if second else headA
        return first