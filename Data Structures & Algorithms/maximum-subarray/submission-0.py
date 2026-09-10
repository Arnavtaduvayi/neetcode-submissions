class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute force would mean trying every possible combination 
        # sliding window
        # start at i,j = 0,1 
        # move j by 1 and track sum using var currsum
        # if nums[j] >= currsum move i = j
        # also use a maxsum var to keep track of the highest sum we saw

        i, j = 0, 0
        currsum = nums[0]
        maxsum = currsum
        
        while (j < len(nums) - 1) :
            j += 1
            currsum += nums[j]
            if nums[j] > currsum :
                i = j
                currsum = nums[j]
            maxsum = max(currsum, maxsum)

        return maxsum

        #cs = 8
        #ms = 8
        #i = 2
        #j = 7