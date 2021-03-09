#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/5
# Desc:
# Param:
# Function:
"""
如果初始数组有7个
对这个数组进行for循环且一边循环一边删除
因为for循环记得是index得数量
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<=1:
            return index

        list = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        # range(1,index) [1,2,3...,index-1]
        for i in range(1,index):
            print(i2,i3,i5)
            number = min(list[i2]*2,list[i3]*3,list[i5]*5)
            list.append(number)

            if number%2 == 0:
                i2 = i2+1
            if number%3 == 0 :
                i3 = i3 + 1
            if number%5 == 0:
                i5 = i5 + 1
        return list[-1]






    # def GetUglyNumber_Solution(self, index):
    #     list = [2,3,4,5]
    #     max = 5
    #     if index == 1:
    #         return 1
    #     elif index == 2:
    #         return 2
    #     elif index == 3:
    #         return 3
    #     elif index == 4:
    #         return 4
    #     elif index == 5:
    #         return 5
    #     else:
            # 这里有n*m的复杂度；进行优化
            # while (len(list) < index-1 ):
            #     max = max+1
            #     for i in list:
            #          if max%i==0 and max/i in list:
            #              list.append(max)
            #              break

            # return list[-1]


if __name__ == '__main__':
    ss = Solution()
    print(ss.GetUglyNumber_Solution(2))
    # a = [3,2,8,9]
