class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        sum = 0

        while l < r :
            if maxL > maxR :
                r -= 1
                if height[r] > maxR :
                    maxR = height[r]
                if maxR - height[r] > 0:
                    sum += maxR - height[r]
            else :
                l += 1
                if height[l] > maxL :
                    maxL = height[l]
                if maxL - height[l] > 0:
                    sum += maxL - height[l]

        return sum