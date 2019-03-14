# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 14:35
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 101. Symmetric Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if (left is None and right != None) or (left != None and right == None) or (left.val != right.val):
            return False
        return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)

    def isSymmetric1(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        q = []
        q.append(root)
        q.append(root)
        while len(q) != 0:
            left = q.pop(0)
            right = q.pop(0)
            if left is None and right is None:
                continue
            if (left is None and right is not None) or (left is not None and right is None) or (left.val != right.val):
                return False
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True
