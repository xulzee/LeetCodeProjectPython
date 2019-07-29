# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 19:41
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : qq.py
# @Software: PyCharm

# while True:
#     try:
#         n = int(input())
#         high = [0] * len(n)
#         for i in len(n):
#             high.append(int(input()))
#
#     except:
#         break

#
# # while True:
# #     try:
# import queue
# import sys
# q = queue.Queue()
# for i in sys.stdin:
#     number = int(i.split()[0])
#     for i in range(1, number + 1):
#         q.put(i)
#
#     first, second = 0, 0
#     flag = True
#     if q.qsize() == 1:
#         print(q.get(), end='')
#     while q.qsize() >= 2:
#         first = q.get()
#         if flag:
#             print(first, end='')
#             flag = False
#         else:
#             print("", first, end='')
#         second = q.get()
#         q.put(second)
#     print("", q.get())
#     break
#     # except:
#     #     break


# while True:
#     try:
#         N = int(input())
#         array = [0] * N
#         diff_array = [0] * N
#         corrd_array = [0] * N
#         temp = input().split()
#         for i in range(N):
#             array[i] = int(temp[i])
#
#         for right in range(1, N):
#             mins = abs(array[right] - array[0])
#             Coord = 0
#             for left in range(1, right):
#                 if abs(array[right] - array[left]) < mins:
#                     mins = abs(array[right] - array[left])
#                     Coord = left
#             diff_array[right] = abs(array[right] - array[Coord])
#             corrd_array[right] = Coord + 1
#         for j in range(1, N):
#             print(diff_array[j], corrd_array[j])
#
#
#     except:
#         break


def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j - 1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i - 1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    a = [1, 3]
    b = [2]
    print(median(a, b))
