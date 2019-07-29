# # # -*- coding: utf-8 -*-
# # # @Time    : 2019/2/28 14:55
# # # @Author  : xulzee
# # # @Email   : xulzee@163.com
# # # @File    : 242. Valid Anagram.py
# # # @Software: PyCharm
# # from typing import List
# #
# #
# # # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
# #
# #
# # class Solution:
# #     def reverseList(self, head: ListNode) -> ListNode:
# #         pre_node = head
# #         head = head.next
# #         next_node = head.next
# #         while head.next != None:
# #             head.next = pre_node
# #             pre_node = head
# #             head = next_node
# #             next_node = next_node.next
# #         head.next = pre_node
# #         return head
# #
# #
# #
# # if __name__ == '__main__':
# #     numbers = [1, 2, 3, 4, 5]
# #     # Now convert that list into linked list
# #     dummyRoot = ListNode(0)
# #     ptr = dummyRoot
# #     for number in numbers:
# #         ptr.next = ListNode(number)
# #         ptr = ptr.next
# #
# #     ptr = dummyRoot.next
# #     Solution().reverseList(ptr)
# #     pass
# #
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
#         if head is not None and head.next is not None:
#             last_node = None
#             while head != None:
#                 next_node = head.next
#                 head.next = last_node
#                 last_node = head
#                 head = next_node
#             return last_node
#         return head
#
#
# def stringToListNode():
#     # Generate list from the input
#     numbers = [1, 2, 3, 4, 5]
#
#     # Now convert that list into linked list
#     dummyRoot = ListNode(0)
#     ptr = dummyRoot
#     for number in numbers:
#         ptr.next = ListNode(number)
#         ptr = ptr.next
#
#     ptr = dummyRoot.next
#     return ptr
#
#
# def listNodeToString(node):
#     if not node:
#         return "[]"
#
#     result = ""
#     while node:
#         result += str(node.val) + ", "
#         node = node.next
#     return "[" + result[:-2] + "]"
#
#
# def main():
#     while True:
#         try:
#             head = stringToListNode();
#             print(head.val)
#             ret = Solution().reverseList(head)
#
#             out = listNodeToString(ret);
#             print(out)
#         except StopIteration:
#             break
#
#
# if __name__ == '__main__':
#     main()

class Solution:
    # n 个骰子 凑成 sum 有多少种方式
    def Process(self, n, sum):
        if n == 1 or sum == n:
            return 1
        if sum < n or sum > 6 * n or n < 0:
            return 0
        return self.Process(n - 1, sum - 1) + \
               self.Process(n - 1, sum - 2) + \
               self.Process(n - 1, sum - 3) + \
               self.Process(n - 1, sum - 4) + \
               self.Process(n - 1, sum - 5) + \
               self.Process(n - 1, sum - 6)

    def dynamicProcess(self, n):
        dp = [[0] * (6 * n + 1) for i in range(n + 1)]  # 第 0 行 没有意义，不使用
        # dp : (n + 1) 行， 6n + 1列
        dp[1][1:7] = [1] * 6  # n == 1
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):  # j : sum
                if j == i:
                    dp[i][j] = 1
                elif j == i + 1:
                    dp[i][j] = dp[i - 1][j - 1] + \
                               dp[i - 1][j - 2]
                elif j == i + 2:
                    dp[i][j] = dp[i - 1][j - 1] + \
                               dp[i - 1][j - 2] + \
                               dp[i - 1][j - 3]
                elif j == i + 3:
                    dp[i][j] = dp[i - 1][j - 1] + \
                               dp[i - 1][j - 2] + \
                               dp[i - 1][j - 3] + \
                               dp[i - 1][j - 4]
                elif j == i + 4:
                    dp[i][j] = dp[i - 1][j - 1] + \
                               dp[i - 1][j - 2] + \
                               dp[i - 1][j - 3] + \
                               dp[i - 1][j - 4] + \
                               dp[i - 1][j - 5]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + \
                               dp[i - 1][j - 2] + \
                               dp[i - 1][j - 3] + \
                               dp[i - 1][j - 4] + \
                               dp[i - 1][j - 5] + \
                               dp[i - 1][j - 6]
        return dp


if __name__ == '__main__':
    Solution().dynamicProcess(6)
