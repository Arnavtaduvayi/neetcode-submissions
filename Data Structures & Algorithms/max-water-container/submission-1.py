class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0

        i = 0
        j = len(heights) - 1

        while i < j :
            lower = heights[i]
            if heights[j] < heights[i] : 
                lower = heights[j]
            area = (j-i) * lower
            if area > highest :
                highest = area

            if lower == heights[i] :
                i += 1
            else : 
                j -= 1

        return highest