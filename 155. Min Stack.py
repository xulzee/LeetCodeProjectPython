# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 13:53
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 155. Min Stack.py
# @Software: PyCharm

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            if self.min_stack[-1] > x:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return 0
        return self.min_stack[-1]

if __name__ == '__main__':
# Your MinStack object will be instantiated and called as such:
    x = 1
    obj = MinStack()
    obj.push(x)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
