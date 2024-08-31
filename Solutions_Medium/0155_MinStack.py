class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if self.data == []:
            self.data = [(val, None)]
        else:
            self.data.append((val, self.getMin()))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        if self.data[-1][1] is not None:
            return min(self.data[-1][0], self.data[-1][1])
        else:
            return self.data[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
