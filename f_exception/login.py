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


def inOut():
    username = input("请输入账号：\n")
    password = input("请输入密码：\n")
    return username, password


def register():
    """实现账户的注册功能"""
    username, password = input()
    temp = username + '|' + password
    with open('login.md', 'w') as f:
        f.write(temp)


def login():
    """登录函数"""
    username, password = input()
    with open('login.md', 'r') as f:
        info = f.read()
    info = info.split('|')
    if username == info[0] and password == info[1]:
        return True
    else:
        return False


def getNick(func):
    '''获取昵称'''
    with open('login.md', 'r') as f:
        info = f.read()
    info = info.split('|')
    if func:
        print(f'{info[0]}您好，欢迎访问无涯课堂！')
        # print('{0}您好，欢迎访问无涯课堂！'.format(info[0]))
    else:
        print('请登录系统')


if __name__ == '__main__':
    while True:
        try:
            t = input('1、注册 2、登录 3、退出系统\n')
            if isinstance(t, float):
                t = int(t)
            elif isinstance(t, str):
                if len(t) == 1:
                    t = ord(t)  # 将字母转成数字
                elif len(t) > 1:
                    t = ord(list(t)[0])

        except Exception as e:
            print(e.args)
        else:
            if t == 1:
                register()
            elif t == 2:
                getNick(login())
            elif t == 3:
                import sys

                sys.exit(1)
            else:
                print('输入错误，请继续...,请输入1,2,3')
                continue
        finally:
            print('欢迎您的访问~')
