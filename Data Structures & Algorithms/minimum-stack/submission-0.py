class MinStack:

    def __init__(self):
        self.stack = [] 
        self.stack1 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack1 : 
            self.stack1.append(min(val, self.stack1[-1]))
        else : 
            self.stack1.append(val)
            

    def pop(self) -> None:
        self.stack.pop()
        self.stack1.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack1[-1]
