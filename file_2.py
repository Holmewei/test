#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"

import sys
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            print("不是一个纯数字的字符串")
            break
    else:
        print("是一个纯数字的字符串")


isNum("sys.argv[1]")
