#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/5
# Desc:
# Param:
# Function:


class Solution:
    def GetNumberOfK(self, data, k):
        j = 0
        for i in data:
            if i == k:
                j = j+1
            elif i>k:
                return j

        return j