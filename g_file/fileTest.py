#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/1/3 17:47
# @Author   : ZhangTao
# @File     : fileTest.py
"""
open()函数的操作：
1.要操作的文件名称
2.以什么样的方式操作
r：只读模式
w：只写模式【不可读，不存在就创建，存在就清空内容】
x：只写模式【不可读，不存在就创建，存在就报错】
a：增加模式【可读，不存在就创建，存在只增加内容】
“+”：表示可以同时读写某个文件，具体为：
r+：读写
w+：写读
x+：写读
a+：写读
"""
import json

"""w-->写文件"""
# f = open('file.json', 'w')
# temp = {
#     'name': 'insane',
#     'age': 20,
#     'address': 'sichuan'
# }
# f.writelines(temp) # 无序列化，只会写key
# f.close()
# json.dump(temp, open('file.json', 'w'))  # 进行序列化

"""a-->追加"""
# f = open('file.json', 'a')
# f.write('wuya')
# f.close()

"""
r-->读文件
read()-->读取文件的所有内容
readlines()-->按行读取，默认读取文件的第一行
read(7)-->只读取文件的前7个字符
"""
# f = open('file.json', 'r')
# print(f.read())  # 读取文件的所有内容
# for i in f.readlines():
#     print(i)
#
# print(f.read(3)) # 读取前3个字符

"""
文件的上下文处理
"""
with open('file1', 'w') as f:
    f.write('wuya')
