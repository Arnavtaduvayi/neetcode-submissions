class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}

        for each in s:
            if each not in mapS:
                mapS[each] = 1
            else:
                mapS[each] += 1

        for each in t:
            if each not in mapT:
                mapT[each] = 1
            else:
                mapT[each] += 1

        return mapS == mapT