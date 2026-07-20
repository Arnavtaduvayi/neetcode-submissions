class MedianFinder:
    
    #smaller stack (maxheap), bigger stack(minheap)
    #have to balance it - if one stack has more than one extra, then balance it (pop and put in other)
    #have to make sure that the biggest in small is less than smallest in big. otherwise switch
    # can do len() on them since heaps are just lists


    def __init__(self):
        self.small = []
        self.big = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.big :
            if - self.small[0] > self.big[0] :
                heapq.heappush(self.big, - heapq.heappop(self.small))
        if len(self.small) > len(self.big) + 1 :
            heapq.heappush(self.big, - heapq.heappop(self.small))
        if len(self.big) > len(self.small) :
            heapq.heappush(self.small, -heapq.heappop(self.big))


    def findMedian(self) -> float:
        
        if len(self.small) > len(self.big) : 
            return - self.small[0]
        return (- self.small[0] + self.big[0]) / 2.0