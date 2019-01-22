class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # for i in range(len(A)):
        #     for j in range(i, len(A)):
        #         if A[i] > A[j]:
        #             A[i] = A[i] ^ A[j]
        #             A[j] = A[i] ^ A[j]
        #             A[i] = A[i] ^ A[j]

        # A = sorted(A)
        # if A.count(A[len(A)//2]) > A.count(A[len(A)//2 - 1]):
        #     return A[len(A)//2]
        # else:
        #     return A[len(A)//2-1]

        tmp = set()
        for x in A:
            if x in tmp:
                return x
            else:
                tmp.add(x)


if __name__ == '__main__':
    A = [1,2,3,3]
    print(Solution().repeatedNTimes(A))
