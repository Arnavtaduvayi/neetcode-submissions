class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapx = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mapx:
                return [mapx[comp], i]
            else: 
                mapx[nums[i]] = i
        