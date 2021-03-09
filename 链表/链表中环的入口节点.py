#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/4
# Desc:
# Param:
# Function:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:

    """
    3种情况：
    0、输入空列表
    1、完全不指向
    2、自己的终点指向七点
    3、自己的终点指向起点的一半
    """
    def EntryNodeOfLoop(self, pHead):
        p_temp = pHead
        pHead_list = []
        if pHead:
            while pHead:
                pHead_list.append(pHead)
                if pHead.next in pHead_list:
                    break
                pHead = pHead.next

            if not pHead:
                return None

            while p_temp:
                if p_temp != pHead.next:
                    p_temp = p_temp.next
                else:
                    return p_temp
        return None



if __name__ == '__main__':

    a = ['a','b','c']
    print(a.index('d'))

