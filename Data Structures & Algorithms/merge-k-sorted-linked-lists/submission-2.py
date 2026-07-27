# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #put all in stack, then pop
        stack = []
        ctr = 0
        for head in lists :
            while not head == None :
                heapq.heappush(stack, head.val)
                head = head.next
                ctr += 1
        dummy = ListNode(0, None)
        curr = dummy
        for i in range (ctr) :
            curr.next = ListNode(heapq.heappop(stack), None)
            curr = curr.next
        return dummy.next
        
            