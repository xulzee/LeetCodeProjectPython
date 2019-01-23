class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        output = [[1]]
        lastline = [1]
        for i in range(1, numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(lastline[j] + lastline[j-1])
            lastline = temp
            output.append(temp)
        return output


if __name__ == '__main__':
    N = 5
    print(Solution().generate(5))
