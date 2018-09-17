#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"



x = int(input("num1:"))
y = int(input("num2:"))


try:
     print(fun(x,y))
except TypeError as e:
     print(e,"需要给函数添加两个参数")