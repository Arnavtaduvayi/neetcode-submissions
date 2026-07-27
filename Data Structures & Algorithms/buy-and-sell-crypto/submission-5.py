class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Start i and j at 0 and 1. If prices[j] is < prices[i] then i = j. calc max at 
        #each move

        i, j = 0, 1
        cmax = 0
        while i <= j and j < len(prices) :
            cmax = max(cmax, prices[j] - prices[i])
            if prices[j] < prices[i] :
                i = j
            else :
                j += 1
        return cmax