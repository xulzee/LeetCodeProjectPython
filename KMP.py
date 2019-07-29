# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : KMP.py
# @Software: PyCharm


def get_next(s: 'str'):
    next_list = [-1] * len(s)
    i, j = 0, -1
    while i < len(s) - 1:
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            if s[i] == s[j]:
                next_list[i] = next_list[j]
            else:
                next_list[i] = j
        else:
            j = next_list[j]
    return next_list


def index_kmp(s: 'str', t: 'str'):
    i, j = 0, 0
    next_list = get_next(t)
    while i < len(s) and j < len(t):
        if j == -1 or s[i] == t[j]:
            j += 1
            i += 1
        else:
            j = next_list[j]
    if j >= len(t):
        return i - len(t)
    else:
        return -1


def isPalindrome(s):
    if not len(s):
        return True
    s = "".join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


if __name__ == '__main__':
    s = input()
    if len(s) % 2 != 0:
        print(len(s))
    else:
        slow = 0
        fast = len(s) // 2
        while fast < len(s):
            if s[fast] != s[slow]:
                break
            fast += 1
            slow += 1
        if fast < len(s) - 1:
            print(len(s))
        else:
            print(len(s) // 2)
    # s = input()
    # t = input()
    # n = int(input())
    # for i in range(n):
    #     str_in = input().split()
    #     left, right = int(str_in[0]) - 1, int(str_in[1])
    #     count = 0
    #     temp = s[left:right]
    #     while (True):
    #         ret = index_kmp(temp, t)
    #         if ret != -1:
    #             count += 1
    #             left = ret + len(t)
    #             temp = temp[left:]
    #         else:
    #             break
    #     print(count)
