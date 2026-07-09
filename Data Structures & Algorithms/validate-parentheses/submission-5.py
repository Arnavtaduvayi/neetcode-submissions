class Solution:
    def isValid(self, s: str) -> bool:
        # have a hashmap with the parenthesis as key and the closing one as value
        # add whatever opening parenthesis to stack. once you come across a closing 
        #parenthesis, 

        stack = []
        hmap = {"(" : ")" , "{" : "}", "[" : "]"}
        
        for each in s: 
            if each == "(" or each == "{" or each =="[" :
                stack.append(hmap[each])
            else :
                if stack and (each == stack.pop()) :
                    continue
                else :
                    return False
        
        if stack :
            return False
        else: 
            return True