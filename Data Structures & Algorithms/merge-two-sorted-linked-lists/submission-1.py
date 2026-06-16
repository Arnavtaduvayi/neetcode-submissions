# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #I need a dummy node to start the third list
        # and then I just traverse list 1 and list 2 and see
        #which node is smaller than the other. Based on that, 
        #I add the smaller node to my new lsit. 
        tail = ListNode()
        first = tail
        while list1 is not None or list2 is not None :
            if list1 is None :
                tail.next = list2
                list2 = list2.next
            elif list2 is None:
                tail.next = list1
                list1 = list1.next
            elif list1.val <= list2.val :
                tail.next = list1
                list1 = list1.next
            elif list1.val > list2.val :
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        return first.next