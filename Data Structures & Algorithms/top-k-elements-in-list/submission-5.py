class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         #can use bucket sort type thing. Since the most amount of times 
         # a number can show up is len(nums) times, we make a frequency array 
         #where each index is hwo many times a number has shown up. Then, just go backwards
         #until you find the one k away from the end. 

         #OR, use a hashmap; track how many occurances of each element, then use 
         #occurances as a weight in a pq. Pop from pq k times

        hmap = Counter(nums)
        hp = []

        for key, val in hmap.items():
            heapq.heappush(hp, (-val, key))
        
        res = []

        for i in range(k):
            val, ans = heapq.heappop(hp)
            res.append(ans)
        
        return res
        
        
