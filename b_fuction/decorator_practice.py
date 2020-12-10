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

"""
装饰器：被装饰的函数是装饰函数的参数
执行步骤：
1、执行getInfo函数的时候，把被装饰的函数f1当做参数来传递
2、getInfo函数的返回值会重新赋值
3、一旦结合了装饰器后，调用f1函数其实执行的是inner函数的内部，原来的函数f1被覆盖
4、被装饰的函数f1重新赋值给装饰器的内层函数inner
"""
def getInfo(func):
    def inner():
        print('《Python自动化测试实战》')
        func()
    return inner

@getInfo
def f1():
    print('网易云课堂')

def f2():
    print('51CTO平台')

def login(func):
    def inner(token='123'):
        if token == '123':
            return func(token)
        else:
            return '请登录系统'
    return inner
@login
def profile(token):
    """个人主页"""
    return '你的主页信息'

"""利用动态参数，解决函数是否需要传入形式参数的问题"""
def outer(func):
    def inner(*args, **kwargs):
        print(args, kwargs)
        func()
    return inner

