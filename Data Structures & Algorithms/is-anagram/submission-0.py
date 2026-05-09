class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mySet = {}

        for i in range(1, len(s)+1):
            key = s[i-1:i]
            if key in mySet:
                mySet[key] = mySet[key] + 1
            else:
                mySet[key] = 1
        
        for i in range(len(t)):
            if t[i] not in mySet:
                return False
            elif t[i] in mySet:
                mySet[t[i]] = mySet[t[i]] - 1
                if mySet[t[i]] <= 0 : 
                    del mySet[t[i]]
                
        return True

        