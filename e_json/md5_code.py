#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/30 20:48
# @Author   : ZhangTao
# @File     : md5_code.py
"""
对请求参数做ASCII码排序
做url encode编码：name=wuya&age=18&city=xian&work=tester
做md5-->sign
"""

dict1 = {'name': 'wuya', 'age': 18, 'city': 'xian', 'work': 'tester'}

# 排序
# dict1 = dict(sorted(dict1.items(), key=lambda item: item[0]))
# print(dict1)

# url encode编码
from urllib import parse

# datas = parse.urlencode(dict1)
# print(datas)

# md5加密
import hashlib


# md5 = hashlib.md5()
# md5.update(datas.encode('utf-8'))
# print(md5.hexdigest())

def getMd5(**kwargs):
    dict1 = dict(sorted(kwargs.items(), key=lambda item: item[0]))
    datas = parse.urlencode(dict1)
    md5 = hashlib.md5()
    md5.update(datas.encode('utf-8'))
    return md5.hexdigest()


print(getMd5(name='insane', age=19))
print(getMd5(**dict1))
