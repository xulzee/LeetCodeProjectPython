# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 0:09
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 98. Validate Binary Search Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root: TreeNode, lower, upper):
        if root == None:
            return True
        if root.val >= upper or root.val <= lower:
            return False
        return self.helper(root.left, lower, root.val) and self.helper(root.right, root.val, upper)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, float('-inf'), root.val) and self.helper(root.right, root.val, float('inf'))



    def inOrder(self, root: TreeNode, l: List):
        if root == None:
            return
        self.inOrder(root.left, l)
        l.append(root.val)
        self.inOrder(root.right, l)

    def isValidBST1(self, root: TreeNode) -> bool:
        if root == None:
            return True

        l = []
        self.inOrder(root, l)
        for i in range(1, len(l)):
            if l[i] <= l[i-1]:
                return False
        return True
