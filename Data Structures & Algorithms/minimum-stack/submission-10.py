class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        elif val < self.min:
            self.min, val = val, 2*val - self.min
        self.stack.append(val)
        
    def pop(self) -> None:
        popped = self.stack.pop()

        if len(self.stack) == 0:
            self.min = None
        elif popped < self.min:
            self.min = 2*self.min - popped
        
    def top(self) -> int:
        top = self.stack[-1]

        if top < self.min:
            top = self.min

        return top
        
    def getMin(self) -> int:
       return self.min