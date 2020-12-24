#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/16 20:26
# @Author   : ZhangTao
# @File     : time_module.py
import time as t
# print(dir(t))

# 获取时间戳
print(int(t.time()))

# 获取当前时间
print(t.localtime(t.time()))
nowTime = t.strftime('%y-%m-%d %H:%M:%S', t.localtime())

# 休眠
t.sleep(1)
print(nowTime)