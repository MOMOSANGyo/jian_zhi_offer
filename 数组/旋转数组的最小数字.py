#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/5
# Desc:
# Param:
# Function:
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray)==0:
            return 0
        else:
            a =  sorted(rotateArray)
            return a[0]
        # write code here



