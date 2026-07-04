class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (r-l)//2
        while l < r :
            #if you are in the smaller section of the array
            if nums[mid] < nums[r] :
                r = mid 
                mid = l + (r-l)//2
            else :
                l = mid + 1
                mid = l + (r-l)//2

        return nums[mid]