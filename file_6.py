#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
# sum = 0
# for i in  range(1,101):
#     sum = sum + i
#     print(sum)

import os,sys
def fun(path):
    isdir,isfile,join = os.path.isdir,os.path.join()  #函数引用
    isdir = os.listdir(path)
    dirs = [i for i in isdir if isdir(join(path,i))]
    files = [i for i in isdir if isfile(join(path,i))]

    if dirs:
        for d in dirs:
            fun(join(path,d))
    if files:
        for f in files:
        print(join(path,f))

fun("/home")
