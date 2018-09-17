#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
import os
def isNum(s):
    counter = 0
    for i in s:
        if i in '0123456789':
            pass
        else:
            break
    else:
        print(s)
        counter += 1
    print(counter)
for i in os.listdir("/proc"):
    isNum(i)