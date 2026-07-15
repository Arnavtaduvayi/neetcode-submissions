class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        #have one pointer moving through list, one at front, and one at end. 
        # if the total is too high, move the end pointer to the left
        #if the total is too low, move the front pointer to the right. 
        #keep going for all iterations and whenever we get ==0, add to a list as a list

        ans = []
        nums.sort()
        hset = {}

        for j in range(len(nums)) :
            i, k = j + 1, len(nums)-1
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            while i < k :
                if nums[i] + nums[j] + nums[k] > 0 :
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0 :
                    i += 1
                else :
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    while i < k and nums[i] == nums[i - 1] :
                        i += 1
        return ans