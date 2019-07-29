def LastRemaining_Solution(n, m):
    # write code here
    # 所有人入圈
    flag = [1] * n
    # 记录已经出圈的人
    count = 0
    # 报数
    num = 0
    while count < n - 1:
        for i in range(n):
            if flag[i] == 1:
                num += 1
                if num == m:
                    count += 1
                    flag[i] = 0
                    num = 0
                if count == n - 1:
                    break
    for i in range(n):
        if flag[i] == 1:
            return i
    return 0
print(LastRemaining_Solution(4,2))