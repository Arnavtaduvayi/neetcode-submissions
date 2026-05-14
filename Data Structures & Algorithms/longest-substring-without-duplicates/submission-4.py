class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hNum = 0
        num = 0
        LSI = {}
        i=0
        for j in range (len(s)) :
            if s[j] in LSI :
                i = max(LSI[s[j]] + 1, i)
                LSI[s[j]] = j
            else :
                LSI[s[j]] = j
            
            num = (j-i) + 1

            if num > hNum :
                hNum = num
        return hNum
            