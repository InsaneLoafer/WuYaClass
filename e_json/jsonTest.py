#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/29 20:01
# @Author   : ZhangTao
# @File     : jsonTest.py
import json
import requests

"""
序列化：把Python的数据类型转为str的类型过程 
反序列化：把str的数据类型转化为Python数据类型
"""

"""字典的序列化与反序列化"""
dict1 = {'name': 'insane', 'age': 18}

# 序列化dict->str
dict_str = json.dumps(dict1)
print(dict_str, type(dict_str))

# 反序列化
str_dict = json.loads(dict_str)
print(str_dict, type(str_dict))

"""列表的序列化与反序列化"""
list1 = ['admin', 'wuya', 'insane']

# 序列化：
list_str = json.dumps(list1)
print(list_str, type(list_str))

# 反序列化
str_list = json.loads(list_str)
print(str_list, type(str_list))

"""
元祖的序列化与反序列化
注：元祖反序列化后为列表
"""
tuple1 = ("a", "b", "c")

# 序列化
tuple_str = json.dumps(tuple1)
print(tuple_str, type(tuple_str))

# 反序列化:
str_tuple = json.loads(tuple_str)
print(str_tuple, type(str_tuple))

"""文件的序列化与反序列化"""
r = requests.get(url='http://www.weather.com.cn/daka/sk/101190408.html')
print(type(r.content))
print(r.content.decode('utf-8'))
# 对文件的序列化：就是服务端的响应数据写到文件中
# json.dump(r.content.decode('utf-8'), open('weather.json', 'w'))

# 对文件的反序列化：就是读取文件内容
dict2 = json.load(open('weather.json', 'r'))
print(dict2, type(dict2))

"""
1、文件反序列化，类型是Unicode
2、进行编码，把Unicode类型转化为str类型
3、然后使用反序列化，把str转成字典类型
"""
# json.dump(r.content, open('weather1.json', 'w'))
# dict3 = json.loads((json.load(open('weather1.json', 'r'))).encode('utf-8'))
# print(dict3, type(dict3))
