class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = 0

        while left <= right :
            mid = left + (right - left)//2
            print('jet')
            if nums[mid] >= nums[left] :
                #we are in sorted potion (to left) 
                if target >= nums[left] and target < nums[mid] :
                    right = mid - 1
                else :
                    left = mid + 1
            else :
                #we are in sorted potion (to right) 
                if target > nums[mid] and target <= nums[right] :
                    left = mid + 1
                else :
                    right = mid - 1

            if nums[mid] == target :
                return mid
     
        return -1