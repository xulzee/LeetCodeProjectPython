# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 0:06
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : Array To Queue.py
# @Software: PyCharm
class Solution:
    def __init__(self, size):
        self.array = [0] * size
        self.first = 0
        self.last = 0
        self.size = 0

    def peek(self):
        if self.size == 0:
            return None
        return self.array[self.first]

    def push(self, obj):
        if self.size == self.array:
            return "Stack is full"
        self.size += 1
        self.array[self.last] = obj
        if self.last == len(self.array) - 1:
            self.last = 0
        else:
            self.last = self.last + 1

    def poll(self):
        if self.size == 0:
            return "Stack is empty"
        self.size -= 1
        tmp = self.first
        if self.first == len(self.array) - 1:
            self.first = 0
        else:
            self.first += 1
        return self.array[tmp]
