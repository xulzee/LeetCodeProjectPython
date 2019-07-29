# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 16:37
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : pdd.py
# @Software: PyCharm

while True:
    try:
        s = list(input())
        m = [0] * 26
        n = [0] * len(s)
        for i in range(len(s)):
            s[i] = s[i].lower()
            m[ord(s[i]) - ord('a')] += 1
        pos = 0
        ans = 0

        for j in range(len(s)):
            temp = s[j]
            if m[ord(temp)-ord('a')] == 1:
                if s[j] < s[pos]:
                    pos = j
                    break
            elif m[ord(temp)-ord('a')] == 2:
                if s[j] < s[pos]:
                    pos = j
        print(s[pos])











        d = {}
        for i in range(len(s)):
            s[i] = s[i].lower()

        for j in range(len(s)):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1

        pos = 0
        flag = False
        while True:
            if d[s[pos]] == 1:
                break
            else:
                flag = False
                for x in range(pos + 1, len(s)):
                    if s[x] < s[pos]:
                        pos = x
                        flag = True
                        break
                if not flag:
                    break

        print(s[pos])
    except:
        break

