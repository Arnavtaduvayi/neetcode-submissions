class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap  = {}
        for each in strs :
            val = "".join(sorted(each))
            if val not in hmap :
                hmap[val] = []
                hmap[val].append(each)
            else:
                hmap[val].append(each)
        
        return list(hmap.values())