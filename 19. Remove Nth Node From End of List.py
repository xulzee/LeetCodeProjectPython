# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 16:20
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 19. Remove Nth Node From End of List.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head
        slow = dummy_node
        fast = dummy_node
        while (fast.next != None):
            if n <= 0:
                slow = slow.next
            fast = fast.next
            n -= 1
        slow.next = slow.next.next
        return dummy_node.next


