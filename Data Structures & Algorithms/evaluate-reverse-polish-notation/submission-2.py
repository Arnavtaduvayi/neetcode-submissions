import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opmap = {"+" : operator.add, 
                "-" : operator.sub, 
                "*" : operator.mul, 
                "/" : operator.truediv
        }

        for each in tokens :
            if not (each == "+" or each == "-" or each == "*" or each == "/") :
                stack.append(int(each))
            else :
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(opmap[each](num2, num1)))
        return stack.pop()

