#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/15
# Desc:
# Param:
# Function:

class Solution:
    # -*- coding:utf-8 -*-
    class Solution:
        def __init__(self):
            self.vals = []

        def Insert(self, num):
            # write code here
            self.vals.append(num)
            self.vals.sort()

        def GetMedian(self, a):
            # write code here
            length = len(self.vals)
            if length == 0:
                return 0
            if length % 2:
                return self.vals[int(length / 2)]
            return (self.vals[int(length / 2) - 1] + self.vals[int(length / 2)]) / 2


