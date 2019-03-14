# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 11:25
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 102. Binary Tree Level Order Traversal.py
# @Software: PyCharm

# Definition for a binary tree node.
from typing import List
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = queue.Queue()
        q.put(root)
        while q.empty() == False:
            cur = []
            for i in range(q.qsize()):
                temp = q.get()
                cur.append(temp.val)
                if temp.left is not None:
                    q.put(temp.left)
                if temp.right is not None:
                    q.put(temp.right)
            res.append(cur)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        level = 0
        self.dfs(level, res, root)
        return res


    def dfs(self, level: int, result: List[List[int]], node: TreeNode):
        if node is not None:
            if level == len(result):
                result.append([])

            result[level].append(node.val)
            self.dfs(level + 1, result, node.left)
            self.dfs(level + 1, result, node.right)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)   # 得到一个二叉树

            ret = Solution().levelOrder(root)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
