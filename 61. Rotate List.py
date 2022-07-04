# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''idea: fast and slow pointers'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # use a fast and a slow pointer to find the pivot point
        fast = slow = head
        
        if head == None: 
            return head
        
        # count the length of the list
        n = 1
        temp = head
        while temp.next != None:
            temp = temp.next
            n += 1
        
        # reduce k
        k %= n
        if k == 0:
            return head
        
        for i in range(k):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        # now slow points to the one node before the pivot point and fast to the last node of the list
        # do the rotation
        result = slow.next
        slow.next = None
        fast.next = head
        return result
        