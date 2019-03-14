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
    print(next_list)
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
        return 0


if __name__ == '__main__':
    s, t = 'qwewacdabcasd', 'abc'
    print(index_kmp(s, t))
