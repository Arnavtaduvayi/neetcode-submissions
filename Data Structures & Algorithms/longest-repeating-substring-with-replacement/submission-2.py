class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {}
        i=0
        res = 0
        for j in range(len(s)):
            if s[j] not in table: 
                table[s[j]] = 1
            else:
                table[s[j]] += 1
            highest = -1
            for each in table.values() :
                highest = max(each, highest)
            if ((j-i + 1) - highest > k) :
                table[s[i]] -= 1
                i += 1
            res = max(res, j-i + 1)

        return res