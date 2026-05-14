class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        hSum = 0

        while j != len(prices) :
            if prices[j] - prices[i] > hSum :
                hSum = prices[j]-prices[i]

            if prices[j]-prices[i] < 0 :
                i+= 1
            elif prices[j]-prices[i] >= 0 :
                j += 1
        return hSum