class MinStack:

    def __init__(self):
        self.stack = []
        self.minPref = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minPref[-1] if self.minPref else val)
        self.minPref.append(val)
        
    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack)-1]
        self.minPref = self.minPref[:len(self.minPref)-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minPref[-1]
