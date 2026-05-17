class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        track = Counter(s1)        

        for j in range (len(s2) - len(s1) + 1) :
            if Counter(s2[j:j+len(s1)]) == track :
                return True

        return False
