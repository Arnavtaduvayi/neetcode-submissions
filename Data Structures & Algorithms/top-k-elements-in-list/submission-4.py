import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #add all to hmap, then go through hmap and add them all to a pq, pop the amount of times needed.

        hmap = {}

        for each in nums :
            if each not in hmap :
                hmap[each] = 1
            else: 
                hmap[each] += 1
        
        pq = []

        for key, val in hmap.items() :

            heapq.heappush(pq, (-val, key))

        output = []

        for i in range(k) :
            val, key = heapq.heappop(pq)
            output.append(key)

        return output