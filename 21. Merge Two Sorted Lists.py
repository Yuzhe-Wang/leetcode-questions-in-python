# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None)
        curr = res
        while list1 != None or list2 != None:
            if list1 == None:
                curr.next = list2
                break
            elif list2 == None:
                curr.next = list1
                break
            else:
                a = list1.val
                b = list2.val
                if a <= b:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                    curr.next = None
                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
                    curr.next = None
        return res.next