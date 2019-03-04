# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 10:55
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 234. Palindrome Linked List.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> bool:
        if head == None or head.next == None :
            return head

        t = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return t

    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        if fast.next != None:
            slow = slow.next

        slow = self.reverseList(slow)

        while slow != None:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True



def stringToListNode(numbers):

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def main():
    while True:
        try:
            line = [1,0,1]
            head = stringToListNode(line);

            ret = Solution().isPalindrome(head)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
