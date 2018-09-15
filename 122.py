#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="songwei"

info = {}
name = input("your name:")
age = int(input("your age:"))

info["name"] = name
info["age"] = age

#print(info.items())
#for i in info.items():
    # print(i)
for k,v in info.items():
    print("%s--->%s" %(k,v))
