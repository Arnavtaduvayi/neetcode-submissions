class Solution:
    def findMin(self, nums: List[int]) -> int:
        #One half MUST be sorted. do you store the first in the sorted side and 
        #look at the opposite of the sorted side? And then eventually youll find the one? 
        # must account for edge case of if it rotates 0 times (both sides sorted)

        l = 0
        r = len(nums) - 1
        m = l + ((r-l)//2)
        smallest = float('inf')
        while l <= r : 
            if nums[m] < nums[r] :
                if nums[l] < nums[m] : 
                    return nums[l]
                else :
                    smallest = min(smallest, nums[m])
                    r = m - 1 
                    m = l + ((r-l)//2)
            else :
                smallest = min(smallest, nums[m])
                l = m + 1
                m = l + ((r-l)//2)

        return smallest