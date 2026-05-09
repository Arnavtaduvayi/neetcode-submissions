class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [[] for i in range(len(nums) + 1)]
        maps = {}
        output = []

        for i in range(len(nums)):
        
            if nums[i] not in maps:
                maps[nums[i]] = 1
        
            elif nums[i] in maps:
                maps[nums[i]] += 1


        for num, count in maps.items():
            lst[count].append(num)            

        for i in range(len(nums), -1, -1):
            for each in lst[i]:
                output.append(each)
                if len(output) == k:
                    return output
