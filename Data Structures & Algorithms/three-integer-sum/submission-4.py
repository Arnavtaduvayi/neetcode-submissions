class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # im thinking same logic as twosumII but the target is -nums[i]
        # and i goes through every number in for loop
        nums.sort()
        answer = []
        for i in range(len(nums)) :
            if i > 0 and nums[i] == nums[i-1] :
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k :
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                    
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1 

                else: 
                    answer.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                         j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k-=1
            


        return answer
            
