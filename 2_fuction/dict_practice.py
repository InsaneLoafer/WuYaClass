#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 10:29
# @Author   : ZhangTao
# @File     : dict_practice.py

dict1 = {'name': 'wuya', 'age': 18, 'address': 'xian'}
dict2 = {'status': 0, 'msg': 'ok', 'datas': [
    {'name': 'wuya', 'age': 18, 'address': 'xian'},
    {'name': 'weike', 'age': 20, 'address': 'lanzhou'}
]}
dict3 = {'language': 'Python'}

'''对字典进⾏ascill码的排序'''
dict_sorted = sorted(dict1.items(), key=lambda item: item[0])
print(dict_sorted)

'''随机获取字典的值'''
print(dict2.popitem())

'''字典的循环处理'''
for key, value in dict1.items():
    print(key, ':', value)

'''字典的删除'''
del dict1['name']
print(dict1)

'''字典的清空'''
# dict1.clear()
# print(dict1)

'''字典的合并'''
dict1.update(dict3)
print(dict1)

'''字典的复制'''
dict4 = dict1.copy()
print(dict4)

'''字典推捯式'''
dict5 = [key for key, value in dict1.items()]
print('字典:\n', dict5)
