class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #i iterating through list in outer for loop 
        #j is i+1
        #k is at the end of list
        #move k-- if number is >0
        #move j++ if number <0
        #once we have a solution, add it to output, and then keep iterating j until it isnt
        #the same value as j-1
        nums.sort()
        output = []
        for i in range (len(nums)) :
            if i > 0 and nums[i-1] == nums[i] :
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k :
                if nums[i] + nums[j] + nums[k] > 0: 
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0: 
                    j += 1
                else :
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while (nums[j-1] == nums[j]) and j < k :
                        j += 1
                    k -= 1

        return output