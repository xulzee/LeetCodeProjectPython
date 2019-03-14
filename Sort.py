# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 22:36
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : Sort.py
# @Software: PyCharm
import random


class Solution:
    def swap(self, array: list, i, j):
        if i == j:
            return
        array[i] = array[i] ^ array[j]
        array[j] = array[i] ^ array[j]
        array[i] = array[i] ^ array[j]

    def bubblesort(self, array: list):
        # 时间复杂度：O(n^2)  空间复杂度：O(1)
        for i in range(len(array)):
            for j in range(len(array) - 1, i, -1):
                if array[j] < array[j - 1]:
                    self.swap(array, j, j - 1)

    def insertsort(self, array: list):
        for i in range(1, len(array)):
            for j in range(i - 1, -1, -1):
                if array[j] > array[j + 1]:
                    self.swap(array, j, j + 1)
                else:
                    break

    def selectsort(self, array: list):
        # 时间复杂度：O(n^2)  空间复杂度：O(1)
        for i in range(len(array)):
            min = i
            for j in range(i + 1, len(array)):
                if array[j] < array[i]:
                    min = j
            if min != i:
                self.swap(array, min, i)

    def merge(self, array: list, L: int, R: int, mid: int):
        temp = [0] * (R - L + 1)
        p_l = L
        p_r = mid + 1
        i = 0
        while p_l <= mid and p_r <= R:
            if array[p_l] < array[p_r]:
                temp[i] = array[p_l]
                i += 1
                p_l += 1
            else:
                temp[i] = array[p_r]
                i += 1
                p_r += 1
        while p_l <= mid:
            temp[i] = array[p_l]
            i += 1
            p_l += 1

        while p_r <= R:
            temp[i] = array[p_r]
            i += 1
            p_r += 1

        for i in range(R - L + 1):
            array[L + i] = temp[i]

    def mergesort(self, array: list, L: int, R: int):
        # 时间复杂度：O(n^2)  空间复杂度：O(1) 最好的情况
        if L == R:
            return array[L]
        mid = (L + R) // 2
        self.mergesort(array, L, mid)
        self.mergesort(array, mid + 1, R)
        self.merge(array, L, R, mid)

    def smallsummerge(self, array: list, L: int, R: int, mid: int):
        temp = [0] * (R - L + 1)
        p_l = L
        p_r = mid + 1
        i = 0
        res = 0
        while p_l <= mid and p_r <= R:
            if array[p_l] < array[p_r]:
                res += array[p_l] * (R - p_r + 1)
                temp[i] = array[p_l]
                i += 1
                p_l += 1
            else:
                temp[i] = array[p_r]
                i += 1
                p_r += 1
        while p_l <= mid:
            temp[i] = array[p_l]
            i += 1
            p_l += 1

        while p_r <= R:
            temp[i] = array[p_r]
            i += 1
            p_r += 1

        for i in range(R - L + 1):
            array[L + i] = temp[i]
        return res

    def smallsum(self, array: list, L: int, R: int):
        if L == R:
            return 0
        mid = (L + R) // 2
        return self.smallsum(array, L, mid) + self.smallsum(array, mid + 1, R) + self.smallsummerge(array, L, R, mid)

    def quicksort(self, l: list):
        if l == None or len(l) < 2:
            return
        self.quicksortprocess(l, 0, len(l) - 1)

    def quicksortprocess(self, array: list, L: int, R: int):
        if L < R:
            pass
            self.swap(array, random.randint(L, R), R)
            res = self.quicksortpartition(array, 0, R)
            self.quicksortprocess(array, 0, res[0] - 1)
            self.quicksortprocess(array, res[1] + 1, R)

    def quicksortpartition(self, array: list, L: int, R: int):
        less = L - 1
        more = R
        while L < more:
            if array[L] < array[R]:
                self.swap(array, L, less + 1)
                less += 1
                L += 1
            elif array[L] > array[R]:
                self.swap(array, L, more - 1)
                more -= 1
            else:
                L += 1
        self.swap(array, R, more)
        return [less + 1, more]

    def heapsort(self, array: list):
        if array == None or len(array) < 2:
            return
        for i in range(len(array)):
            self.heapinsert(array, i)  # 大根堆

        size = len(array) - 1
        self.swap(array, 0, size)

        while size > 0:
            self.heapify(array, 0, size)
            size -= 1
            self.swap(array, 0, size)

    def heapinsert(self, array: list, index: int):
        # parent_index = (index - 1) // 2
        while array[index] > array[int((index - 1) / 2)]:
            self.swap(array, index, int((index - 1) / 2))
            index = int((index - 1) / 2)

    def heapify(self, array: list, index: int, size: int):
        L = index * 2 + 1
        largest = 0
        while L < size:
            if L + 1 < size:
                if array[L] < array[L + 1]:
                    largest = L + 1
                else:
                    largest = L
            else:
                largest = L
            if array[index] > array[largest]:
                largest = index
            if largest == index:
                break
            self.swap(array, index, largest)
            index = largest
            L = index * 2 + 1


if __name__ == '__main__':
    for i in range(1000):
        test = [random.randint(0, 100) for j in range(200)]
        x = test.copy()
        # print(test)
        # test = [40, 37, 90, 69, 91, 67, 78, 18, 15, 42, 88, 10, 76, 85, 97, 57, 60, 7, 99, 19]
        Solution().bubblesort(test)
        x = sorted(x)
        if x != test:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            print(test)
            print(x)
