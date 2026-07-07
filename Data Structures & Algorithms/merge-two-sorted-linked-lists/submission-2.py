# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make a dummy node, then use a while(?) to go through and see as long as each curr is not 
        # None, compare the values of both and whatever is less, put into the new dummy list. 

        dummy = ListNode(0)
        mcurr = dummy
        curr1 = list1
        curr2 = list2


        while curr1 or curr2 :
            if curr1 == None :
                while curr2 != None:
                    mcurr.next = curr2
                    mcurr = mcurr.next
                    curr2 = curr2.next
            elif curr2 == None :
                while curr1 != None:
                    mcurr.next = curr1
                    mcurr = mcurr.next
                    curr1 = curr1.next
            else :
                if curr1.val >= curr2.val :
                    mcurr.next = curr2
                    mcurr = mcurr.next
                    curr2 = curr2.next
                elif curr1.val < curr2.val :
                    mcurr.next = curr1
                    mcurr = mcurr.next
                    curr1 = curr1.next

        return dummy.next
