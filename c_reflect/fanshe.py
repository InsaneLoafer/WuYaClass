#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/10 12:41
# @Author   : ZhangTao
# @File     : fanshe.py

"""
反射：
1、根据字符串的形式去某个模块中寻找东西--> getattr()
2、根据字符串的形式去某个模块中判断东西是否存在--> hasattr()
3、根据字符串的形式去某个模块中设置东西-> setattr()
4、根据字符串的形式去某个模块中删除东西--> delattr()
"""

# # 通过__import__导入目标模块并放在一个对象中
# f = __import__('login')
#
# # 通过对象找login模块中index的字符串并调用
# f.index()
import login

# # 调用login中的logout函数
# f = getattr(login, 'logout')
# f()

# 如何找到Person中的info方法并调用它
# obj = login.Person()
# # 判断是否存在info函数
# if hasattr(obj, 'info'):
#     f = getattr(obj, 'info')
#     f()
# else:
#     print('sorry')

# 设置函数
# obj = login.Person()
# f = setattr(obj, 'exit', 'this is a exit method')
# f2 = hasattr(obj, 'exit')
# print('setattr后的结果为：', f2)
#
# f3 = delattr(obj, 'exit')
# print('delattr后的结果为：', f3)

f = delattr(login, 'str1')
print(f)
f2 = hasattr(login, 'str1')
print(f2)
