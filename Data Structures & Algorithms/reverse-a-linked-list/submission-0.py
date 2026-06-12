# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return head
        elif head.next is None :
            return head
        n = head.next
        c = head
        p = None
        ct = 0

        while c is not None :
            n=c.next
            c.next = p
            p=c
            c=n
            
        head = p
        return head