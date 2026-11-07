class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #O(n^2) solution to sort then 
        #have an outer loop starting at 
        #every index, i, and we have j = i+1 and k that starts at end
        #if the sum of i,j,k is > 0, we decrement k. if < 0, then inc j
        #if == 0, then add to output list 
        j = 0
        k = len(nums) - 1

        res = []
        nums.sort()

        for i in range(len(nums) - 2) :
            j = i + 1
            k = len(nums) - 1
            if i > 0 :
                if nums[i] == nums[i-1] :
                    continue

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum == 0 :

                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return res