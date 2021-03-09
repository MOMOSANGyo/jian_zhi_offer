#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/9
# Desc:
# Param:
# Function:
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        len_input = len(tinput)
        result_list = []
        input = sorted(tinput)
        if k > len_input:
            return result_list
        for i in range(0,k):
            result_list.append(input[i])

        return  result_list

if __name__ == '__main__':
    ss =Solution()
    print(ss.GetLeastNumbers_Solution([1,2,3,4],5))