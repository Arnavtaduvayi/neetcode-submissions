class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #start i at idx len(nums), move goalpost towards left. If we can reach len(nums) using len(nums) - 1, then we only have to get to len(nums) - 1. Hence, goalpost shift.

        i = len(nums) - 2
        goalpost = len(nums) - 1
        
        while i >= 0:
            if i + nums[i] >= goalpost :
                goalpost = i
            i -= 1

        if goalpost == 0 :
            return True

        return False

