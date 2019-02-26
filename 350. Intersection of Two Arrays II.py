# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:16
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 350. Intersection of Two Arrays II.py
# @Software: PyCharm
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = {}
        result = []
        for i in nums1:
            record[i] = record.get(i, 0) + 1

        for i in nums2:
            if i in record and record[i] :
                result.append(i)
                record[i] -= 1

        return result


if __name__ == '__main__':
    A = [1,2,2,1]
    B = [2]
    print(Solution().intersect(A, B))
