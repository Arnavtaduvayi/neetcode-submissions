class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #make two new lists, one with all the products from the left to right
        #and another one with all the products from the right to left. 
        #when looking at a number, just multiply the i-1 for the left array 
        #and the i+1 for the right array. 

        larry = []
        rarry = [0] * len(nums)
        output = []
        lsum = 1
        for i in range (len(nums)) :
            lsum *= nums[i]
            larry.append(lsum)
        
        lsum = 1
        for i in range (len(nums) - 1, -1, -1) :
            lsum *= nums[i]
            rarry[i] = lsum

        for i in range(len(nums)) :
            if (i + 1) >= len(nums) :
                output.append(larry[i-1])
            elif (i-1) < 0 :
                output.append(rarry[i+1])
            else :
                output.append(larry[i-1] * rarry[i+1])

        return output