#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/16 20:34
# @Author   : ZhangTao
# @File     : os_module.py
import os
# print(os.system('ipconfig'))
# print(dir(os))

# 创建文件夹
# os.mkdir('c:/log')

# 删除文件夹
# os.rmdir('c:/log')

# 重命名文件
# os.rename('c:/log', 'c:/new_log')

# 对目录的处理
print('当前文件的目录', os.path.dirname(__file__))
print('文件当前目录的上一级目录', os.path.dirname(os.path.dirname(__file__)))

# 实现对d_sys_modules目录下文件内容的读取
base_dir = os.path.dirname(os.path.dirname(__file__))
f = open(os.path.join(base_dir, 'd_sys_modules/time_module.py'), 'r', encoding='utf-8')
print(f.read())

"""
请求参数不确定，可能有一个，可能有N个(使用动态参数)
"""
def f(*args, **kwargs):
    return kwargs
print(f(name='wuya', age='18'))