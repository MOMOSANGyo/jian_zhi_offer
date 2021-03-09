#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangxin
# Date: 2021/3/1
# Desc:有错误，类方法的缓存没释放
# Param:
# Function:



###  ##########################
###  ListNode的python实现
###  ##########################
class Node(object):
    def __init__(self):
        self.val = None #存值
        self.next = None #存指针

class Node_handle():
    def __init__(self):
        self.cur_node = None
# 查找
    def find(self,node,num,a = 0):
        while node:
            if a == num:
                return node
            a += 1
            node = node.next
# 增加
    def add(self,data):#表首插入，新的值放入表首
        node = Node() #初始化一个节点类【自定义】
        node.val = data #给节点赋值
        node.next = self.cur_node #给节点的指针赋值，指针指向下一节点的内存地址，默认为None
        self.cur_node = node #将本节点的内存地址赋值给属性cur_node
        return node
# 打印
    def printNode(self,node):
        while node:
            print ('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next
# 删除
    def delete(self,node,num,b = 1):
        if num == 0:
            node = node.next
            return node
        while node and node.next:
            if num == b:
                node.next = node.next.next
            b += 1
            node = node.next
        return node
# 翻转
    def reverse(self,nodelist): #翻转前后的链表地址发生改变
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next #把下一个节点的内存地址传过去
        result = Node()
        result_handle =Node_handle()
        for i in list:
            result = result_handle.add(i)
        return result

###  ##########################
###  ##########################

###  ##########################
###  牛客网代码实现
###  ##########################

class ListNode:
    def __init__(self):
        self.val = None
        self.next = None

class Solution:
    def __init__(self):
        self.cur_node = None
    def Add(self,value):
        node = ListNode()
        node.val = value
        node.next = self.cur_node
        self.cur_node = node

        return node
    # 返回合并后列表并排序
    def Merge(self, pHead1, pHead2):
        if pHead1 is None and pHead2 is None:
            resultNode = ListNode()
            return resultNode#不可返回一个空值？
        all_list = []
        while pHead1:
            all_list.append(pHead1.val)
            pHead1 = pHead1.next



        while pHead2:
            all_list.append(pHead2.val)
            pHead2 = pHead2.next

        result = sorted(all_list,reverse=True)

        for i in result:
            resultNode=self.Add(i)
        return resultNode



if __name__ == '__main__':
    a = [1,9,3]
    b = [4,5,6]
#add 方法再调用时不是释放内存？？
    ss = Solution()
    a_ListNode = Node()
    for i in a: #a为set{}时，循环输出自动排序
        a_ListNode = ss.Add(i)


    while a_ListNode:
        print('aaaaaaaaaaaaa',a_ListNode.val)
        a_ListNode = a_ListNode.next


    for i in b:
        b_ListNode = ss.Add(i)

    result = ss.Merge(a_ListNode,b_ListNode)

    while b_ListNode:
        print('bbbbbbbbbbb',b_ListNode.val)
        b_ListNode = b_ListNode.next

"""
因为solution中的属性cur_node一直在更新，导致add方法展现出“内存没有释放”的现象，每次调用Add一直都在同一个链表上进追加
"""
    # ss = Solution()
    # print(ss.Merge(a,b))
    #
    # l1 = Node()
    # print(l1) #打印的是实例的内存地址
    #
    #
    #
    # ListNode_1 = Node_handle()
    # l1_list = [1, 8, 3]
    # for i in l1_list:
    #     l1 = ListNode_1.add(i)
    #
    # # 直接打印链表，所显示的地址为表首地址。
    #
    # ListNode_1.printNode(l1)#{3，8，1}

    #
    # a = 0
    # while l1:
    #     # list.append(nodelist.val)
    #     a = a + 1
    #     print('********************',a)
    #     print('l1',l1)
    #     print('l1.next',l1.next)
    #     print('********************',a)
    #     l1 = l1.next


    # l1 = ListNode_1.find(l1, 1)
    # ListNode_1.printNode(l1)
    # l1 = ListNode_1.delete(l1, 0)
    # ListNode_1.printNode(l1)
    # l1 = ListNode_1.reverse(l1)
    # ListNode_1.printNode(l1)


