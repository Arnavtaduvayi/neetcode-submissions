class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smap = {}
        hNum = 0
        i=0
        for j in range(len(s)):
            if s[j] not in smap :
                smap[s[j]] = j
            else:
                i = max(smap[s[j]]+1, i)
                smap[s[j]] = j
            if (j-i)+1 > hNum :
                hNum = (j-i)+1
        return hNum