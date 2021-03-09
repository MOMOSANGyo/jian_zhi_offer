#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/1
# Desc:
# Param:
# Function:
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
#         非递归版本
# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         # write code here
#         #初始化
#         tmp = ListNode(0)
#         pHead = tmp
#         while pHead1 and pHead2:
#             if pHead1.val < pHead2.val:
#                 tmp.next = pHead1
#                 pHead1 = pHead1.next
#             else:
#                 tmp.next = pHead2
#                 pHead2 = pHead2.next
#             tmp = tmp.next
#         if not pHead1:
#             tmp.next = pHead2
#         if not pHead2:
#             tmp.next = pHead1
#         return pHead

# 递归版本，比对链表的头两个值，如果a比b小取a，然后迭代返回，对a取下一个节点与b比较
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1,pHead2.next)
            return pHead2
