import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # could use PQ to just add all elements to it, but 
        #would be nlogn complexity, not n

        #The O(n) is definitely to do a merge sort type of algorithm

        mheap = []
        ct = 0

        for lst in lists :
            curr = lst
            while curr != None :
                heapq.heappush(mheap, (curr.val, ct, curr))
                curr = curr.next
                ct += 1
        

        dummy = ListNode(0)
        curr = dummy
        
        while mheap :
            val, ct, node = heapq.heappop(mheap)
            curr.next = node
            curr = curr.next

        return dummy.next