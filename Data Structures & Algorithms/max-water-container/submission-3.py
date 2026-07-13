class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #start i,j on either side, calc the water for each iteration, and move the lower bar
        # inwards since thats the limiting reactant. 

        i=0
        j= len(heights) - 1

        maxw = 0

        while i < j :
            maxw = max(maxw, ((j - i) * (min(heights[i], heights[j]))))

            if heights[i] <= heights[j] :
                i += 1
            else :
                j -= 1

        return maxw
        