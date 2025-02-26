class MinStack:

    def __init__(self):
        self.stack = []
        self.minAtMoment = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minAtMoment) == 0 or val < self.minAtMoment[-1]:
            minValue = val
        else:
            minValue = self.minAtMoment[-1]
        self.minAtMoment.append(minValue)

    def pop(self) -> None:
        self.minAtMoment.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minAtMoment[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()