# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 22:20
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 21. Merge Two Sorted Lists.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        head = ListNode(0)
        now = head

        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                head.next = l2
                head = head.next
                l2 = l2.next
                continue
            if l2.val > l1.val:
                head.next = l1
                head = head.next
                l1 = l1.next
                continue

        while l1 != None:
            head.next = l1
            l1 = l1.next
            head = head.next

        while l2 != None:
            head.next = l2
            l2 = l2.next
            head = head.next

        return now.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        res = ListNode(0)

        if l1.val <= l2.val:
            res = l1
            res.next = self.mergeTwoLists(l1.next, l2)
        else:
            res = l2
            res.next = self.mergeTwoLists(l1, l2.next)

        return res





def stringToListNode(numbers):

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
            line = [1,2,4]
            l1 = stringToListNode(line);
            line = [1,3,4]
            l2 = stringToListNode(line);

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break
if __name__ == '__main__':
    main()

