class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #start 0,1 if its negative, i jumps to j 
        #if i and j are the same, j moves to right
        #else, j moves right

        i,j = 0, 1
        maxp = 0
        for j in range(len(prices)):
            if prices[j] < prices[i] :
                i = j
            
            maxp = max(maxp, prices[j]-prices[i])

        return maxp