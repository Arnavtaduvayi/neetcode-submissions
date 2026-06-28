class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.replace(" ", "").lower()
        i = 0 
        j = len(t) - 1
    
        while i < j :
        
            if not t[i].isalnum():
                i += 1
                continue
            if not t[j].isalnum():
                j -= 1
                continue

            elif t[i] == t[j] :
                i += 1
                j -= 1
                continue
            else:
                return False

        return True