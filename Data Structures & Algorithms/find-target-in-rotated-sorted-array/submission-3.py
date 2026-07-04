class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (r - l)//2

        while l <= r: 
            mid = l + ((r - l) // 2)

            if target == nums[mid] :
                return mid

            elif nums[l] <= nums[mid]: 
                #then, left side of the array is sorted. 
                if target < nums[mid] and target >= nums[l] :
                    #if target falls between the sorted section of the array
                    r = mid - 1
                else: 
                    #it doesnt matter if left side is sorted, its not within that range so it must be on right.
                    l = mid + 1
            else :
                #left side of array isnt sorted; right side must be sorted
                if target > nums[mid] and target <= nums[r] :
                    #target falls btwn mid and right side (sorted part of array)
                    l = mid + 1
                else: 
                    r = mid - 1
      

        return -1