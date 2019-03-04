# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:26
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 237. Delete Node in a Linked List.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def stringToListNode(nums):
    # Generate list from the input
    numbers = nums

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    try:
        line = [1, 2, 3]
        node = stringToListNode(line)
        n = 1

        ret = Solution().deleteNode(node, n)

        out = listNodeToString(node)
        if ret is not None:
            print("Do not return anything, modify node in-place instead.")
        else:
            print(out)
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
