#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 10:56
# @Author   : ZhangTao
# @File     : filter_practice.py
"""
filter 函数练习
将序列中满足函数要求的值返回
"""

list1 = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda a: a > 2, list1)))
