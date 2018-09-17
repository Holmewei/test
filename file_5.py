#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
import os
proc_list = []
def isNum(a):
    for i in a:
        if i in '0123456789':
            pass
        else:
            break
    else:
        proc_list.append(a)

for proc in os.listdir('/proc'):
    isNum(proc)
print(proc_list)