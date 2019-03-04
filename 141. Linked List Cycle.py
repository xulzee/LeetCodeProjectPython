# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 17:16
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 141. Linked List Cycle.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
