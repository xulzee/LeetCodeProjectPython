# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 20:18
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : JD.py
# @Software: PyCharm


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        path = []
        sum = 0
        self.FindPathCore(root, expectNumber, path, sum)
        return sorted(self.res, key=lambda x: -len(x))

    def FindPathCore(self, root, expectNumber, path, sum):
        sum += root.val
        path.append(root.val)
        isLeaf = root.right is None and root.left is None
        if sum == expectNumber and isLeaf:
            self.res.append(path[:])
        if root.left:
            self.FindPathCore(root.left, expectNumber, path, sum)
        if root.right:
            self.FindPathCore(root.right, expectNumber, path, sum)
        # sum -= path[-1]
        path.pop()


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(4)
    print(Solution().FindPath(root, 22))
