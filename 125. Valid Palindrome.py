# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 23:53
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 125. Valid Palindrome.py
# @Software: PyCharm
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i].isalnum():
                stack.append(s[i].lower())
        j, k = 0, len(stack) - 1
        while j < k:
            if stack[j] != stack[k]:
                return False
            j += 1
            k -= 1
        return True


if __name__ == '__main__':
    A = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(A))
