# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 23:28
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : Array To Stack.py
# @Software: PyCharm
class Solution:
    def __init__(self, size):
        self.array = [0] * size
        self.size = 0

    def peek(self):
        if self.size == 0:
            return None
        return self.array[self.size - 1]

    def push(self, obj):
        if self.size == len(self.array):
            return "Stack is full"
        self.array[self.size] = obj
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Stack is empty"
        self.size -= 1
        return self.array[self.size]