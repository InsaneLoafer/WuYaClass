#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 14:23
# @Author   : ZhangTao
# @File     : decorator_practice.py

"""
1、函数可以当成一个变量
2、函数的参数也可以是函数
3、函数是可以嵌套的

开放封闭原则：
1、封闭：已实现的功能代码尽可能的不要做修改
2、开放：对现有的功能代码可扩展

需求：在调用 f1 或 f2 时，先打印 f3 内容，再打印各自内容
"""


def getInfo():
    print('《Python自动化测试实战》')

def f1():
    print('网易云课堂')

def f2():
    print('51CTO平台')
