#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 10:29
# @Author   : ZhangTao
# @File     : dict_sort.py

"""
对字典进行ascill排序
"""
dict1 = {'name': 'insane', 'age': 18, 'addr': 'chengdu'}
dict_sorted = sorted(dict1.items(), key=lambda item:item[0])
print(dict_sorted)
