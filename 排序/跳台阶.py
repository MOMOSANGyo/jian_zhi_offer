#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/9
# Desc:
# Param:
# Function:
class Solution:
    def __init__(self):
        self.num = 0
    #     复杂度高
    # def jumpFloor(self, number):
    #     if number == 1:
    #         self.num = self.num+1
    #         # print(self.num,'最后一步')
    #         self.jumpFloor(number-1)
    #         return self.num
    #
    #     elif number == 2:
    #         # self.num = self.num+2
    #         self.jumpFloor(number-2)
    #         return self.num
    #     elif number>2:
    #         self.num = self.num + 2
    #         # print(self.num)
    #         self.jumpFloor(number-1)
    #         self.jumpFloor(number-2)
    #         return self.num
    def jumpFloor(self, number):
        if number <= 2:
            if number == 1:
                self.num = self.num+1
            else:
                self.num = self.num + 2
            return self.num
        else:
            self.num = self.num+2
            self.jumpFloor(number-1)
            return  self.num





if __name__ == '__main__':
    ss =Solution()
    print(ss.jumpFloor(2))