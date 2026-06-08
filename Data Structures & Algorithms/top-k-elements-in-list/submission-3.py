import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for each in nums: 
            if each in hmap:
                hmap[each] += 1
            else: 
                hmap[each] = 0
        
        arr = []
        for key, value in hmap.items():
            arr.append((-1 * value,key))
        
        heapq.heapify(arr)

        res = []

        for each in range(k) :
            value, key = heapq.heappop(arr)
            res.append(key)
        
        return res