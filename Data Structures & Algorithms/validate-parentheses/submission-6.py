class Solution:
    def isValid(self, s: str) -> bool:
        #add all possibilities to a hashmap, then if you see an opening char, expect the hmap 
        # value of that char to be the closing one. 

        hmap = {"(" : ")" , "{" : "}", "[" : "]"}
        tracker = []

        for each in s :
            if each == "(" or each == "{" or each == "[" :
                tracker.append(hmap[each])
            else :
                if not tracker :
                    return False
                if not (each == tracker.pop()) :
                    return False
        
        if tracker :
            return False
        else :
            return True