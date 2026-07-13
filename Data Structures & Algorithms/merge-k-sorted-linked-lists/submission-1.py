# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #could add all to a heapq, but that is O(n*logn)

        dummy = ListNode(0, None)

        hep = []

        #iterate through all the heads
        for each in lists :
            while not (each == None) :
                heapq.heappush(hep, each.val)
                each = each.next
        curr = dummy

        for i in range(len(hep)) :
            curr.next = ListNode(heapq.heappop(hep))
            curr = curr.next
        return dummy.next
