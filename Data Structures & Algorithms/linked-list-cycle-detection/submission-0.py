# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #have a fast node skipping two nodes at a time 
        # and have a slow node skipping one node at a time
        # if the fast node overtakes the slower node, then we know we are in a 
        #loop. 
        slow = head
        fast = head

        while slow != None and fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast :
                return True
        
        return False    