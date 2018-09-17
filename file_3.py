#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
def fibs(num):
    fib = [0,1]
    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])
    print(fib)


fibs(10)
fibs(20)


