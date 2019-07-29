# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : Graph.py
# @Software: PyCharm


class Node:
    def __init__(self, value):
        self.value = value
        self.inDegree = 0
        self.outDegree = 0
        self.nextNodes = []
        self.edges = []


class Edge:
    def __init__(self, weight):
        self.weight = weight
        self.fromNode = None
        self.toNode = None


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []


