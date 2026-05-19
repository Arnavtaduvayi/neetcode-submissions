class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for each in s :
            if each == "(" or each == "{" or each == "[" :
                stack.append(each)
            elif stack: 
                hold = stack.pop()
                if hold == "(" and not (each == ")") :
                    return False
                elif hold == "[" and not (each == "]") :
                    return False
                elif hold == "{" and not (each == "}") :
                    return False
            else: 
                return False


        if not stack : 
            return True
        else: 
            return False