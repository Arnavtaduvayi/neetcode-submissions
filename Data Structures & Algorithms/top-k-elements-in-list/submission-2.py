class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        heap = []
        ans = []
        for each in nums :
            if each in counts :
                counts[each] += 1
            else :
                counts[each] = 1
        for x in counts :
            send = (-counts[x], x)
            heapq.heappush(heap, send)
        
        for i in range (k) :
            ans.append(heapq.heappop(heap)[1])

        return ans