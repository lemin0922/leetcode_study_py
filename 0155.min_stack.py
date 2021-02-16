class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = 2 ** 31 - 1
        self.min_index = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_value > x:
            self.min_value = x
            self.min_index = -1
        else:
            self.min_index -= 1

    def pop(self) -> None:
        del self.stack[-1]
        self.min_index += 1
        if self.min_index == 0 and len(self.stack) > 0:
            self.min_value = min(self.stack)
            idx = self.stack.index(self.min_value)
            self.min_index = idx - len(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_index]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()