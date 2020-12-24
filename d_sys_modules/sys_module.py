#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/16 20:55
# @Author   : ZhangTao
# @File     : sys_module.py
import sys
import os
# 以列表形式打印当前目录
print(sys.argv)

# 打印版本号
print(sys.version)
# 打印平台
print(sys.platform)

# 打印Python下的各个库
for item in sys.path:
    print(item)
"""
1、标准库：D:\Program Files\Python38\lib
2、第三方库：D:\Program Files\Python38\lib\site-packages
3、自定义的库
"""

# 添加路径到系统路径
dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'd_sys_modules')
sys.path.append(dir_path)
print(sys.path)
