#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/2/1
# Desc:斐波那契数列是将杨辉三角按斜线，fn = fn-1+fn-2
# Param:
# Function:
# -*- coding:utf-8 -*-
# import numpy as np


class Solution:
    def Fibonacci(self, n):
        """
        :param n:
        :return:
        """
        # write code here

        f = [[0 for i in range(40)] for i in range(40)]
        # f[0][0] = 0
        f[1][0] = 1
        f[2][0] = 1
        f[2][1] = 1
        if n <= 2:
            pass
        else:
            # 行索引
            for i in range(3, n + 1):
                # 列索引
                # print(i)
                for j in range(0, i + 1):
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
        result = 0
        for i in range(n):
            result = result + f[n - i][i]

        return result


if __name__ == '__main__':
    ss = Solution()
    a = ss.Fibonacci(3)
    # f = ss.Fibonacci(3)
    print(a)
