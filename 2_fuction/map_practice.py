#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 10:54
# @Author   : ZhangTao
# @File     : map_practice.py
"""
map 函数练习:
将一个可迭代的序列按照某个函数，对序列中的每一个值都进行操作
"""

list1 = [2, 3, 4, 34, 5]
print(list(map(lambda a: a + 100, list1)))
