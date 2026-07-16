class MedianFinder:

    def __init__(self):
        self.big = []
        self.small = []

    def addNum(self, num: int) -> None:
        #small is a maxheap, big is a minheap. We want half of the elements in each
        #All elemnts in small are smaller than big. just peek at both top elements and 
        #if small[0] is greater than big[0], then put small[0] into big. 
        #Need to readjust the number of nums in each heap - if there is more in big, then 
        #pop and add to small - do same for opposite. 

        heapq.heappush(self.small, -num)

        if self.small and self.big and (- self.small[0] > self.big[0]):
            heapq.heappush(self.big, - heapq.heappop(self.small))
        if len(self.small) - len(self.big) > 1 :
            heapq.heappush(self.big, - heapq.heappop( self.small))
        elif len(self.big) - len(self.small) > 1 :
            heapq.heappush(self.small, - heapq.heappop(self.big))

    def findMedian(self) -> float:
        # you have size. Just peek at the heap with more if odd, otherwise, peek at both and 
        #find avg of those two

        if (len(self.big) + len(self.small)) % 2 == 0 :
            return ( - self.small[0] + self.big[0]) / 2
        else :
            if len(self.small) > len(self.big) :
                return - self.small[0]
            else :
                return self.big[0]