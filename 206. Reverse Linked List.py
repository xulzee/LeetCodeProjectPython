# # -*- coding: utf-8 -*-
# # @Time    : 2019/2/28 14:55
# # @Author  : xulzee
# # @Email   : xulzee@163.com
# # @File    : 242. Valid Anagram.py
# # @Software: PyCharm
# from typing import List
#
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre_node = head
#         head = head.next
#         next_node = head.next
#         while head.next != None:
#             head.next = pre_node
#             pre_node = head
#             head = next_node
#             next_node = next_node.next
#         head.next = pre_node
#         return head
#
#
#
# if __name__ == '__main__':
#     numbers = [1, 2, 3, 4, 5]
#     # Now convert that list into linked list
#     dummyRoot = ListNode(0)
#     ptr = dummyRoot
#     for number in numbers:
#         ptr.next = ListNode(number)
#         ptr = ptr.next
#
#     ptr = dummyRoot.next
#     Solution().reverseList(ptr)
#     pass
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is not None and head.next is not None:
            last_node = None
            while head != None:
                next_node = head.next
                head.next = last_node
                last_node = head
                head = next_node
            return last_node
        return head


def stringToListNode():
    # Generate list from the input
    numbers = [1,2,3,4,5]

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
    while True:
        try:
            head = stringToListNode();
            print(head.val)
            ret = Solution().reverseList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
