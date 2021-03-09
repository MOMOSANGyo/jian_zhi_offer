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
class Solution:
    # 返回ListNode
    def __init__(self):
        self.cur_node = None
    def ReverseList(self, pHead):
        # write code here

        if pHead:
            while pHead:
                #每次只做一个节点，然后把节点相连
                node = ListNode(0)

                node.val = pHead.val
                node.next = self.cur_node
                self.cur_node = node
                pHead = pHead.next

        else:
            node = pHead

        return node


