# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:35
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : neteasy.py
# @Software: PyCharm

while True:
    try:
        ###############Iput Module#######################
        testNumber = int(input())
        for i in range(testNumber):
            # 读取一个数据点
            # 处理该数据点
            # 输出该数据点答案
















        ruleNumber = int(input())
        ruleList = {}
        for i in range(ruleNumber):
            tmp1, tmp2 = input().split()
            ruleList[tmp1] = tmp2
        failNumber = int(input())
        failList = list(input().split())
        testSample = input()
        #####################################################
        if testNumber < 0 or testNumber > 50:
            print(-1)
            break
        if ruleNumber < 0 or ruleNumber > 26:
            print(-1)
            break
        if failNumber < 0 or failNumber > 26:
            print(-1)
            break
        if len(testSample) < 0 or len(testSample) > 200:
            print(-1)
            break


        #################################################
        def matchData(dic, str):
            result = []
            for key, value in dic.items():
                if value == str:
                    result.append(key)
            return result


        ######函数功能是判断faillist里面的字符串计算打印次数
        def countFail(ruleList, failList, str):
            failCount = 0
            if str in ruleList.values():
                res = matchData(ruleList, str)
                for i in res:
                    if i not in failList:
                        failCount += 2
                        break
                    else:
                        countFail(ruleList, failList, i)
            else:
                return -1
            return failCount


        # 开始计数
        count = 0
        for i in range(len(testSample)):
            a = testSample[i]
            if testSample[i] not in failList:
                count += 1
            else:
                count += countFail(ruleList, failList, testSample[i])
        print(count)
    except:
        break
