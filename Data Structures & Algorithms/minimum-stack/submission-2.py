class MinStack:

    def __init__(self):
        self.stack = []
        self.minPref = []
        self.currMin = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.currMin is None) or (val < self.currMin):
            self.currMin = val
            print(self.currMin)
        
        self.minPref.append(self.currMin)
        
    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack)-1]
        self.minPref = self.minPref[:len(self.minPref)-1]
        if len(self.minPref) > 0:
            self.currMin = self.minPref[-1]
        else:
            self.currMin = None
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin
