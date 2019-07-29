# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 17:07
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : pdd2.py
# @Software: PyCharm


while True:
    try:
        n, d = map(int, input().split())
        hash = {}
        road = {}
        result = []
        for i in range(n):
            a, b = map(int, input().split())
            hash[a] = b
            road[i+1] = a
        for j in range(1, n+1):
            for k in range(j+1, n+1):
                if road[k] - road[j] > d:
                    result.append(hash[road[k]] + hash[road[j]])
        print(max(result))
    except:
        break
