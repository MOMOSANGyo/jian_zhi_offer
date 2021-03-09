#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/2
# Desc:
# Param:
# Function:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 两个链表长度不一致
"""
处理步骤
1、将长度长的链表向短的列表靠齐，将长的链表多出的部分截断
2、将两个链表的值逐一比对，当出现第一个相同的点时，后面的点必然相同

"""
class Solution:
    def __init__(self):
        self.cur_node = None
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        else:
            p1 = pHead1
            p2 = pHead2
            len_p1 = 0
            len_p2 = 0
            while p1:
                len_p1 = len_p1+1
                p1 = p1.next

            while p2:
                len_p2 = len_p2+1
                p2 = p2.next

            if len_p1>len_p2:
                i = len_p1 - len_p2
                while i:
                    pHead1 = pHead1.next
                    i = i-1
            elif len_p2>len_p1:
                j = len_p2 - len_p1
                while j:
                    pHead2 = pHead2.next
                    j = j-1

            while pHead1 :
                if pHead1.val != pHead2.val:
                    pHead1 = pHead1.next
                    pHead2 = pHead2.next
                else:
                    break
            return pHead1


# 内存超限
# class Solution:
#     def __init__(self):
#         self.cur_node = None
#     def ReverseList(self, pHead):
#         # write code here
#
#         if pHead:
#             while pHead:
#                 #每次只做一个节点，然后把节点相连
#                 node = ListNode(0)
#
#                 node.val = pHead.val
#                 node.next = self.cur_node
#                 self.cur_node = node
#                 pHead = pHead.next
#
#         else:
#             node = pHead
#
#         return node
#     def FindFirstCommonNode(self , pHead1 , pHead2 ):
#         if not pHead1 or not pHead2:
#             return None
#         else:
#             p1 = self.ReverseList(pHead1)
#             p2 = self.ReverseList(pHead2)
#
#             if p1.val != p2.val:
#                 return None
#             else:
#                 while p1 and p2:
#                     if p1.val == p2.val:
#                         node = ListNode(p1.val)
#                         node.next = self.cur_node
#                         self.cur_node = node
#                     else:
#                         return node






