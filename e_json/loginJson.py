#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/7 22:13
# @Author   : ZhangTao
# @File     : demo.py
"""
需求：注册账户，然后注册的账户登录到系统后，显示登录的昵称
1、注册的函数
2、登录的函数
3、登录成功后获取昵称的函数
"""
import json

def inOut():
    username = input("请输入账号：\n")
    password = input("请输入密码：\n")
    return username, password


def register():
    """实现账户的注册功能"""
    username, password = inOut()
    temp = username + '|' + password
    # with open('login.md', 'w') as f:
    #     f.write(temp)
    json.dump(temp,open('login.md','w'))


def login():
    """登录函数"""
    username, password = inOut()
    # with open('login.md', 'r') as f:
    #     info = f.read()
    f= json.load(open('login.md','r'))
    info = f.split('|')
    if username == info[0] and password == info[1]:
        return True
    else:
        return False


def getNick(func):
    '''获取昵称'''
    # with open('login.md', 'r') as f:
    #     info = f.read()
    info = json.load(open('login.md','r'))
    info = info.split('|')
    if func:
        print(f'{info[0]}您好，欢迎访问无涯课堂！')
        # print('{0}您好，欢迎访问无涯课堂！'.format(info[0]))
    else:
        print('请登录系统')


if __name__ == '__main__':
    while True:
        t = int(input('1、注册 2、登录 3、退出系统\n'))
        if t == 1:
            register()
        elif t == 2:
            getNick(login())
        elif t == 3:
            import sys

            sys.exit(1)
        else:
            print('输入错误，请继续...')
            continue
