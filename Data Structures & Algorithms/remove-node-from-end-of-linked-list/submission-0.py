# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        while curr != None :
            curr = curr.next
            length += 1
        
        targ = length - n
      
        if targ == 0 :
            return head.next
      
        curr = head

        for i in range(targ-1) :
            curr = curr.next
        n = curr.next.next
        curr.next = n

        return head
        