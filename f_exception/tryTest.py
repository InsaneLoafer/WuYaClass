#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/30 21:07
# @Author   : ZhangTao
# @File     : tryTest.py
def div(a, b):
    return a / b


"""
try-->except执行步骤：
1、try代码执行正常，就不会执行except的代码
2、只有try代码执行异常，才会执行except的代码
"""
# try:
#     div(1, 0)
# except KeyError as e:
#     print(e.args)
# except ValueError as e:
#     print(e.args)
# except ZeroDivisionError as e:
#     print(e.args)
# except WindowsError as e:
#     print(e.args)

# def f(*args,**kwargs):
#     return kwargs
# print(f(name=1))

# 所有异常的父类 Exception
"""分母为0的情况"""
try:
    div(1, 0)
except Exception as e:
    print(e.args)

"""分母为字符串的情况"""
try:
    div(1, {'name': 'wuya'})
except Exception as e:
    print(e.args)

"""分母为float类型的情况"""
try:
    div(1, 1.01)
except Exception as e:
    print(e.args)

"""
try--except--else--finally
1.先执行try，如果执行通过，就执行else代码，最后执行finally
2.如果try执行失败，就直接执行finally
"""

try:
    div(1,0)
except Exception as e:
    raise Exception('我是执行失败了')
else:
    print('pass')
finally:
    print('finally')