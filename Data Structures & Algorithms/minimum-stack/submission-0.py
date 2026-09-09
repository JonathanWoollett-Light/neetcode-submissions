class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.ordered) > 0: self.ordered.append(min(self.ordered[-1],val))
        else: self.ordered.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.ordered.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ordered[-1]
        
