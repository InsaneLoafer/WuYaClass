#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 10:41
# @Author   : ZhangTao
# @File     : lamda_practice.py
"""
lamda 匿名函数：
格式： lambda a,b:a+b
冒号前面为参数，冒号后面为对参数的操作
"""

"""
利用lambda函数和三目运算定义登录函数
"""
login = lambda username, password: print('登录成功') if username == 'wuya' and password == 'admin' else print('登录失败')
login('wuya', 'admin')

"""
需求：
1、对请求参数尽心ascill排序
2、排序后，对请求参数进行md5的加密
"""

def data(**kwargs):
    return dict(sorted(kwargs.items(), key=lambda item: item[0]))

dict1 = {'name': 'wuya', 'age': 18, 'addr': 'xian'}
print(data(**dict1))
