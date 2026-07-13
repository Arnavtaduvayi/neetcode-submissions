class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #have i and j = 0, 1 ; if prices[j] < prices[i] then i = j
        #keep j moving otherwise; we want the smallest for i ; calculate maxp along the way

        i, j = 0, 1

        maxp = 0

        while j < len(prices) :
            maxp = max(maxp, prices[j] - prices[i])
            if prices[j] < prices[i] :
                i = j
            else :
                j += 1
        return maxp