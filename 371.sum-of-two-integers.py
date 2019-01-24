class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # python中一直左移是不会溢出的，所以要手动模拟32位int型
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        MASK = 0x100000000
        while b != 0:
            carry = (a & b) << 1  # 表示进位
            a = (a ^ b) % MASK  # 对其取余则将范围限制在[0,2^32-1]内，也就是int的范围
            b = carry % MASK  # 同理
        # 如果小于MAX_INT就不用处理了，如果溢出就要：
        # 以4位bit为例，从0000-1111，可以表示的范围为[0,15]，如果计算出16那就是溢出了，
        # 16是10000，此时的MIN_4BIT为16，取余为0，0000异或1111为1111再取反就是0了，
        # 将范围限制在了4位bit的范围内
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

if __name__ == '__main__':
    a = -1
    b = 1
    print(Solution().getSum(a, b))
